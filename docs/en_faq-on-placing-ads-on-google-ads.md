---
title: FAQ on placing ads on Google Ads
category: admitad-publishers
section: affiliate-links-and-creatives
language: en
source: https://support.mitgo.com/knowledge-base/article/faq-on-placing-ads-on-google-ads-and-yandex-direct_6
---

# FAQ on placing ads on Google Ads

## I’ve joined a program. Can I place ads on Google Ads?


You can place ads on Google Ads if the program allows contextual advertising.


To determine if it does, go to the program page, and in the menu on the left, choose Rules → Traffic Sources.


Scroll to the SEM section. In the right column, there will be specified whether the traffic is allowed.

- Allowed — means that the traffic type is allowed and you can place ads on Google Ads. In this case, make sure to check the permission for the Brand bidding traffic type to correctly specify a list of negative keywords. [How to check](#question-4)
- Forbidden — the advertiser does not permit contextual advertising. If you place ads, the advertiser has the right to disconnect you from the program and cancel all your actions.
- Needs approval — the advertiser discusses the terms for placing ads individually with each publisher. [Contact Admitad support](https://support.admitad.com/hc/en-us/articles/360020421978#create) and ask for permission to place ads.


If the traffic type you're interested in is missing in the Traffic Types section on the program page, [contact Admitad support](https://support.admitad.com/hc/en-us/articles/360020421978) or your manager to learn whether it is allowed.

## Can I use the name of a brand in headlines and texts of advertisements?


It depends on the rules of a specific program.


To check whether the brand bidding is allowed, go to the program page and click Rules → Traffic types in the left menu.


Find Brand bidding.

- Allowed — means this traffic type is allowed in the program.
- Forbidden — means that the advertiser prohibited this traffic type. You can't use the brand name, transliteration, incorrect spelling, and derivatives of it.

In this case, make sure to add all inquiries the advertiser specified to the negative keywords list when setting up the ad campaign. [Where to get the list of negative keywords](#question-4)
- Needs approval — the advertiser discusses the terms for placing ads individually with each publisher. [Contact Admitad support](https://support.admitad.com/hc/en-us/articles/360020421978#create) and ask for permission to place ads.

## Where can I find the list of negative keywords for an ad?


You can find the list of negative keywords in:

- The description on the affiliate program page.
- The program rules (Rules → Basics).
- For some programs, the table that is downloaded when [exporting affiliate programs](https://support.admitad.com/hc/en-us/articles/360019182618-Overview-of-the-affiliate-program-catalog#sort-and-export) from the [catalog](https://store.admitad.com/en/catalog/) or My Programs section (the negative keywords column).

  
If you can’t find the list of negative keywords in the program, but brand bidding is forbidden (Menu → Rules → Traffic Sources), create the list yourself.


What should be included in it:

- the name of the brand (Tinkoff).
- transliterations of it.
- misspellings of it (tinkof, tenkof, tenkoff).
- derived words (tcs, tcsbank).

## What options do I have for setting up links for contextual advertising?

### Creating deeplinks


You can create deeplinks to send users right to the page of the product or product category being advertised. This will raise the ad’s conversion rate.


For instance, you place an ad for Nike sneakers being sold by Lamoda. It would be logical to take users right to the brand’s page, but the standard program link leads to the main page only. In this case, you can create a deeplink and use it to send users to the needed section (Nike’s).

[How to create a deeplink](https://support.admitad.com/hc/en-us/articles/360019283878-Deeplink#how-to-make-deeplink)

### Adding SubIDs


You can add SubIDs to links in ads to track how much revenue ads generate for you.


For instance, you’re fine\-tuning your work with a new program and, as a test, place 20 ads for different goods using different keywords. Add SubIDs to them with the ID values for the ad and the keywords in order to track what ads get the most clicks and completed actions in Admitad Partner Network reports.


You can add up to 5 SubIDs (subid, subid1\-subid4\) to a link. If the first SubID comes right after the "/", it’ll be added preceded by a "?", and the rest will be separated by "\&".

> Example
> 
> 
> 
> https://ad.admitad.com/g/vh8fva0nqac09fee9900adaede9fe3/*?subid\=4\&subid1\=iphone\_x*

#### Dynamic SubIDs


With dynamic SubIDs, the values related to each ad get entered into the link automatically replacing the SubIDs.


In the example above, we talked about 20 ads with different ad IDs and keywords. Instead of putting SubID values into each one manually, you can put the {ad\_id} parameter in the link instead of IDs and {keyword} instead of keywords.

> Example
> 
> 
> 
> https://ad.admitad.com/g/vh8fva0nqac09fee9900adaede9fe3/*?subid\={ad\_id}\&subid1\={keyword}*
> 
> 
> 
> *Then, when a user clicks the link, this will be the link that gets created:  
> https://www.lamoda.ru/b/2047/brand\-nike/?subid\=7\&subid1\=buy\_airpods*
> 
> 
> 
> *The {ad\_id} parameter will take the value of the ad ID, while {keyword} will be replaced with the ad’s keyword — here, “buy\_airpods.”*

  
The SubID values match the values on Google Ads.

[List of parameters for Google Ads](https://support.google.com/google-ads/answer/6305348?...&hl=en)

## How do I add affiliate links (including deeplinks) to Google Ads ads?


Admitad Partner Network has a special tool, Google Ads, which provides ready\-to\-use information for creating Google Ads. Among other things, it helps you create deeplinks and add them to SubID links.


For more information on the tool and on how to add ready\-to\-use data to an advertisement, see [How do I paste an affiliate link into Google Ads?](https://support.admitad.com/hc/en-us/articles/360019150757).


The tool is not available for programs for which contextual advertising is disabled.

## Do I have to enter every SubID value manually?


No, you can use [dynamic SubIDs](#dynamic-subid) in the link.
