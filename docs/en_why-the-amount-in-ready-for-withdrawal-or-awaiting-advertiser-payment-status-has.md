---
title: Why the amount in "Ready for withdrawal" or "Awaiting advertiser payment" status has decreased
category: admitad-publishers
section: finance-balance-payment-terms-and-methods
language: en
source: https://support.mitgo.com/knowledge-base/article/why-the-amount-in-ready-for-withdrawal-or-awaiting-advertiser-payment-status-has-decreased_5
---

# Why the amount in "Ready for withdrawal" or "Awaiting advertiser payment" status has decreased

The amount in Ready for withdrawal or Awaiting advertiser payment status may decrease for one of the reasons described below.

## Violation of program rules

According to the rules, the advertiser has the right to:

- Return confirmed actions to processing for additional verification if they suspect that you have violated program rules in the course of your work ([Learn more](#recheck)).
- Decline previously verified actions if violations of affiliate program rules on these actions are detected ([Learn more](#violations)).

### The advertiser returned the action to processing for additional verification

In this case:

- In the Balance Details section, funds in Ready for withdrawal or Awaiting advertiser payment status will move to On hold status.
- In the [Reports on actions](https://store.admitad.com/en/webmaster/statistics/actions/) section, the status of these actions will change to On hold.

  
The advertiser will then verify these actions again:

- If the verification doesn’t confirm any violations, the actions will once again be given Confirmed status in reports, and rewards for them will move to Ready for withdrawal or Awaiting advertiser payment status.  
Funds in Ready for withdrawal status will be available for withdrawal the next day.
- If the verification reveals rule violations, the advertiser has the right to decline the actions. [Read more about declining actions](#violations)

### The advertiser has discovered violations of the program rules and declined actions

The next scenario depends on whether you have managed to withdraw rewards for declined actions from Admitad:

- [You have not yet withdrawn rewards for declined actions](#before-withdrawal).
- [You have already managed to withdraw rewards from Admitad](#after-withdrawal).

#### If you have not yet withdrawn rewards

In this case:

- In the Balance Details section, the reward amount for declined actions will be deducted from rewards in Ready for withdrawal and/or Awaiting advertiser payment status.
- In the [Reports on actions](https://store.admitad.com/en/webmaster/statistics/actions/) section, the status of these actions will change to Declined.
- Under [Balance history](https://store.admitad.com/en/webmaster/balance-history/), you’ll see a Withdrawal operation with the specified reason Payment for action ID\*\*\* with the reward amount deducted because the action was declined.

This operation will be reflected in the [Balance history](https://store.admitad.com/en/webmaster/balance-history/) only if funds in Ready for withdrawal status have been deducted from the balance. The operation will not be displayed if funds in Awaiting advertiser payment status are deducted. [Learn more](https://support.admitad.com/hc/en-us/articles/4404837822225#balance-history-logic)

#### If you have already managed to withdraw rewards

In this case:

- In the Balance Details section, the reward amount for declined actions will be deducted from rewards in Ready for withdrawal status.  
  

	- If there are insufficient funds in the program currency in Ready for withdrawal status, the missing amount will be deducted from funds in other currencies.
	- If the total amount of funds in Ready for withdrawal status is less than the amount that should be returned to the advertiser, they will be deducted from the balance, i.e., the total in one of the currencies in Ready for withdrawal status will turn negative.
- In [Reports on actions](https://store.admitad.com/en/webmaster/statistics/actions/), the status of these actions will remain Confirmed. This is caused by the system’s technical features.

- In the [Balance history](https://store.admitad.com/en/webmaster/balance-history/) section, you’ll see the operation with the type Withdrawal and the reason Fine for fraudulent actions.  
  

	- The comment on the reason will contain the program to which the fine relates.
	- The fine currency will match the program’s currency.

You can view the breakdown details by clicking Learn more in the reason and download a detailed report on the declined actions from the popup that opens.

If funds for declined actions under the affiliate program were deducted in several currencies, the [Balance history](https://store.admitad.com/en/webmaster/balance-history/) will show a separate deduction operation for each currency. In addition, a breakdown of each applied fine will contain all actions for which rewards were returned to the advertiser as part of one processing of fraudulent actions.

## The advertiser made a mistake when processing actions

For example, the advertiser calculated the reward incorrectly or assigned the wrong statuses.

In this case, until the advertiser provides the correct data:

- Actions will be returned to On hold status in the reports.
- Payments for the actions will change to On hold status in the Balance Details section.

Once the advertiser provides the correct statuses, all actions and rewards will get the corresponding status in the system.  
  

## Technical failure

In case of a technical failure, funds for actions that have been rejected or not yet processed may end up in Ready for withdrawal status.

In this case:

- You will receive an email notification about technical problems in the program.
- Actions will be returned to On hold status in reports, and rewards will switch to On hold status.

After troubleshooting, all actions and rewards will receive the corresponding status in the system.
