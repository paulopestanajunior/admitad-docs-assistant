---
title: API для паблишера
category: takprodam
section: takprodam-for-publisher
language: ru
source: https://support.admitad.ru/knowledge-base/article/api-%D0%B4%D0%BB%D1%8F-%D0%BF%D0%B0%D0%B1%D0%BB%D0%B8%D1%88%D0%B5%D1%80%D0%B0
---

# API для паблишера

Для доступа к [API](https://api.takprodam.ru/doc/publisher/redocly/) используйте API токен из личного профиля («Профиль» → «Общие настройки профиля» → «Генерация API токена»).


API — это инструмент, который позволяет:

- оптимизировать работу с платформой Такпродам;
- получать актуальную информацию о комиссиях, товарах, акциях, площадках;
- эффективно управлять продвижением товаров и увеличивать доход.

## Как работает API


Вы отправляете со своего сервера HTTP\-запрос типа GET к нашему API, чтобы получить нужную информацию из вашего кабинета. Мы принимаем запрос, обрабатываем его и отправляем ответ в формате JSON на ваш сервер. Для аутентификации запрос должен содержать уникальный токен из вашего личного профиля.

## Методы (типы) запроса


В запросах Get products list with links, Get promotions list и Get promotion products обязательно указывайте id вашей площадки. Получить id площадки можно через API\-запрос Get source list.

## Get commissions list


Возвращает информацию о комиссиях.
  
URL запроса — https://api.takprodam.ru/v2/publisher/commission/

#### Список параметров для запроса:

| Название | Допустимое значение |
| --- | --- |
| id | id комиссии |
| subid | Произвольный идентификатор, который вы можете использовать для дополнительной категоризации и отслеживания трафика |
| status | Статус комиссии: - pending — в ожидании - approved — подтверждена - declined — отклонена |
| payment\_type | Модель оплаты: - cpa — оплата за заказ - cpc — оплата за клик с учетом продаж (СРС с учетом продаж) - cpmc — оплата за переход по ссылке с витрины на товар (СРС с витриной) |
| created\_at\_from | Дата создания комиссии: начало периода |
| created\_at\_to | Дата создания комиссии: конец периода |
| updated\_at\_from | Дата обновления статуса комиссии: начало периода |
| updated\_at\_to | Дата обновления статуса комиссии: конец периода |
| page | Номер страницы |
| limit | Число записей на странице (по умолчанию выбрано число 50; допустимое значение от 1 до 1000\) |

Пример использования (разверните)
Пример запроса с использованием утилиты curl

```

	 -H "Host: api.takprodam.ru" \
	 -H "Accept: application/json" \
	 -H "Authorization: Bearer YOUR_API_TOKEN" \
	 "[https://api.takprodam.ru/v2/publisher/commission/?...](https://api.takprodam.ru/v2/publisher/commission/?id=id&subid=subid&status=status&payment_type=payment_type&created_at_from=created_at_from&created_at_to=created_at_to&updated_at_from=updated_at_from&updated_at_to=updated_at_to&page=1&limit=50) \
	 --compressed

```
`Пример ответа API-сервера в формате JSON

```

	{
	 "total_count": 1000,
	 "page": 1,
	 "limit": 50,
	 "items": [
	 {
	 "id": "string",
	 "payment_type": "cpa",
	 "status": "pending",
	 "commission_date": "2021-01-01",
	 "source": {
	 "id": 0,
	 "title": "string",
	 "status": "verification",
	 "source_type": {
	 "id": 0,
	 "type": "social_network",
	 "title": "string",
	 "slug": "string"
	 },
	 "source_url": "string",
	 "created_at": "2019-08-24T14:15:22Z"
	 },
	 "order_product": {
	 "id": 0,
	 "title": "string",
	 "sku": "string"
	 },
	 "click_product": {
	 "id": 0,
	 "title": "string",
	 "sku": "string"
	 },
	 "subid": "string",
	 "marketplace": "ozon",
	 "commission_amount": 0.1,
	 "cart_amount": 0.1,
	 "created_at": "2019-08-24T14:15:22Z",
	 "updated_at": "2019-08-24T14:15:22Z"
	 }
	 ]
	}

````#### `Описание полей ответа API-сервера на Get commissions list`

`| Поле | Описание |
| --- | --- |
| id | Уникальный идентификатор комиссии |
| payment_type | Модель оплаты комиссии |
| status | Текущий статус комиссии |
| commission_date | Дата регистрации комиссии |
| source | Площадка |
| order_product | Информация о товаре, который заказан (только для Ozon) |
| click_product | Товар, по которому был совершен клик, приводящий к заказу (только для WB) |
| subid | Дополнительный идентификатор для отслеживания источника трафика (если вы его указали при формировании ссылки) |
| marketplace | Название маркетплейса |
| commission_amount | Размер комиссии |
| cart_amount | Сумма заказа |
| created_at | Дата и время заказа |
| updated_at | Дата и время последнего обновления статуса заказа |

## Get products list with links


Возвращает информацию о товарах с партнерскими ссылками.  
URL запроса — https://api.takprodam.ru/v2/publisher/product/

#### Список параметров для запроса:

| Название | Допустимое значение |
| --- | --- |
| source_id | id площадки (узнать id вашей площадки можно через API-запрос Get source list) |
| subid | Произвольный идентификатор, который вы можете использовать для дополнительной категоризации и отслеживания трафика. |
| marketplace | Название маркетплейса: «Ozon», «Wildberries», «Avito», «Aliexpress» |
| category_id | id категории товара в виде числа (чтобы узнать соответствие числового кода названию категории товара, используйте запрос Get product categories list) |
| favorite | Избранное (добавить в «Избранное» товар или удалить его оттуда можно только через личный кабинет) |
| payment_type | Модель оплаты: - cpa — оплата за заказ - cpc — оплата за клик с учетом продаж (СРС с учетом продаж) - cpmc — оплата за переход по ссылке с витрины на товар (СРС с витриной) |
| page | Номер страницы |
| limit | Число записей на странице (по умолчанию выбрано число 50; допустимое значение от 1 до 1000) |

Пример использования (разверните)
Пример запроса с использованием утилиты curl

```

	 -H "Host: api.takprodam.ru" \
	 -H "Accept: application/json" \
	 -H "Authorization: Bearer YOUR_API_TOKEN" \
	 "[https://api.takprodam.ru/v2/publisher/product/?sou...](https://api.takprodam.ru/v2/publisher/product/?source_id=source_id&subid=&marketplace=marketplace&category_id=category_id&favorite=0&payment_type=cpa&page=1&limit=50) \
	 --compressed


```

Пример ответа API-сервера в формате JSON

```

	{
	 "total_count": 1000,
	 "page": 1,
	 "limit": 50,
	 "items": [
	 {
	 "id": "string",
	 "product_id": 0,
	 "title": "string",
	 "image_url": "string",
	 "price": 0.1,
	 "commission": 0.1,
	 "product_category": "string",
	 "marketplace_title": "string",
	 "store_title": "string",
	 "external_link": "string",
	 "favorite": true,
	 "payment_type": "cpa",
	 "tracking_link": "string",
	 "legal_text": "string"
	 }
	 ]
	}

```

#### Описание полей ответа API-сервера на Get products list with links

| Поле | Описание |
| --- | --- |
| id | Уникальный идентификатор товара |
| product_id | Уникальный идентификатор товара на маркетплейсе |
| product_sku | Уникальный идентификатор товара – SKU (артикул производителя) |
| title | Название товара |
| image_url | Ссылка на изображение |
| price | Цена товара |
| commission | Комиссия за продвижение |
| product_category | Категория товара (чтобы узнать соответствие названий категорий их числовым кодам, используйте запрос Get product categories list) |
| marketplace_title | Название маркетплейса |
| store_title | Название магазина |
| external_link | Прямая ссылка на товар на маркетплейсе |
| favorite | Избранное |
| payment_type | Модель оплаты |
| tracking_link | Партнерская ссылка на товар |
| legal_text | Маркировка рекламы |

## Get product categories list


Возвращает информацию о категориях товаров для продвижения.  
URL запроса — https://api.takprodam.ru/v2/publisher/product-category/


Категории товаров обозначаются в виде чисел или названий. Метод Get product categories list позволяет соотнести числовой код категории с ее названием.

#### Список параметров для запроса:

| Название | Допустимое значение |
| --- | --- |
| product-category | Категория товара |

Пример использования (разверните)
Пример запроса с использованием утилиты curl

```

	 -H "Host: api.takprodam.ru" \
	 -H "Accept: application/json" \
	 -H "Authorization: Bearer YOUR_API_TOKEN" \
	 "[https://api.takprodam.ru/v2/publisher/product-cate...](https://api.takprodam.ru/v2/publisher/product-category/) \
	 --compressed


```

Пример ответа API-сервера в формате JSON

```

	{
	 "items": [
	 {
	 "id": 0,
	 "title": "string"
	 }
	 ]
	}

```

#### Описание полей ответа API-сервера на Get product categories list

| Поле | Описание |
| --- | --- |
| id | Уникальный идентификатор категории |
| title | Название категории товара |

## Get promotions list


Возвращает информацию о действующих акциях и промокодах.  
URL запроса — https://api.takprodam.ru/v2/publisher/promotion/

#### Список параметров для запроса:

| Название | Допустимое значение |
| --- | --- |
| source_id | id площадки (узнать id вашей площадки можно через API-запрос Get source list) |
| promotion_id | id акции/промокода |
| marketplace | Название маркетплейса: «Ozon», «Wildberries», «Avito», «Aliexpress» |
| promotion_type | Тип акции/промокода: - global_sale — глобальные акции и распродажи маркетплейсов - sale — акции от продавцов - coupon — промокоды от продавцов |
| favorite | Избранное (добавить в избранное товар или удалить его оттуда можно только через личный кабинет) |
| page | Номер страницы |
| limit | Число записей на странице (по умолчанию выбрано число 50; допустимое значение от 1 до 1000) |

Пример использования (разверните)
Пример запроса с использованием утилиты curl

```

	 -H "Host: api.takprodam.ru" \
	 -H "Accept: application/json" \
	 -H "Authorization: Bearer YOUR_API_TOKEN" \
	 "[https://api.takprodam.ru/v2/publisher/promotion/?s...](https://api.takprodam.ru/v2/publisher/promotion/?source_id=source_id&promotion_id=promotion_id&marketplace=marketplace&promotion_type=promotion_type&favorite=0&page=1&limit=50) \
	 --compressed


```

Пример ответа API-сервера в формате JSON

```

	{
	 "total_count": 1000,
	 "page": 1,
	 "limit": 50,
	 "items": [
	 {
	 "id": 0,
	 "title": "string",
	 "promotion_type": "global_sale",
	 "marketplace_title": "string",
	 "store_title": "string",
	 "discount_type": "fixed",
	 "discount_value": 0,
	 "start_date": "2019-08-24T14:15:22Z",
	 "end_date": "2019-08-24T14:15:22Z",
	 "coupon": "string",
	 "landing_link": "string",
	 "legal_text": "string"
	 }
	 ]
	}

```

#### Описание полей ответа API-сервера на Get promotions list

| Поле | Описание |
| --- | --- |
| id | Уникальный идентификатор акции/промокода |
| title | Название акции/промокода |
| promotion_type | Тип акции/промокода |
| marketplace_title | Название маркетплейса |
| store_title | Название магазина |
| discount_type | Тип скидки (в рублях или процентах) |
| discount_value | Размер скидки |
| start_date | Дата начала акции |
| end_date | Дата окончания акции |
| coupon | Текст промокода |
| landing_link | Ссылка на витрину товаров, которые участвуют в акции |
| legal_text | Маркировка рекламы |

## Get promotion products


Возвращает информацию о товарах, участвующих в акциях.  
URL запроса — https://api.takprodam.ru/v2/publisher/promotion/product/

#### Список параметров для запроса:

| Название | Допустимое значение |
| --- | --- |
| source_id | id площадки (узнать id вашей площадки можно через API-запрос Get source list) |
| subid | Произвольный идентификатор, который вы можете использовать для дополнительной категоризации и отслеживания трафика. |
| marketplace | Название маркетплейса: «Ozon», «Wildberries», «Avito», «Aliexpress» |
| category_id | id категории товара (чтобы узнать соответствие числового кода названию категории товара, используйте запрос Get product categories list) |
| favorite | Избранное (добавить в избранное товар или удалить его оттуда можно только через личный кабинет) |
| promotion_id | id акции/промокода (можно узнать через запрос Get promotion list) |
| page | Номер страницы |
| limit | Число записей на странице (по умолчанию выбрано число 50; допустимое значение от 1 до 1000) |

Пример использования (разверните)
Пример запроса с использованием утилиты curl

```

	 -H "Host: api.takprodam.ru" \
	 -H "Accept: application/json" \
	 -H "Authorization: Bearer YOUR_API_TOKEN" \
	 "[https://api.takprodam.ru/v2/publisher/promotion/pr...](https://api.takprodam.ru/v2/publisher/promotion/product/?source_id=source_id&subid=&marketplace=marketplace&category_id=category_id&favorite=0&promotion_id=promotion_id&page=1&limit=50) \
	 --compressed


```

Пример ответа API-сервера в формате JSON

```

	{
	 "total_count": 1000,
	 "page": 1,
	 "limit": 50,
	 "items": [
	 {
	 "id": "string",
	 "product_id": 0,
	 "title": "string",
	 "image_url": "string",
	 "price": 0.1,
	 "price_discount": 0.1,
	 "discount_percent": 0.1,
	 "commission": 0.1,
	 "product_category": "string",
	 "marketplace_title": "string",
	 "store_title": "string",
	 "promotion_id": 0,
	 "favorite": true,
	 "tracking_link": "string",
	 "legal_text": "string"
	 }
	 ]
	}

```

#### Описание полей ответа API-сервера на Get promotion products

| Поле | Описание |
| --- | --- |
| id | Уникальный идентификатор товара |
| product_id | Уникальный идентификатор товара на маркетплейсе |
| product_sku | Уникальный идентификатор товара – SKU (артикул производителя) |
| title | Название товара |
| image_url | Ссылка на изображение |
| price | Цена товара |
| price_discount | Цена товара со скидкой |
| discount_percent | Процент скидки |
| commission | Комиссия за продажу |
| product_category | Категория товара (чтобы узнать соответствие названий категорий их числовым кодам, используйте запрос Get product categories list) |
| marketplace_title | Название маркетплейса |
| store_title | Название магазина |
| promotion_id | Уникальный идентификатор акции/промокода |
| favorite | Избранное |
| tracking_link | Партнерская ссылка |
| legal_text | Маркировка рекламы |

## Get source list


Возвращает информацию о статусах площадки.  
URL запроса — https://api.takprodam.ru/v2/publisher/source/


Идентификатор площадки, полученный в ответе, используется в следующих API-запросах: Get products list with links, Get promotions list, Get promotion products.

#### Список параметров для запроса:

| Название | Допустимое значение |
| --- | --- |
| status | Статус площадки: - verification — на проверке - approved — подтверждена - declined — отклонена |

Пример использования (разверните)
Пример запроса с использованием утилиты curl

```

	 -H "Host: api.takprodam.ru" \
	 -H "Accept: application/json" \
	 -H "Authorization: Bearer YOUR_API_TOKEN" \
	 "[https://api.takprodam.ru/v2/publisher/source/?stat...](https://api.takprodam.ru/v2/publisher/source/?status=status) \
	 --compressed


```

Пример ответа API-сервера в формате JSON

```

	{
	 "items": [
	 {
	 "id": 0,
	 "title": "string",
	 "status": "verification",
	 "source_type": {
	 "id": 0,
	 "type": "social_network",
	 "title": "string",
	 "slug": "string"
	 },
	 "source_url": "string",
	 "created_at": "2019-08-24T14:15:22Z"
	 }
	 ]
	}

```

#### Описание полей ответа API-сервера на Get source list

| Поле | Описание |
| --- | --- |
| id | Уникальный идентификатор площадки |
| title | Название площадки |
| status | Статус площадки |
| source_type | Тип площадки |
| source_url | Ссылка на площадку |
| created_at | Дата создания площадки |`
