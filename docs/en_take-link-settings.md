---
title: Take Link settings
category: takeads
section: take-link
language: en
source: https://support.mitgo.com/knowledge-base/article/take-link-settings_5
---

# Take Link settings

For the Website platform type, you can use the JS code, WP plugin, or API integration.


After deploying and testing the integration script on your website, you can configure your integration settings in the [Dashboard](https://account.takeads.com/dashboard) section. [Learn more](https://admitad.useresponse.com/knowledge-base/article/take-link-settings_5#settings-in-account)


There you can:

- Specify domains you want to exclude from affiliation.  
For example: you run an affiliate program with Amazon and don't want to replace your direct links with Takeads.
- Transform plain text links or brand names to clickable tracking links if there's an offer in the [Takeads catalog](https://account.takeads.com/merchants).
- Specify sections or elements of your website where you want Take Link to work.


If you integrated your platform via JavaScript code, you can also change the platform source code to configure your integration. [Learn more](https://admitad.useresponse.com/knowledge-base/article/take-link-settings_5#settings-in-code)

## Change Take Link settings


To configure Take Link:

1. Go to [Dashboard](https://account.takeads.com/dashboard), and in the Platforms section, find the platform you want to update.
2. In the Actions column, click Configure.
3. Select the JS settings tab.


There are 2 groups of settings:

Global

- Blacklist. This excludes domains whose links you don't want to convert to tracking links. [Learn more](#blacklist)
- Section Targeting. This enables/disables Take Link for specific areas on every page of your website. [Learn more](#section-targeting)

Miscellaneous

- Link Activator. This converts plain\-text links into clickable tracking links. [Learn more](#link-activator)
- Branding Words. This converts plain\-text brand names into tracking links. [Learn more](#branding-words)

### Blacklist


This setting allows you to exclude certain website domains from processing. When enabled, Take Link won't process blacklisted links found on your platform. These links won't get any tags to track actions and clicks, even if there’s a relevant offer in the [Takeads catalog](https://account.takeads.com/merchants).

How to use Blacklist:


1\. Toggle the switch to enable this option.


2\. Enter the website domain and click Add. Specify the domain in the format hostname.tld. For instance, *booking.com*.


3\. Click Save at the bottom of the page.

*By default, the Blacklist applies to links to domains of some social media, search engines, news and entertainment websites, and other resources directly promoting products and services.*

### Section Targeting

This setting allows you to define where on your website Take Link transforms direct links by specifying:

- Active areas. Take link will process such sections and elements, i.e., convert default links into tracking links there.
- Inactive areas. Take Link will ignore these areas, leaving all links unchanged.


If you don't use Section Targeting, the whole page where the JavaScript code is deployed will be set as active. All links with available ad offers will be converted into tracking links.

How to use Section Targeting:


1\. Toggle the switch to enable this option.


2\. Select the section targeting rule:

- Active in. Take Link will only process the specified area of the page on your website.  
If you set at least one active area, Take Link will convert default links into tracking links in this area only, ignoring all other sections and elements.


For example, you can enable Take Link only for the area containing the main content (highlighted in green):

- Inactive in. Take Link will ignore the specified area of the page on your website.  
If you set at least one inactive area, Take Link will ignore links in this area only and will be active in all other sections and elements of the website.


For example, you want to exclude the banner area (highlighted in red):


To combine active and inactive areas, set an inactive area within an active one. The reverse setup, an active area within an inactive one, won't work*.*


To ensure that Take Link functions properly, it's recommended to avoid using active and inactive areas at the same time. Usually, adding only the Inactive in rule is enough to prevent link processing in the specified areas of the page.


2\. Specify the parameters of the element for which you set the rule:

- Element types:
	- \<div\>
	- \<span\>
	- \<article\>
	- \<section\>
	- \<table\>
	- \<tr\>
	- \<td\>
	- \<p\>
- Element IDs:
	- id
	- class
- Specify the element name manually.


3\. Click Add.


4\. Click Save at the bottom of the page.

> Example
> 
> *With the settings shown in the screenshot below, Take Link will process content in all areas \<div id\="postmenu"\>.*

### Link Activator


 This setting allows Take Link to convert plain text links into clickable tracking links if there's a relevant offer in the [Takeads catalog](https://account.takeads.com/merchants).


To do this:


1\. Toggle the switch to enable this option.


2\. Click Save at the bottom of the page.

> Example  
> Before: *https://www.booking.com/hotel/in/the\-foothills.de.html*
> 
> After: https://www.booking.com/hotel/in/the\-foothills.de.html


Link Activator ignores links that:

- Contain domains you added to Blacklist.
- Are in the inactive area you specified in Section Targeting.

### Branding Words


This setting allows Take Link to recognize brand names in your content and convert them into tracking links. These links will be evenly distributed on your platform's webpage.

How to use Branding Words:


1\. Toggle the switch to enable this option.


2\. Optional. In the Blacklist words section, specify brand names (e.g., "Nike" or "nike") that Take Link should not convert into tracking links. Then, click Add.


3\. Optional. Set the maximum number of brand names on one page that Take Link will convert into tracking links


2\. Click Save at the bottom of the page.


A brand name will only be converted into a tracking link if there's a relevant offer in the [Takeads catalog](https://account.takeads.com/merchants). Otherwise, the brand name will just become clickable.


In the text below, Take Link automatically found two mentions of Xiaomi and converted them into tracking links.

### Configuring JavaScript code in the page source


You can configure the JavaScript code on your website using the following features:

- [Customized SubID in tracking links](#subid)
- [Highlighted tracking links](#affiliate-link-style)
- [Customized density of tracking links](#links-density)

#### Custom SubID in tracking links


A SubID is a tag that helps track actions and clicks for:

- [tracking links on a specific page](#page-subid)
- [specific tracking links](#link-subid)


After you add a SubID, you will receive information about actions and clicks through the link with this SubID in the [Reports](https://account.takeads.com/stats) section. 


SubIDs can only be added to tracking links, i.e., links processed by Take Link. SubIDs can't be added to default links for which Take Link didn't find an advertiser in the [Takeads catalog](https://account.takeads.com/merchants)

How to add SubIDs to all tracking links on a page


Define the variable ao\_subid within the HTML template of the page.


The variable's value:

- can be anything
- must be in string format.


Use the section or page name as the title to make performance analysis more convenient. For example, you can use the value main\_page for the homepage:

```
  var ao_subid = 'main_page';

```

If you don't define ao\_subid or if it's empty, a SubID won't be added to tracking links.

How to add SubID to specific tracking link 


Add the attribute data\-ao\_subid with any value you need to a tracking link. Example:

```
<a href="//aliexpress.ru/item/1005001612796759.html?" data-ao_subid="link_inside_review_block">Buy</a>

```
#### Highlight tracking links


You can highlight the links that Take Link processed and converted into tracking links. This setting is useful if laws in your country require publishers to mark tracking links, or if you want to inform users about advertising content on your website.


You can highlight tracking links using the following methods:

- [Set specific font options](#set-font) (e.g., change the typeface or its size, color, or appearance; add some special characters).
- [Add a logo to a brand name](#set-logo)


Visual indication is only available for tracking links, i.e., links processed by Take Link. For example, if a plain\-text link is made clickable (because Link Activator was enabled in Take Link settings) but wasn't converted into a tracking link because no ad offering was found for it, it will not be highlighted.

How to change typeface of tracking link


To do this, add a specific class for processed links to the code using the variable var ao\_marker\_classname.

Example:

```
  var ao_marker_classname = 'custom_class_for_affilated_links';

```

Tracking links processed by the code in the example will look like the one in the screenshot below. In this case, the code processed Realme, Poco, and Oppo links:


Be sure to define all the classes in your CSS file.

How to add brand logo to tracking link 


To add a brand logo to a tracking link, enable logos using var ao\_offer\_show\_logo \= true.


You can also customize how logos look. To do that, add a specific class using ao\_logo\_classname.

Example:

```
  var ao_offer_show_logo = true;  var ao_logo_classname = 'custom_сlass_for_logos';

```

Tracking links processed by the code shown in the example will have brand logos and will look like this:

#### Customize density of tracking links for Branding Words option


You can manage the number of tracking links on your platform webpage by specifying the number of letters after a keyword that must be skipped before the next keyword is converted into a tracking link.


To do this:


1\. In the HTML template of the page, before the convertlink.com/script/ code fragment, add the bw\_spacing\_in\_letters variable.


2\. Specify the value of the added variable as a number. This number shows how many letters after a keyword must be skipped before the next keyword is converted into a tracking link.

- The minimum value is 0\. The maximum value is 5000\.
- By default, the value in Take Link is 120\.


If you set the bw\_spacing\_in\_letters value to 0, Take Link will consequently convert every keyword or brand name it finds into a tracking link until it reaches the end of the page or the [Max brand names on page](#max-brand-names) limit.

Example:

```
    var bw_spacing_in_letters = 200;

```

According to the code above:

1. Take Link finds the first keyword or brand name on the page and converts it into a tracking link.
2. Take Link skips the next 200 letters in the text, even if it contains brand names or keywords.
3. Take Link finds and converts the next keyword into a tracking link.


This process continues until the end of the page or until the [Max brand names on page](#max-brand-names) limit is reached.
