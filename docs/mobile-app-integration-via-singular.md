---
title: Mobile app integration via Singular
section: technical-integration
source: https://support.mitgo.com/knowledge-base/article/mobile-app-integration-via-singular_2
---

# Mobile app integration via Singular

If you’re not connected to the [Singular](https://www.singular.net/) tracking system, select another integration method. [Learn more](https://admitad.useresponse.com/knowledge-base/article/mobile-in-app-tracking_2#setting-up)

If you have a mobile app, your manager will suggest setting up mobile tracking for your affiliate program when you join Admitad.

To set up integration with Admitad, follow these steps:

- [Add Admitad to the Singular tracking system](#add-admitad)
- [Configure the settings in Singular](#make-settings)
- [Create a tracker URL](#tracker-id)

## Step 1\. Add Admitad to Singular

1\. Log into your [Singular account](https://app.singular.net/).

2\. In the lefthand menu, choose Attribution → Partner configuration.

3\. Click Add Partner and, in the opened field, type Admitad.

4\. In the opened window, fill out the following fields by selecting the following in the drop\-down list:

- App. Your app name.
- Site. Your website URL.

5\. Click Save and go to the next step.

## Step 2\. Configure the settings in Singular

1\. In the Partner Configuration section, click Admitad and, in the right corner, click .

2\. In the window that opens, specify the following information:

- In the Postback Key field, add the `postback_key` value. [How to get postback\_key](#get-postback_key)
- In the Click\-through attribution lookback window section, choose the period for how far back the tracker should look for a corresponding click that led to the installation.

3\. In the Install Postbacks section, choose the desired event. “Install” is set by default.

4\. In the Event Postbacks section, make sure that the value of the Event Name field corresponds to the respective value in the Actions section of your Admitad account (Program → Actions → InApp event column).

5\. Set up the postback URL if needed. If it’s not required, click Done and go to [the next step](#tracker-id).

You can:

- Change the event name in the `tracking` parameter if you’ve entered the identifier in the event name
- Add the `price` parameter if you need to send the purchase amount in the postback.

To do so, click  on the right of the Event Postback section and make the necessary changes.

After that, click Done and go to the next step.

- https://ad.admitad.com/r?pk\={{p\_k}}\&uid\={cl?Admitad}\&oid\={UTCM}\&tracking\=confirmed\_purchase\&device\={ANDI}\&client\_id\={AIFA}\&price\={AMOUNT}

## Step 3\. Create a tracker URL

1\. In the lefthand menu, choose Attribution → Manage Links and click “Admitad”.

If the section is empty, enable the Show Legacy Links switch in the top\-right corner.

2\. Fill out the following fields:

- Link Type — choose “Partner”
- Source Name — choose “Admitad”
- Tracking Link Name — add the “Admitad Tracking Link” name.

3\. Expand the Link Settings and Redirects section and enable the Android and/or iOS tracking option(s) according to the app to be integrated.

4\. In the If the app is not installed go to field below, add the link to the app on Google Play or the App Store. If you enable both options, add links to Google Play and the App Store in the respective fields.

5\. Scroll down and expand the Attribution settings section.

In this section:

- You can enable re\-engagement for existing users if you want to track all actions (1\). [Learn more](https://support.singular.net/hc/en-us/articles/360044494651-Re-engagement-FAQ)
- You need to set the cookie lifetime period in the Click\-through deterministic install subsection (2\).

6\. Scroll down and expand the Link Summary section.

Copy the URL from the Click\-through tracking link field and click Done.

> Tracker URL example  
> https://truemeds.sng.link/Dd108t/wvms?idfa\={{subid}}\&aifa\={{subid}}\&s\={{publisher\_id}}\&pshid\={{publisher\_id}}\&cl\={{admitad\_uid}}

7\. Send the tracker URL to an Admitad representative.

Done! You have set up the integration of your mobile app with Admitad via the Singular tracking system.

## FAQ

### Where do I find the postback\_key value?

- If you have a manager, contact them and ask them to provide you with the  `postback_key`  value.
- If you don’t have a manager, you can get the `postback_key` value in your personal account:

	- In the General settings section
	- In the Integration section.

- 1\. In your account, go to the  General settings  section (Program → General settings).

2\. In the  Tracking and transition settings  section, go to the  Tracking actions from  field and select  browser and mobile application.

3\. The  `postback_key` value will be displayed in the Token field.
- 4\. In your account, go to the Integration section (Program → Integration).

5\. Click Next and open the Custom integration tab on the Integration methods page.

6\. In Custom integration, choose Postback and click Next.

7\. Find the  `postback_key` value in the table at the top of the screen (the Integration setup: unique parameter values for your program section).
