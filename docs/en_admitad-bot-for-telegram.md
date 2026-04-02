---
title: Admitad Bot for Telegram
category: admitad-publishers
section: tools
language: en
source: https://support.mitgo.com/knowledge-base/article/admitad-bot-for-telegram_5
---

# Admitad Bot for Telegram

Admitad Bot is a Telegram bot that helps you get and check [affiliate links](https://support.admitad.com/hc/en-us/articles/4403304880529#affiliate-link-en) using your smartphone or any other device.  
  

## How to use the bot

1\. [Add the bot to Telegram and log in to your Admitad account](#how-start-work).

2\. [Pick an ad space](#choosing-ad-space).

For the selected ad space, Admitad Bot can:

- [Generate a deeplink](#generating-deeplinks)
- [Add a SubID to an affiliate link](https://support.mitgo.com/hc/en-us/articles/360019378578#command-generating-deeplink-with-subid)
- [Processing a post with embedded links](#process-post) (converting all links in the post to affiliate)
- [Create a deeplink for Hot Products](#generating-deeplinks-for-hot-products) (if you work with the AliExpress program)
- [Check previously created deeplinks](#testing-deeplinks)
- [Get a coupon and/or promo code](#get-coupons-promo-codes)
- [View reports on ad spaces and/or programs.](#get-statistics)

*Users with [guest accounts](https://support.admitad.com/hc/en-us/articles/360019106457) can access all the bot's features without restrictions.*

 

### Getting started with the bot

1\. Find Admitad Bot on Telegram:

- Follow the link <https://t.me/admitad_bot>
- Or enter "admitad affiliate bot" in Telegram's search bar and find it in the search results.

2\. Click Start at the bottom of the screen.

3\. Select language: EN, RU, UK, ES, or PT.  
You can change the language anytime.  
To do so, in the bottom\-left corner, click Menu → `/change_language` and select the language.

4\. The bot will tell you about its features and suggest logging in to your Admitad account. This is what you need to get started.  
Click Log in.

5\. You'll be redirected to the login page in your browser.  
Enter your Admitad account's email and password and log in to the system. Then return to Telegram.

Done! You can now start working with the bot.

 

### Selecting an ad space

Your next step is selecting an [ad space](https://support.admitad.com/hc/en-us/articles/360019245557):

- If you have only one space, the bot will choose it automatically.
- If you have several ad spaces, choose one from the list.

The bot will remember what ad space you chose and will suggest it next time by default.

You can change the ad space whenever you want.  
For that, in the bottom left\-hand corner, click Menu → /changewebsite and pick an ad space.

 

### Creating a deeplink

Admitad Bot can generate a [deeplink](https://support.admitad.com/hc/en-us/articles/360019283878) even if your ad space isn't connected to the affiliate program or if the program isn't in the [Admitad Store](https://store.admitad.com/en/catalog/) catalog.

In this case, the bot will find a similar program in Admitad Lite's database and send a deeplink. There are over 30,000 advertisers in Admitad Lite, and a publisher doesn't have to join them.

1\. Send the bot a link for which you want to get a deeplink.

2\. The bot will determine which program the link belongs to and generate a deeplink. In a reply, you'll receive a shortened affiliate link to post on your ad space immediately.

You can also send the bot several links in one message, separating them with spaces or by pressing Shift\+Enter, and get deeplinks for all of them at once.

Note. The bot won't create a deeplink and will send you a message saying, "No affiliate program for this link found on Admitad" in the following cases:

- Your ad space isn't connected to the program, and this program isn't found in Admitad Lite.
- JavaScript redirection was set up for the link you sent to the bot. In this case, the bot won't be able to use the additional link to visit the website.  
*Redirections are usually used if the URL has changed and the website owner wants to retain the audience.*

- 1\. We sent one link to the Shein website.

2\. They responded with a shortened affiliate link (deeplink) to the related Admitad program: https://fas.st/o0GDcE.

- 1\. We want to generate deeplinks for two programs—Booking and Nike—so we send two links at once.

*Note that Booking is found in Admitad, but we aren't connected to it. This is why the bot found a substitution in Admitad Lite.*

2\. They responded with shortened affiliate links to the Admitad and the Admitad Lite programs.

 

### Creating a deeplink with a SubID with a command

To generate a deeplink with a [SubID](https://support.admitad.com/hc/en-us/articles/360019285478), add the following details to your message, separating these with spaces:

- Link you want to add a SubID to
- Add the `/subid` command at the end
- Add SubID value or values: You can add up to 5 SubIDs to one link. The first value will be added as SubID, the second as SubID1, etc.

In a reply, you'll receive a deeplink with a SubID or SubIDs.

You can only add a SubID if there's only one link in the message. If you need to get a deeplink with a SubID for several links, split them into several messages, one link in each.

- 1\. We added the original link and two SubIDs ("blue" and "12") to the message.

2\. The bot sent us the following:

	- Original link
	- Name of the found affiliate program
	- Deeplink with SubIDs
	- List of SubIDs

 

### Processing a post: replacing links with affiliate ones

Admitad Bot allows you to:

- [Replace links in the post with deeplinks](#change-links-to-deeplinks)
- [Add SubIDs to all deeplinks in the post at once](#add-subid-to-post-links)

#### Specifics of processing links in posts

Admitad Bot can find and process the following links in posts:

- Direct and embedded links
- Shortened links like *bit.ly*
- Links from other affiliate networks

When processing shortened links and links from other affiliate networks, Admitad Bot will remove additional parameters from them. This may affect which page of the target website the user will be taken to after following the link. We recommend checking such links after processing to ensure they're valid.

Note. Admitad Bot will only replace links with deeplinks and add SubID to them if the post contains:

- Links to Admitad affiliate programs and your ad space are connected to such programs
- Links to programs that aren't in the [Admitad Store](https://store.admitad.com/en/catalog/) catalog but are in the Admitad Lite database.

 

#### Processing a post: replacing embedded links with deeplinks

1\. Send the bot a post with embedded links (just copy\-paste or forward it).

2\. In a reply, you'll receive a post in which links will be replaced with deeplinks.

3\. Publish the processed post on your ad space.

If the bot can't process any links, it'll send information about it in the next message.

- 1\. We sent the bot a post with an embedded link.

2\. In a reply, we received the following:

	- Post with a deeplink
	- Message from the bot containing the following:
	
		- Original links
		- Name of the found affiliate program
		- Deeplink

- 1\. We forwarded a post with embedded links to the bot.

2\. In a reply, we received the following:

	- Post with the embedded deeplink and the link that couldn't be converted to a deeplink
	- Message from the bot containing the following:
	
		- Original link that was converted to an affiliate link
		- Name of the found affiliate program
		- Deeplink
		- Link for which there's no Admitad program
		- The reason why the link couldn't be made an affiliate

 

#### Adding SubIDs to links in a post

You can also add [SubIDs](https://support.admitad.com/hc/en-us/articles/360019285478) to links in a post. Admitad Bot will replace standard links with deeplinks.

To add SubIDs, do the following, separating all details with spaces:

- Paste the text into the message, or forward it
- Add the `/subid` command at the end of the post
- Add SubID value or values: You can add up to 5 SubIDs to one link. The first value will be added as SubID, the second as SubID1, etc.

The SubIDs specified in the message will be added to all affiliate links in the post.

- 1\. We sent the following message to the bot:

*{Our post} /subid black*

, where */subid* is the corresponding command, and *black* is a SubID that will be added to each link in our post.

2\. In a reply, we received the following:

	- Post with an embedded deeplink to which SubID *black* was added
	- Message from the bot containing the following:
	
		- Original link
		- Name of the found affiliate program
		- Deeplink with the built\-in SubID
		- Used SubID

- 1\. We sent the following message to the bot:

*{Forwarded post} /subid may sale*

, where*/subid* is the corresponding command added to the comments to the forwarded post, and *may* and *sale* are SubIDs that will be added to each link in our post.

2\. In a reply, we received the following:

	- Post with embedded deeplinks, to each of which SubIDs *may* and *sale* will be added
	- Message from the bot containing the following:
	
		- Original links
		- Name of the found affiliate program
		- Deeplink with SubIDs
		- List of SubIDs

 

### Creating a deeplink for Hot Products

If you work with the AliExpress program and send the bot a link to a product that belongs to the [Hot Products category](https://support.admitad.com/hc/en-us/articles/360019124717), the bot will notify you about this and show a special reward rate for this product.

The deeplink will be generated in a unique way to give you this higher reward.

- 

Admitad Bot doesn't check if an AliExpress product is available for affiliate marketing. To check if a product is an affiliate, use [Link tester](https://support.admitad.com/hc/en-us/articles/360019308938#How-to-check-whether-the-link-is-affiliate) or Reward calculation on the AliExpress WW or AliExpress RU\&CIS page.

 

### Checking a generated deeplink

Apart from generating deeplinks, Admitad Bot can check already generated links.  
Just send a deeplink to the bot. If the link is valid, you'll see a green check mark next to it in a reply.

  
  

If it's not, you'll see a red cross.

  
You can also check shortened affiliate links, but only if they were shortened using Admitad tools (Shortlink, the extension, or this bot).

 

### How to get coupons and promo codes

Coupons and promo codes are special offers from advertisers (such as discounts, gifts, etc.) that help you motivate users to perform target actions.

To get a coupon or promo code:

1\. Choose the `/get_coupons` command. To do this, enter "/" in the message field, or click the Menu button on the left.

You can also add a request to find specific coupons and/or promo codes. For that, add a space after the `/get_coupons` command and add the necessary keywords: an affiliate program name, a coupon/promo code name.

2\. If you have active coupons or promo codes for the chosen ad space, the bot will send them as a list.

You'll get the following information on each coupon or promo code:

- program name
- coupon name
- promo code (if it's needed to use the offer)
- validity period
- shortened affiliate link
- More link: Click it to get further information about the coupon or promo code, such as its description, offer type, full link, etc.

If there are no available promo codes for your chosen ad space, or it's not yet connected to any program, the bot will let you know. Connect your ad space to the target program in your dashboard or change to another ad space using the `/change_website` command.

You can filter promo codes and coupons by type:

- Personal. Unique promo codes assigned to a specific publisher
- Exclusive. Coupons only intended for Admitad publishers
- Scheduled. Coupons that are not active yet

### Where to find reports

The bot allows you to view reports on your ad space or programs for the last 7 days.

To view reports:

1\. Choose the `/check_stats` command. To do this, enter "/" in the message field, or click the Menu button on the left.

2\. If there are data available in the reports for the chosen ad space, the bot will send them as a list:

- the name of the ad space and the period of reports shown
- number of views if you're using banners
- number of clicks on affiliate links on the ad space
- CTR
- eCPC
- eCPM
- CR \- conversion rate
- number of leads
- number of sales
- amount for confirmed actions
- amount for actions on hold
- amount for declined actions

If there's no last 7 days' data for the chosen ad space (or if it's not connected to any programs), you'll receive a notification saying, "No weekly report for ad space *ad\_space\_name*."

You can filter the reports you receive:

- by today's date by clicking Today's report
- by program by clicking Report on programs. The bot will send you the reports for those programs on which information is already available.
