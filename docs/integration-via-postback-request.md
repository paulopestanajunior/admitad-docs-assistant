---
title: Integration via postback request
section: technical-integration
source: https://support.mitgo.com/knowledge-base/article/integration-via-postback-request_2
---

# Integration via postback request

Integration is a process in which you set up how to send information on target actions performed on your website to the Admitad system.

*A target action is a purchase, registration, completed application form, or other expected action performed by a user whom an Admitad publisher led to your website.* 

## General information: specifics and recommendations

- You can only initiate integration if the following is done for your program:
	- A tracking link is already generated in General Settings.
	- A target action is added, and a related rate is set up in Actions.


If you don't have a manager, you need to generate a tracking link on your own (see [this guide](https://support.admitad.com/hc/en-us/articles/4405926794513#tracking-link)) and add at least one action and at least one rate (see [this guide](https://support.admitad.com/hc/en-us/articles/4405926785809)).  
If you have a personal manager, they will do this for you.

- Integration is a mandatory step to continuing your work and starting an affiliate program with Admitad.
- To accelerate integration, you might want to involve your specialist and delegate this process to them, providing them with these instructions.


Once integration is complete, all target action details (date, order ID, order amount, etc.) will be sent to Admitad automatically.

## What integration via postback request is, and how it works

 *To implement integration via postback, you need to have access to your project's back end.*

Here's how it works:


1\. Your server sends all information on what users did on your website to the Admitad server.


2\. The Admitad server receives this information, after which it appears in reports.


