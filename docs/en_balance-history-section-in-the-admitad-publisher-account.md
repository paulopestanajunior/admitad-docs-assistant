---
title: "Balance history" section in the Admitad publisher account
category: admitad-publishers
section: finance-balance-payment-terms-and-methods
language: en
source: https://support.mitgo.com/knowledge-base/article/balance-history-section-in-the-admitad-publisher-account_5
---

# "Balance history" section in the Admitad publisher account

In the [Balance history](https://store.admitad.com/en/webmaster/balance-history/) section (Finance → Balance history) you can review all transactions in your Admitad account.


The data is presented as a table containing a list of operations, starting with the most recent. [Learn more](#data-in-history)

## How to find an operation in the balance history


Use the filter above the table to search for particular operations. You can search by one parameter or by several at the same time. You can search by:

- date
- currency
- operation type
- reason
- target action ID. The IDs of all actions can be found in the section [Reports on actions](https://account.admitad.com/ru/webmaster/statistics/actions/).

## What data is available


The table contains the following columns:

Date — the date of the operation.

Amount — the amount that was credited to or withdrawn from the balance.

Currency — the currency in question.

Operation type:

- Credit — funds were added to the balance.

For example, the crediting of rewards for a target action; the return of funds following a payment request that could not be carried out; or the crediting of funds following a withdrawal made in error.
- Withdrawal means debiting funds from the balance.  
For example, a withdrawal occurs when you transfer funds to your [Admitad Earnings Wallet](https://support.mitgo.com/hc/en-us/articles/23936688584849). A withdrawal also occurs when a commission for a target action was charged because the advertiser declined that action. [See here for more on declining already confirmed actions](https://support.admitad.com/hc/en-us/articles/360019116897).


Withdrawals in the Balance history section are only shown for confirmed actions. For instance, if some actions with the "On hold" or "Confirmed, awaiting advertiser payment" statuses, rewards for such actions will just disappear from your balance and won't appear in the Balance history section. You'll be able to find the information on such actions in the report on actions by filtering by the "Declined" status.

Reason — the reason funds were credited or withdrawn.

- Payment for action ID\*\*\* — this means the advertiser confirmed the action with ID\*\*\* and the relevant reward was credited to the balance.

If the advertiser later declines the confirmed action, another operation with the reason Payment for action ID\*\*\* will appear in your balance, but this time it will be a withdrawal.

[See here for more on declining already confirmed actions.](https://support.admitad.com/hc/en-us/articles/360019116897)


Click on the text of the reason to see detailed information about the action: which program and ad space it is tied to, the rate, the order amount, etc.
- Payment request means you have transferred funds to your Admitad Earnings Wallet and the specified amount was debited from your Admitad balance.
- Fine for fraudulent actions — this means that some rewards you've already withdrawn from Admitad were debited from your balance and returned to the advertiser's balance as they declined some earlier confirmed action due to the violation of program rules. [Learn more](https://support.admitad.com/hc/en-us/articles/360019116897)
	- - In the comment, the program the deduction is related to is specified.
		- To view the detailed information, click Learn more. The pop\-up window will open where you'll be able to download the detailed report on all declined actions.
- Balance transaction. This reason is used for manual balance transactions and for requests from the Lost Orders tool that have been confirmed by Admitad without involving the advertiser. Such a transaction will have the following comment: “Program {program name}. Lost Order No. {order name}. Confirmed by Admitad.”
- Transfer between publishers — used for transfers from your Admitad balance to a [GetUniq](https://getuniq.me/en/services/) balance. Also used for amounts the rewards for which were decreased due to the use of the [Instant Payout service](https://support.admitad.com/hc/en-us/articles/4403557147665). In this case, the operation will have the comment "Instant Pay fee."
- Referral payment — for cases when funds were credited under the conditions of an Admitad referral program. [See here for more on referral programs](https://support.admitad.com/hc/en-us/articles/360019209518).
- Instant Payout Lite. Used for transactions related to [Instant Payout Lite](https://support.admitad.com/hc/en-us/articles/4403557147665) requests.

The reason may contain the following comments:

	- *Instant Payout Lite Request ID\*\*\**. Means that the funds were made Ready for withdrawal after the Instant Payout Lite request was completed.
	- *Instant Payout Lite fee on request ID\*\*\**. Means that the reward decrease amount was charged after the Instant Payout Lite request was completed.
	- *Adjusting the balance for a previously paid reward for Action ID \*\*\* from Instant Payout Lite ID request \*\*\*\**. Means the following debit as part of the balance adjustment: the advertiser paid for the confirmed actions, and the system now debits this amount since these funds had already been credited to your balance under the related Instant Payout Lite request.
- Instant Payout Pro. Used for transactions related to [Instant Payout Pro](https://support.admitad.com/hc/en-us/articles/4403557147665#instant-payout-pro) requests.

The reason may contain the following comments:

	- *Instant Payout Pro Request ID\*\*\**. Means that the funds were made Ready for withdrawal after the Instant Payout Pro request was completed.
	- *Adjusting the balance for a previously paid reward for Action ID\*\*\* from Instant Payout Pro ID request \*\*\*\**. Means the following debit as part of the balance adjustment: the advertiser paid for the confirmed actions, and the system now debits this amount since these funds had already been credited to your balance under the related Instant Payout Pro request.
	- *Compensation on Instant Payout Pro request\*\*\** is an additional amount of reward for actions mentioned in the Instant Payout Pro request, which the advertiser confirmed and paid for. The compensation means that the reward amount predicted by the system turned out to be lower than the final amount, so Admitad credited the difference to your balance. [Learn more about compensations](https://support.admitad.com/hc/en-us/articles/4403557147665#recalculation-pro)
- Comment — additional information on the operation.
