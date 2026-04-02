---
title: Integration through an XML file
category: admitad-advertisers
section: technical-integration
language: en
source: https://support.mitgo.com/knowledge-base/article/integration-through-an-xml-file_2
---

# Integration through an XML file

Integration is a process during which you configure sending information about target actions performed on your website to the Admitad system.

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

## What integration through an XML file is, and how it works


Integration with an XML file is a way to integrate your website with the Admitad system where you need to create on your server an XML file with a certain structure where information about target actions on your website will be saved.

How it works. Using the permanent link to your XML file stored on your server, the Admitad Partner Network server will, at predefined regular intervals, access this file and upload new target action data from it to Admitad reports.


To make sure that only Admitad Partner Network can view your XML file, you can restrict access to the file. For example, you can set up access with a username and a password or specify the Admitad server's IP.


It's advisable that you set as high a frequency for uploading data to your XML file as possible so that:

- Information in Admitad reports is regularly and swiftly updated
- Publishers can keep track of their performance in real time


Read more about other integration methods in [Choosing an integration method](https://support.admitad.com/hc/en-us/articles/4405926820113#how-to-choose-integration-method).

## How to integrate your system using an XML file


To integrate your website using an XML file, do the following (you can find instructions for each step below):

- [Set up writing the *admitad\_uid* parameter's value to cookie files](#how-to-set-admitad_uid-in-cookies).
- [Set up deduplication of target actions](#how-to-set-deduplication).
- [Prepare your XML file](#how-to-prepare-xml-file)
- [Test\-drive your integration](#how-to-test-xml-file).


If there are both web and mobile versions of the website and/or a quick order form or a one\-click order form, make sure information about orders placed in these locations is also uploaded to your XML file.

### How to set up writing the value from the admitad\_uid GET parameter to cookies


The admitad\_uid value is registered when a user visits your website. Save this value in the cookie file and keep it there for as many days as specified in your agreement with Admitad) (90 days by default).


Use the script to set up writing the `admitad_uid` value to a cookie file.


Add the admitad\_uid value tracking code to all pages of your website. You need to do this because the user can go to any page of your website through the link.


Neither the cookie nor its lifetime should change when a user comes from a free source (e.g., organic search, etc.). Admitad uses the [Last Paid Click](https://support.admitad.com/hc/en-us/articles/4403304880529#last-paid-click-last-cookie-wins-en) attribution model, where the action is attributed to the last paid traffic source.

*Below are examples for a JavaScript and a PHP script. You can use one of these or any other programming language.*


Pay attention to the comments in code examples. All comments are added after //.

- ```
if (isset($_GET['admitad_uid'])) {  
$days = 90; // Cookie lifetime (days)  
setcookie('_aid', $_GET['admitad_uid'], time() + 60 * 60 * 24 * $days, '/');  
}  
  
function get_admitad_uid() {  
if (!isset($_COOKIE['_aid']) {  
return null;  
}  
  
return $_COOKIE['_aid'];  
}
	
```
- ```
<script type="text/javascript">  
//Cookie lifetime (days)  
var days_to_store = 90;  
  
//Parameters of a cookie containing Admitad UID value  
var uid_cookie_name = 'admitad_uid'; // Name of a cookie storing UID  
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


Setting up deduplication is a required step to complete integration, even if you only cooperate with one paid traffic source (Admitad).


After you set up deduplication, target action data is passed to Admitad under the Last Paid Click attribution model. If a publisher with Admitad was the last paid traffic source, that action should be attributed to Admitad.


You can use the following methods to set up deduplication of target actions:

Method 1


1\. Set up creating the cookie that will store the last paid traffic source on all pages of your website. By default, Admitad passes the parameter utm\_source\=admitad.


2\. Set up sending order data to your XML file for the cases when a traffic source cookie stores an `admitad` value.

Method 2


If there was a transition with the traffic source GET parameter different from Admitad, set up deleting the *admitad\_uid* cookie.

### How to prepare an XML file for integration


Prepare your XML file for integration. To do that, add the required parameters to it. If necessary, you can add additional parameters to the file.


Values of the customer's order should be substituted in the parameters.  
Note. You have to set up the logic of parameter substitution on your own.  
[Examples of XML files](#examples)


The set of required and additional parameters depends on the type of target action that you expect from the user.


Action types:

- Sale. A user has bought something or placed/paid for the order.
- Lead. A user has filled out a form and sent their data (e.g., applied for a service, signed up, etc.).


Click on an action type to see which parameters are required for it.


To see actions in your affiliate program, go to your account.

#### Parameters for Sale

- In the Parameter name, the main parameters are highlighted in bold, and in italics are aliases, which are additional names of the main parameter.  
In settings, you can specify not the main parameter itself but its alias, and Admitad will be able to process it.

| Parameter name | Description | Type | Note |
| --- | --- | --- | --- |
| uid, *key* | Admitad ID | String | A generated value passed in `admitad_uid` when the user visits the site.   If you allow [contextual ads](https://support.admitad.com/hc/en-us/articles/4403304880529#contextual-advertising-en), at the moment when a user clicks on a contextual ad placed by publishers through Google Ads, the gclid value [generated by Google](https://support.admitad.com/hc/en-us/articles/360019066437) will be written to `admitad_uid` instead of uid.   To make sure action tracking runs smoothly, your server must accept and pass the gclid value as a whole. [Learn more about gclid length](https://support.google.com/analytics/answer/2938246?hl=ru#:~:text=%D0%94%D0%BB%D0%B8%D0%BD%D0%B0%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%B0%20GCLID,%D0%B4%D0%BB%D0%B8%D0%BD%D0%B0%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20gclid%20%E2%80%93%20100%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2)   Example:*CjwKCAjwmJeYBhAwEiwAXlg0AfVR\-r9TC\-9ecMaEOJO7rbkmyt6j9QNyDFKqZ9YQTFdWxO2lQxvhPBoCO1sQAvD\_BwE* |
| order\_id, *oid* | Your internal order ID | String, 1 to 100 characters | Your internal order ID.   Note: Make sure you can find the order by this ID in your CRM system. This ID will be used during [verification](https://support.admitad.com/hc/en-us/articles/4405920549905). |
| action\_code, *ac*, *product*,*product\_code* | Target action code | Integer | A variable which is the target action code from your program settings.   [How to find an action code](#action-code-parameter) |
| tariff\_code, *tc* | Rate code | Integer | A variable which is the rate code from your program settings.   [How to find a rate code](#tariff-code-parameter) |
| currency\_code | Currency code | String, 3 characters | Defined in ISO 4217\. Letters only.   Example: *EUR, USD*. |
| position\_id | Item number in cart | Integer | A variable varying from 1 to N, where N \= position\_count. |
| position\_count | Items in cart | Integer | A variable with the value N that depends on what's in the user's cart. |
| quantity | Product quantity | Integer |  |
| payment\_type | Target action type | String, 4 characters | A constant with the value "sale". |
| product\_id | Your internal item ID | String, 1 to 100 characters | Product ID that must match the ID from the product feed if you use this tool.   [Learn more about the product feed](https://support.admitad.com/hc/en-us/articles/4405920538897) |
| price | Product price | Integer or decimal | Use a period as a divider.   Example:  	- Correct: 2\.65 	- Incorrect: 2,65 |
| datetime\_action, *now* | Date and time of action | String, 19 characters | Format: *YYYY\-MM\-DD hh:mm:ss*.   Example: *2022\-08\-25 00:00:00* |
- You can add additional parameters if you need to.

| Parameter name | Description | Type | Note |
| --- | --- | --- | --- |
| promocode | Personal promo code code | String, 255 characters | Use this parameter if you need to set up passing personal promo codes.   [Learn more](#how-to-set-info-about-promocodes) |
| tracking | Additional order information | String, 255 characters | Use this parameter to pass additional information for Admitad specialists during verification. |

#### Parameters for Lead

- In the Parameter name, the main parameters are highlighted in bold, and in italics are aliases, which are additional names of the main parameter.  
In settings, you can specify not the main parameter itself but its alias, and Admitad will be able to process it.

| Parameter name | Description | Type | Note |
| --- | --- | --- | --- |
| uid, *key* | Admitad ID | String | A generated value passed in `admitad_uid` when the user visits the site.   If you allow [contextual ads](https://support.admitad.com/hc/en-us/articles/4403304880529#contextual-advertising-en), at the moment a user clicks the contextual ads placed by publishers through Google Ads, the gclid value [generated by Google](https://support.admitad.com/hc/en-us/articles/360019066437) will be written to `admitad_uid` instead of uid.   To make sure action tracking runs smoothly, your server must accept and pass the gclid value as a whole. [Learn more about gclid length](https://support.google.com/analytics/answer/2938246?hl=ru#:~:text=%D0%94%D0%BB%D0%B8%D0%BD%D0%B0%20%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%B0%20GCLID,%D0%B4%D0%BB%D0%B8%D0%BD%D0%B0%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20gclid%20%E2%80%93%20100%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2)   Example: *CjwKCAjwmJeYBhAwEiwAXlg0AfVR**\-r9TC\-9ecMaEOJO7rbkmyt6**j9QNyDFKqZ9YQTFdWxO2l**QxvhPBoCO1sQAvD\_BwE* |
| order\_id, *oid* | Your internal order ID | String, 1 to 100 characters | Your internal order ID.   Note: Make sure you can find the order by this ID in your CRM system. This ID will be used during [verification](https://support.admitad.com/hc/en-us/articles/4405920549905).   If several target actions should be set up for your affiliate program but the user id will remain the same, add the prefix to the order ID. [Learn more](#order-id-prefix) |
| action\_code, *ac*, *product*, *product\_code* | Target action code | Integer | A variable which is the target action code from your program settings.   [How to find an action code](#action-code-parameter) |
| tariff\_code, *tc* | Rate code | Integer | A variable which is the rate code from your program settings.   [How to find a rate code](#tariff-code-parameter) |
| datetime\_action, *now* | Date and time of action | String, 19 characters | Format: *YYYY\-MM\-DD hh:mm:ss*.   Example: *2022\-08\-25 00:00:00* |
- You can add additional parameters if you need to.

| Parameter name | Description | Type | Note |
| --- | --- | --- | --- |
| currency\_code | Currency code | String, 3 characters | Defined in ISO 4217\. Letters only.   Example: *EUR, USD*. |
| position\_id | Item number in cart | Integer | A variable varying from 1 to N, where N \= position\_count. |
| position\_count | Items in cart | Integer | A variable with the value N that depends on what's in the user's cart. |
| quantity | Product quantity | Integer |  |
| payment\_type | Target action type | String, 4 characters | A constant with the value "lead". |
| product\_id | Your internal item ID | String, 1 to 100 characters | Product ID that must match the ID from the product feed if you use this tool.   [Learn more about the product feed](https://support.admitad.com/hc/en-us/articles/4405920538897) |
| price | Product price | Integer or decimal | Use a period as a divider.   Example:  	- Correct: 2\.65 	- Incorrect: 2,65 |
| promocode | Personal promo code code | String, 255 characters | Use this parameter if you need to set up passing personal promo codes.   [Learn more](#how-to-set-info-about-promocodes) |
| tracking | Additional order information | String, 255 characters | Use this parameter to pass additional information for Admitad specialists during verification. |

#### XML file examples


This section presents examples of XML files for different types of target action.


Click an example to learn more about it.

- Below is an example of a cart with three items.

| Item | Product name | Price | Quantity | Cost |
| --- | --- | --- | --- | --- |
| 1 | Chainsaw | 2,000 | 3 | 6,000 |
| 2 | Desk lamp | 1,790 | 2 | 3,580 |
| 3 | Welding set | 4,050 | 1 | 4,050 |
|  |  |  | Total | 13,630 |


Assign a unique \<payment\> tag to each item.  
In the example below, the values of the following parameters change inside the tags:

	- quantity (`quantity`)
	- price (`price`)
	- item number in cart (`position_id`)
	- target action code (`action_code`);
	- rate code (`tariff_code`)
	- internal product ID (`product_id`)
```
<?xml version="1.0" encoding="UTF-8"?>
<payment_list version="2">
    <payment>
        <uid>admitad_uid</uid>
        <order_id>15</order_id>
        <product_id>125</product_id>
        <tracking>Handheld tools - Chainsaw</tracking>
        <quantity>3</quantity>
        <currency_code>USD</currency_code>
        <price>2,000</price>
        <position_id>1</position_id>
        <payment_type>sale</payment_type>
        <action_code>1</action_code>
        <tariff_code>1</tariff_code>
        <position_count>3</position_count>
        <datetime_action>2019-12-31 00:00:00</datetime_action>
    </payment>
    <payment>
        <uid>admitad_uid</uid>
        <order_id>15</order_id>
        <product_id>57</product_id>
        <tracking>Desk lamp</tracking>
        <quantity>2</quantity>
        <currency_code>USD</currency_code>
        <price>1,790</price>
        <position_id>2</position_id>
        <payment_type>sale</payment_type>
        <action_code>2</action_code>
        <tariff_code>2</tariff_code>
        <position_count>3</position_count>
        <datetime_action>2019-12-31 00:00:00</datetime_action>
    </payment>
    <payment>
        <uid>admitad_uid</uid>
        <order_id>15</order_id>
        <product_id>71</product_id>
        <tracking>Welding set</tracking>
        <quantity>1</quantity>
        <currency_code>USD</currency_code>
        <price>4,050</price>
        <position_id>3</position_id>
        <payment_type>sale</payment_type>
        <action_code>2</action_code>
        <tariff_code>1</tariff_code>
        <position_count>3</position_count>
        <datetime_action>2019-12-31 00:00:00</datetime_action>
    </payment>
</payment_list>
	
```
- Below is an example of a target action for the banking sector (action type Lead).

| Item | Product name | Price | Quantity | Cost |
| --- | --- | --- | --- | --- |
| 1 | Sign up | \- | \- | \- |

```
<?xml version="1.0" encoding="UTF-8"?>
<payment_list version="2">
    <payment>
        <uid>admitad_uid</uid>
        <order_id>15</order_id>
        <payment_type>lead</payment_type>
        <action_code>1</action_code>
        <tariff_code>1</tariff_code>
        <datetime_action>2019-12-31 00:00:00</datetime_action>
    </payment>
</payment_list>
	
```

#### How to set up data sending for personal promo codes


Personal promo codes are promo codes that contain a unique code word by which target actions are tracked. Such promo codes are assigned to certain publishers. [Learn more about personal promo codes](https://support.admitad.com/hc/en-us/articles/4405926834577)


If you plan to use personal promo codes:


1\. Make sure there is a Promo code field in the order form on your website.


2\. Write the unique promo code from the order form to the `promocode` parameter.


3\. Make sure all orders with the unique promo code are passed to Admitad. Test the request to be 100% confident.


You need to pass order info to Admitad if the request contains:

- Both 
`admitad_uid` and a personal promo code
- A personal promo code only
- `admitad_uid` only


Information about an order with a personal promo code must not be sent to other channels.

## How to test an XML file after setup


1\. After you create an XML file with the structure described above and set up sending target action data to it, you will get a testing link in Integration.

- 1\.1 In your account, go to the Integration section (Program → Integration).


1\.2 Click Next and, on the Integration methods page, open the Custom integration) tab.


1\.3 In Custom integration, choose XML and click Next.


1\.4 Scroll the page down to Integration testing and copy the test link from the corresponding field.


2\. Place some test orders and make sure that:

- The 
`admitad_uid` value is processed on all pages of the website and written to the cookie.
- The lifetime of the cookie containing the 
`admitad_uid` value matches the value specified in the agreement. If there is no agreement, it must be 90 days.
- The cookie is not deleted if a user comes from an organic search.  
To check this, do the following during your test order:
	- 1\. Follow the test affiliate link.
	- 2\. Follow the organic link.
	- 3\. Place an order and check if it appears in the system.
- Writing data to an XML file works for all target actions and rates used in your program.  
Check this by placing several orders to make sure tracking runs smoothly in each case.
- A unique tag is created for each item in the cart \<payment\>.
- The order number and amount are passed correctly. As for the cost of each item, you have to pass the amount that the user actually paid after applying a promo code, less the cost of shipment.


2\. Check other settings if you use them.

- If you use personal promo codes, place a test order as follows:
	- 1\. Go to your website through a direct link without any parameters.
	- 2\. Use the personal promo code in your order and make sure Admitad counts the order.
- If you use other paid sources, place a test order as follows:
	- 1\. Follow an affiliate link from another source.
	- 2\. Follow Admitad's affiliate network.
	- 3\. Place an order and make sure Admitad counts it.
- If you have:
	- a mobile version of the website
	- a quick order form
	- and/or a one\-click order form,
make sure tracking is set up for all platforms and purchase methods.


4\. After you place your test orders, instruct Admitad specialists on how they can access your XML file containing information about these orders. The specialists will upload and process the file within 3 to 4 days.


5\. If tracking runs smoothly, actions will appear in Admitad reports in an hour.


To check this, go to your Admitad account → Reports → On actions and make sure the report correctly shows the target action and its info:

- The target action name in the Rate column in the report matches the name of this target action in the Actions section.
- The action ID in the Order ID column matches the action ID in your system.
- The order amount in Admitad corresponds to the test order amount.

  
Let an Admitad specialist know that the test was successful. The program will now be prepared for launch.


6\. If the action didn't appear in reports in an hour, make sure that:

- You sent an Admitad specialist a valid file link.
- You specified all required parameters correctly.
- You used the correct case in tags.


To identify the error, go to the Request log section (Program → Integration → Integration test). You will see the error text in Result.


Fix the error and start another test. [Learn more about Request log](https://support.admitad.com/hc/en-us/articles/4405920527633)

## FAQ

### Where do I find the action\_code value?


1\. In your account, go to the Integration section (Program → Integration).


2\. Click Next and, on the Integration methods page, open the Custom integration) tab.


3\. In Custom integration, choose XML and click Next.


4\. In the Action column of the table, find the action whose code you need.  
You will find the action\_code value in this action's row in the Action code column (Integration setup: unique parameter values for your program).

### Where do I find the tariff\_code value?


1\. In your account, go to the Integration section (Program → Integration).


2\. Click Next and, on the Integration methods page, open the Custom integration) tab.


3\. In Custom integration, choose XML and click Next.


4\. In the Rate column of the second table, find the rate whose code you need.


Find the `tariff_code` value in this rate's row in the Rate code column (Integration setup: unique parameter values for your program).

### How do I write order\_id for several actions if the order number is the user ID?


Some affiliate programs (e.g., online games) use the user ID instead of the order number in reports.


So if you need to add several target actions for such programs, you need to add a prefix to the order ID (order\_id). Use prefixes that clearly represent the action that you mean.

- | Target action | Parameter and its value | Prefix |
| --- | --- | --- |
| Sign up | order\_id\=reg\_123123 | reg\_ |
| Reaching Level 5 | order\_id\=lvl5\_123123 | lvl5\_ |

[Back to required parameters](#required-lead-parameters)
