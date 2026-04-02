---
title: "Payments history" section in Admitad
category: admitad-publishers
section: finance-balance-payment-terms-and-methods
language: en
source: https://support.mitgo.com/knowledge-base/article/payments-history-section-in-admitad_5
---

# "Payments history" section in Admitad

The [Payments history](https://store.admitad.com/webmaster/account/payouts_list/) section shows previous transfers to [Admitad Earnings Wallet](https://earnings.admitad.com/), a payment service for Admitad partners that allows managing funds and withdrawing them in any convenient way.


After you transfer funds to Admitad Earnings Wallet (see [this guide](https://support.admitad.com/hc/en-us/articles/9117474273809)), the funds will be credited to your Admitad Earnings Wallet. There you can create a payment request (see [this guide](https://support.mitgo.com/hc/en-us/articles/24007268129809)) to withdraw your earnings.


You can find information about created payment requests in the [Transaction history](https://earnings.admitad.com/history) section of Admitad Earnings Wallet. There you can also track statuses of your withdrawal requests, download invoices, request extracts, etc. 

## Data in the "Payments history" section

- ID is an Admitad Earnings transaction identifier.
- Date is the date when the funds were transferred to Admitad Earnings Wallet.
- Status is the transaction status.
	- Created means the transfer to Admitad Earnings Wallet is being processed.  
	If this status doesn't change after 10 minutes, [contact support](https://support.admitad.com/hc/en-us/articles/360020421978).
	- Processed means your funds were transferred to Admitad Earnings Wallet. You can now go to the service and withdraw your earnings (see [this guide](https://support.mitgo.com/hc/en-us/articles/24007268129809)).
	- Declined means the system couldn't transfer funds to Admitad Earnings Wallet. Try transferring funds again or [contact support](https://support.admitad.com/hc/en-us/articles/360020421978).
- Original amount is the amount transferred to Admitad Earnings Wallet.
- Transferred is the amount transferred to Admitad Earnings Wallet.
- Payment method. Always ["Admitad Earnings"](https://earnings.admitad.com/). Click on it to go to your account in this service.
- Invoice. This column will be empty, because information on payment request invoices is currently stored in [Admitad Earnings](https://earnings.admitad.com/).
- Account statement is an XLSX file containing information on the actions in the request. [Learn more](#statement)
- Comment. Always "Funds transferred to [Admitad Earnings](https://earnings.admitad.com/)".


Earlier, payments were processed within Admitad. This is why the section may show historical details about older payment requests, as well as related extracts and invoices.

## Statement on the request for transferring funds to Earnings Wallet


A statement, which is an XLSX file, is generated when you transfer your earnings from Admitad to Earnings wallet to further transfer funds to your bank account, PayPal wallet, etc.


The statement contains the following:

- Statistics tab (required) that contains information about the actions mentioned in the request for transferring funds to Earnings Wallet.
- Instant Payout tab that contains information about actions mentioned in the request and processed by Instant Payout.


If the request for transferring funds to Earnings Wallet doesn't contain actions stored in the Instant Payout request, the statement won't contain the Instant Payout tab.

- - Admitad ID. Action ID.
	- Ad space ID. The ID of the ad space from which the user came before performing the action.
	- Ad space name. The name of the ad space from which the user came before performing the action.
	- Program. The name of the program for which the actions were performed.
	- Time of action. Date and time when the action was performed.
	- Processing time. Date and time when the action was processed by the advertiser.
	- Reward amount. The amount of the reward for the action.
- - Instant Payout Lite request ID. The ID of the request for changing the status of funds from Awaiting advertiser payment to Ready for withdrawal.
	- Date Instant Payout Lite request was created. The date when the request for changing the status of funds from Awaiting advertiser payment to Ready for withdrawal was created.
	- Admitad ID. The ID of the action mentioned in the Instant Payout Lite request.
	- Date action was created. Date and time when the action was performed.
	- Program ID. The ID of the program with which the actions, processed by Instant Payout Lite under the request, are associated.
	- Program. The name of the program with which the actions, processed by Instant Payout Lite under the request, are associated.
	- Currency. Program currency.
	- Initial publisher reward. The reward for the target action before the latter was mentioned in the Instant Payout Lite request.
	- Reward decrease. The percentage by which the reward was reduced during using Instant Payout Lite. [Learn more](https://support.admitad.com/hc/en-us/articles/4403557147665-Admitad-Instant-Payout#terms-of-use)
	- Final publisher reward. The amount of the reward for the target action after reduction.


A statement may contain negative transactions with the comment "Adjusting the balance for a previously paid reward for Action \[payment\_ID] from Instant Payout Lite ID request \[application\_ID]".


The reward for these actions was previously credited to your balance under the Instant Payout Lite request.


Instant Payout is an archived tool that is not available to new publishers.
