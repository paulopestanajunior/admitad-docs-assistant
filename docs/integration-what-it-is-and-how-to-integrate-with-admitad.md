---
title: Integration: What it is and how to integrate with Admitad
section: technical-integration
source: https://support.mitgo.com/knowledge-base/article/what-system-integration-is-and-how-to-integrate-with-admitad_2
---

# Integration: What it is and how to integrate with Admitad

## What integration is


System integration is a process of operationally combining two different independent systems: for example, your website or app and the Admitad system.


If you're planning to join an Admitad affiliate program, you must integrate your system with Admitad so that you can do the following:

- Track the [target actions](https://support.admitad.com/hc/en-us/articles/4403304880529-Admitad-Partner-Network#action-en) of your website visitors or app users.
- Submit activity reports to Admitad.

*Such target\-action reports will include the following information: program code, action code, rate code, order number, order amount, and other action details.*


The Admitad system will save any data submitted by your website and/or application and track the publisher from whose ad space the user came to your website and performed the target action. This will ensure that the target action is correctly assigned.


Proper configuration of the integration process ensures that all user target actions are properly registered and correctly assigned to publishers.


This way, you can control your affiliate program costs, and your publishers can be properly and fully reimbursed.


Read more about [mobile app integration](https://support.admitad.com/hc/en-us/articles/4405926817809).

## Admitad integration methods


Not all integration methods allow for accurate tracking of actions. For example, if order data is transmitted to Admitad from the advertiser's site via the user's browser, some of it may be lost due to browser privacy settings and the operation of ad blockers — as a result, publishers lose their deserved rewards for generated orders.

### Priority integration methods S2S


To ensure that action data is not lost during transmission, we recommend sending it directly to Admitad from the primary source — that is, from where orders are generated. This is called server\-to\-server (S2S) tracking.


The primary source of data can be:

- a server where databases with information about orders are located;
- CRM where orders are generated;
- CMS where orders are generated.


The priority integration methods with Admitad are:

- [Integration via postback request](https://support.mitgo.com/knowledge-base/article/integration-via-postback-request_2) from the server, from CRM or CMS.
- [Integration via XML file](https://support.mitgo.com/knowledge-base/article/integration-through-an-xml-file_2) — exporting orders from the server, from CRM or CMS to an XML file that Admitad has access to via a link.
- [Integration via API](https://support.mitgo.com/knowledge-base/article/what-system-integration-is-and-how-to-integrate-with-admitad_2#integration-via-API) — if you have your own API or plans for its development.
- [Integration via Shopify plugin](https://support.mitgo.com/knowledge-base/article/integration-via-tracking-codes-for-shopify_3) — if your website is created on the Shopify platform.


We recommend choosing one of these integration methods because only they can ensure the complete data transfer. If the technical capabilities of your site do not allow this, you can contact the developer and ask him to set up S2S\-connection for you. We, in turn, are ready to provide him guidance on the implementation logic.

### Undesirable integration methods


In addition to S2S connection, other integration methods are possible, but they carry the risks of data loss. Therefore, we do not recommend using them, although technically it is possible.


Starting June 1, 2025, Admitad moving to new standart of inegration and will apply Loss Adjustment calculations for untracked orders caused by browser\-based tracking methods like GTM, Tag Tag, and other type of integration.  
We strongly recommend transitioning to new integration standards now to ensure accurate tracking and avoid potential revenue discrepancies. Our team is ready to assist with the transition. More details you can read [here](https://www.admitad.com/blog/commitment-to-conversion-tracking/).


Undesirable integration methods include:

- Any frontend integration — when action data is transmitted not from the server, but from the site via the user's browser. Browser restrictions (for example, ad blockers) lead to the fact that some data will not be transmitted.
	- [Integration via plugin for WordPress](https://support.mitgo.com/knowledge-base/article/integration-via-wordpress-plugin_3)
	- [Integration via tracking code](https://support.mitgo.com/knowledge-base/article/integration-via-tracking-code_2)
	- [Integration via GTM Template](https://support.mitgo.com/knowledge-base/article/integration-via-gtm-template_2)
- Integration using third\-party web analytics systems, such as Google Analytics 4\. These systems also receive statistics not from the server, but from the site.
- Using a tracking platform: Affise, Trackier, etc. Although the data is transmitted from the tracking platform to Admitad via S2S, the tracking platform itself usually receives this data from the user's browser.

## Choosing integration method


For accurate tracking of target actions, we recommend choosing priority integration methods described in the section below. In other respects, the choice depends on the technical capabilities of your site. 

Scheme for choosing an integration method


Priority methods are highlighted in green, undesirable ones in red.


If the technical capabilities of your site do not allow you to immediately choose a priority integration method, you can contact the developer and ask him to set up S2S\-connection for you. We, in turn, are ready to provide him guidance on the implementation logic.

## Specifics and advantages of integration methods

### Priority methods

- [Postback integration](https://support.mitgo.com/knowledge-base/article/what-system-integration-is-and-how-to-integrate-with-admitad_2#integration-via-postback)
- [XML integration](https://support.mitgo.com/knowledge-base/article/what-system-integration-is-and-how-to-integrate-with-admitad_2#integration-via-XML)
- [Proprietary API integration](https://support.mitgo.com/knowledge-base/article/what-system-integration-is-and-how-to-integrate-with-admitad_2#integration-via-API)
- [Shopify plugin integration](https://support.mitgo.com/knowledge-base/article/integration-via-tracking-codes-for-shopify_3)

Deduplication settings and cross\-device tracking configuration are available as part of all these integration methods.

- Deduplication is a data processing technique for eliminating any duplicate copies of the same data, including target actions. The technique is also used to identify paid traffic sources and assign their corresponding orders.

Paid traffic sources are third\-party resources that you pay to attract customers on certain terms (e.g., you pay for a visit to your website, ad view, application, registration, or purchase). Examples include targeted advertising, contextual advertising, sponsored posts on influencers' channels, etc.

Cross\-device tracking refers to technology that enables the tracking of user target actions across multiple devices. [Read more](https://support.admitad.com/hc/en-us/articles/360019209738)

#### Postback integration


As part of postback integration, your server will send a request, or a postback, to the Admitad server, providing target action data generated by users of your website.


The Admitad server will analyze the data and settle publisher accounts.

Pros:

- Because it contains a private authorization key, a postback ensures secure data transfer. If necessary, the logs can be checked for the source of the request.
- Server\-to\-server (back\-end) postback is the most accurate technique for receiving and sending conversion data, protected from any front\-end changes.

Cons:

- Implementation requires access to the server side of the website.


Read more about [postback integration](https://support.admitad.com/hc/en-us/articles/4405926814865).

#### XML integration


With XML integration, any data about the target actions of users will be exported to an XML file with a special structure. The Admitad server, at specified intervals, will access this file and transfer any new data from the file to the Admitad server for analysis.

Pros:

- Can restrict access to a file that is username\- and password\-protected.
- If configured properly, publishers can receive information about actions with minimal delay.
- If you have any technical problems, you will be able to recover any lost activity data from Admitad analytics.

Cons:

- Data may be shown with delays in case of a long processing queue of the XML file.


Read more about [XML integration](https://support.admitad.com/hc/en-us/articles/4405920523409).

#### АРI integration


If your website operates with its own API, please forward your API documentation to an Integration Services specialist to work out a customized approach to the integration of your website.

Pros:

- Flexible configuration of data collection terms.
- Minimal API modifications on your side.
- Activity deduplication and cross\-device tracking configuration capabilities.

Cons:

- The most time\-consuming integration method, which requires a team of developers to implement and test the code.

### Undesirable methods


Starting June 1, 2025, Admitad moving to new standart of inegration and will apply Loss Adjustment calculations for untracked orders caused by browser\-based tracking methods like GTM, Tag Tag, and other type of integration.  
We strongly recommend transitioning to new integration standards now to ensure accurate tracking and avoid potential revenue discrepancies. Our team is ready to assist with the transition. More details you can read [here](https://www.admitad.com/blog/commitment-to-conversion-tracking/).

- [Integration via plugin for WordPress](https://support.mitgo.com/knowledge-base/article/integration-via-wordpress-plugin_3)
- [Integration via tracking code](https://support.mitgo.com/knowledge-base/article/integration-via-tracking-code_2)
- [Integration via Google Analytics API](https://support.mitgo.com/knowledge-base/article/integration-via-google-analytics-api_2)
- [Integration via GTM Template](https://support.mitgo.com/knowledge-base/article/integration-via-gtm-template_2)

## Getting started with integration


1\. Before integrating, please make sure that you have added at least one target action and its rate to your program. Otherwise, the process will fail.

- If you have a personal manager, they will add actions and rates for you.
- If you don't have a manager, you need to add actions and rates in Actions (Program → Traffic settings → Actions and rewards). See [this guide to adding actions](https://support.admitad.com/hc/en-us/articles/4405926785809).


2\. Next, open your personal account, go to Integration (Program → Integration) and click Next.


3\. Select the integration method that best matches your needs:

- Pre\-made plugin integration if you've chosen to integrate a CMS website hosted by WordPress, Shopify.
- Custom integrations if you've chosen to integrate by using either postback, XML, tracking code, or Google Analytics API.


4\. Select your integration method and click Next.


5\. The opened Integration Settings page has the following sections:

- Your program integration settings: Refer to this section to verify the requirements for configuring your program integration settings.
- Deduplication settings: Refer to this section for the link to the instructions on how to configure the deduplication settings.
- Integration testing: Here, you can find a test link, which you can use to verify whether the integration has been successful and whether the tracking of the target actions for your website has been properly configured.


6\. Go to the instructions and follow all the steps specified for your selected integration method.

- Instructions for priority integration methods:
	- [Postback integration](https://support.admitad.com/hc/en-us/articles/4405926814865)
	- [XML integration](https://support.admitad.com/hc/en-us/articles/4405920523409)
	- [Shopify plugin integration](https://support.mitgo.com/knowledge-base/article/integration-via-tracking-codes-for-shopify_3)
- Instructions for undesirable integration methods:
	- [WordPress plugin integration](https://support.admitad.com/hc/en-us/articles/10005651768465)
	- [Tracking code integration](https://support.admitad.com/hc/en-us/articles/4405926812305)
	- [Google Analytics API integration](https://support.admitad.com/hc/en-us/articles/4405920524945)
	- [GTM Template integration](https://support.mitgo.com/knowledge-base/article/integration-via-gtm-template_2)
