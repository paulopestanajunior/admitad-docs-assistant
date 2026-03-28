FROM python:3.11-slim

# Cria usuário não-root (exigido pelo HF Spaces)
RUN useradd -m -u 1000 user
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

# Baixa modelos de embedding e reranker durante a build
# (assim não precisa baixar em runtime — mais rápido pra iniciar)
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('intfloat/multilingual-e5-large')"
RUN python -c "from sentence_transformers import CrossEncoder; CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')"

# Dá permissão pro usuário
RUN chown -R user:user /app
USER user

# HuggingFace Spaces exige porta 7860
EXPOSE 7860

# Startup: ingere docs + inicia backend e frontend
CMD bash -c "\
    if [ ! -d 'chroma_db' ]; then python ingest.py; fi && \
    uvicorn api:app --host 0.0.0.0 --port 8000 & \
    streamlit run app.py \
        --server.port 7860 \
        --server.address 0.0.0.0 \
        --server.headless true \
        --browser.gatherUsageStats false \
"