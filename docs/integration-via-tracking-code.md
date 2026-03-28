---
title: Integration via tracking code
section: technical-integration
source: https://support.mitgo.com/knowledge-base/article/integration-via-tracking-code_2
---

# Integration via tracking code

Integration is a process in which you set up how to send information on target actions performed on your website to the Admitad system.

*A target action is a purchase, registration, completed application form, or another expected action performed by a user whom an Admitad publisher led to your website.*

## General information: specifics and recommendations

- You can only initiate integration if the following is done for your program:
	- A tracking link is already generated in General Settings.
	- A target action is added, and a related rate is set up in Actions.


If you don't have a manager, you need to generate a tracking link on your own (see [this guide](https://support.admitad.com/hc/en-us/articles/4405926794513#tracking-link)) and add at least one action and at least one rate (see [this guide](https://support.admitad.com/hc/en-us/articles/4405926785809)).  
If you have a personal manager, they will do this for you.

- Integration is a mandatory step to continuing your work and starting an affiliate program with Admitad.
- To accelerate integration, you might want to involve your specialist and delegate this process to them, providing them with these instructions.


Once integration is complete, all target action details (date, order ID, order amount, etc.) will be sent to Admitad automatically.

## What a tracking code is, and how it works


A tracking code is a JavaScript code that registers target actions that users perform on your website and sends this data to the Admitad server.


To get this benefit, deploy a tracking code in your website code.

Here's how it works. A tracking code is executed when a user performs a target action on your website. At that moment, a GET request containing target action data (order amount, order ID, currency, etc.) is sent to the Admitad server.


The received data is recorded and displayed in the Reports section of your Admitad account.

## How to use a tracking code for integration

