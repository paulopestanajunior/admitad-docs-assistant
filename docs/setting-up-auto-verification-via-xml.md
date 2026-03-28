---
title: Setting up auto-verification via XML
section: technical-integration
source: https://support.mitgo.com/knowledge-base/article/setting-up-auto-verification-via-xml_2
---

# Setting up auto-verification via XML

Read about the verification and its types in [this article](https://support.admitad.com/hc/en-us/articles/4405920549905).


To set up an auto\-verification via XML, you need to create an XML file with a set of data described below and provide specialists of the Admitad tracking department with the link to this file. They will check whether the file structure is correct, statuses and orders amounts are transferred without mistakes, make the necessary settings and inform you about the result.

## Confidentiality


To hide the file from outsiders, we suggest that you either use HTTP Basic authorization to access the file (recommended) or just encrypt the name of the file, for example: http://myshop.com/23dvgdsfkl4tkerlgsfd.xml

## Update frequency


You must update the file at least once a day so that the tracking department can compare it with Admitad data.

## Contents of the auto\-verification file

- We recommend storing the action data for 3 months.
- Namespaces are required, the namespace of a root element must be *xmlns\=”http://admitad.com/payments\-revision”*.
- The Payments root element may contain any number of Payment elements.
- Every Payment must have two obligatory child elements:
	- OrderID
	- Status.
- Non\-obligatory elements:
	- OrderAmount and Reward, they are required, if the order amount or reward amount has been changed.
	- currency\_code for passing the order and reward currency:
		- if you don't pass currency\_code, the currency specified in the affiliate program will be used for currency\_code by default;
		- If you pass currency\_code and the currency in it differs from the affiliate program currency, the amounts in the "amount" and "reward" parameters will be converted to the program currency using the exchange rate in the system at the moment when the target action was recorded.
	- Another non\-obligatory element is Comment that is used to explain why you declined the order.

An order can be declined, if:

- The order was cancelled,
- The order was refused,
- The order was returned,
- The order was not purchased,
- Data are filled out incorrectly.

Note that:

- Names of all elements are case sensitive;
- The following tags are not allowed:  
\<OrderAmount\>None\</OrderAmount\> — noncompliance with the value type;  
\<Comment/\> — empty tags.

## Example of the file contents

Example 1:


If you want only to confirm or decline actions, the file must contain the following information:

| Parameter | Description |
| --- | --- |
| OrderID | Order number |
| Status | Status of an order (1 – confirmed, 2 – declined) |
| Comment | In this parameter you can write the reason for declining an order (up to 30 characters) |

```
<Payments xmlns=”http://admitad.com/payments-revision”>
<Payment>
<OrderID>123456</OrderID>
<Status>2</Status>
<Comment>Returned</Comment>
</Payment>
</Payments>

```

Example 2:


If you want to confirm actions and change the order amount so that the system recalculates the publishers’ reward itself, it is necessary to preliminarily agree on this setting with the tracking department. The setting is used only in programs with percent rates.


Required parameters:

| Parameter | Description |
| --- | --- |
| OrderID | Order number |
| Status | Status of an order (1 – confirmed, 2 – declined) |
| Order amount | Amount of an order (a decimal non\-negative number with a period separator) |

```
<Payments xmlns=”http://admitad.com/payments-revision”>
<Payment>
<OrderID>123456</OrderID>
<OrderAmount>1000</OrderAmount>
<Status>1</Status>
</Payment>
</Payments>

```

Example 3:


If you want to change the publishers' rewards, you should preliminarily agree this setting with the tracking department.


Required parameters:

| Parameter | Description |
| --- | --- |
| OrderID | Order number |
| Status | Status of an order (1 – confirmed, 2 – declined) |
| Reward | Reward of a publisher (a decimal non\-negative number with a period separator) |

```
<Payments xmlns=”http://admitad.com/payments-revision”>
<Payment>
<OrderID>123456</OrderID>
<OrderAmount>1000</OrderAmount>
<Reward>100</Reward>
<Status>1</Status>
</Payment>
</Payments>

```
## Obtaining information on pending orders from Admitad


You can ask an Admitad specialist to provide you with a link for an XML file where you can obtain information on pending actions.

Example of a link:  
https://www.admitad.com/sid103584/en/advertiser/advcampaign/5441/payments/xml\_export/?uid\=rksNfWrTIQesLvZ


If you want to get information about the actions performed within a certain period, you can add the following parameters to the link:

start\-date – lower bound of a period in ISO date format (for example, 2014\-01\-01\)  
end\-date – upper bound of a period in ISO date format (for example, 2014\-01\-31\)


Then the link will look like  
https://www.admitad.com/sid103584/en/advertiser/advcampaign/5441/payments/xml\_export/?uid\=rksNfWrTIQesLvZ  
\&start\-date\=2014\-01\-01\&end\-date\=2014\-01\-31


You can use this information to verify orders statuses for certain actions and then send them to the Admitad side in the auto\-verification file.
