---
title: Postback URL
category: admitad-publishers
section: tools
language: en
source: https://support.mitgo.com/knowledge-base/article/postback-url_5
---

# Postback URL

If, when working with Admitad, you use your own system of sales and leads statistics, you can add your server's postback URL to our system, and instantly get information about completed conversions.

Using your own statistics system is convenient because you can obtain all initial data about the target action and convert it at your discretion to necessary tables, graphs, charts, or use it in your own applications. It also facilitates working with several affiliate networks, as all the stats will be gathered in one location. The data is transmitted using GET or POST HTTP requests from the Admitad server to your server.

You may use over 20 parameters that contain all possible information about the action — from the moment when the customer clicks on your affiliate link, to the status of your earnings. Properly analyzed, all this data may significantly help you to improve the conversion rate of your advertisements.

 

## Adding postback URL

1\. Select Postback URL in the Tools menu.

2\. Click Add postback URL.

You can add several postback URLs, and configure them for various purposes.

  
3\. From the Event type menu, select the event for which the information will be transmitted to this Postback URL:

- Action — the request will be sent every time the action is performed (lead or sale).
- Program status — the request is sent upon changes in the status of the affiliate program to which your ad space is connected: when the program seizes or restarts its operation.
- A referral joined — an empty request (without any parameters) will be transmitted upon registration of the new publishers that you brought to Admitad through your [referral link](https://support.admitad.com/hc/en-us/articles/360019209518).
- Status of cooperation with the program — the data will be transmitted:
	- upon approval or rejection of the ad space after moderation;
	- upon rejection of the ad space in active cooperation;
	- upon re\-approval of the ad space after termination of cooperation.Select the program and the ad space below.

  
4\. Select the ad space for which you wish to retrieve statistics in the Ad space field.

You can also select All ad spaces, and sort all actions in your system by parameters Ad space name or Ad space ID. Details about available parameters will be shown [below](https://help.admitad.com/ru/topic/71-kod-optimizatsii-postback-veb-mastera#types).

  
5\. If you would like to receive information on the events of a particular program, choose it from the list in the Program field.

Here you can also leave the Admitad Store item.

  
6\. If you specify a certain affiliate program from the list, the Rate menu will also be available for you.

In this case, you can also select nothing, and information on all rates will be transmitted.

  
7\. If a specific rate has not been selected, you can specify the desired action type — Sale, Lead or leave All.

- Sale — an action when a user has confirmed the order on the website of the online store. However, this order may still be edited in the future, or it can be completely canceled.
- Lead — user’s action that may imply registration, subscription to newsletters, installation of the application, or reaching a certain level in an online game.
- All — both sales and leads

  
8\. Specify the type of request that you would prefer to use for obtaining information in the HTTP method field.

The main difference between the GET and the POST methods is the way of transmitting the data.

- The GET method sends all collected information as a part of the URL, by adding the parameters and their values to the end of the link.
- The POST method sends the data in the body of the request, rather than in the URL.

More information about the features of each method is available [here](http://www.w3schools.com/tags/ref_httpmethods.asp).

  
9\. Select which statuses of actions you would like to receive the data about in the Action status field.

- Created — this status appears when a visitor you brought to the advertiser's performed the target action and it appeared in the reports. Until the advertiser confirms or declines this action, the action will remain in this status.
- Confirmed — the advertiser has checked the action and confirmed it.
- Declined — the advertiser has checked the action and declined it.
- On hold — the action had been confirmed but was again placed on hold afterwards. Unlike this status, the Created status is assigned to the actions that are first entered into the system.
- Paid — reward for the confirmed action has the Ready for withdrawal status. To get this status, add the variable \[\[\[reward\_ready]]] to the link.

  
10\. Enter the link to your server that will be used for receiving the HTTP request in the Link field.

  
11\. Select one of the two editing modes:

- Simple mode — the mode where the request will contain the complete set of parameters, and the parameters themselves will have standard names adopted in the Admitad system.
- Advanced mode allows to create a list of desired parameters and assign the names that you are already using in your own system. To do so, enter the Parameter name into the same\-name field and drag the appropriate value from the right pane to the Parameter content field.

  
If you select the GET request, in the Generated link line you will see the URL, where the selected parameters and their contents are displayed after the symbol ?:

  
This is what the link will look like for HTTP requests sent to your server, but \[\[\[...]]] will be substituted by real parameters values.  
 

12\. After all the required parameters are added, test the link. To do so, at the bottom of the page, click Test.

  
Depending on the selected request type, you will see the following in the opened window:

| GET | POST |
| --- | --- |
| The URL with the test parameter values that will be sent to your server. By editing the code, you can replace these values with your own values. | The top field displays the URL that will be used for the request, and the bottom one displays the parameters and their test values from the body of the request. In this case, you cannot insert your own test values. |

  
Click the Test button to send the request, and you will see the following message: "The request has been sent to your address."

Check the receipt of the sent data in your statistics system.

- If the request has been sent successfully, but no data arrived, contact [Admitad support](https://support.admitad.com/hc/en-us/articles/360020421978).
- If the server does not accept POST requests, is unavailable, or its address has been specified incorrectly, you will see the following message: "An error occurred during the request. Check the address."

  
13\. If you are sure that correct data arrives at your server, close the test window and save the new postback URL.

It will appear in the table. You will be able to edit or test it again in the column Settings.

 

## Types of parameters and their valid values

### Parameters for the event type "Action"

| Name | Type | Description |
| --- | --- | --- |
| offer\_id | integer | Affiliate program ID |
| offer\_name | string | Affiliate program name |
| admitad\_id | integer | Payment ID |
| website\_name | string | Ad space name |
| website\_id | integer | Ad space ID |
| subid | string | [SubID](https://support.admitad.com/hc/en-us/articles/360019285478)Can be used for subid, subaccount, source\_id, affiliate\_id, creative\_id,adset\_id values. |
| action | string | Tariff (or rate) name |
| action\_id | integer | Action ID |
| subid1 | string | SubID1 |
| subid2 | string | SubID2 |
| subid3 | string | SubID3 |
| subid4 | string | SubID4Can be used for click\_id, transaction\_id values. |
| payment\_sum | real | Amount of your earnings |
| payment\_status | string, *allowed values*: | Payment status |
| `new` | New payment that has been neither confirmed nor declined yet |
| `approved` | Payment confirmed |
| `declined` | Payment declined |
| `pending` | Confirmed payment placed on hold again |
| currency | string (max. length \= 3\) | Program currency |
| order\_id | integer | Order number |
| order\_sum | real | Order amount |
| click\_time | Unix\-time | Click time |
| time | Unix\-time | Action time |
| conversion\_time | integer | Duration of conversion (in seconds) is the time elapsed from the moment of the click to the moment of the action (conversion) |
| type | string, *allowed values*: | Action type |
| `lead` |
| `sale` |
| country\_code | string | Country code in the format US / FR / DE |
| user\_agent | string | User\-Agent |
| user\_referer | string | User\-Referer |
| reward\_ready | string, *allowed values*: | The reward has been assigned the Read for withdrawal status or removed from it\*.\*If the reward has been removed from the Ready for withdrawal status, it has either returned to the On hold status or to the advertiser's balance as they declined the action. |
| `true` |
| `false` |

 

### Parameters for the event type "Program status"

| Name | Type | Description |
| --- | --- | --- |
| offer\_id | integer | Affiliate program ID |
| offer\_name | string | Affiliate program name |
| offer\_status | string, *allowed values*: | New status of the affiliate program |
| `active` | The affiliate program is active and cooperates with you |
| `denied` | Admitad no longer cooperates with this affiliate program |
| `disabled` | The program has been deactivated, but may again become active |
| `dead` | The program has been closed, and will no longer work in the Admitad |

 

## Parameters for the event type "Status of cooperation with the program"

| Name | Type | Description |
| --- | --- | --- |
| offer\_id | integer | Affiliate program ID |
| offer\_name | string | Name of affiliate program |
| website\_id | integer | Ad space ID |
| partnership\_status | string, allowed values: | Status of cooperation with the program |
| `accepted` | \- successful connecting the ad space to the program |
| `denied` | \- disconnecting the ad space of the program |

 

## Transferring click\_id and transaction\_id

If you want to transfer your click\_id and transaction\_id parameters in the affiliate link, use the subid4 parameter to do so.

> Link example:  
> https://ad.admitad.com/g/f469ae904cb7e16523942b59d5275c/?subid4\={click\_id}

In this link, change the parameter in braces to your click\_id value.
