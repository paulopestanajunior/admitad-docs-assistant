---
title: How to get coupons and promo codes for Admitad programs
category: admitad-publishers
section: tools
language: en
source: https://support.mitgo.com/knowledge-base/article/how-to-get-coupons-and-promo-codes-for-admitad-programs_1
---

# How to get coupons and promo codes for Admitad programs

Coupons and promo codes are special offers from advertisers, including discounts, gifts with orders, free delivery, etc. They help additionally motivate users and encourage them to perform [target actions](https://support.mitgo.com/knowledge-base/article/admitad-partner-network-glossary_6#action-en).


In the Coupons and promo codes section (Tools → Coupons and promo codes), you can find:

- all coupons for all programs
- tracking promo codes issued to your ad space
- personal promo codes that advertisers have agreed and provided upon your request. [How to request a promo code from an advertiser](https://support.mitgo.com/knowledge-base/article/how-to-request-a-promo-code-from-an-admitad-advertiser_6).


You can only get a coupon if your ad space is already connected to a program. [What to do if your ad space is not yet connected to the program](#faq-0)


You can get coupons or promo codes in one of the following ways:

- [In the Coupons and promo codes and Promo code programs sections of your personal account](#account).
- [Using the Admitad Bot in Telegram](#telegram-bot).
- [Via API](#api).


You can only request access to a tracking promo code in the Promo code programs section.

## How to get coupons and promo codes in your account


1\. Go to the Tools → Coupons and promo codes section.


Tracking promo codes can also be obtained in the Promo code programs section. Learn more in the article ["How to get a tracking promo code for a program"](https://support.mitgo.com/knowledge-base/article/creator-programs-description-and-features#get_promo)


2\. To quickly find specific coupons and promo codes:

- Enter a keyword in the search bar above the list of coupons and click Search.
- Use the filters on the left. You can use one or several filters.


You can find filter descriptions below. Click a filter name to expand its description.

- ◆ Ad space. Here you can select one of your ad spaces for which you want to get a promo code. 

◆ Region. Use this filter to find coupons and promo codes for a specific country.  
You might want to select the regions that match your audience's region. For example, if you know your subscribers are from Germany, it makes sense to offer them coupons valid there.

◆ Langauge. This filter helps you find coupons and promo codes in a certain language.  
If your ad space mostly targets French\-speaking users, it would be reasonable to offer them coupons in French.
- Using this filter, you can find coupons and promo codes:

	- Only for the programs to which your ad space is already connected. For this, check the Only joined programs option.
	- Find coupons and promo codes for certain programs. To do that, start typing the program name in the Search by program field and then check the relevant program.
- ◆ Admitad specials. Use this filter to find exclusive coupons and promo codes only available in Admitad.

◆ Personal promo codes. This filter will help you find promo codes that you can use without placing an affiliate link.  
Personal promo codes have a set of features:

	- Such promo codes contain a unique keyword word used to track target actions.
	- Advertisers can provide them at your request. [How to request a promo code](https://support.mitgo.com/knowledge-base/article/how-to-request-a-promo-code-from-an-admitad-advertiser_6).
	- You can use them to keep track of statistics in the corresponding section (Reports → on personal promo codes). [Learn more about this section](https://support.mitgo.com/knowledge-base/article/admitad-reports_1).
◆ Coming soon. This filter will let you find coupons and promo codes that will become available later. Use them to prepare for a deal and plan your content.

◆ Coupon link. This filter will help you find coupons. A coupon link is activated automatically only when users follow the affiliate link.

◆ Promo code. You can find promo codes using this filter. A user must enter a keyword to get a discount when placing an order. With that said:

	- If this is a personal promo code, you don't have to place an affiliate link.
	- With tracking promo codes, the user can either use only the promo code or follow the affiliate link and enter the promo code. Learn more from [Promo code programs: description and features](https://support.mitgo.com/knowledge-base/article/creator-programs-description-and-features).
- Using this filter, you'll find coupons and promo codes that apply to a specific product category. For example, you might want to use it if you own a blog about books and are looking for book\-related deals.
- Use this filter to find coupons and promo codes for AliExpress Hot Products.


3\. After you find relevant coupons or promo codes, you can:

- Get a single coupon or promo code.
- Export coupons or promo codes as a file (XML, CSV, or XLSX) or get an export link.


Switch to the tab with the instructions.

- 4\. Select a coupon or promo code.


Pay attention to the terms of the deal and its validity period to avoid posting a coupon or promo code that is about to expire.


5\. Click Get code on the coupon or promo code card.


If there's no Code button in the card, your ad space isn't connected to this program. [What to do in this case](#faq-0)


6\. In the pop\-up window, you'll see information about the coupon or promo code and two fields with affiliate links that you can place on your ad space.

	- Link. Following this link, the user will see the deal terms shown in an iframe at the top of the screen.
	- Direct link. Following this affiliate link, the user will be directed to the deal or product page.  
	*You might want to use a direct link since browsers sometimes block iframe.*
*In this window, you can also generate a deeplink to redirect a user to a certain webpage: a product or product category to which the coupon or promo code applies. To do that, click Deeplink generator, paste the product/category link into the field, and click Generate.*

  
7\. Place the coupon/promo code and its affiliate link on your ad space.


If you use a personal promo code, you don't have to place an affiliate link. Actions will be tracked by the keyword.
- The file will only include coupons and promo codes for the programs to which your ad space is connected. If you use filters, the file will only contain the relevant promo codes.


8\. Click Export in the top\-right corner and:

	- Select Download XML/CSV/Excel (depending on the preferred format). The file will be saved to your computer.
	- Or click Get link to copy the file link in the preferred format. Following it will save the file to your computer.
	- | Parameter | Description |
	| --- | --- |
	| id | Coupon ID |
	| name | Coupon name |
	| site | Direct link to the advertiser's website |
	| rating | Coupon rating |
	| advcampaign\_id | Program ID |
	| advcampaign\_name | Program name |
	| logo | Link to the file containing the program logo |
	| description | Coupon description (deal terms) |
	| species | Coupon format:  	- action — deal 	- promocode — promo code |
	| promocode | Keyword (applicable to promo codes only) |
	| promolink | Coupon link (when clicking it, the iframe coupon header will appear) |
	| gotolink | Coupon direct link (leads to the deal page) |
	| date\_start | Coupon start date |
	| date\_end | Coupon end date |
	| types | Coupon type. Can be represented in the following values:  	- 1 — Free delivery 	- 2 — Order discount 	- 3 — Gift for an order |
	| exclusive | Whether a coupon belongs to an exclusive program |
	| categories | Coupon category |
	| special\_category | Special coupon category |
	| discount | Discount amount: A fixed amount or percentage. Only the coupons of the discount for an order type have this parameter. |
9\. You're all set! Use the file to deploy coupons and promo codes on your ad space.

## How to get coupons and promo codes using the Telegram bot


To use Admitad Bot, your device must have [Telegram messenger](https://telegram.org/?setln=en) installed.


Admitad Bot is a Telegram bot that allows users to access the main features of their Admitad account.


To get coupons or promo codes for an affiliate program:


1\. Find [Admitad Bot on Telegram](https://t.me/admitad_bot) and log in to your account following [this guide](https://support.mitgo.com/knowledge-base/article/admitad-bot-for-telegram_5#how-start-work). 


2\. Get coupons and promo codes following [this guide](https://support.mitgo.com/knowledge-base/article/admitad-bot-for-telegram_5#get-coupons-promo-codes).

## How to get coupons and promo codes via API


Using the API, you can get:

- A list of all coupons
- A list of all coupons available for your ad space
- A list of coupon categories
- a list of tracking promo codes issued to your ad space.


To learn more, see the [Coupons](https://developers.admitad.com/knowledge-base/article/coupons_1) API method.

## FAQ on coupons and promo codes

- [How do I get a promo code or coupon if my ad space isn't connected to a program?](#faq-0)
- [Will the system attribute the order to me if the user applies a promo code but visits the advertiser's website without going through my affiliate link?](#faq-1)
- [Can I generate an affiliate link to the deal page by myself?](#faq-2)
- [Can I use coupons or promo codes from sources other than Admitad in my ad space?](#faq-3)

### How do I get a promo code or coupon if my ad space isn't connected to the program?


To obtain a coupon:


2\. In the coupon card, click Join program. You will be redirected to the program page.


3\. Connect your ad space to the program following [this guide](https://support.mitgo.com/knowledge-base/article/how-to-join-an-affiliate-program_3#join-on-page).


1\. Once your ad space is connected to the program, you'll be able to get coupons and promo codes for it following the [guide above](#all-methods).


To get a tracking promo code, go to the Promo code programs section and request a code. Once the tracking promo code is issued to your ad space, it will appear in the Coupons and promo codes section.

### Will the system attribute the target action to me if the user applies a promo code but visits the advertiser's website without going through my affiliate link?


The action will be credited if you use:

- Tracking promo codes: Tracking can occur only via the promo code or both the promo code and link, but the promo code always has priority. To find such a promo code in the Coupons \& Deals section, select Tracking promo codes in the coupon type filter.
- You'll see coupons and promo codes for affiliate programs from Admitad Store.
	- You can request such a promo code from the advertiser ([here's how you can do it](https://support.mitgo.com/knowledge-base/article/how-to-request-a-promo-code-from-an-admitad-advertiser_6)).
	- To find such a promo code in Coupons and promo codes, check the Personal promo codes option in the filter by coupon type.


For coupons, it's mandatory that users follow the affiliate link.

### Can I generate an affiliate link to the deal page by myself?


Yes, you can do it with the [Deeplink Generator](https://support.mitgo.com/knowledge-base/article/deeplink_20) tool. However, make sure that it's not prohibited by the program rules. If in doubt, confirm using self\-created links in a [ticket to Admitad support](https://support.mitgo.com/knowledge-base/article/how-to-contact-admitad-support_6). Some advertisers have different coupons for different marketing channels, and they prohibit using those that publishers could independently find online.


Another advantage of the ready\-to\-use coupon links is their detailed analytics. When using custom links, all clicks and actions will be counted under one Default link section, while using ready\-made links allows you to see the breakdown by separate coupons and understand which ones work and which don't. To do so, go to the Reports on programs section and click the program name.


You can also view the statistics on personal promo codes in the corresponding section (menu → Reports → on personal promo codes.  
[Learn more about this section](https://support.mitgo.com/knowledge-base/article/admitad-reports_1#Reports-on-take&go-promocodes)

### Can I use coupons or promo codes from sources other than Admitad in my ad space?


No, you cannot use coupons and/or promo codes that aren't placed in Admitad or aren't intended for your ad space.


Actions made after following your affiliate links and using coupons or promo codes from third\-party sources will be declined. In addition, the advertiser may disconnect you from the affiliate program for such behavior.


Admitad strongly recommends that you only use coupons and promo codes designed for your ad space and available to you in the Promo code programs and Coupons and promo codes sections (Tools → Coupons and promo codes).
