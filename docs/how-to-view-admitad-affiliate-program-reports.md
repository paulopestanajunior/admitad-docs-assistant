---
title: How to view Admitad affiliate program reports
section: working-with-publishers
source: https://support.mitgo.com/knowledge-base/article/how-to-view-admitad-affiliate-program-reports_6
---

# How to view Admitad affiliate program reports

The information presented in the Reports section will help you:

- Analyze the performance of your affiliate program and publishers who joined it
- Optimize program management to generate more target actions

## How to find reports


To get to the section, in the upper menu, hover over the Reports section and click the subsection you need:

- [On time](#time-report)
- [On actions](#action-report)
- [On publishers](#publishers-report)
- [On ad spaces](#adspaces-report)
- [On banners](#banner-report)
- [On landing pages](#landing-report)
- [On channels](#channels-report)
- [On groups](#groups-report)
- [On countries](#geo-report)


All information is arranged as a table. Read the full description of each subsection below.


In each subsection, you can:

- View and filter data in the table
- Export the report as an Excel file. Just click Export
- View report export history


Reports are updated several times a day. If the system is experiencing an increased load, report updates may take longer.


At the bottom of the page is the total value for each column of the report table:

- Page total. Shown if there is more than one page
- Total. This is the total for all available data for a selected period

## Reports by time


In this section, you can track publishers' performance in your program by day or month for a selected period.

### Things to know

- If you view the report by day, the table will only show the days for which there is information in at least one column.
- The report shows the number of target actions of two types: leads and sales. If your program uses [bonuses](https://support.admitad.com/hc/en-us/articles/4405926852113-%D0%91%D0%BE%D0%BD%D1%83%D1%81%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B8-%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D1%8B), the amount of bonuses will be included in the values in the Amount column. But their number won't be shown anywhere.  
There might be a situation where the Leads and Sales columns will be empty, and the total of bonuses will appear in the Amount column.

### Data and indicators in the table

- Date. Date or month (depending on the setting you selected).  
The values in this column are clickable and lead to the [Reports on actions](#action-report) section with data for the selected period.
- Views. If publishers use your banners or coupons on their sites, this column will show the total number of unique views for such publishers.  
You can view reports for each ad creative in Reports on banners. [Learn more](#banner-report)
- Clicks. The total number of clicks on ad creatives and/or the affiliate link on the sites of all publishers.
- CTR. The percentage ratio of the number of clicks to the number of views for the selected period.  
Calculated according to the following formula: 
`Clicks / Views × 100%`
.

*All CTR values that are 100% and higher are shown as 100%.*
- CPC. Earnings per click. Calculated according to the following formula: 
`Amount (Confirmed + On hold) / Clicks`
.
- eCPM. Earnings per 1,000 views.  
Calculated according to the following formula: 
`Amount (Confirmed + On hold) / views × 1,000`
.
- CR (Conversion Rate). The percentage ratio of the total number of target actions and leads (on hold, confirmed, and declined) to the total number of clicks. Calculated according to the following formula: 
`(Leads + Sales) / Clicks × 100%`
.
- Actions / Amount. The number of target actions (leads and sales) performed by users for the selected period and the amount of the publisher's reward for them.

The values in the Leads and Sales columns are clickable. You can click them to go to the Reports on actions section, where you will see the information for the selected period. [Learn more](#action-report)


It contains some extra columns:

	- On hold. These are leads and sales registered by the system but which you haven't [verified](https://support.admitad.com/hc/en-us/articles/4405920549905) yet and estimated amounts of publisher rewards for these target actions.
	- Confirmed. These are leads and sales that you confirmed during [verification](https://support.admitad.com/hc/en-us/articles/4405920549905) and the amounts of publisher rewards for these target actions.  
	*Also displayed for this indicator is the confirmation percentage, which is the ratio of confirmed actions to the sum of confirmed and declined actions. If there are no confirmed or declined actions, "—" will be in the column.*
	- Declined. These are leads and sales that you declined during [verification](https://support.admitad.com/hc/en-us/articles/4405920549905) and the amount of publisher rewards for these actions.

## Reports on actions


This section shows information on all target actions generated by the publishers who contribute or used to contribute to your affiliate program.

### Data and indicators in the table

- ID. A unique action number assigned by Admitad. Under the ID is the flag of the country where the action was performed.  
The  icon means that the click referrer (i.e., the page from which the user came to your website) doesn't match the ad space's URL.  
If you click the value in this cell, you will see visitor information and detailed action information.
- Click time. The date and time when the user came to your site.
- Action time. The date and time when the user performed the target action on your website.
- Conversion time. The period that elapsed from the moment of the click to the moment when the action was performed.
- Ad space / Publisher. The name of the ad space where the click occurred and the ID of its owner.  
The ad space name is clickable and leads to the page of this ad space in My publishers.
- Country. The name of the country where the action was performed.
- Rate. The rate that applies to the performed action.  
Based on the rate, the system calculates the reward to the publisher specified in the Expenses on publishers column.
- Order ID. A unique order number in your system.
- Order amount. The amount of the user's order. It's not specified for leads.


You should take note if you see an order amount that's seemingly too large.

- Status. The action status is:
	- On hold if you haven't processed the target action yet.
	- Confirmed if you have confirmed the target action.
	- Declined if you have declined the target action.
- Date processed.
	- In this section, you will see the date when the hold period will end, i.e., the time by which you should finish processing these actions for actions with the On hold status.  
	If you fail to process the actions by this time, the hold period will be automatically prolonged for the same period, and the estimated processing date will be automatically pushed back.
	- For actions with the Confirmed or Declined status, you will see the date when you processed them.
- Total expenses. The sum of the Admtiad fee and the publisher's reward which is calculated based on the rate of the action.

## Reports on publishers


This section shows information on all publishers you have cooperated with and/or cooperate with today.

### Data and indicators in the table

- Publisher. The publisher's ID.  
If you click a value in this column, you will see a [report on time](#time-report) for the publisher for the selected period.
- Views. If publishers use your banners or coupons on their sites, this column will show the total number of unique views for such publishers.  
You can view reports for each ad creative in Reports on banners. [Learn more](#banner-report)
- Clicks. The total number of clicks on ad creatives and/or the affiliate link on the sites of all publishers.
- CTR. The percentage ratio of the number of clicks to the number of views for the selected period.  
Calculated according to the following formula: 
`Clicks / Views × 100%`
.  
*All CTR values that are 100% and higher are shown as 100%.*
- eCPC. Earnings per click. Calculated according to the following formula: 
`Amount (Confirmed + On hold) / Clicks`
.
- eCPM. Earnings per 1,000 views.  
Calculated according to the following formula: 
`Amount (Confirmed + On hold) / views × 1,000`
.
- CR (Conversion Rate). The percentage ratio of the total number of target actions and leads (on hold, confirmed, and declined) to the total number of clicks. Calculated according to the following formula: 
`(Leads + Sales) / Clicks × 100%`
.


The average for this column is 0\.5% to 1\.5%. It may be 5% for content sites. If the publisher's conversion rate is 80\-100%, be sure their traffic is of sufficient quality.  
Take into account the number of clicks and actions. If the publisher only has 1 click and a related action, there will be nothing suspicious about the 100% conversion rate. If the publisher has 1,000 clicks and 900 actions and the conversion rate is 100%, this may be a sign of poor traffic quality.

- Actions / Amount. The number of target actions (leads and sales) performed by users for the selected period and the amount of money for them.  


The values in the Leads and Sales columns are clickable. You can click them to go to the Reports on actions section, where you'll see the information for a specific publisher for the selected period. [Learn more](#action-report)


Action statuses:

	- On hold. Leads and sales that were registered by the system but which you haven't processed yet, and the amount for the actions on hold.
	- Confirmed. Leads and sales that you confirmed during verification, and amounts of publisher rewards for these target actions. Also displayed for this indicator is the confirmation percentage, which is the ratio of confirmed actions to the sum of money for confirmed and declined actions. If there are no confirmed or declined actions, the column will contain "—".
	- Declined. Leads and sales that you declined, and the amount for the declined actions.


The report shows the number of target actions of two types: leads and sales. If your program uses [bonuses](https://support.admitad.com/hc/en-us/articles/4405926852113-%D0%91%D0%BE%D0%BD%D1%83%D1%81%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B8-%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D1%8B), the amount of bonuses will be included in the values in the Amount column. But their number won't be shown anywhere.  
There might be a situation where the Leads and Sales columns will be empty, and the amount of bonuses will appear in the Amount column.

## Reports on ad spaces


This section shows information on all ad spaces where publishers place and/or placed information on your products or services.

### A few things to keep in mind

- Information in this section will be helpful if, for example, you decide to compare the performance of different ad spaces of one publisher.
- The report shows the number of target actions of two types: leads and sales. If your program uses [bonuses](https://support.admitad.com/hc/en-us/articles/4405926852113-%D0%91%D0%BE%D0%BD%D1%83%D1%81%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B8-%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D1%8B), the amount of bonuses will be included in the values in the Amount column. But their number won't be shown anywhere.  
There might be a situation where the Leads and Sales columns will be empty, and the amount of bonuses will appear in the Amount column.

### Data and indicators in the table

- Ad space. The name of the publisher's ad space.  
If you click on a value in this column, you will see a [report on time](#time-report) for this ad space for the selected period.
- Views. If publishers use your banners or coupons on their site, this column will show the total number of unique views of banners.  
You can view reports by creative in Reports on banners. [Learn more](#banner-report)
- Clicks. The total number of clicks on creatives and/or the affiliate link for specific ad spaces.
- CTR. The percentage ratio of the number of clicks to the number of views for the selected period.  
Calculated according to the following formula: 
`Clicks / Views × 100%`
.  
*All CTR values that are 100% higher than are shown as 100%.*
- eCPC. Earnings per click. Calculated according to the following formula: 
`Amount (Confirmed + On hold) / Clicks`
.
- eCPM. Earnings per 1,000 views.  
Calculated according to the following formula: 
`Amount (Confirmed + On hold) / views × 1,000`
.
- CR (Conversion Rate). The percentage ratio of the total number of target actions and leads (on hold, confirmed, and declined) to the total number of clicks. Calculated according to the following formula: 
`(Leads + Sales) / Clicks × 100%`
.


The average for this column is 0\.5% to 1\.5%. It may be 5% for content sites. If the publisher's conversion rate is 80\-100%, be sure their traffic is of sufficient quality.  
Take into account the number of clicks and actions. If the publisher only has 1 click and a related action, there will be nothing suspicious about the 100% conversion rate. If the publisher has 1,000 clicks and 900 actions and the conversion rate is 100%, this may be a sign of poor traffic quality.

- Actions / Amount. The number of target actions (leads and sales) performed by users on a specific ad space for the selected period and the amount of the publisher's reward for them.

The values in the Leads and Sales columns are clickable. You can click on them to go to the Reports on actions section, where you will see the information for a specific ad space for the selected period. [Learn more](#action-report)


Action statuses:  

	- On hold. These are leads and sales that were registered by the system but which you haven't processed yet and the amount for actions on hold.
	- Confirmed. These are leads and sales that you confirmed during verification and the amounts of publisher rewards for these target actions. Also displayed for this indicator is the confirmation percentage, which is the ratio of confirmed actions to the sum of confirmed and declined actions. If there are no confirmed or declined actions, the column will contain "—".
	- Declined. These are leads and sales that you declined and the amount for the declined actions.

## Reports on banners


In this section, you can see which of the added coupons demonstrated the best performance and generated the largest revenue.

### Things to know

- This section contains information on banners, as well as coupons and affiliate links.
- When comparing coupons, refer to the number of confirmed actions and their amount.
- The report shows the number of target actions of two types: leads and sales. If your program uses [bonuses](https://support.admitad.com/hc/en-us/articles/4405926852113-%D0%91%D0%BE%D0%BD%D1%83%D1%81%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B8-%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D1%8B), the amount of bonuses will be included in the values in the Amount column. But their number won't be shown anywhere.  
There might be a situation where the Leads and Sales columns will be empty, and the total of bonuses will appear in the Amount column.

### Data and indicators in the table

- Banner. The name of the creative or affiliate link.  
If you click a value in this column, you will see a report on time for this creative or affiliate link for the selected period.
- Views. If the publisher uses your banners or coupons on their ad space, this column will show the number of unique views for a specific ad space or affiliate link.
- Clicks. The total number of clicks for a specific ad creative or affiliate link.
- CTR. The percentage ratio of the number of clicks to the number of views for the selected period.  
Calculated according to the following formula: 
`Clicks / Views × 100%`
.  
*All CTR values that are 100% and higher are shown as 100%.*
- eCPC. Earnings per click. Calculated according to the following formula: 
`Amount (Confirmed + On hold) / Clicks`
.
- eCPM. Earnings per 1,000 views.  
Calculated according to the following formula: 
`Amount (Confirmed + On hold) / views × 1,000`
.
- CR (Conversion Rate). The percentage ratio of the total number of target actions and leads (on hold, confirmed, and declined) to the total number of clicks. Calculated according to the following formula: 
`(Leads + Sales) / Clicks × 100%`
.
- Actions / Amount. The number of target actions (leads and sales) performed by users for the selected period and the amount for them.

The values in the Leads and Sales columns are clickable. You can click on them to go to the Reports on actions section, where you will see the information for a specific ad creative or affiliate link for the selected period. [Learn more](#action-report)


Action statuses:  

	- On hold. These are leads and sales that were registered by the system but which you haven't processed yet and the amount for actions on hold.
	- Confirmed. These are leads and sales that you confirmed during verification and the amounts of publisher rewards for these target actions. Also displayed for this indicator is the confirmation percentage, which is the ratio of confirmed actions to the sum of confirmed and declined actions. If there are no confirmed or declined actions, the column will contain "—".
	- Declined. These are leads and sales that you declined and the amount for the declined actions.

## Reports on landing pages


In this section, you can track the performance of your [landing pages](https://support.admitad.com/hc/en-us/articles/4405920540817).

### Things to know

- By default, information is sorted by the value of target actions, so you can see landing pages with the highest revenue for a selected period.
- When analyzing landing pages, refer to the amount of confirmed actions and the conversion rate for them.
- The report shows the number of target actions of two types: leads and sales. If your program uses [bonuses](https://support.admitad.com/hc/en-us/articles/4405926852113-%D0%91%D0%BE%D0%BD%D1%83%D1%81%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B8-%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D1%8B), the amount of bonuses will be included in the values in the Amount column. But their number won't be shown anywhere.  
There might be a situation where the Leads and Sales columns will be empty, and the total of bonuses will appear in the Amount column.

### Data and indicators in the table

- Landing page. The name of the landing page.  
If you click a value in this column, you will see a report on time for this landing page for the selected period.
- Views. You will see 0.
- Clicks. The total number of clicks for a specific landing page.
- CTR. The percentage ratio of the number of clicks to the number of views for the selected period. Since the number of views is 0, "—" will always be in this column.
- eCPC. Earnings per click. Calculated according to the following formula: 
`Amount (Confirmed + On hold) / Clicks`
.
- eCPM. Earnings per 1,000 views. Since the number of views is 0, "—" will always be in this column.
- CR (Conversion Rate). The percentage ratio of the total number of target actions and leads (on hold, confirmed, and declined) to the total number of clicks. Calculated according to the following formula: 
`(Leads + Sales) / Clicks × 100%`
.
- Actions / Amount. The number of target actions (leads and sales) performed by users for the selected period and the amount for them.

The values in the Leads and Sales columns are clickable. You can click them to go to the Reports on actions section, where you'll see the information for a specific landing page for the selected period. [Learn more](#action-report)


Action statuses:  

	- On hold. These are leads and sales that were registered by the system but which you haven't processed yet and the amount for actions on hold.
	- Confirmed. These are leads and sales that you confirmed during verification and the amounts of publisher rewards for these target actions. Also displayed for this indicator is the confirmation percentage, which is the ratio of confirmed actions to the sum of confirmed and declined actions. If there are no confirmed or declined actions, the column will contain "—".
	- Declined. These are leads and sales that you declined and the amount for the declined actions.

## Reports on channels


In this section, you will find information on all the channels of your affiliate program and compare their performance.


If you need to compare the performance of the publishers or ad spaces within a channel, you might want to use the Reports on publishers section (see [this guide](#publishers-report)) or the Reports on ad spaces section (see [this guide](#adspaces-report)) to filter information by a specific channel.

### Things to know

- By default, information is sorted by the value of target actions, so you can see the channel with the highest revenue for the selected period if you have several.
- The report shows the number of target actions of two types: leads and sales. If your program uses [bonuses](https://support.admitad.com/hc/en-us/articles/4405926852113-%D0%91%D0%BE%D0%BD%D1%83%D1%81%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B8-%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D1%8B), the amount of bonuses will be included in the values in the Amount column. But their number won't be shown anywhere.  
There might be a situation where the Leads and Sales columns will be empty, and the total of bonuses will appear in the Amount column.

### Data and indicators in the table

- Channel. The channel name for publishers.  
If you click on a value in this column, you will see a [report on time](#time-report) for this channel for the selected period.
- Views. If publishers use your banners or coupons on their site, this column will show the total number of unique views for such publishers.  
You can view reports for each ad creative in Reports on banners. [Learn more](#banner-report)
- Clicks. The total number of clicks on creatives and/or the affiliate link for a specific channel.
- CTR. The percentage ratio of the number of clicks to the number of views for the selected period.  
Calculated according to the following formula: 
`Clicks / Views × 100%`
.  
*All CTR values that are 100% and higher are shown as 100%.*
- eCPC. Earnings per click. Calculated according to the following formula: 
`Amount (Confirmed + On hold) / Clicks`
.
- eCPM. Earnings per 1,000 views.  
Calculated according to the following formula: 
`Amount (Confirmed + On hold) / views × 1,000`
.
- CR (Conversion Rate). The percentage ratio of the total number of target actions and leads (on hold, confirmed, and declined) to the total number of clicks. Calculated according to the following formula: 
`(Leads + Sales) / Clicks × 100%`
.
- Actions / Amount. The number of target actions (leads and sales) performed by users within a specific channel for the selected period and the amount of money for them.

The values in the Leads and Sales columns are clickable. You can click them to go to the Reports on actions section, where you'll see the information for a specific channel for the selected period. [Learn more](#action-report)


Action statuses:  

	- On hold. These are leads and sales that were registered by the system but which you haven't processed yet and the amount for actions on hold.
	- Confirmed. These are leads and sales that you confirmed during verification and the amounts of publisher rewards for these target actions. Also displayed for this indicator is the confirmation percentage, which is the ratio of confirmed actions to the sum of confirmed and declined actions. If there are no confirmed or declined actions, the column will contain "—".
	- Declined. These are leads and sales that you declined and the amount for the declined actions.

## Reports on groups


In this section, you will find information on all the groups of your affiliate program and compare their performance.


If you need to compare the performance of the publishers or ad spaces within a group, you might want to use the Reports on publishers section (see [this guide](#publishers-report)) or the Reports on ad spaces section (see [this guide](#adspaces-report)) to filter information by a specific group.

### Things to know

- By default, information is sorted by the value of target actions, so you can see the channel with the highest revenue for the selected period if you have several.
- The report shows the number of target actions of two types: leads and sales. If your program uses [bonuses](https://support.admitad.com/hc/en-us/articles/4405926852113-%D0%91%D0%BE%D0%BD%D1%83%D1%81%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B8-%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D1%8B), the amount of bonuses will be included in the values in the Amount column. But their number won't be shown anywhere.  
There might be a situation where the Leads and Sales columns will be empty, and the total of bonuses will appear in the Amount column.

### Data and indicators in the table

- Group. The group name for publishers.  
If you click on a value in this column, you will see a [report on time](#time-report) for this group for the selected period.
- Views. If publishers use your banners or coupons on their site, this column will show the total number of unique views for such publishers.  
You can view reports for each ad creative in Reports on banners. [Learn more](#banner-report)
- Clicks. The total number of clicks on creatives and/or the affiliate link for a specific channel.
- CTR. The percentage ratio of the number of clicks to the number of views for the selected period.  
Calculated according to the following formula: 
`Clicks / Views × 100%`
.  
*All CTR values that are 100% and higher are shown as 100%.*
- eCPC. Earnings per click. Calculated according to the following formula: 
`Amount (Confirmed + On hold) / Clicks`
.
- eCPM. Earnings per 1,000 views.  
Calculated according to the following formula: 
`Amount (Confirmed + On hold) / views × 1,000`
.
- CR (Conversion Rate). The percentage ratio of the total number of target actions and leads (on hold, confirmed, and declined) to the total number of clicks. Calculated according to the following formula: 
`(Leads + Sales) / Clicks × 100%`
.
- Actions / Amount. The number of target actions (leads and sales) performed by users within a specific group for the selected period and the amount for them.

The values in the Leads and Sales columns are clickable. You can click them to go to the Reports on actions section, where you'll see the information for a specific group for the selected period. [Learn more](#action-report)


Action statuses:  

	- On hold. These are leads and sales that were registered by the system but which you haven't processed yet and the amount for actions on hold.
	- Confirmed. These are leads and sales that you confirmed during verification and the amounts of publisher rewards for these target actions. Also displayed for this indicator is the confirmation percentage, which is the ratio of confirmed actions to the sum of confirmed and declined actions. If there are no confirmed or declined actions, the column will contain "—".
	- Declined. These are leads and sales that you declined and the amount for the declined actions.

## Reports on countries


This section shows the reports on countries where target actions for your affiliate program were performed.


This information may come in handy if you need to find out in which regions your program performs the best.

### Things to know

- By default, information is sorted by the value of target actions, so you can see the country with the highest revenue for the selected period.
- The report shows the number of target actions of two types: leads and sales. If your program uses [bonuses](https://support.admitad.com/hc/en-us/articles/4405926852113-%D0%91%D0%BE%D0%BD%D1%83%D1%81%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B8-%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D1%8B), the amount of bonuses will be included in the values in the Amount column. But their number won't be shown anywhere.  
There might be a situation where the Leads and Sales columns will be empty, and the total of bonuses will appear in the Amount column.

### Data and indicators in the table

- Country. The name of the country where users performed the target action.
- Views. If publishers use your banners or coupons on their site, this column will show the total number of unique views for such publishers.  
You can view reports for each ad creative in Reports on banners. [Learn more](#banner-report)
- Clicks. The total number of clicks on creatives and/or the affiliate link for a specific country.
- CTR. The percentage ratio of the number of clicks to the number of views for the selected period.  
Calculated according to the following formula: 
`Clicks / Views × 100%`
.  
*All CTR values that are 100% and higher are shown as 100%.*
- eCPC. Earnings per click. Calculated according to the following formula: 
`Amount (Confirmed + On hold) / Clicks`
.
- eCPM. Earnings per 1,000 views.  
Calculated according to the following formula: 
`Amount (Confirmed + On hold) / views × 1,000`
.
- CR (Conversion Rate). The percentage ratio of the total number of target actions and leads (on hold, confirmed, and declined) to the total number of clicks. Calculated according to the following formula: 
`(Leads + Sales) / Clicks × 100%`
.
- Actions / Amount. The number of target actions (leads and sales) performed by users in a specific country for the selected period and the amount for them.

Action statuses:  

	- On hold. These are leads and sales that were registered by the system but which you haven't processed yet and the amount for actions on hold.
	- Confirmed. These are leads and sales that you confirmed during verification and the amounts of publisher rewards for these target actions. Also displayed for this indicator is the confirmation percentage, which is the ratio of confirmed actions to the sum of confirmed and declined actions. If there are no confirmed or declined actions, the column will contain "—".
	- Declined. These are leads and sales that you declined and the amount for the declined actions.
