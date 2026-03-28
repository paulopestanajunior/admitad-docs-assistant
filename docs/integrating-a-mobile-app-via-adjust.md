---
title: Integrating a mobile app via Adjust
section: technical-integration
source: https://support.mitgo.com/knowledge-base/article/integrating-a-mobile-app-via-adjust_1
---

# Integrating a mobile app via Adjust

To be integrated with Admitad, your app must be integrated with the Adjust SDK. [Learn more](https://help.adjust.com/en)

If you have a mobile app, your manager will suggest that you activate mobile tracking for your affiliate program when you join the Admitad Partner Network.

Integrating a mobile app with Admitad includes three key steps:

1. [Integrating the app with Adjust](https://support.mitgo.com/hc/en-us/articles/14491449747729-%D0%98%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-Adjust#h_01HYG7CNYK2G8SYQTCCT9NX5YJ)
2. [Setting up integration on Admitad's end](https://support.mitgo.com/hc/en-us/articles/14491449747729-%D0%98%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-Adjust#h_01HYG7CNYKRRJR81A5Q76K3PYS)
3. [Setting up integration with Admitad on the mobile platform](https://support.mitgo.com/hc/en-us/articles/14491449747729-%D0%98%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-Adjust#h_01HYG7CNYKH1YR134F1KTAA0BE)

## Step 1\. Integrating the app with Adjust

- [Integrate your app with Adjust](#integration-adjust)
- [Set up sending target events](#target-events)

### Integrate your app with Adjust


If you haven't integrated with AppMetrica yet, follow the instructions on the official website: [Integration with Adjust](https://help.adjust.com/en/article/integrate-adjust-sdk)

### Set up sending target events from your app to the mobile tracker


The events in the app allow you to evaluate user engagement based on their behavior. Such events may include clicks on links, downloads, impressions, purchases, etc. Mobile tracking services help set up the events that the app will track.

[Learn more about setting up events in Adjust](https://help.adjust.com/en/article/add-events)

## Step 2\. Setting up integration on Admitad's end


The process of setting up integration in your Admitad account includes the following steps:

- [Select the type of tracking in your Admitad account](#tracking-type)
- [Set up the target action in your Admitad account](#target-action)

### Select the tracking type in the program


In your Admitad account, choose the action tracking type:

- Browser
- Mobile app
- Browser and mobile app
1. Go to your Admitad account → Profile.
2. Select General settings.
3. Proceed to Tracking and transition settings.
4. In the Type of mobile tracking field, select Adjust.
5. In the Tracking action from field, select the tracking type from the dropdown list.


If you chose Browser and mobile application, copy the link from the Tracking link for the website field and paste it into the Tracking link for the mobile app field. It will then be [replaced with another one](https://support.mitgo.com/hc/en-us/articles/14491449747729-%D0%98%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-Adjust#h_01HYG7CNYMN9QCZ3QWWQ26S9KP).

### Set up the target action in your Admitad account


You can now create a mobile action with the necessary in\-app events:

1. In your Admitad account, go to Program \- Actions and rewards \- New.
2. Fill out the following fields:
- Name. A descriptive name of the action that the publisher will see. The action name should be concise and easy to understand because it's shown in All Programs and on the program page (e.g., Purchase, Paid order, Request, etc.).
- Channel. Leave this field empty.
- Action from. Select the mobile tracker through which integration is configured.
- InApp event. Select an option that seems most relevant to the target action.
- Hold period. The period during which the actions should be processed. The standard value is 30 days.
- Status. Select the status. If you want the action to take effect immediately, select Active. Otherwise, leave it inactive.
- Vendor action. Leave this field empty.
- System's fee. Leave this field empty.
- System fee as a percentage of the total amount. Leave this field empty.
- Commission. Set the type and amount of the reward.  
\- Fixed — publishers will receive a fixed amount, regardless of the order amount.  
\- Percentage — publishers will receive a percentage of the order amount.
3. Click Create.

## Step 3\. Setting up integration with Admitad on the mobile platform


The process of setting up integration in the tracker includes the following steps:

- [Add Admitad as a partner in the tracker](#admitad-partner)
- [Set up attribution](#attribution)
- [Set up postback](#postback)
- [Add a tracking link to Admitad](#tracking-link)
- [Test the integration](#test)

### Add Admitad as a partner in the tracker


You can find a detailed guide on how to add Admitad as a partner on Adjust's website: [Setting up Admitad as a partner](https://help.adjust.com/en/partner-setup/admitad)

### Set up attribution


Attribution allows you to distribute the value between traffic sources that generated a conversion. In other words, this is a way to track the user's path from the first click to the target action. The attribution settings will determine whether the publisher receives their reward based on user behavior and how the user interacts with traffic sources. Learn more about attribution methods and setup on the mobile tracker website:

[How to set up attribution in Adjust](https://help.adjust.com/en/article/attribution-settings-app-level)

### Set up postback requests

Postback is a tool that notifies the partner when the user completes a target action (e.g., installs an application through their ads). Usually, HTTP requests are used for notifications.

Adjust has some preset postback requests for Admitad. You just need to configure in\-app event mapping from the app by specifying the name of the target action to your Admitad account. For that, do the following:

1. In Adjust, go to Campaign Lab → Partners → Admitad → Data Sharing.
2. In the Map your events field, set the correlation between the in\-app event and the action name in Admitad.

### Add a tracking link to your Admitad account


To enable Admitad to track user activity in your app, provide us with a tracking link. You can set up and get this link in the selected mobile tracking service.


Please note that in some services, link configuration depends on how many platforms (Android, iOS) your app runs on. You can only set one link for a mobile app in Admitad, so use one link from the mobile tracker for both operating systems (Android and iOS).


To get a transition link, do the following:

1. Go to Campaign Lab → Partners → Admitad → Links → Link URLs.
2. Copy the link from the Click URL field.

### Test the integration


To check if the integration settings are correct, you might want to test everything before launching the advertising campaign. Learn more about testing methods for every service:

[How to carry out testing in Adjust](https://help.adjust.com/en/article/testing-console)
