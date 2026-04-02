---
title: Integrating a platform with Takeads
category: takeads
section: platforms
language: en
source: https://support.mitgo.com/knowledge-base/article/integrating-a-platform-with-takeads
---

# Integrating a platform with Takeads

Set up the integration with Takeads for automatic link tracking and statistics — available only for platforms with the “Approved” status. Learn more about statuses


Select your preferred integration method. Further actions depend on your choice.

- For website, you can use JS code or API integration.
- For app or extension, only API integration is available.
- To integrate your platform with JavaScript, you need to have access to the source code of your website.


1\. Follow the on\-screen instructions. 

	- If your website was built on a CMS other than WordPress (e.g., HubSpot, Joomla, etc.), you need to deploy the JavaScript code in all templates whose content you want to process with Take Link.
	- If you don't use a CMS system, you need to deploy the JavaScript code manually on all pages whose content you want to process with Take Link. *Pages and templates where you don't deploy the JavaScript code will not be processed by Take Link.*
	- If you use dynamic content generation (e.g., if your website operates as a single\-page application and uses such frameworks as Angular, React, or Vue), you'll need to initialize the JavaScript code after deployment. Learn more about initialization methods.
2\. After placing the code on your website and verifying it, click Next.
- 1\. Add the origin for your platform and click Next.

	- What origins are, and how they work
	
	
	
	Authorized origins are a security feature used to prevent unauthorized access to private data. Attackers can easily steal personal information and do other malicious activities without this feature.  
	In the Take API, an origin is mainly defined by its protocol, domain name, and port number if the website port is anything other than port 80\.  
	The website sends requests to the Takeads API only from the authorized origin. If any other origin attempts to access the API, the request will be blocked as it doesn't match the allowed origin.
2\. If you use server\-to\-server integration with the Take API and don't make client\-side requests, select the corresponding checkbox.


 3\. Get your Public key to use with the Takeads API. This key allows you to make platform\-level requests.


4\. Click Finish.


Optional. For JS methods, configure the integration settings:

- Blacklist. Forbid Takeads from replacing direct links to certain websites with tracking links. To do so, add domains of such websites to Blacklist.
- Section Targeting. Set up Takeads to monetize only specific website sections or elements. You can both include or exclude them.
- Link Activator. Allow Takeads to turn inactive links into clickable links to monetize them.
- Branding Words. Allow Takeads to embed tracking links into brand names on the website. You can also set the maximum number of such names on a page and/or forbid Takeads from embedding links into certain brand names.

[Learn more about available settings](https://support.mitgo.com/knowledge-base/article/take-link-settings_5)
