---
title: Parallel tracking
category: admitad-publishers
section: ad-spaces
language: en
source: https://support.mitgo.com/knowledge-base/article/parallel-tracking_6
---

# Parallel tracking

Parallel tracking is a type of tracking introduced by Google for Google Ads. Parallel tracking helps page load more quickly, which can reduce the number of lost visits. This, in turn, can lead to increased conversions, and improved ad performance.  
  
  
  

How it works

  
  

Parallel tracking is mandatory for Search, Shopping, Display, and Video campaigns. For Hotel campaigns, parallel tracking is optional.  
  

## The difference between current (sequential) and parallel tracking

Let’s take an ordinary ad, where the landing page URL is specified in the Final URL field, and the affiliate link plus the parameter *?ulp\={lpurl}* is pasted into the Tracking template field.

When sequential tracking is used, a user clicks on the ad and is sent

1\. First through the affiliate link to the Admitad page,

2\. Then redirected via the final URL to the advertiser’s site.

During the second step, when the user is redirected to the landing page, Admitad parameters and the advertiser’s parameters are added to the final URL. Using these parameters, Admitad is able to track the click, and the advertiser can specify that the click belongs to the publisher in their statistics.

  
  

With parallel tracking, the user is taken directly to the final URL while the tracking template is loaded in the background.

  
  

## The impact of parallel tracking on CPA tracking

If you leave the ad settings unchanged, when parallel tracking is enabled, the final URL will have neither Admitad’s nor the advertiser’s parameters.

To the advertiser, the traffic the ad generates will thus look like organic traffic.

Admitad, too, will be unable to track these clicks: though the affiliate link will be loaded in the background, it will be impossible to map it with the final URL, as the latter will not have Admitad’s parameters.  
  

## What do I need to do to avoid losing traffic?

Follow these steps to make sure clicks and actions continue to be tracked fully and correctly for your ads:

1\. Enable auto\-tagging in your Google Ads account.  
Read more about it in a Google article "[About auto\-tagging](https://support.google.com/google-ads/answer/3095550?hl=en)".

2\. When creating ads, use [Admitad's tool](https://support.admitad.com/hc/en-us/articles/360019150757) that will generate final URLs, tracking templates, and final URL suffixes for you to paste in your ad.  
We highly recommend using the tool not only when creating new ads, but also for updating the parameters of ones that are already running.