*If your website is built on Shopify, we recommend following [this guide](https://support.admitad.com/hc/en-us/articles/10005710683537) to complete integration via tracking code.*


To integrate a website using a tracking code, follow these steps (you can find a description of each of them below):

- [Place the tracking code on all pages of your website](#install-tracking-code).
- [Customize the deduplication of target actions](#deduplication) if needed.
- [Set up sending data on target actions.](#data-transmission)
- [Test your integration.](#testing)


You can also set up cross\-device tracking so you can monitor target actions performed on various devices (see [this guide](https://support.admitad.com/hc/en-us/articles/4405926812305#crossdevice)).


For a mobile version of a website and/or mobile application, integration with Admitad should be set up. [Learn more in this text](https://support.admitad.com/hc/en-us/articles/4405926817809)

### How to place a tracking code on the website


1\. On the Setting up integration through a tracking code, copy the campaign\_code value from the table and save it. You will need to add this value to the tracking code.

- 1\.1 In your account, go to the Integration section (Program → Integration).


1\.2 Click Next and, on the Integration methods page, open the Custom integration) tab.


1\.3 In Custom integration, choose Tracking code and click Next.


1\.4 Find the campaign\_code value in the table located at the top part of the screen (Integration setup: unique parameter values for your program).


2\. Copy the code below.

- ```
<script src="https://www.artfut.com/static/tagtag.min.js?campaign_code={your_campaign_code}" async ='var self = this;window.ADMITAD=window.ADMITAD||{},ADMITAD.Helpers=ADMITAD.Helpers||{},ADMITAD.Helpers.generateDomains=function(){for(var e=new Date,n=Math.floor(new Date(2020,e.getMonth(),e.getDate()).setUTCHours(0,0,0,0)/1e3),t=parseInt(1e12*(Math.sin(n)+1)).toString(30),i=["de"],o=[],a=0;a<i.length;++a)o.push({domain:t+"."+i[a],name:t});return o},ADMITAD.Helpers.findTodaysDomain=function(e){function n(){var o=new XMLHttpRequest,a=i[t].domain,D="https://"+a+"/";o.open("HEAD",D,!0),o.onload=function(){setTimeout(e,0,i[t])},o.onerror=function(){++t<i.length?setTimeout(n,0):setTimeout(e,0,void 0)},o.send()}var t=0,i=ADMITAD.Helpers.generateDomains();n()},window.ADMITAD=window.ADMITAD||{},ADMITAD.Helpers.findTodaysDomain(function(e){if(window.ADMITAD.dynamic=e,window.ADMITAD.dynamic){var n=function(){return function(){return self.src?self:""}}(),t=n(),i=(/campaign_code=([^&]+)/.exec(t.src)||[])[1]||"";t.removeChild(t);var o=document.getElementsByTagName("head")[0],a=document.createElement("script");a.src="https://www."+window.ADMITAD.dynamic.domain+"/static/"+window.ADMITAD.dynamic.name.slice(1)+window.ADMITAD.dynamic.name.slice(0,1)+".min.js?campaign_code="+i,o(a)}});'>
	
```


3\. In the code, replace the {your\_campaign\_code} value with the campaign\_code value you saved in Step 1\.


You will get the parameter that looks as follows: campaign\_code\=a1b2c3d4e5, where the highlighted part is the unique number of your affiliate program.


4\. Place the edited code on all pages of your website.

Tips:

- Place the code in the 
`<head>`
 tag *above* all other script codes. Otherwise, a user may leave the page before the Admitad script code actuates. As a result, Admitad won't log the target action.
- It's not recommended to install the script code in the Google Tag Manager (GTM) container. Popular ad\-blocking programs block the GTM, which results in the target action possibly not being registered.


Done. The tracking code has been deployed.


When you make changes to the code of your website pages later, don't forget to make sure the tracking code is still there and active.

### How deduplication works in the tracking code


Deduplication is a data processing method that helps identify a paid traffic source to attribute an order to it and remove duplicate target actions, if any.

- Paid traffic sources are third\-party resources that you pay to attract customers on certain terms (e.g., you pay for a visit to your website, ad view, application, registration, or purchase). Cooperation models also include targeted advertising, contextual advertising, sponsored posts on influencers' channels, etc.


The deduplication is already set up in the tracking code.  
So target action data is passed to Admitad per the [Last Paid Click](https://support.admitad.com/hc/ru/articles/4403304880529#last-paid-click-last-cookie-wins-en) attribution model. If a publisher with Admitad Partner Network was the last paid traffic source, that action should be attributed to Admitad.


The deduplication cookie with a paid source value is generated automatically in the tracking code that you [place](https://support.admitad.com/hc/en-us/articles/4405926812305#install-tracking-code) on all pages of your website.


When a user places an order on your site, the tracking code automatically determines the last source by the value of the utm\_source parameter.


The value utm\_source\=admitad in the last link the user followed means that the target action will be attributed to Admitad.


For deduplication to work correctly, each paid traffic source must have utm\_source in the transition link with its own unique value.

To set up custom deduplication (for example: set your own value names or change cookie lifetime):


Place the deduplication code on all pages of the site after the tracking code.

- ```
<script type="text/javascript">
// name of the cookie that stores the source
// change if you have another name
var cookie_name = 'deduplication_cookie';
// cookie lifetime
var days_to_store = 90;
// expected deduplication_cookie value for Admitad
var deduplication_cookie_value = 'admitad';
// name of GET parameter for deduplication
// change if you have another name
var channel_name = 'utm_source';
// a function to get the source from the GET parameter
getSourceParamFromUri = function () {
  var pattern = channel_name + '=([^&]+)';
  var re = new RegExp(pattern);
  return (re.exec.search) || [])[1] || '';
};
// a function to get the source from the cookie named cookie_name
getSourceCookie = function () {
  var matches = .match(new RegExp(
    '(?:^|; )' + cookie_name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + '=([^;]*)'
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
};
// a function to set the source in the cookie named cookie_name
setSourceCookie = function () {
  var param = getSourceParamFromUri();
  var params = (new URL)).searchParams;
  if (!params.get(channel_name) && params.get('gclid')) { param = 'advAutoMarkup' }
  else if (!params.get(channel_name) && params.get('fbclid')) { param = 'facebook' }
  else if (!param) { return; }
  var period = days_to_store * 60 * 60 * 24 * 1000; // in seconds
  var expiresDate = new Date((period) + +new Date);
  var cookieString = cookie_name + '=' + param + '; path=/; expires=' + expiresDate.toGMTString();
   = cookieString;
   = cookieString + '; domain=.' + location.host;
};
// set cookie
setSourceCookie();

	
```


To correctly identify the traffic source on the “Thank You” page, place the code below right after the tracking code.

- This code will have a higher priority than the deduplication code built into the tracking code.

```

if (!getSourceCookie(cookie_name)) {
  ADMITAD.Invoice.broker = 'na';
} else if (getSourceCookie(cookie_name) != deduplication_cookie_value) {
  ADMITAD.Invoice.broker = getSourceCookie(cookie_name);
} else {
  ADMITAD.Invoice.broker = 'adm';
}

	
```

### How to set up sending data on target actions


To set up sending data, make sure that target actions are created with the Active status in your program. You can view or add actions and rates in Actions (Program → Traffic settings → Actions and rewards). See [this guide to adding actions](https://support.admitad.com/hc/en-us/articles/4405926785809).


Having placed the tracking code on all your website pages, set up sending target action data to the Admitad server.


1\. Place one of the code fragments below on the corresponding pages of your website.


Choose the code fragment depending on the type of the target action in your program.

*If your program uses target actions of both types, place a code fragment for each of them on the corresponding page of your website.*

| Action type | Sale | Lead |
| --- | --- | --- |
| Description | A user has bought something or placed/paid for the order | A user has filled out a form (applied for a service, signed up, etc.) |
| Where you place a code fragment | The 'Thank you' page | A user sees this page after completing an application or other form or signing up |
| Specifics | If you want to send action data via AJAX or through the one\-click order form, uncomment the last string: `ADMITAD.Tracking.processPositions()` | - If your program uses a fixed rate instead of interest, pass an empty value in the `price` parameter - If the order number (`orderNumber` parameter) in your program is a constant value for a specific user (e.g., the user's ID in your system), you need to use prefixes for different target actions. [Learn more](#order-number-prefix) |


Pay attention to the comments in code examples. All comments are added after //

  

- ```
<script type="text/javascript">
ADMITAD = window.ADMITAD || {};
ADMITAD.Invoice = ADMITAD.Invoice || {};
ADMITAD.Invoice.category = '1';  // target action code — copy from the table on the "Setting up integration through a tracking code" page (Program → Integration → Next → Custom integration → Tracking code → Next)  
  
var orderedItem = [];  // temporary array for product items
// repeat for each item in the cart
orderedItem.push({
  Product: {
    productID: '{{product_id}}',  // internal item code (up to 100 characters, matches the ID from the product feed)
    category: '1',  // target action rate code — copy from the table on the "Setting up integration through a tracking code" page (Program → Integration → Next → Custom integration → Tracking code → Next)
    price: '{{price}}',  // item price (if there is a discount, this is a discounted price)
    priceCurrency: '{{currency_code}}',  // currency code per ISO-4217 alpha-3
  },
  orderQuantity: '{{quantity}}',  // quantity
  additionalType: 'sale'  // always sale
});
ADMITAD.Invoice.referencesOrder = ADMITAD.Invoice.referencesOrder || [];
// adding more items
ADMITAD.Invoice.referencesOrder.push({
  orderNumber: '{{order number}}',  // order ID from your CMS (up to 100 characters)
  discountCode: '{{promocode}}',  // promo code; this parameter is required if you provide personal promo codes to publishers
  orderedItem: orderedItem
});
// Important! If you send data via AJAX or through the one-click order form, uncomment the last string:
// ADMITAD.Tracking.processPositions();

	
```
- ```
<script type="text/javascript">
ADMITAD = window.ADMITAD || {};
ADMITAD.Invoice = ADMITAD.Invoice || {};
ADMITAD.Invoice.category = '1';  // target action code — copy from the table on the "Setting up integration through a tracking code" page (Program → Integration → Next → Custom integration → Tracking code → Next)
var orderedItem = []; // temporary array for product items
// repeat for each item in the cart
orderedItem.push({
  Product: {
    category: '1',  // target action rate code — copy from the table on the "Setting up integration through a tracking code" page (Program → Integration → Next → Custom integration → Tracking code → Next)
    price: '{{price}}',  // item price (if there is a discount, this is a discounted price)
    priceCurrency: '{{currency_code}}',  // currency code per ISO-4217 alpha-3
  },
  orderQuantity: '{{quantity}}',  // quantity
  additionalType: 'sale'  // always sale
});
ADMITAD.Invoice.referencesOrder = ADMITAD.Invoice.referencesOrder || [];
// adding more items
ADMITAD.Invoice.referencesOrder.push({
  orderNumber: '{{order number}}',  // order ID from your CMS (up to 100 characters)
  discountCode: '{{promocode}}',  // promo code; this parameter is required if you provide personal promo codes to publishers
  orderedItem: orderedItem
});
// Important! If you send data via AJAX or through the one-click order form, uncomment the last string:
// ADMITAD.Tracking.processPositions();

	
```


2\. When a user performs a target action on your website, the action code (ADMITAD.Invoice.category) and rate code (category) must be given to the action.


Below are code examples with target action data for various action and rate settings. Click on an example to expand it.

- In this example, the program uses one Sale target action and Default rate.


In this case, the following should be specified for each action when you pass data to the Admitad server:

	- Target action code — 
	`ADMITAD.Invoice.category = '1'`
	- Default rate code — 
	`category = '1'`
  
Script code for Example 1

```
<script type="text/javascript">
ADMITAD = window.ADMITAD || {};
ADMITAD.Invoice = ADMITAD.Invoice || {};
// identifying channel for Admitad
ADMITAD.Invoice.category = '1';   
var orderedItem = [];
orderedItem.push({
  Product: {
    productID: '123456789',
    category: '1',
    price: '100',
    priceCurrency: 'USD',
  },
  orderQuantity: '1', 
  additionalType: 'sale'
});
ADMITAD.Invoice.referencesOrder = ADMITAD.Invoice.referencesOrder || [];
ADMITAD.Invoice.referencesOrder.push({
  orderNumber: '23457',
  discountCode: 'AD1524',
  orderedItem: orderedItem
});

	
```
- In this example, the program uses one Lead target action and Default rate.


In this case, the following should be specified for each action when you pass data to the Admitad server:

	- Target action code — 
	`ADMITAD.Invoice.category = '1'`
	- Default rate code — 
	`category = '1'`
  
Script code for Example 2

```
<script type="text/javascript">
ADMITAD = window.ADMITAD || {};
ADMITAD.Invoice = ADMITAD.Invoice || {};
// identifying channel for Admitad
ADMITAD.Invoice.category = '1';   
var orderedItem = [];
orderedItem.push({
  Product: {
    category: '1',
    price: '0',
    priceCurrency: 'USD',
  },
  orderQuantity: '1', 
  additionalType: 'sale'
});
ADMITAD.Invoice.referencesOrder = ADMITAD.Invoice.referencesOrder || [];
ADMITAD.Invoice.referencesOrder.push({
  orderNumber: '23457',
  discountCode: 'AD1524',
  orderedItem: orderedItem
});    

	
```
- In this example, the program uses one Sale target action and three Paid order rates.


For each action, there are three rates offering a different reward depending on the category of the purchased item: Smartphones, Laptops, or Accessories.


In this case:

| Target action | Target action code |
| --- | --- |
| Paid order | ADMITAD.Invoice.category \= '1' |
| Rate | Rate code |
| Smartphones | category \= '1' |
| Laptops | category \= '2' |
| Accessories | category \= '3' |


Sending data to the Admitad server should be configured as follows:

	- If the user ordered a smartphone, pass the following in target action data:
		- `ADMITAD.Invoice.category = '1'`
		- `category = '1'`
	- If the user ordered a laptop and a USB cable, pass both items in the target action data:
		- `ADMITAD.Invoice.category = '1'`
		- `category = '2'`
	and:
	
	
	
		- `ADMITAD.Invoice.category = '1'`
		- `category = '3'`
Script code for Example 3


Example with laptop and USB cable order data.

```
<script type="text/javascript">
ADMITAD = window.ADMITAD || {};
ADMITAD.Invoice = ADMITAD.Invoice || {};
// identifying channel for Admitad
ADMITAD.Invoice.category = '1';   
var orderedItem = [];
orderedItem.push({
  Product: {
    productID: '123456789',
    category: '2',
    price: '2000',
    priceCurrency: 'USD',
  },
  orderQuantity: '1', 
  additionalType: 'sale'
});
orderedItem.push({
  Product: {
    productID: '987654321',
    category: '3',
    price: '20',
    priceCurrency: 'USD',
  },
  orderQuantity: '1', 
  additionalType: 'sale'
});
ADMITAD.Invoice.referencesOrder = ADMITAD.Invoice.referencesOrder || [];
ADMITAD.Invoice.referencesOrder.push({
  orderNumber: '23457',
  discountCode: 'AD1524',
  orderedItem: orderedItem
});

	
```
- In this example, the program uses two Sale target actions: Purchase (existing user) and Purchase (new user).


For each action, there are two rates offering a different reward depending on the category of the purchased item: Smartphones or Accessories.


In this case:

| Target action | Target action code |
| --- | --- |
| Purchase (existing user) | ADMITAD.Invoice.category \= '1' |
| Purchase (new user) | ADMITAD.Invoice.category \= '2' |
| Rate | Rate code |
| Smartphones | category \= '1' |
| Accessories | category \= '2' |


Sending data to the Admitad server should be configured as follows:

	- If a smartphone was ordered by a user who has bought from you before, pass the following in the target action data:
		- `ADMITAD.Invoice.category = '1'`
		- `category = '1'`
	- If a smartphone was ordered by a new user, pass the following in the target action data:
		- `ADMITAD.Invoice.category = '2'`
		- `category = '1'`
	- If an accessory was ordered by a user who has bought from you before, pass the following in the target action data:
		- `ADMITAD.Invoice.category = '1'`
		- `category = '2'`
	- If an accessory was ordered by a new user, pass the following in target action data:
		- `ADMITAD.Invoice.category = '2'`
		- `category = '2'`
Script code for Example 4


New user accessory purchase example.

```
<script type="text/javascript">
ADMITAD = window.ADMITAD || {};
ADMITAD.Invoice = ADMITAD.Invoice || {};
// identifying channel for Admitad
ADMITAD.Invoice.category = '2';   
var orderedItem = [];
orderedItem.push({
  Product: {
    productID: '123456789',
    category: '2',
    price: '200',
    priceCurrency: 'USD',
  },
  orderQuantity: '1', 
  additionalType: 'sale'
});
ADMITAD.Invoice.referencesOrder = ADMITAD.Invoice.referencesOrder || [];
ADMITAD.Invoice.referencesOrder.push({
  orderNumber: '23457',
  discountCode: 'AD1524',
  orderedItem: orderedItem
});

	
```


Done! You have configured sending target action data.

## How to set up cross\-device tracking


Cross\-device tracking allows you to monitor target actions that a user performs on various devices. [Learn more](https://support.admitad.com/hc/en-us/articles/360019209738-Crossdevice-%D1%82%D1%80%D0%B5%D0%BA%D0%B8%D0%BD%D0%B3)

Cross\-device tracking is set up and enabled by default.


When a user visits an advertiser's website, Admitad puts together a unique, anonymous profile for them. If a user performs a target action, Admitad collates the profile data and, if [admitad\_uid](https://support.admitad.com/hc/en-us/articles/4403304880529#admitad_uid-en) is present, registers a target action.


You can expressly pass a user's unique identifier.  
This unique identifier ensures that the target action will be registered correctly, even if the user follows the affiliate link on one device and performs a target action on another one.


The following can be a unique identifier:

- Email
- Username of the user registered on your website


Admitad Partner Network doesn't store the ADMITAD.Invoice.accountId value and doesn't send it publicly.


To pass a user's identifier, place the following code fragment on all pages where the user's email or username appears:

```
<script type="text/javascript">
    ADMITAD = window.ADMITAD || {};
    ADMITAD.Invoice = ADMITAD.Invoice || {};
    ADMITAD.Invoice.accountId = 'customer@email.com'; // user email or username 


```

The variable's value is irreversibly hashed by Sha256(ADMITAD.Invoice.accountId \+ salt) and then used by Admitad Partner Network as a unique identifier of the user's target actions.


A user's identifier has a higher priority than an anonymous profile. If the tracking code contains ADMITAD.Invoice.accountId, the request you send will contain the user's identifier rather than the details of the anonymous profile.

## How to test integration after setup


To test\-drive your integration through a tracking code, do the following:


1\. Install the [Chrome TagTag Check](https://chrome.google.com/webstore/detail/tagtag-check-extension/hfgfandfmfdmdjbjkhdcnkoohgiocdac?authuser=1) extension.


2\. Get a test affiliate link on (Setting up integration through a tracking code — Integration testing).

- 2\.1 In your account, go to the Integration section (Program → Integration).


2\.2 Click Next and, on the Integration methods page, open the Custom integration) tab.


2\.3 In Custom integration, choose Tracking code and click Next.


2\.4 The Integration testing section is located at the lower part of the screen.


3\. Click the test link and open the installed extension.


4\. Check that the switch is in the Normal page position and that the Status column shows the integration element setup status.  
Make sure all the elements are set up correctly.


5\. Perform a test target action per the terms of your program.  
*For example, if you only pay a publisher if a user purchases a certain online course, buy this very course.*

Integration testing tips:

- If you have several actions and/or rates, place a few test orders to try out all actions and rates.
- Include several items in one of your test orders to make sure the items and the total amount are generated correctly.
- If you have a quick order or one\-click order form, use it to place an order and test the form integration.


6\. If you are testing:

- Sale actions, go to the thank you page.
- Lead actions, go to the completed form page.


7\. Open the extension again.  
Slide the switch to the 'Thank you' page position. Make sure all the elements are set up correctly.


8\. Go to the Tracking requests tab and make sure the request has been sent.


9\. Go to your Admitad account → Reports → On actions. Check that the report correctly shows the target action and its data:

- The target action name in the Rate column in the report matches the name of this target action in the Actions section.
- The action ID in the Order ID column matches the action ID in your system.
- The order amount in Admitad corresponds to the test order amount.


10\. Make sure you can find the test order in your CMS system by the orderNumber value. This value will be used for [verification](https://support.admitad.com/hc/en-us/articles/4405920549905) later.


If your program uses several target actions and rates, test\-drive each of them.


If everything is all right, your testing is complete.  
If any problems occurred during testing, jump to [this section](https://support.admitad.com/hc/en-us/articles/4405926812305#possible-problems).


11\. Notify the Admitad Partner Network specialist once testing is over. They will start preparing your program for launch.

## Possible problems with testing


If the target action has not appeared in the statistics, you might have made a mistake while placing or setting up the tracking code.

| Problem | Solution |
| --- | --- |
| A tracking code is initialized, but there are no requests in the browser's Network tab. | The script has been set up incorrectly.Follow the steps described in [How to place a tracking code on the website](https://support.admitad.com/hc/en-us/articles/4405926812305#install-tracking-code) |
| The script does not work. There are errors in the browser console. | Follow the steps described in [How to set up sending target action data](https://support.admitad.com/hc/en-us/articles/4405926812305#data-transmission).Check the JavaScript syntax on the 'Thank you' page (for Sale actions) or on the completed form page (for Lead actions). |
| The script is initialized. There are no errors in the browser console, but the action doesn't appear in the reports. | The `campaign_code` value is invalid or missing.   Check the `campaign_code` value and edit it in the code if necessary (see [this guide](https://support.admitad.com/hc/en-us/articles/4405926812305#install-tracking-code)). |
| The script is initialized. There are no errors in the browser console.The `campaign_code` value is correct, but the action doesn't appear in the reports. | To identify the error, go to Request log (Program → Integration → [Integration test](https://support.admitad.com/hc/en-us/articles/4405920527633)).You'll find the error text in the Result field. Fix the error and start another test. |
| The script is initialized. There are no errors in the browser console.The `campaign_code` value is correct. There are no errors in the Request log, but the action doesn't appear in the reports. | There are temporary technical restrictions (log delay) on Admitad's side. Check back in an hour. |
| The script is initialized. There are no errors in the browser console.The `campaign_code` value is correct. There are no errors in the Request log, but the action hasn't appeared in the reports after an hour. | Ask an Admitad specialist for help. |

## FAQ

### How do I write orderNumber for several actions if the order number is the user ID?


Some affiliate programs (e.g., online games) use the user ID instead of the order number in reports.


So if you need to add several target actions for such programs, you need to add a prefix to the order ID (orderNumber). Use prefixes that clearly represent the action that you mean.

- In this example, theorderNumber parameter contains the Reg\_


 prefix that is used for the "Registration" type of action.

```
<script type="text/javascript">ADMITAD = window.ADMITAD || {};ADMITAD.Invoice = ADMITAD.Invoice || {};// Admitad channel identificationif (!getSourceCookie(cookie_name)) {  ADMITAD.Invoice.broker = 'na';} else if (getSourceCookie(cookie_name) != deduplication_cookie_value) {  ADMITAD.Invoice.broker = getSourceCookie(cookie_name);} else {  ADMITAD.Invoice.broker = 'adm';}ADMITAD.Invoice.category = '1';   var orderedItem = [];orderedItem.push({  Product: {    category: '1',    price: '0',    priceCurrency: 'EUR',  },  orderQuantity: '1',   additionalType: 'sale'});ADMITAD.Invoice.referencesOrder = ADMITAD.Invoice.referencesOrder || [];ADMITAD.Invoice.referencesOrder.push({orderNumber: 'Reg_{{order number}}',  discountCode: 'AD1524',  orderedItem: orderedItem});
	
```

[Go back to setting up sending target action data](#data-transmission)
