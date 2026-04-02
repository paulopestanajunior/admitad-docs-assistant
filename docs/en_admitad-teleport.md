---
title: Admitad Teleport
category: admitad-publishers
section: tools
language: en
source: https://support.mitgo.com/knowledge-base/article/admitad-teleport_8
---

# Admitad Teleport

Admitad Teleport is a tool for Admitad publishers who own a website, browser, or browser extension. When Teleport is enabled, users will get to the advertiser’s website directly through your link: with no redirects to the affiliate network’s website. Down the road, more target actions will be tracked and captured.


You can find Admitad Teleport in the upper menu of your personal account in the Tools section.  
 

## Who can access Admitad Teleport?


Currently, you can use Admitad Teleport if:

- Your ad space is a cashback service, browser, browser extension, dropshipping store, affiliate store, coupon service, loyalty program, search engine, or mobile app.
- You lead users to an internal page from which they are redirected to the advertiser’s website.
- You have experience using Admitad API, or there is a technical specialist on the team.


If you own an ad space of any other type but can modify its code, [contact Admitad support](https://support.admitad.com/hc/en-us/articles/360020421978) or your manager to learn whether you’re eligible to use the tool.


Admitad Teleport doesn’t support [Third\-Party Advertisers programs](https://support.admitad.com/hc/en-us/articles/4403380734737) and links generated with [MoneyLink](https://support.admitad.com/hc/en-us/articles/360019326278).

## Admitad Teleport benefits

Admitad Teleport eliminates redirects to the affiliate network’s website and accidental blocks


The diagram reflects the standard model flow and Admitad Teleport’s flow. You can find the description under the diagram.

  
Usually, when a user clicks on an affiliate link in your ad space, the user travels across a few redirects: link → Admitad website → advertiser’s website.


Since the browser performs a redirect to the Admitad website in the background, the user doesn’t notice it. But this is when the link obtains special tags that allow target action data to be tracked.


In some cases, this data may be lost. For instance, when the browser/ad blocker/antivirus program blocks a redirect.


As a result, part of the redirects and target actions go under the radar, and the conversion rate declines.


When you enable Admitad Teleport, the user lands straight on the advertiser’s website—with no redirect to the affiliate network’s website. Concurrently, target actions are fully recorded. In the aftermath, you don’t lose the income that ad blockers may take away from you when Admitad Teleport is disabled.

Admitad Teleport helps boost conversions amidst GDPR, ePrivacy, and other personal data protection regulations


With GDPR and ePrivacy rules—and their analogs in other regions—having become law, the user has to give their consent to having their personal data processed on every website along the redirect journey, i.e., both on your website and the Admitad website.


This may lead to a situation where users don’t agree to disclose any data.


And since Admitad Teleport excludes any redirects to the affiliate network’s website, the user will only have to accept the processing of personal data on your website.


This will hugely contribute to your conversions when the age of strict privacy comes.  
  

## Using Teleport API


Subsection contents:

- [How Teleport API works](#how-api-works)
- [How to set up Teleport API](#setting-up-via-api)
- [How to test Teleport API](#api-testing)
- [Restrictions and possible errors](#api-limitations)

### How Teleport API works


The diagram below visualizes the logic behind the Teleport API operation. A description of all the steps is provided below the diagram.

  
1\. A user clicks on the product link that leads to the redirect page on your website. This is the moment when you send a server request to Admitad according to the [guide below](#setting-up-via-api).


2\. Admitad registers the click and returns a JSON array with a link to the product page on the advertiser’s website. The link will contain all the necessary parameters for tracking target actions.


3\. Extract the link from the array and route the user to it. They’ll be redirected to the advertiser’s website (and they’ll notice it).  
 

### How to set up Teleport API


1\. Decide on the Admitad affiliate links you want to transform.


Apart from ad.admitad.com, all Admitad’s tracking domains are supported, except for link shorteners (e.g., fas.st or ali.ski).

Example of a link: https://ad.admitad.com/g/1e8d114494b7e165239416525dc3e8/


2\. Replace the link part /g/ with /tptv2/.


For example, we’ll transform the above link: https://ad.admitad.com/tptv2/1e8d114494b7e165239416525dc3e8/


3\. Add the following parameters to the link:

| Parameter name | Parameter description |
| --- | --- |
| user\_agent(url\-encoded)*required* | It helps Admitad filter out bot traffic from your ad spaces (e.g., from search engine crawlers) and not display it in your reports.   Specifics   When sending a request to Teleport API: - From a browser or webview: In user\_agent, pass a standard dynamic view. Example: Mozilla/5\.0 (Windows NT 10\.0; Win64; x64\); AppleWebKit/537\.36 (KHTML, like Gecko); Chrome/94\.0\.4606\.85; YaBrowser/21\.11\.1\.932; Yowser/2\.5; Safari/537\.36\. - From a mobile app. In user\_agent, pass a [unique application identifier](#bundle-id), as well as additional parameters including OS name, OS version\*, and device\_model\*.\**If the application can define the marked parameters*.   [How to learn the unique application identifier](#bundle-id) |
| referer(url\-encoded)*required* | It assists in troubleshooting action tracking and resolving disputes with the advertiser.   Specifics   When sending a request to Teleport API: - From a browser or webview: Pass the domain of your website from which a user followed an affiliate link (e.g., *https://example.com*). - From a mobile app. Pass your website domain in the format *https://example.com*. |
| ip\_addr(url\-encoded)*required* | It’s needed to ensure that: - Rewards for programs where the rate depends on the user country are accrued to your account correctly. - You can work with the programs where the advertiser’s website’s final URL depends on the user country. - It’s easier to troubleshoot action tracking and help resolve disputes with the advertiser.   Since a request via Teleport API will come from your server, our system won’t be able to detect the user country.   Important: You have to pass the IPs of visitors who clicked on the link leading to the advertiser’s website. Don’t pass your server’s IP as the parameter value.   [What to do if you can’t pass ip\_addr](#no-ip-addr) |
| country\_code(two letters per ISO standard 3166\-1 alpha\-2\)*optional* | This parameter may be required by programs that only allow traffic from one or several certain countries.  You can detect a user’s country with services like MaxMind. |
| subid(string, up to 50 characters long, combination "%00" is not allowed)*optional* | Pass this parameter if you want to analyze the performance of a certain link or ad. You can pass up to five different SubIDs. [Learn more about SubID](https://developers.admitad.com/hc/en-us/articles/7930476170001-Deeplink-generator) |

- How to learn the identifier:

	- [Of an iOS app (Bundle ID).](#app-store)
	- [Of an Android app (package name).](#google-play)#### How to learn an iOS app identifier (Bundle ID or package ID)

For your apps


1\. Open [iTunes Connect](https://itunesconnect.apple.com/).


2\. Go to My Apps and select an app.


3\. When on the app page, go to More and click About this App.


4\. You will see the app identifier in the Bundle ID field.

  

For any apps


1\. Find an app on the [App Store](https://www.apple.com/app-store/) and open its page.


2\. From the page link, copy the numerical identifier specified between the "id" and the first "?".

> Example  
> Link: https://itunes.apple.com/en/app/app\-name/id123456789?l\=en\&mt\=12  
> Identifier: 123456789


3\. Paste the numerical identifier after the "\=" into this link:

*https://itunes.apple.com/lookup?id\=*


You will get a link of the following format: https://itunes.apple.com/lookup?id\=123456789  
Click on it.


4\. After you click on the link, the file "1\.txt" will be automatically downloaded to your PC.  
The identifier will be specified in bundleId.

> Example  
> "bundleId": "Example.App.en"

  

#### How to learn an Android app identifier (package name)

For your apps


1\. Open [Google Play](https://play.google.com/).


2\. Go to Google Play Console and select an app.


3\. The identifier is specified next to the app logo and name.  
Example: *com.example.bundle*.

  

For any apps


1\. On [Google Play](https://play.google.com/), find an app and go to its page.


2\. The app identifier is specified in the link after the "?id\=".

> Example  
> Link: https://play.google.com/store/apps/details?id\=com.example.bundle  
> Identifier: com.example.bundle

> Example of a link with all parameters:
> 
> *https://ad.admitad.com/tptv2/1e8d114494b7e165239416525dc3e8/?country\_code\=RU\&ip\_addr\=0\.0\.0\.0\&user\_agent\=Chrome\&referer\=https%3A%2F%2Fwww.google.com\&subid\=1\&subid1\=2\&subid2\=3\&subid3\=4\&subid4\=5*


4\. Instead of redirect, forward the GET request from your server to the Admitad server.


Teleport API only allows requests from your server; browser requests won’t pass moderation. Make a request with every user click. You can’t store requests in the cache.


5\. Admitad will return a JSON array with the link to the advertiser’s website.

`[  

"redirect_url"  

]`

> Example of a redirect\_url link:
> 
> *https://www.advertiser.com?admitad\_uid\=b8b3fba19a9d6788408610c627f5045e\&utm\_source\=admitad\&utm\_medium\=affiliate*


6\. Extract the link from the array and route the user to it.  
 

### How to test Teleport API


Place a test order to make sure target action tracking is working correctly. The action must appear in your reports.


In some programs, actions take up to 24 hours to appear in statistics.

### Restrictions and possible errors

1. [If you pass a broken affiliate link in the request, the response will contain a dummy URL.](#teleport-dummy)
2. [The error {"%Parameter name% is required"} is shown after a request to the affiliate program](#ip-addr-is-mandatory)
3. [Affiliate links of some programs are temporarily unsupported by Teleport API.](#teleport-limited-support)

1\. If you pass a broken affiliate link in the request, the response will contain a dummy URL


If:

- You or the advertiser decided to terminate cooperation and disconnected the ad space from the affiliate program
- The program was suspended
- The affiliate link contains an error,


the response will contain a [dummy](https://ad.admitad.com/dummy/) URL.


You’d better still redirect the user to the dummy page but track such redirects in the [Broken links](https://support.admitad.com/hc/en-us/articles/360019181197) section. If necessary, correct the affiliate link or redirect traffic to the programs to which your ad space is connected.  
 

2\. The error 
`{"%Parameter name% is required"}`

 is shown after a request to the affiliate program


If you see this error, make sure you added all the required parameters from [this table](#parameter-table), add the missing parameters, and repeat the request.

If you can’t pass ip\_addr in the request, use a series of redirects to the standard address (change /tptv2 back to /g/).


Teleport API will accept such links, and the traffic will pass through classic redirects.

3\. Affiliate links of some programs are temporarily unsupported by Teleport API


Some programs in the catalog are temporarily incompatible with Teleport API. The list of such programs is constantly changing.


We’re trying to make Teleport API available for all integrations, so the program may appear in and disappear from the list of programs with limited support. [How do I know that a program is temporarily incompatible with Admitad Teleport?](#programs-with-limited-support)


If you try to request these programs, the response will be a standard affiliate link ‘/tptv2/’ will automatically be replaced with ‘/g/’. Direct the user through the received link. Traffic for such programs will go through classic redirects, and actions will be tracked.

## User consent to passing online identifiers


If your website visitors are subject to GDRP/ePrivacy, Clause 9\.6 of the [Admitad Terms for Publishers](https://account.admitad.com/webmaster/terms_of_use/) prescribes that you must obtain their consent to passing online identifiers from the users when using Admitad Teleport. 

## Admitad Teleport FAQ

- [How do I find out if Teleport doesn’t support my program?](#programs-with-limited-support)
- [Does Teleport support Third\-Party Advertisers programs?](#third-party-advertisers)
- [Does Teleport transform links generated with MoneyLink?](#lite-and-moneylink)
- [Why do I see redirects for some programs even when using Teleport?](#redirects)
- [Will an extra request to Admitad affect my ad space’s performance and page loading speed on the user’s end?](#does-it-affect-my-adspace)
- [What if a user follows a link again (after saving it to Bookmarks or from browser history)?](#second-click)
- [Can there be any antispam issues with the AliExpress affiliate program?](#antispam)
- [Does using Teleport affect cookie lifetime?](#cookie-lifetime)

### How do I find out if Teleport doesn’t support my program?


1\. Copy the program’s affiliate link and replace /g/ with /tptv2/. [How to get an affiliate link](https://support.admitad.com/hc/en-us/articles/360019067357)


2\. Follow the link with /tptv2/ in your browser to see what loads. If the program is temporarily unsupported, the /tptv2/ parameter in the link will automatically be changed to /g/.

  
 

### Does Teleport support Third\-Party Advertisers programs?


No, it doesn’t.

### Does Teleport transform links generated with MoneyLink?


No, Admitad Teleport can’t transform such links.

### Why do I see redirects for some programs even when using Teleport?


In some programs, users can be redirected to their internal action tracking platform rather than to the advertiser’s website, after which another redirect will happen. In the future, we plan to set up tracking so that the user will be redirected straight to the ultimate advertiser address in any case.  
 

### Will an extra request to Admitad affect my ad space’s performance and page loading speed on the user’s end?


An extra request takes dozens of milliseconds, so Teleport’s operation doesn’t differ much from the regular handling of affiliate links. Our server is ready to bear a load similar to the one it experiences during clicks without using the tool.  
 

### What if a user follows a link again (after saving it to Bookmarks or from browser history)?


If the user follows a Teleport link saved in their browser to get to the advertiser’s website:

- The repeating click won’t be counted.
- Target actions will be attributed to you during the Postclick Cookie lifetime (you can find it on the program page).
- The Postclick Cookie lifetime will be calculated from the time of the original click.

### Can there be any antispam issues with the AliExpress affiliate program?


No, there won’t be any issues of this kind.  
 

### Does using Teleport affect cookie lifetime?


No. The period during which the user remains "associated" with the program after the original click on your link will be the same.
