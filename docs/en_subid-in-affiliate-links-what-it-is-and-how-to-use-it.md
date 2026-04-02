---
title: SubID in affiliate links: what it is and how to use it
category: mitgame
section: affiliates
language: en
source: https://support.mitgo.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_10
---

# SubID in affiliate links: what it is and how to use it

A SubID is a parameter that can be added to [affiliate links](https://support.admitad.com/hc/en-us/articles/4403304880529#affiliate-link-en). It works like a special tag that helps track how many clicks and actions users performed after following a certain link or clicking on a certain ad.

## What SubIDs are needed for

Such an addition will allow filtering data in reports by SubID and analyze the performance of every specific link or ad.

Example

You're cooperating with a perfume store and want to place five affiliate links for different brands of cologne in your Facebook group. You'd like to know what cologne interests your subscribers most. Add SubIDs with the names of the brands (for instance: lacoste, kenzo, dkny, givenchy, calvin klein) to the affiliate links. Then you'll be able to filter the data in reports by SubID and see the number of clicks and actions for each link. By analyzing this data, you'll be able to determine which brands suit your subscribers and which you can drop.

A few more cases where SubIDs could come in handy:

- If you use the same affiliate link in your ad space several times. For instance, you included it in several posts in your Facebook group. Using SubIDs will let you know which post was the most successful.
- If you do SEM, you can use SubIDs with key phrases from the ad or the region at which it's targeted. Then you'll get reports broken down according to key phrases and regions.
- If you work with mobile programs, you can use SubIDs with parameters that are important to you but that Admitad doesn't track: click\_id (cid), aff\_sub, subaccount, adset\_id, source\_id, etc. (See "[click\_id and transaction\_id macro](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#click-id-and-transaction-id)")

Up to five SubIDs can be added to one link (SubID\-SubID4\), allowing you to get fairly detailed reports. By designing a system of assigning SubIDs that's convenient for you, you'll be better able to analyze your traffic and find the best way to place ads.

If you're going to use a personal promo code along with an affiliate link, do not add the SubID3 parameter to this link. The value you assign to this parameter will automatically be replaced by the information on the personal promo code. This is how the system works.  
  
You can use other parameters with personal promo codes: SubID, SubID1, SubID2, and SubID4\.

## How to add SubIDs to affiliate links

There are several ways to add SubIDs:

- In the [Deeplink section](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#adding-via-deeplink-on-programspage) on the program page. This method only allows adding one SubID to an affiliate link.
- Using the [Deeplink generator](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#adding-via-deeplink-generator). This method allows adding one SubID to several affiliate links.
- [Manually](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#adding-manually) — this way, you can add all five SubIDs to the link (SubID\-SubID4\). You can use this method if you need to pass click\_id or transaction\_id.

### How to add SubID in the Deeplink section of the program page

This method is only available if the program supports deeplinks. 

1\. Go to My programs and open the page of the program you need.

2\. In the left menu, click Banners and links → Deeplink.

If you don't see the Deeplink section in the menu, this means the program does not support deeplinks. Use another [method to add a SubID](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#how-to-add-subid) or select the program that supports deeplinks. 

 3\. You will see the page where you will be able to create a deeplink and add a SubID to it. In the SubID field (1\), enter the value you are going to add to the link as a tag. Later, you will be able to use this value to find and view the statistics (clicks, actions, etc.) for the link in the Reports on SubID section.

SubID requirements:

- Latin or Cyrillic letters, special characters, and spaces
- no more than 50 characters long
- do not use the "%00" combination

4\. In the new window, go to the advertiser website and open the page on which users will land after they follow the deeplink. Copy the page link and paste it to the Insert the link to the product or another page on the advertiser's website field (2\).

5\. In the Copy deeplink field (3\), you will see the deeplink with the specified SubID. Copy the link and deploy it in your ad space. 

In this section, you can also add a SubID to a standard affiliate link. For that, enter the SubID value but leave the Insert the link to the product or another page on the advertiser's website field empty. After that, paste the standard link with the specified SubID copied from the Copy deeplink field.

[\>\>\> Back to SubID adding methods](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#how-to-add-subid)

### How to add SubID using Deeplink generator

\> This method is only available if the program supports deeplinks.

1\. Go to the [Deeplink generator](https://account.admitad.com/en/webmaster/deeplink_generator/) page (Tools → Deeplink Generator).

2\. In the Ad space field (1\), select your ad space.

- If you only have one ad space, it will be added automatically.
- If you have several ad spaces, start entering the name and pick the one you need from the list.

3\. In the Program field (2\), select the program for which you need to create a deeplink with a SubID. You can create a deeplink only for those programs to which your ad space is already connected.

If you don't see the program you need on the list, this means the program does not support deeplinks. Select another program or use another [SubID adding method](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#how-to-add-subid).

4\. In the SubID tracking field (3\), enter the value you need to add to the link as a tag. Later, you will be able to use this value to find and view the statistics (clicks, actions, etc.) for the link in the Reports on SubID section. SubID requirements:

- Latin or Cyrillic letters, special characters, and spaces
- no more than 50 characters long
- do not use the "%00" combination

5\. In the new window, go to the advertiser website and open the page on which users will land after they follow the deeplink. Copy the link to the page and paste it to the field The list of links to generate deeplinks (4\).

You can paste several links to different pages of the advertiser website to this field. In this case, a deeplink with the specified SubID will be created for each of them.

6\. Click Generate.

7\. You will see the generated deeplinks in the Generated deeplinks field. The specified SubID will be added to each link.

You can copy the generated deeplinks or download them as a CSV file.

If you don't want to handle such a lengthy link, you can shrink by using [Shortlink](https://account.admitad.com/en/webmaster/shortlink/).

[\>\>\> Back to SubID adding methods](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#how-to-add-subid)

### Manually

You can add up to five parameters (SubID\-SubID4\) manually using the symbol \&. SubID requirements:

- Latin or Cyrillic letters, special characters, and spaces
- SubID, SubID1, SubID2, SubID3 must be no more than 50 characters long
- SubID4 must be no more than 120 characters long
- do not use the "%00" combination

If you need to add SubIDs not to a standard link, but to a [deeplink](https://support.admitad.com/hc/en-us/articles/360019283878), the SubID parameters can be entered both before and after the deeplink.

#### Examples

- [Example 1: Adding one SubID to a standard affiliate link](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#zp-1-0)
- [Example 2: Adding several SubIDs to a standard affiliate link](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#zp-2-0)
- [Example 3: Adding several SubIDs to a deeplink](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#zp-3-0)
- [Example 4: Addings several SubIDs to an affiliate link with a token (unique identifier)](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#zp-4-0)

[\>\>\> Back to SubID adding methods](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#how-to-add-subid)

## click\_id and transaction\_id macro

If you want to include your click\_id or transaction\_id parameters in the affiliate link, use SubID4\.

*Example of a link:* https://ad.admitad.com/g/f469ae904cb7e16523942b59d5275c/?subid4\={click\_id}

In this link, the value in curly brackets {click\_id} needs to be replaced with your click\_id value.

## How to see reports broken down by SubID

1\. Go to Reports → on SubID.

2\. The data is given as a table. By default, it's divided according to SubID. To see data for SubID1\-SubID4, make the corresponding selection in the field Show by.

Using filters, you can get data for a certain period, ad space, or program. Data can also be sorted by name, number of clicks, conversion rate, or actions.

## Limitations in reporting when using SubID

### Limitations on the number of unique codes

You can only see reports on SubID1, SubID2, SubID3, or SubID4 if the number of unique values for the SubID in the past 30 days doesn't exceed 100,000\. If it does, the SubID will disappear from the field Show by, and you won't be able to get data on it. For instance, if you've created 140,000 unique SubID2 values in the past 30 days, the only options in the Show by field will be SubID, SubID1, SubID3, and SubID4.

There are two ways this could happen:

1\. You've used more than 100,000 unique values for a SubID\-SubID4 parameter in the past three days. Grouping by this SubID will be disabled immediately, and you'll get a message in [the notification center](https://support.admitad.com/hc/en-us/articles/360020412238).

2\. You've used more than 100,000 unique values for a SubID\-SubID4 parameter in the past 30 days. [In the notification center](https://support.admitad.com/hc/en-us/articles/360020412238) you'll receive a warning that grouping for this SubID will be disabled in five days. If you really need such a large number of SubID values, create [an Admitad support request](https://support.admitad.com/hc/en-us/articles/360020421978) asking them to restore the grouping function within five days.

This won't affect tracking. In both cases, the SubIDs will continue to be recorded in the system and will be reflected in the section On Actions. You'll also be able to get them through the API method [Reports on actions](https://developers.admitad.com/hc/en-us/articles/7930541032849-Publisher-reports#reports-by-actions).

## Examples of how SubIDs can be used

[Example 1](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#example-1)

[Example 2](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#example-2)

[Example 3](https://admitad.useresponse.com/knowledge-base/article/subid-in-affiliate-links-what-it-is-and-how-to-use-it_16#example-3)

### Example 1

Let’s say you're a blogger who put a review of an action camera on YouTube. To monetize the video, you placed an affiliate link to the product page on aliexpress.com. To identify clicks and sales for this link, you marked it with subid\=action\_camera\_review.

You ended up with the following affiliate link:

https://alitems.com/g/1e8d114494c20f67753f16525dc3e8/?ulp\=https%3A%2F%2Fwww.aliexpress.com %2Fitem%2FAction\-Camera\-Full\-HD\-DVR\-Sport\-DV\-SJ4000\-upgrade\-version\-30m\-Wifi\-receiver\-1080P\-Helmet\- Waterproof%2F32231073816\.html\&subid\=action\_camera\_review

You put links with different SubID values in other video reviews: for example, subid\=tripod in the review of a tripod and subid\=waterproof\_box in the review of a waterproof box.

Now you'll be able to see how many clicks and sales were made via each affiliate link in Reports on SubID.

Then you saw that another AliExpress store sells the same camera in yellow and decided to offer it to your subscribers, too. As before, you need to see all the clicks and sales for the new link. You want to know both if your review makes subscribers buy this camera in general and which color is more popular.

You need to mark the new link with the same subid\=action\_camera\_review (this way we'll know that the traffic came from your review) and enter a new subid\=yellow marking to identify the color of the product.

Now the link will look like this:

https://alitems.com/g/1e8d114494c20f67753f16525dc3e8/?ulp\=https%3A%2F%2Fwww.aliexpress.com %2Fitem%2FAction\-Camera\-Full\-HD\-DVR\-Sport\-DV\-SJ4000\-upgrade\-version\-30m\-Wifi\-receiver\-1080P\-Helmet\- Waterproof%2F32231073816\.html\&subid\=action\_camera\_review\&subid1\=yellow

You'll change the link for the grey camera, as well, by adding subid1\=grey. The SubID value will remain the same: action\_camera\_review. But the subid\=grey tag will be added to it.

To see the report on SubID1, select Show by SubID1. We see that the yellow camera is more popular.

Thus, in our system, SubID is the identifier of a certain video on your YouTube channel and SubID1 is the identifier of a specific model of that product.

### Example 2

You're placing an advertisement for a travel service on a social network for the first time and aren't yet sure what audience it should be targeted at. To avoid wasting money, you decide to run a small test first: create several identical ads with different audience locations, ages, and genders.

You use three locations: Paris, Lyon, and Marseille. To distinguish between them in reports, you add a SubID parameter and use the names of the cities as the values.

https://ad.admitad.com/g/49c113f01e7122a2cb0502b3e23ee2/?subid\=paris https://ad.admitad.com/g/49c113f01e7122a2cb0502b3e23ee2/?subid\=lyon https://ad.admitad.com/g/49c113f01e7122a2cb0502b3e23ee2/?subid\=marseille

Then you need to set an appropriate audience age. You figure that the ads will be most relevant for users 18\-30 and 30\-45 years old, because they travel the most. You introduce a new parameter, SubID1, which will contain the age of the users. For convenience's sake, you mark the first group with 1 and the second with 2\. The SubID parameter remains so that you can still track the city.

https://ad.admitad.com/g/49c113f01e7122a2cb0502b3e23ee2/?subid\=paris\&subid1\=1 https://ad.admitad.com/g/49c113f01e7122a2cb0502b3e23ee2/?subid\=paris\&subid1\=2 https://ad.admitad.com/g/49c113f01e7122a2cb0502b3e23ee2/?subid\=lyon\&subid1\=1

Finally, you want to know whether the trips interest men or women more, so you make SubID2 the parameter for specifying gender.

The final links will look like this:

https://ad.admitad.com/g/49c113f01e7122a2cb0502b3e23ee2/?subid\=paris\&subid1\=1\&subid2\=man https://ad.admitad.com/g/49c113f01e7122a2cb0502b3e23ee2/?subid\=paris\&subid1\=1\&subid2\=woman https://ad.admitad.com/g/49c113f01e7122a2cb0502b3e23ee2/?subid\=paris\&subid1\=2\&subid2\=man https://ad.admitad.com/g/49c113f01e7122a2cb0502b3e23ee2/?subid\=paris\&subid1\=2\&subid2\=woman

The same principle is used to create links for the other locations.

Now you can compare the ads by three parameters — city, age, and gender — and decide what the target audience should be.

In the reports, you see that users in Paris and Lyon click on the ads in almost equal numbers, while interest in Marseille is only half as strong. Thus, it's better to concentrate on the first two cities.

  
After analyzing the reports on SubID1 and SubID2, you see that users 18\-30 years old got interested more often than the users 30\-45 years old.

  
Women are almost twice as interested as men.

Thus, using SubIDs, you identified the appropriate audience: women in Paris and Lyon between the ages of 18 and 30\.

### Example 3

If you place SEM ads, you can create SubIDs containing keywords and key phrases to determine which keywords get the most clicks and lead to the largest number of conversions.

These are just a few examples of ways you can use SubIDs. The actual scope of the tool is much broader. You can create your own SubID system to suit your needs and interests.
