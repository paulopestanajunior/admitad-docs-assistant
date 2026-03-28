---
title: Shopify plugin integration
section: technical-integration
source: https://support.mitgo.com/knowledge-base/article/integration-via-tracking-codes-for-shopify_3
---

# Shopify plugin integration

If your site is built on the [Shopify](https://www.shopify.com/) platform, you can quickly integrate it with the Admitad system using the Admitad Tracking plugin.


The plugin is a software module that you need to install on your site and configure. As a result, your site will be integrated with the Admitad system.

## General information: features and recommendations


You can start the integration only if your program has:

- a tracking link configured in the General settings section;
- a target action added and a rate set for it in the Actions section.


If you do not have a manager, you will need to independently create a tracking link ([instruction](https://support.mitgo.com/knowledge-base/article/how-to-fill-out-the-general-program-settings-in-admitad_5#tracking-link)), as well as add at least one action and at least one rate ([instruction](https://support.mitgo.com/knowledge-base/article/how-to-create-and-manage-actions-and-rates-in-the-affiliate-program_5)).  
If you have a personal manager, they will set everything up for you.

- Integration is a mandatory step to continue. Without it, you cannot launch an affiliate program in Admitad.
- To configure the integration, you must have access to the admin panel of your website on the Shopify platform. If you do not have access, send this integration instruction to a colleague who has the necessary access.


When the integration is completed, all data about target actions — action date, order ID and its amount, currency, discount code, etc. — will be sent to Admitad automatically.

## How the Shopify plugin works


Admitad Tracking operates on the Last Paid Click attribution model, where the target action is credited to the last paid traffic source.

What is a paid traffic source (expand)
A paid traffic source is any third\-party resource that you pay to attract users to your site under certain conditions: for each visit to the site, an ad view, a request, a registration, or a purchase.

  
The plugin automatically sends data for each target action to Admitad. Admitad registers actions if they are performed via a link with the utm\_source\=admitad parameter and/or using the promo code you specified in the Tracking promo codes section of your Admitad account.

Advantages

- Tracks actions by link and by promo code.
- Uses its own attribution model, which does not depend on Shopify's internal analytics or third\-party analytics services like Google Analytics 4, etc.
- Provides secure transmission of information through the back\-end, preventing data loss due to browser privacy settings or ad blockers.
- Provides information about the last paid source (utm\_source) and Admitad click ID (if available) for each order.

Disadvantages


In the current version, the plugin can track only one target action with one rate. This means your program must have a single target action added and a single rate configured for the action.

## How to install the plugin on your site


1\. Log in to [Shopify](https://www.shopify.com/) — the admin panel of your site will open.


2\. Go to Settings → Apps and sales channels.


3\. In the top right corner, click Shopify App Store — you will be taken to the Shopify App Store.


4\. Enter "Admitad Tracking" in the search and click its name — the [plugin page](https://apps.shopify.com/admitad-tracking) will open.


5\. Click Install — the plugin installation will begin, and you will be redirected to your site.


6\. In the window that opens, review the information about what data from your site will be accessible to Admitad Tracking.


7\. Click Install to complete the installation. The plugin will appear on the site dashboard in the Apps block, and also in Settings → Apps and sales channels.

## How to configure the plugin


1\. Click Admitad Tracking in the admin panel of the site — a window with the plugin settings will open.


2\. Fill out the required fields:

- Campaign code — specify the unique code of your program in Admitad.  
[How to get the value of the parameter](#how-to-get-the-value-of-the-postback_key-and-campaign_code-parameters)
- Postback key — specify the value of the postback\_key parameter from your Admitad account. This is needed to authenticate the postback request.  
[How to get the value of the parameter](#how-to-get-the-value-of-the-postback_key-and-campaign_code-parameters)
- Cookie lifetime — specify the cookie lifetime: the number of days the cookie will be active. 90 days by default.


The value must match the Cookie lifetime setting in your Admitad account (Program → General settings) and correspond to the cookie lifetime specified in your contract with Admitad.

- Main source indicators — specify the parameter for identifying the paid traffic source. By default, the standard parameter utm\_source is selected.


3\. In the Additional source indicators block, add additional tracking parameters if needed. These parameters allow you to identify a paid traffic source in cases where the links of these sources are not mapped with the main parameter (utm\_source).  
For example, if you have a Google Ads campaign with auto\-mapping, the links may not contain the standard parameter utm\_source\=google. Instead, they will include a unique parameter gclid. Using an additional paid sources parameter, you will ensure correct tracking and attribution of traffic from Google Ads.


4\. Click Save.

### How to obtain the values of postback\_key and campaign\_code parameters?


If you have a manager, ask them for the values of the postback\_key and campaign\_code parameters.


If you have access to the account, you can obtain the values of these parameters in your account:


1\. Go to the Integration section (Program → Integration).


2\. Click Next and on the Integration methods page select the Custom integration tab.


3\. On the Custom integration tab, select Postback and click Next — the values of the postback\_key and campaign\_code parameters are shown in the table at the top of the screen (section Integration setup: unique parameter values for your program).

## How to test the integration after setup


For new advertisers, integration testing is performed during onboarding or with a manager, not via the account.


1\. Get a test affiliate link on the Setting up integration for Shopify page in the Integration testing block.

How to find the Integration testing block (expand)
1\.1 In your account, go to the Integration section (Program → Integration).


1\.2 Then click Next and on the Integration methods page select Shopify. Click Next.


1\.3 The Integration testing block is located at the bottom of the screen.

  
2\. Follow the link and perform the target action according to your program terms.

Recommendations for integration testing:

- Include several product items in one of the test orders to ensure that the items and the total order amount are transmitted correctly.
- If you have a quick or "One\-Click" order form, place an order through it to test the form integration.


The test order will appear in Admitad reports within an hour.


If after an hour or more the order does not appear in the reports, check that the integration setup is correct. If the problem persists, report it to an Admitad specialist.


3\. Go to your Admitad account → Reports → By actions and check that the target action and its data are correctly displayed in the reports:

- the target action matches the affiliate program settings;
- The order ID in Admitad matches the order ID in your system;
- The order amount in Admitad matches the amount of the test order.


4\. Inform an Admitad specialist that testing is complete — the program will be queued for launch.


You're all set! Integration testing is complete.

## How to remove the plugin from your site


1\. Open the admin panel of your website and go to Settings → Apps and sales channels.


2\. In the row with the "Admitad Tracking" plugin name, click the three dots, then click Uninstall.
