---
title: How to fill out the general program settings in Admitad
category: admitad-advertisers
section: affiliate-program-settings
language: en
source: https://support.mitgo.com/knowledge-base/article/how-to-fill-out-the-general-program-settings-in-admitad_5
---

# How to fill out the general program settings in Admitad

To prepare your program for launch, you have to fill out the General settings section.


These settings determine the working principle of your program in the Admitad.

## Procedure for filling out the general program settings


The procedure of filling out the settings depends on the type of program management.

- Management via an account manager — in this case, contact your manager and they will add or edit information in your program.
- Independent management — in this case, you add information about the program on your own.


To add or change settings in the program on your own, go to the General settings section (Program → Program profile → General settings).


Below you will find tips on filling out all the fields in this section.


If you want a manager to set up your program, switch to Plus or Enterprise plan. [Learn more](https://support.admitad.com/hc/en-us/articles/10967590646545)

## Currency


In the Currency field, select the currency in which the publishers will receive their reward for [target actions](https://support.admitad.com/hc/en-us/articles/4403304880529#action-en) for your affiliate program.


The currency cannot be changed if the program is already launched.

## Product feeds


This is not mandatory to fill out.


If your project is an online store, then it is advisable to add one or several product feeds. This will make your program more attractive to publishers.


You can add a feed on your own or via your manager by giving him or her the product feed file. [More about product feeds and requirements to them](https://support.admitad.com/hc/en-us/articles/4405920538897)

- A product feed is a product catalog in XML, CSV, or Google Merchant format, containing information about the product.

	- Publishers use product feeds from the program to create services for product comparison, showcase websites, and email newsletters with descriptions and images of the product.
	- Product feeds also allow publishers to maintain up to date and correct information about products from your catalog on their ad spaces, and to update it in a timely fashion.

## Tracking link for a website


A tracking link is a link that leads to your website and includes all the necessary GET parameters of the Admitad, as well as your own UTM tags.

To generate a tracking link:  


1\. Check that the link to your website or app is correct.  
Link format: *www.yourshop.com/*


If the link is incorrect, delete it and enter the link to your website homepage into the field. The link should end with a "/" character.


2\. After "/" add the special parameter —?admitad\_uid\={{admitad\_uid}}.

Example: *www.yourshop.com/?admitad\_uid\={{admitad\_uid}}*

*This parameter is mandatory. Without it, tracking target actions will not work in the program.* 


If for any reason you cannot transmit `{{admitad_uid}}` in the admitad\_uid parameter, then you can transmit it in another parameter, for example utm\_content.

Example: www.yourshop.com/?utm\_content\={{admitad\_uid}}


Once the user follows the partner link, instead of the {{admitad\_uid}} variable, the [UID](https://support.admitad.com/hc/en-us/articles/4403304880529#admitad_uid-en) value of the specific publisher from which the user came will be inserted.


The link will look like this: *www.yourshop.com/?admitad\_uid\=sjdj383829echh3h39*


3\. Optional: you can also add additional tags to mark traffic into the link. These will help you obtain the necessary information about clicks.

Example 1: *www.yourshop.com/admitad\_uid\={{admitad\_uid}}\&utm\_source\=admitad*

Example 2: *www.yourshop.com/admitad\_uid\={{admitad\_uid}}\&utm\_source\=admitad\&utm\_medium\=cpa*

## Program regions


In the Program regions block, place checkmarks by regions:

- where you operate (have a store, deliveries),
- also for traffic from which you are willing to pay publishers.


The selected regions will be displayed on the program page in the Regions section. This information will enable publishers to understand whether their ad spaces are suitable for your program.

## Program category


In the Program category block, place checkmarks for 1, 2 or 3 categories that correspond to your company's area of activity.


In these categories, publishers will see your program in the [Admitad Store program catalog](https://account.admitad.com/en/catalog/).

## Main program category


In the Main program category block, place a checkmark by one category that most closely matches your company's focus.

## What to do after filling out the general program settings


After filling out all the fields and blocks, press Save changes.


It's ready. The general settings are filled out and saved.


Proceed to filling out and configuring other parameters of your program:

- [How to add a description for an affiliate program in Admitad](https://support.admitad.com/hc/en-us/articles/4405926792849)
- [How to add rules to a program in Admitad](https://support.admitad.com/hc/en-us/articles/4405920516113)
- [How to configure traffic types in the Admitad program](https://support.admitad.com/hc/en-us/articles/4405920514193)
