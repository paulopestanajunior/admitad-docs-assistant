---
title: Lost orders
category: admitad-publishers
section: tools
language: en
source: https://support.mitgo.com/knowledge-base/article/lost-orders_1
---

# Lost orders

Lost orders is a tool you can use to submit a request to:

- search for an order that was made but didn’t get included in Admitad reports;
- change the status of an order that was declined by the advertiser, despite being in compliance with the rates and the program regulations. Such requests are called appeals.

The advertiser will process the request, and if the order really was created in compliance with the requirements regarding rates and the program regulations, the advertiser will accept it and pay you your due reward.

You can only submit requests for orders. The tool is not available for leads.

## How do I create a request?

1\. Go to Tools → Lost orders. Click Create a request.

  
2\. You will see the tool’s user agreement. If you agree with its terms and conditions, click Accept.  
If you do not accept the terms and conditions, you will be unable to create requests.

[Guests](https://support.admitad.com/hc/en-us/articles/360019106457) are not allowed to can accept the terms and conditions, it can be done only by the account owner.

3\. Enter the order ID under which the order was registered in the advertiser’s system.

4\. Select the affiliate program under which the order was made.  
If the program isn’t listed, that means it isn’t supported by the Lost Orders tool.

5\. If you keep your own statistics on customers' requests, fill in the field Request ID. Once the request has been processed, you’ll be able to use this ID to identify the customer and contact them.

6\. You will see one of these forms below:

- If the order with the ID you entered is already registered in Admitad reporting, the fields Upload invoice and Comment will appear after you fill in the fields Order ID and Affiliate program.
- If the order is not in the reports, i.e. is lost, the system will display the following fields: Ad space, Order date, Order amount, Estimated reward, Upload invoice, and Comment.

  
Regardless of the form option, all fields are mandatory.

- Ad space — select the ad space from which the user went to the advertiser's site and made the order.
- Order date — the date the user placed the order.
- Order amount — given in the currency of the program.
- Estimated reward — calculate the reward you should receive for this order using the formula "order amount × program rate."  
If the order has items with different rates, calculate the reward separately for every rate and then add them together to get the estimated reward total.  
  

> Example
> 
> 
> 
> 
> | Order items | Program rates |
> | --- | --- |
> | Tablet Samsung Galaxy Tab A 7\.0" 8GB LTE Black1 pc × $153\.30 \= $153\.30 | Tablets — 1\.0% |
> | Tablet case Samsung 3 pcs × $6\.14 \= $18\.41 | Accessories — 1\.5% |
> | Coffee grinder Bosch1 pc × $22\.86 \= $22\.86 Kitchen scales Scarlett1 pc × $16\.73 \= $16\.73 | Kitchen appliances — 1\.9% |
> | Electric toothbrush Braun Oral\-B2 pcs × $22\.86 \= $45\.72 | Health products — 1\.2% |
> 
> 
>   
> Estimated reward calculation:  
> 153\.30 × 0\.01 \+ 18\.41 × 0\.015 \+ (22\.86 \+ 16\.73\) × 0\.019 \+ 45\.72 × 0\.012 \= 1\.53 \+ 0\.28 \+ 0\.75 \+ 0\.55 \= 3\.11  
>   
> Thus, the estimated reward is $3\.11\.
- Upload invoice — upload the scanned copy of the invoice verifying that the order has been made. Supported formats: .img, .jpeg, .pdf, .png.

Take filling the fields Estimated reward and Upload invoice very seriously. Entering the wrong reward totals or uploading unrelated files or invoices of other orders might result in your being barred from using the tool and your requests getting declined.

- Comment — describe why you think the order should be approved.

## Example of a request

  
 

## Possible issues when creating a request

| Issue | Comment |
| --- | --- |
| You entered the order ID and got a message saying "This order status is On hold or Approved." | The order has not been lost or declined by the advertiser. Check the status of the order. To do so:1. Go to Reports — On actions. 2. Filter the actions by program and date range (order date). 3. Find the order ID in the Order ID column and check its status in the Status column.  On hold — the advertiser has yet to process the order. Wait for it to be processed. Approved — the advertiser has approved the order and paid the reward. |
| When creating a request, you saw the following message: “A request with the “Processing” or “Confirmed” status already exists for the order with this number.” | You have already created a request with this order number. You can find it in the section, using search by order number, and check its status. |
| You entered the order ID and got a message saying "This appeal has already been declined by the advertiser." | You have previously filed an appeal for this order, and the advertiser rejected it. To find the previous appeal, go back to the list of all requests and enter the order number in the search box. Appeal status will be Declined. |
| You entered the order ID and got a message saying "The order doesn't belong to Admitad" | The order belongs to another affiliate network. |
| You entered the order ID and got a message saying "You can no longer submit an appeal claim. The appeal period has lapsed." | The order was declined more than 6 months ago. |
| You entered the order ID and got a message saying "You cannot submit a request for orders made more than 150 days ago." | The order was made more than 150 days ago and the appeal period has lapsed |
| You can't find the program you need in the list of affiliate programs. | If the program isn’t on the list, that means it isn’t supported by this tool. Unfortunately, in this case you won’t be able to create a lost order request or submit an appeal claim. You can find out what programs are supported by the tool with the help of the Tools filter in the [Admitad Store](https://store.admitad.com/en/catalog/) section. To do so, filter the programs through the Lost orders tool. |
| You uploaded an invoice and got a message saying "Incorrect file format". | The only supported formats for invoice scans are .img, .jpeg, .pdf, and .png. Make sure the scan is in one of these formats. |

 

## Submitting a request or appeal claim via the API

In addition to being able to submit requests from your account, you can also do so via the Admitad API:

- [Creation of lost order](https://developers.admitad.com/hc/en-us/articles/7930561450001-Lost-orders#creation-of-lost-order) — for orders that were not included in Admitad reports.
- [Creation of appeal](https://developers.admitad.com/hc/en-us/articles/7930561450001-Lost-orders#creating-an-appeal-claim) — for orders that were wrongfully declined by advertisers.

 

## What do I do after submitting the request?

All the requests that get submitted will be compiled in a table, where you’ll be able to check their status at any time.

  
 

- On hold — the advertiser has yet to process the request.
- Approved — the advertiser has agreed that the request was created in compliance with the rates and the regulations of the program. The order has been confirmed.  
Clicking on the status will take you to the reports on actions. That section will be filtered for the order in question so you can see the new status and the reward that was accrued right away.  
Some requests can be confirmed by Admitad without involving the advertiser. In this case, the action will not be registered in your report. The reward for the order will be credited to your balance. In the [balance history](https://store.admitad.com/en/webmaster/balance-history/?_gl=1*t6fbck*_ga*OTk0MTc3NjIxLjE2ODk3NjY2MTE.*_ga_32HHLCD33P*MTcwODU5NzgwMS42Ni4xLjE3MDg1OTc4MDEuNjAuMC4w) you will see the transaction with the following comment: “Program {program name}. Lost order No. {order nuber}. Confirmed by Admitad.”
- Declined — the advertiser has declined the request. To find out why, click on the status or the Learn more button.

If the advertiser has processed a lost order request or appeal claim, and you have already settled the issue with the customer, you can mark the request as resolved, and it will disappear from the list.

  
To see resolved requests again, choose “All” or “Solved” in the “Stage” filter.

  
A solved request can be returned to the main list at any time.