If your website is CMS\-based (e.g., built on 1C\-Bitrix, WordPress, or Shopify), use plugins for faster integration with Admitad. [Guide to integration via plugins](https://support.admitad.com/hc/en-us/articles/4405920529169)


Read more about other integration methods in [Choosing an integration method](https://support.admitad.com/hc/en-us/articles/4405926820113).

Benefits of integration via postback

- This is the most secure integration method since a request contains a private authorization key. On top of that, requests are sent from known IPs, and you can check the source of these requests in logs.
- Since information is sent through the back end, you can make changes to your website with almost no risk of disrupting target action tracking.

## How to set up integration via postback


To integrate a website using a postback request, follow these steps (you can find a description of each of them below):

- [Set up writing *admitad\_uid* to cookie files](#how-to-set-admitad_uid-in-cookies).
- [Set up deduplication of target actions](#how-to-set-deduplication).
- [Set up sending a postback request](#how-to-set-postback-request).
- [Test\-drive your integration](#how-to-test-postback-request).


If there are both web and mobile versions of the website and/or a quick order form or a one\-click order form, set up sending postback requests for them, as well.

### How to set up writing the value from the admitad\_uid GET parameter to cookies


The

`admitad_uid`
 value is registered when a user visits your website. Save this value in the cookie file and keep it there for as many days as specified in your agreement with Admitad.


Use the script to set up writing the

`admitad_uid`
 value to a cookie file.


Add the

`admitad_uid`
 value tracking code to all pages of your website. You need to do this because the user can go to any page of your website through the link.


Neither the cookie nor its lifetime must be modified when a user comes from free sources like organic search or email newsletter. Admitad uses the [Last Paid Click](https://support.admitad.com/hc/en-us/articles/4403304880529#last-paid-click-last-cookie-wins-en) attribution model, where the action is attributed to the last paid traffic source.

*Below are examples for a JavaScript and a PHP script. You can use one of these or any other programming language.*


Pay attention to the comments in code examples. All comments are added after //.

- ```
if (isset($_GET['admitad_uid'])) {  
$days = 90; // Cookie lifetime (days)  
setcookie('_aid', $_GET['admitad_uid'], time() + 60 * 60 * 24 * $days, '/');  
}  
  
function get_admitad_uid() {  
if (!isset($_COOKIE['_aid'])) {  
return null;  
}  
  
return $_COOKIE['_aid'];  
}
	
```
- ```
<script type="text/javascript">  
//Cookie lifetime (days)  
var days_to_store = 90;  
  
//Parameters for creating a cookie containing the Admitad UID value  
var uid_cookie_name = 'admitad_uid'; // Name of cookie storing admitad_uid  
var uid_channel_name = 'admitad_uid'; // function for receiving a source from the GET parameter  
  
function getParamFromUriAdmitad (get_param_name) {  
  var pattern = get_param_name + '=([^&]+)';  
  var re = new RegExp(pattern);  
  return (re.exec.search) || [])[1] || '';  
};  
  
// function for writing the source to the cookie named cookie_name  
function setAdmitadCookie (param_name, cookie_name) {  
var param = getParamFromUriAdmitad(param_name);  
if (!param) { return; }  
  var period = days_to_store * 60 * 60 * 24 * 1000;   // in seconds  
  var expiresDate = new Date((period) + +new Date);  
  var cookieString = cookie_name + '=' + param + '; path=/; expires=' + expiresDate.toGMTString();  
   = cookieString;  
   = cookieString + '; domain=.' + location.host;  
};  
  
// writing value to cookie  
setAdmitadCookie(uid_channel_name, uid_cookie_name);  
  

	
```

### How to set up deduplication


Deduplication is a data processing method that helps identify a paid traffic source to attribute an order to it and remove duplicate target actions if any.

- Paid traffic sources are third\-party resources that you pay to attract customers on certain terms (e.g., you pay for a visit to your website, ad view, application, signup, or purchase). Paid traffic sources include targeted and contextual ads, sponsored posts on social media and profiles of opinion leaders, etc.


Setting up deduplication is a required step to complete integration, even if you only cooperate with one paid traffic source (Admitad Partner Network).


After you set up deduplication, target action data is passed to Admitad under the Last Paid Click attribution model. If a publisher with Admitad was the last paid traffic source, that action should be attributed to Admitad.


You can use the following methods to set up deduplication of target actions:

Method 1


1\. Set up creating the cookie that will store the last paid traffic source on all pages of your website. By default, Admitad passes the parameter

`utm_source=admitad`
.


2\. Set up sending postback requests for the cases when a traffic source cookie stores an

`admitad`
 value.

Method 2


If there was a transition with the traffic source GET parameter different from Admitad, set up deleting the *admitad\_uid* cookie.

### How to set up sending a postback request


Set up sending a postback request of the following type:

```
https://ad.admitad.com/r?campaign_code=your_campaign_code&postback=1&postback_key=your_postback_key&action_code=1&uid=admitad_uid&order_id=123456&tariff_code=1&currency_code=USD&price=1234&quantity=2&position_id=1&position_count=1&product_id=1&client_id=&payment_type=sale

```

You need to use the [required parameters](#required-parameters). If necessary, you can add [additional parameters](#additional-parametrs) to the request.


The values of the customer's order should be substituted in the parameters.  
Note: You have to set up the logic of parameter substitution on your own.  
[Examples of postback requests](#postback-requests-examples)


The Admitad server doesn't have any special response to postback requests.  
You will always see the status "HTTP 200 OK".

#### Required parameters


The set of required parameters depends on the type of target action that you expect from the user.


Action types:

- Sale. A user has bought something or placed/paid for the order.
- Lead. A user has filled out a form and sent their data (e.g., applied for a service, signed up, etc.).


Click the relevant action type to expand the table with the required parameters.


To see actions in your affiliate program, go to your account → Program → Actions and rewards.

- In the Parameter name, the main parameters are highlighted in bold, and in italics are aliases, which are additional names of the main parameter.  
In settings, you can specify not the main parameter itself but its alias, and Admitad will be able to process it.

| Parameter name | Description | Type | Note |
| --- | --- | --- | --- |
| uid | Admitad ID | String | A generated value passed in `admitad_uid` when the user logs in to the site.   If you allow [contextual ads](https://support.admitad.com/hc/en-us/articles/4403304880529#contextual-advertising-en), at the moment when a user clicks on a contextual ad placed by publishers through Google Ads, the gclid value [generated by Google](https://support.admitad.com/hc/en-us/articles/360019066437) will be written to `admitad_uid` instead of uid.   To make sure action tracking runs smoothly, your server must accept and pass the gclid value as a whole. [Learn more about gclid length](https://support.google.com/analytics/answer/2938246?hl=ru#:~:text=%D0%94%D0%BB%D0%B8%D0%BD%D0%B0%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%B0%20GCLID,%D0%B4%D0%BB%D0%B8%D0%BD%D0%B0%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20gclid%20%E2%80%93%20100%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2)   Example: *03b374fa9c2f34069e8df0bda61b8627* |
| campaign\_code | Program code | String, 10 characters | A constant whose value is defined in the postback request.   Example: *1a2b3c4d5e*.   [How to find a program code](#campaign-code-parameter) |
| order\_id, *oid* | Your internal order ID | String, 1 to 100 characters | Your internal order ID.   Note: Make sure you can find the order by this ID in your CRM system. This ID will be used during [verification](https://support.admitad.com/hc/en-us/articles/4405920549905). |
| action\_code, *ac*, *product*, *product\_code* | Target action code | Integer | A variable which is the target action code from your program settings.   [How to find an action code](#action-code-parameter)   Note: If you need to set up passing several actions and rates, go to [this section](#how-to-set-request-for-several-actions-and-tariffs). |
| tariff\_code, *tc* | Rate code | Integer | A variable which is the rate code from your program settings.   [How to find a rate code](#tariff-code-parameter)   Note: If you need to set up passing several actions and rates, go to [this section](#how-to-set-request-for-several-actions-and-tariffs). |
| currency\_code, *currency*, *c* | Currency code | String, 3 characters | Defined in ISO 4217\. Letters only.   Example:*EUR, USD*. |
| position\_id, *pid* | Item number in cart | Integer | A variable varying from 1 to N, where N \= position\_count. |
| position\_count, *pc*, *pn* | Items in cart | Integer | A variable with the value N that depends on what's in the user's cart. |
| payment\_type | Target action type | String, 4 characters | A constant with the value "sale". |
| product\_id, *prid* | Your internal item ID | String, 1 to 100 characters | Product ID that must match the ID from the product feed if you use this tool.   [Learn more about the product feed](https://support.admitad.com/hc/en-us/articles/4405920538897) |
| quantity | Product quantity | Integer |  |
| postback, *pb* | Postback request authorization key | String, 1 character | A constant with the value "1". |
| postback\_key, *postback\_hash*, *pk* | Postback request identification key | String, 32 characters | A constant whose value is defined in the postback request.   Example: *pKetl7uIt8GgZ3yDChh9y4cUKf5FblBS*   [How to find the parameter value](#postback-key-parameter) |
| price, *cart*, *p*, *amount* | Product price | Integer or decimal | Use a period as a divider.   Example:  	- Correct: 2\.65 	- Incorrect: 2,65 |
- In the Parameter name, the main parameters are highlighted in bold, and in italics are aliases, which are additional names of the main parameter.  
In settings, you can specify not the main parameter itself but its alias, and Admitad will be able to process it.

| Parameter name | Description | Type | Note |
| --- | --- | --- | --- |
| uid | Admitad Partner Network ID | String | A generated value passed in the `admitad_uid` parameter when the user logs in to the site.   If you allow [contextual ads](https://support.admitad.com/hc/en-us/articles/4403304880529#contextual-advertising-en), at the moment a user clicks the contextual ads placed by publishers through Google Ads, the gclid value [generated by Google](https://support.admitad.com/hc/en-us/articles/360019066437) will be written to `admitad_uid` instead of uid.   To make sure action tracking runs smoothly, your server must accept and pass the gclid value as a whole. [Learn more about gclid length](https://support.google.com/analytics/answer/2938246?hl=ru#:~:text=%D0%94%D0%BB%D0%B8%D0%BD%D0%B0%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%B0%20GCLID,%D0%B4%D0%BB%D0%B8%D0%BD%D0%B0%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20gclid%20%E2%80%93%20100%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2)   Example: *03b374fa9c2f34069e8df0bda61b8627* |
| campaign\_code | Program code | String, 10 characters | A constant whose value is defined in the postback request.   Example: *1a2b3c4d5e*   [How to find a program code](#campaign-code-parameter) |
| order\_id, *oid* | Your internal order ID | String, 1 to 100 characters | Your internal order ID.   Note: Make sure you can find the order by this ID in your CRM system. This ID will be used during [verification](https://support.admitad.com/hc/en-us/articles/4405920549905).   If several target actions should be set up for your affiliate program but the user id will remain the same, add the prefix to the order ID. [Learn more](#order-id-prefix) |
| action\_code, *ac*, *product*, *product\_code* | Target action code | Integer | A variable which is the target action code from your program settings.   [How to find an action code](#action-code-parameter)   Note: If you need to set up passing several actions and rates, go to [this section](#how-to-set-request-for-several-actions-and-tariffs). |
| tariff\_code, *tc* | Rate code | Integer | A variable which is the rate code from your program settings.   [How to find a rate code](#tariff-code-parameter)   Note: If you need to set up passing several actions and rates, go to [this section](#how-to-set-request-for-several-actions-and-tariffs). |
| payment\_type | Target action type | String, 4 characters | A constant with the value "lead". |
| product\_id, *prid* | Your internal item ID | String, 1 to 100 characters | Product ID that must match the ID from the product feed if you use this tool.   [Learn more about the product feed](https://support.admitad.com/hc/en-us/articles/4405920538897) |
| postback, *pb* | Postback request authorization key | String, 1 character | A constant with the value "1". |
| postback\_key, *postback\_hash*, *pk* | Postback request identification key | String, 32 characters | A constant whose value is defined in the postback request.   [How to find the parameter value](#postback-key-parameter)   Example: *pKetl7uIt8GgZ3yDChh9y4cUKf5FblBS* |
| price, *cart*, *p*, *amount* | Product price | Integer or decimal | Use a period as a divider.   Example:  	- Correct: 2\.65 	- Incorrect: 2,65 |
- You can add additional parameters if you need to.


They can be used in the integration of programs with any action type.

| Parameter name | Description | Type | Note |
| --- | --- | --- | --- |
| client\_id | Your internal client ID |  |  |
| country\_code | Country code | String, 2 characters | Defined in ISO 3166\. Letters only.   Example: *RU, US, TR*.   Only use this parameter if you have set up geotargeting. |
| city | City name | String | Only use this parameter if you have set up geotargeting. |
| promocode | Unique promo code code | String, 255 characters | Use this parameter if you need to set up passing personal promo codes. [Learn more](#how-to-set-request-for-promocodes) |

#### Examples of postback requests


This section presents examples of postback requests for different types of target action.


Click an example to learn more about it.

- Below is an example of a cart with three items.

| Item | Product name | Price | Quantity | Cost |
| --- | --- | --- | --- | --- |
| 1 | TV | 20,000 | 2 | 40,000 |
| 2 | iPhone | 35,000 | 3 | 105,000 |
| 3 | Laptop | 50,000 | 1 | 50,000 |
|  |  |  | Total | 195,000 |


You have to send a postback request for each item.  
The values of the following parameters will vary in the requests presented in the example:

	- price (
	`price`
	)
	- quantity (
	`quantity`
	)
	- item number in cart (
	`position_id`
	)
	- internal product ID (
	`product_id`
	)
  
Postback request for the first item in the cart:

```
https://ad.admitad.com/r?campaign_code=your_campaign_code&postback=1&postback_key=your_postback_key&action_code=1&uid=03b374fa9c2f34069e8df0bda61b8627&order_id=123456&tariff_code=1&currency_code=USD&price=20000&quantity=2&position_id=1&position_count=3&product_id=11&client_id=&payment_type=sale
	
```

Postback request for the second item in the cart:

```
https://ad.admitad.com/r?campaign_code=your_campaign_code&postback=1&postback_key=your_postback_key&action_code=1&uid=03b374fa9c2f34069e8df0bda61b8627&order_id=123456&tariff_code=1&currency_code=USD&price=35000&quantity=3&position_id=2&position_count=3&product_id=21&client_id=&payment_type=sale
	
```

Postback request for the third item in the cart:

```
https://ad.admitad.com/r?campaign_code=your_campaign_code&postback=1&postback_key=your_postback_key&action_code=1&uid=03b374fa9c2f34069e8df0bda61b8627&order_id=123456&tariff_code=1&currency_code=USD&price=50000&quantity=1&position_id=3&position_count=3&product_id=31&client_id=&payment_type=sale
	
```
- Below is an example of a target action for the banking sector (action type Lead).

| Item | Product name | Price | Quantity | Cost |
| --- | --- | --- | --- | --- |
| 1 | Sign up | \- | \- | \- |

```
https://ad.admitad.com/r?campaign_code=your_campaign_code&postback=1&  
postback_key=your_postback_key&action_code=1&uid=03b374fa9c2f34069e8df0bda61b8627&  
order_id=123456&tariff_code=1&price=0&payment_type=lead
	
```

#### How to set up sending a request for several actions and rates


When you set up sending a request for several actions and rates, remember that rates for one action may differ from the rates for another one. [Learn more about actions and rates](https://support.admitad.com/hc/en-us/articles/4405926785809)


In this case:


1\. Define the action performed by the user.


2\. Define the rate or rates for this action.

> Example
> 
> There are two target actions in the program:
> 
> 
> - New user's order: 
> `action_code=1`
> - Existing user's order: 
> `action_code=2`
> 	-
> 
> 
> There are two rates for the action with
> 
> 
> 
> `action_code=1`
> 
> - TV purchase: 
> `tariff_code=1`
> - phone purchase: 
> `tariff_code=2`
> 
> 
> There is only one rate for the action with
> 
> 
> 
> `action_code=2`
> 
> 
> : the default rate
> 
> 
> 
> `tariff_code=1`
> 
> 
> .
> 
> 
> 
> So if the new user (
> 
> 
> 
> `action_code=1`
> 
> 
> ) purchases a TV and a phone, you need to pass
> 
> 
> 
> `action_code=1`
> 
> 
> ,
> 
> 
> 
> `tariff_code=1`
> 
> 
> , and
> 
> 
> 
> `tariff_code=2`
> 
> 
>  in the request.

- Below is an example of a cart with two items and two different rates.

| Item | Product name | Price | Quantity | Cost | Rate code |
| --- | --- | --- | --- | --- | --- |
| 1 | TV | 20,000 | 2 | 40,000 | 1 |
| 2 | iPhone | 35,000 | 3 | 105,000 | 2 |
|  |  |  | Total | 195,000 |  |


You have to send a postback request for each item.  
The values of the following parameters will vary in the requests presented in the example:

	- price (
	`price`
	)
	- quantity (
	`quantity`
	)
	- item number in cart (
	`position_id`
	)
	- internal product ID (
	`product_id`
	)
	- rate code (
	`tariff_code`
	)
  
Postback request for the first item in the cart:

```
https://ad.admitad.com/r?campaign_code=your_campaign_code&postback=1&postback_key=your_postback_key&action_code=1&uid=03b374fa9c2f34069e8df0bda61b8627&order_id=123456&tariff_code=1&currency_code=USD&price=20000&quantity=2&position_id=1&position_count=3&product_id=11&client_id=&payment_type=sale
	
```

Postback request for the second item in the cart:

```
https://ad.admitad.com/r?campaign_code=your_campaign_code&postback=1&postback_key=your_postback_key&action_code=1&uid=03b374fa9c2f34069e8df0bda61b8627&order_id=123456&tariff_code=2&currency_code=USD&price=35000&quantity=3&position_id=2&position_count=3&product_id=21&client_id=&payment_type=sale
	
```

#### How to set up sending a request for personal promo codes


Personal promo codes are promo codes that contain a unique code word by which target actions are tracked. Such promo codes are assigned to certain publishers. [Learn more about personal promo codes](https://support.admitad.com/hc/en-us/articles/4405926834577)


If you plan to use personal promo codes:


1\. Make sure there is a Promo code field in the order form on your website.


2\. Write the personal promo code from the order form to the

`promocode`
 parameter.

- ```
https://ad.admitad.com/r?campaign_code=your_campaign_code&postback=1&postback_key=your_postback_key&action_code=1&uid=03b374fa9c2f34069e8df0bda61b8627&order_id=123456&tariff_code=1&currency_code=USD&price=50000&quantity=1&position_id=3&position_count=3&product_id=31&client_id=&payment_type=sale&promocode=admitad500
	
```


3\. Make sure all orders with personal promo codes are sent to Admitad. Test the request to be 100% confident.


You need to pass order info to Admitad if the request contains:

- Both 
`admitad_uid` and a personal promo code
- A personal promo code only
- `admitad_uid` only


Information about an order with a personal promo code must not be sent to other channels.

## How to test a postback request after setup


1\. After you set up sending postback requests from your server, get a testing link in Integration.

- 1\.1 In your account, go to the Integration section (Program → Integration).


1\.2 Click Next and, on the Integration methods page, open the Custom integration) tab.


1\.3 In Custom integration, choose Postback and click Next.


1\.4 Scroll the page down to Integration testing and copy the test link from the corresponding field.


2\. Place some test orders and make sure that:

- The 
`admitad_uid` value is processed on all pages of the website and written to the cookie.
- The lifetime of the cookie containing the 
`admitad_uid` value matches the value specified in the agreement.
- The cookie is not deleted if a user comes from an organic search.  
To check this, do the following during your test order:
	- 1\. Follow the affiliate link.
	- 2\. Follow the organic link.
	- 3\. Place an order and check if it appears in the system.
- Requests are sent for all target actions and rates used in your affiliate program.  
Test them all by placing several orders to make sure tracking runs smoothly in each case.
- The request is sent for each item in the cart.
- The order number and amount are passed correctly. As for the cost of each item, you have to pass the amount that the user actually paid after applying a promo code, less the cost of shipment.


3\. Check other settings if you use them.

- If you use personal promo codes, place a test order as follows:
	- 1\. Go to your website through a direct link without any parameters.
	- 2\. Apply a unique promo code to your order and make sure Admitad counts the order.
- If you use other paid sources, place a test order as follows:  

	- 1\. Follow an affiliate link from another source.
	- 2\. Follow Admitad's affiliate network.
	- 3\. Place an order and make sure Admitad counts it.
- If you have:
	- a mobile version of the website
	- a quick order form
	- and/or a one\-click order form,
make sure tracking is set up for all platforms and purchase methods.


4\. If tracking runs smoothly, actions will appear in Admitad Partner Network reports in an hour.


To check this, go to your Admitad account → Reports → On actions and make sure the report correctly shows the target action and its info:

- The target action name in the Rate column in the report matches the name of this target action in the Actions section.
- The action ID in the Order ID column matches the action ID in your system.
- The order amount in Admitad matches the test order amount.


Let an Admitad specialist know that the test was successful. The program will now be prepared for launch.


5\. If the action didn't appear in reports in an hour, make sure that:

- You made no mistake when setting up sending postback requests.
- The request contains the 
`campaign_code` and`postback_key` values that you added from the Integration section of your account.


To identify the error, go to the Request log section (Program → Integration → Integration test). You will see the error text in Result. Fix the error and start another test. [Learn more about the "Request log" section](https://support.admitad.com/hc/en-us/articles/4405920527633)

## FAQ

### Where do I find the campaign\_code value?


1\. In your account, go to the Integration section (Program → Integration).


2\. Click Next and, on the Integration methods page, open the Custom integration) tab.


3\. In Custom integration, choose Postback and click Next.


4\. Find the `campaign_code` value in the table located at the top part of the screen (Integration setup: unique parameter values for your program).

### Where do I find the postback\_key value?


1\. In your account, go to the Integration section (Program → Integration).


2\. Click Next and, on the Integration methods page, open the Custom integration) tab.


3\. In Custom integration, choose Postback and click Next.


4\. Find the postback\_key value in the table located at the top part of the screen (Integration setup: unique parameter values for your program).

### Where do I find the action\_code value?


1\. In your account, go to the Integration section (Program → Integration).


2\. Click Next and, on the Integration methods page, open the Custom integration) tab.


3\. In Custom integration, choose Postback and click Next.


4\. In the Action column of the second table, find the action whose code you need.  
You will find the action\_code value in this action's row in the Action code column (Integration setup: unique parameter values for your program).

### Where do I find the tariff\_code value?


1\. In your account, go to Integration (Program → Integration).


2\. Click Next and, on the Integration methods page, open the Custom integration) tab.


3\. In Custom integration, choose Postback and click Next.


4\. In the Rate column of the second table, find the rate whose code you need.  
You will find the tariff\_code value in this rate's row in the Rate code column (Integration setup: unique parameter values for your program).

### How do I write order\_id for several actions if the order number is the user ID?


Some affiliate programs (e.g., online games) use the user ID instead of the order number in reports.


So if you need to add several target actions for such programs, you need to add a prefix to the order ID (order\_id). Use prefixes that clearly represent the action that you mean.

- | Target action | Parameter and its value | Prefix |
| --- | --- | --- |
| Sign up | order\_id\=reg\_123123 | reg\_ |
| Reaching Level 5 | order\_id\=lvl5\_123123 | lvl5\_ |

[Back to required parameters](#lead-required-parameters)
