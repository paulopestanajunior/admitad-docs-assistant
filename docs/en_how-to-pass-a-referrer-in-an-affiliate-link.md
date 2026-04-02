---
title: How to pass a referrer in an affiliate link
category: admitad-publishers
section: affiliate-links-and-creatives
language: en
source: https://support.mitgo.com/knowledge-base/article/how-to-pass-a-referrer-in-an-affiliate-link_4
---

# How to pass a referrer in an affiliate link

When a user clicks an affiliate link you published in your ad space, information about the page on which they clicked that link is passed in the HTTP request header.

This information is called a `"referrer."` It can be used for the following purposes:

- Diagnosing problems when tracking target actions.
- Resolving disputes with the advertiser.  
Advertisers want to know where your traffic comes from so they be sure you aren't violating the terms of the program. You can provide a `referrer` as evidence to resolve a dispute.

Unfortunately, a referrer is not always registered by default, which is why we recommend embedding it in your affiliate links manually.

## How to add a referrer to an affiliate link

1\. Get an encoded value for the URL of your ad space from which the user will follow the affiliate link.

You can use a link encoding service, such as [URLEncoder](https://www.urlencoder.io/).

Example:  
Ad space URL: *https://example.com*  
Encoded URL: *https%3A%2F%2Fexample.com*

  
2\. Add the `ref` parameter with the encoded ad space URL to the affiliate link.

*If the affiliate link contains a token of the format ?erid\=AbcdE1Fgh, add the `ref` parameter after the token and separate it with an \& symbol.*

Example of adding a referrer to an affiliate link without a token:

Affiliate link: *https://ad.admitad.com/g/\<goto\_code\>*

Final link with the `ref` parameter and encoded ad space URL:   
*https://ad.admitad.com/g/\<goto\_code\>/?ref\=https%3A%2F%2Fexample.com*

Example of adding a referrer to an affiliate link with a token: 

Affiliate link with a token: *https://ad.admitad.com/g/\<goto\_code\>/?erid\=AbcdE1Fgh*

Final link with the `ref` parameter and encoded ad space URL:   
*https://ad.admitad.com/g/\<goto\_code\>/?erid\=AbcdE1Fgh\&ref\=https%3A%2F%2Fexample.com*

Done! You have added a referrer to the affiliate link.

 

[Where can I get an affiliate link?](https://support.mitgo.com/hc/en-us/articles/360019067357)
