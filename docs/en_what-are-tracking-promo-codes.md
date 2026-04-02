---
title: What are tracking promo codes?
category: admitad-advertisers
section: tools_1
language: en
source: https://support.mitgo.com/knowledge-base/article/tracking-promo-codes
---

# What are tracking promo codes?

Tracking promo codes enable publishers to promote your offers and track user actions. They can be used with or without affiliate links.


Combining tracking via affiliate links and promo codes ensures more reliable order tracking, even considering browser restrictions and ad blockers. This approach protects publishers from losing orders and improves attribution accuracy.

Advantages of combined link and promo code tracking:

- Reliable tracking. If tracking via affiliate link fails, the order will be tracked via the promo code, and vice versa, minimizing the risk of lost orders.
- Access management. Ability to assign a promo code to a specific ad space and moderate access to each promo code.
- Promo code redistribution. A promo code can be revoked if the publisher uses it ineffectively and reassigned to another ad space.
- Quick stats update. Using link tracking speeds up the display of orders in statistics.
- Traffic marking. Allows publishers to label traffic sources, orders, and audience.


Read also [How to add tracking promo codes to affiliate program](https://support.mitgo.com/knowledge-base/article/how-to-add-smart-promo-codes-to-affiliate-program)

## Integration methods

# 


To track actions via tracking promo codes, you can use:

- Online integration, which includes:
	- [Backend integration via postback requests, XML, or API](#back-integration)
	- [Frontend integration via TagTag or GTM Template](#front-integration).
- [Offline integration](#off-integration) ー tracking via manual file upload into the system.


Learn more about integration methods in the article [Integration: What it is and how to integrate with Admitad](https://support.mitgo.com/knowledge-base/article/what-system-integration-is-and-how-to-integrate-with-admitad_2)


The most effective and preferred method is online integration with tracking via both links and promo codes. This accelerates data appearance in the statistics, allowing publishers to promptly analyze traffic sources and optimize them. If needed, you can also supplement statistics by manually uploading files into the system.


If you use online integration only for link tracking or if it's entirely impossible for you, you can use offline integration for promo code tracking. However, this method has drawbacks:

- Publishers won't be able to tag traffic and correctly attribute orders, which is especially critical for cashback services.
- Data on using promo codes will only be available after uploading the file to the system, which slows down analysis and traffic optimization for publishers.

### Backend integration: Postback request, XML, or API


Backend integration involves transferring action data from the server. This method ensures accurate tracking, unaffected by browser privacy policies, ad blockers, or other tracking restrictions.


If you already have this integration set up for affiliate links, you need to adjust it to work with tracking promo codes.

### Frontend integration: TagTag, GTM Template


With frontend integration, action data is transmitted from the website through the user's browser. Privacy policies and ad blockers significantly impact this method, so it shouldn’t be used as the sole tracking method.


For precise tracking, it’s essential to submit a file with tracking data for all promo code actions alongside frontend integration. This approach ensures no actions are lost.


When setting up frontend integration, ensure that TagTag or Google Tag Manager (GTM) code runs on every page without any special conditions, such as run only for Admitad traffic.


You also need to add Admitad scripts and cookies as exceptions in content control systems or content security policies and mark them as Strictly Necessary.

### Offline integration


With offline integration, you manually submit action data to Admitad for processing and accounting.


For accurate tracking, it's crucial to use a complete and reliable data source, such as your CRM or database. These systems provide accurate information about user actions.


Google Analytics 4 and similar tools aren't suitable as data sources for offline integration due to technical restrictions: their tracking code is often blocked by browsers, potentially leading to lost action data.


Export action data from your system on a weekly basis and send the file to your manager for uploading data into your account. The file must contain the following information:

- Order ID,
- Promo code,
- Product cost,
- Date of action.

## Attribution rules

- Actions using Admitad tracking promo codes are always attributed to Admitad, even if other tracking sources (e.g., other affiliate links) were involved before the promo code was applied. All confirmed orders tied to these tracking promo codes must be paid.
- Tracking actions made with tracking promo codes across all devices is essential. Mobile devices may have tracking limitations, so we recommend using offline integration for them.

## Requirements for tracking promo codes

- When creating tracking promo codes, use the naming format: Admitad1, Admitad2, Admitad3\. This allows identifying them as part of the Admitad network and distinguishing them from general offers.
- To increase program efficiency and stability, we recommend using lifetime tracking promo codes.

 You won't need to monitor their expiration dates and extend them, preventing traffic and order loss.
If lifetime promo codes aren't feasible, set an expiration period of at least 90 days.
- Tracking promo codes should apply to a wide range of products to attract more users and engage publishers. Limiting the range may reduce promo codes effectiveness.
- Admitad promo codes should offer a higher discount than publicly available ones.
