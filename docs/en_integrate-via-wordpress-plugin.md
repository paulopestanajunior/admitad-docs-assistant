---
title: Integrate via WordPress plugin
category: takeads
section: take-link
language: en
source: https://support.mitgo.com/knowledge-base/article/integrate-via-wordpress-plugin_5
---

# Integrate via WordPress plugin

If your website is built on WordPress, you can easily install the Take Link integration script using the Take Link plugin for WordPress.

With the Take Link plugin, you don’t need to edit your website source code. The integration script is automatically implemented in the source code via the plugin.

To integrate your website using the Take Link plugin, do the following:

1\. Install and activate the Take Link plugin ([guide](https://support.admitad.com/hc/en-us/articles/11452082622993#install-plugin)).

2\. Add your website as a platform to Takeads and implement the integration script via the Take Link plugin ([guide](https://support.admitad.com/hc/en-us/articles/11452082622993#add-platform)).

3\. Ensure the integration script is deployed correctly and that Take Link is processing links in your website’s content ([guide](https://support.admitad.com/hc/en-us/articles/11452082622993#test-integration)).

After deploying and testing the integration script on your website, you can [configure your integration settings](https://admitad.useresponse.com/knowledge-base/article/take-link-settings_5).  
  

## Install the Take Link plugin

1\. Open your website’s admin panel. Go to Plugins and click Add New.

2\. In the search field, type Take Link and press Enter. The [Take Link plugin](https://wordpress.com/plugins/monetize-link) will appear on the page.

3\. Click Install Now.

4\. Once installation is finished, click Activate Plugin.

All done! The plugin is now installed. It will appear in the Plugins section among all other installed plugins.  
  

## Add a platform and install an integration script

[Log in](https://account.takeads.com/auth/sign-in) to your Takeads account and add a platform using [this instruction](https://admitad.useresponse.com/knowledge-base/article/how-to-add-a-platform-on-takeads_5).  
  

## Test integration

To verify that the integration script has been installed successfully and that Take Link is processing links in your website’s content, use the Link Redirect Trace extension.

1\. Install the [Link Redirect Trace](https://chrome.google.com/webstore/detail/link-redirect-trace/nnpljppamoaalgkieeciijbcccohlpoh?hl=en) extension for Google Chrome.

2\. Add a link to a brand website, like [Walmart](https://walmart.com/) or [AliExpress](https://best.aliexpress.com/), to any page on your website where the integration script is installed.

3\. Go to your website in Google Chrome and follow the deployed link. On the page, open the extension and make sure you were redirected through *tatrck.com*.

- If Link Redirect Trace shows redirect via tatrck.com, the integration script has been deployed, and Take Link is processing links in your website’s content.
- If Link Redirect Trace doesn’t show redirects via tatrck.com, go back to the [How to install an integration script](https://admitad.useresponse.com/knowledge-base/article/how-to-add-a-platform-on-takeads_5#copy-js-code) section and make sure you’ve completed all steps correctly.

All done! You have checked that the integration script has been installed correctly and that Take Link is processing links in your website’s content.  
Optionally, you can configure your integration using [these instructions](https://admitad.useresponse.com/knowledge-base/article/take-link-settings_5).
