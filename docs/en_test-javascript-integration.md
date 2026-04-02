---
title: Test JavaScript integration
category: takeads
section: take-link
language: en
source: https://support.mitgo.com/knowledge-base/article/test-javascript-integration_5
---

# Test JavaScript integration

To make sure the JavaScript code is deployed correctly and that Take Link is processing links in your website's content, use one of the methods below:

- Find a hash code from the JavaScript code on the page ([guide](#find-script-on-page)).
- Make sure the links on your website's page have converted to affiliate links. Use Link Redirect Trace for it ([guide](#use-link-redirect-trace)).
- Enable debug mode. This method allows you to check whether Take Link's JavaScript code is operating correctly and shows its current settings and statistics ([guide](#enable-debug-mode)).

## Use the hash code to make sure Take Link's JavaScript code is correctly deployed on the website

1\. Go to the page of your platform where the JavaScript code is deployed.

2\. Open the page code. To do that, right\-click View page source.  
You'll see the tab with the source code.

3\. Find the code fragment "convertlink.com/script/" on the page.

To do that, open the Search on page menu by pressing Ctrl\+F (for Windows) or cmd\+F (for MacOS). In the search bar, type `convertlink.com/script/`.

  
  

- If the code fragment is found, it means Take Link's JavaScript code has been deployed.
- If the fragment is not found, make sure that you [deployed JavaScript code correctly](https://admitad.useresponse.com/knowledge-base/article/how-to-add-a-platform-on-takeads_5#copy-js-code) onto the platform.
	- If you still can't find the code fragment on the page, [contact support](https://support.admitad.com/hc/en-us/articles/5256537963153).

## Check Take Link's operation with Link Redirect Trace

1\. Install [Link Redirect Trace](https://chrome.google.com/webstore/detail/link-redirect-trace/nnpljppamoaalgkieeciijbcccohlpoh?hl=en) for Google Chrome.

2\. Add a link to a brand website like [Walmart](https://walmart.com/) or [Aliexpress](https://best.aliexpress.com/) to any page on your website where the JavaScript code is deployed.

3\. Go to your website in Google Chrome and follow the deployed link. On the page, open the extension and make sure you were redirected through *tatrck.com*.

- If Link Redirect Trace shows redirect via tatrck.com, it means the JavaScript code has been deployed and that Take Link is processing links in its content.
- If Link Redirect Trace doesn't show redirect via tatrck.com, make sure that you [deployed JavaScript code correctly](https://admitad.useresponse.com/knowledge-base/article/how-to-add-a-platform-on-takeads_5#copy-js-code) on the platform.
	- If you still can't find the code fragment on the page, [contact support](https://support.admitad.com/hc/en-us/articles/5256537963153).

[What should I do if the links don't turn into affiliate links even though the advertisers are in the catalog?](https://admitad.useresponse.com/knowledge-base/article/take-link-javascript-faq_5#why-my-links-dont-become-affiliate)  
  

## Use debug mode to check Take Link's operation

Debug mode is the interface that allows you to check how Take Link's working and get information about settings and statistics. [Learn more](#debug-other-options)

1\. In the HTML template, add the variable with the following value after the opening tag :

`var ao_ml_debug = true;`

  
  

2\. Go to the page of your platform where the JavaScript code is deployed.

3\. Press Ctrl\+Shift\+I (Windows) or cmd\+option\+I (macOS) to open Developer Tools. 

4\. Open the Console.

  
  

5\. In the Filter field, type TAKE LINK.

  
  

- If you see information without errors, it means the JavaScript code has been deployed and that Take Link is processing links in its content.
- If you see information or no general information, it means the JavaScript has been deployed incorrectly. Check the code, and if you still can't find the code fragment, [contact support](https://support.admitad.com/hc/en-us/articles/5256537963153).

### Other debug mode functions

After the request is completed, you'll also see the results of the script's operation. You'll see the following details:

- SubID added to affiliate links on this page (value of `var ao_subid`).
- Selected [script initialization method](https://admitad.useresponse.com/knowledge-base/article/take-link-javascript-faq_5#how-to-initialize-script-on-dynamic-websites).
- Visual settings of affiliate links:
	- Font change class of affiliate links.
	- Whether logos are enabled and class that defines their appearance.  
	[Learn more about highlighting affiliate networks](https://admitad.useresponse.com/knowledge-base/article/take-link-settings_5#affiliate-link-style)

- The numbers of:
	- Links that were turned into affiliate links after the script's operation.
	- Links whose domains are added to the [Blacklist](https://admitad.useresponse.com/knowledge-base/article/take-link-settings_5#blacklist).
	- Plain\-text links that [Link Activator](https://admitad.useresponse.com/knowledge-base/article/take-link-settings_5#link-activator) turned active.
	- Branded keywords that turned into affiliate links after being processed by [Branding Words](https://admitad.useresponse.com/knowledge-base/article/take-link-settings_5#branding-words).
	- Found branded keywords (brand names).

If you don't want to make the stats available to end users, delete the string with the variable you added in [Step 1](#debug-step-1):

`var ao_ml_debug = true;`
