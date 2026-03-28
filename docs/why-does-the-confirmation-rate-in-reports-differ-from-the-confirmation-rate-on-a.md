---
title: Why does the confirmation rate in reports differ from the confirmation rate on a program page?
section: faq
source: https://support.mitgo.com/knowledge-base/article/why-does-the-confirmation-rate-in-reports-differ-from-the-confirmation-rate-on-a-program-page_5
---

# Why does the confirmation rate in reports differ from the confirmation rate on a program page?

Both indicators represent the percentage of confirmed orders compared to the total number of processed orders, but the periods for which they are calculated are different:

- the confirmation rate in the advertiser reports (advertiser account — Reports — Reports by time) is calculated *for all days up to the current*,
- but when calculating the confirmation rate on a program page, *the last 30 days are not included*.

This logic was implemented on purpose, as recent days usually contain a large number of unprocessed actions, that can affect the statistics.

A detailed scheme for calculating the confirmation rate on a program page is as follows:

1\. 30 days are subtracted from the current date. That is the end date of the period.

2\. Then 360 days are subtracted from the end date. This is the start date.

3\. All actions with the status "Confirmed" within the received period are summed up.

4\. All actions with statuses "Confirmed" and "Rejected" are summarized.

5\. The number of confirmed actions is divided by the number of processed actions and multiplied by 100%.

The received value is the confirmation rate that is displayed on the program page.  
  

So, the confirmation rate on the program page is calculated with a delay of 30 days. Therefore, if in the previous months you declined a lot of actions, but recently things have changed, your confirmation rate will still be low for some time, but eventually it will improve.
