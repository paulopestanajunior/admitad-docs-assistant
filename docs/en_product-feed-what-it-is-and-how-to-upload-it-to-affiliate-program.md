---
title: Product feed: what it is and how to upload it to affiliate program
category: admitad-advertisers
section: tools_1
language: en
source: https://support.mitgo.com/knowledge-base/article/product-feed-what-it-is-and-how-to-upload-it-to-affiliate-program_3
---

# Product feed: what it is and how to upload it to affiliate program

A product feed is a file containing information about the products in your website's catalog. Product feeds are only used in affiliate programs of the *Online stores* category.


Publishers use product feeds that you provide to create price comparison services, online stores, affiliate stores, and email newsletters with product descriptions and images.


With own or ready\-to\-use parsers and plugins, they render the information as they need it and upload it to their ad spaces—forming their own product catalogs.


In the Admitad system, feeds are updated every 6 hours.

## Benefits of product feeds


Product feeds:

- Help publishers timely update product info—e.g. price, availability, specs, etc.—on their platforms.
- Streamline routine and make the program more appealing.

## Creating and uploading product feeds


To upload a feed to the program, you need to do the following:

- Create a product feed file containing data you need.
- Share the product feed link with an Admitad employee.


It's Admitad's responsibility to upload and configure feeds.


If necessary, you can add several feeds to your programs: in different languages, with different product categories, for different price categories, or in different formats (YML, CSV, etc.). In this case, a dedicated file should be created for every feed.


The feed link will be specified in the Product feeds field in the program's General settings.

## Preparing a product feed file


Please follow these recommendations when preparing a product feed:

- Always specify links to product pages without UTM tags.  
After the feed is uploaded, Admitad parameters will be automatically added to product links. If the links already contain tags, this may lead to conflicts and/or compromise publishers' affiliate links.
- Upload images with the best possible resolution.  
This will make your products look more appealing on any device. Publishers will change image sizes if necessary.  
The minimum resolution is 250x250\.
- If possible, add all products from your catalog to the feed.  
The larger your feed, the more effective your ads.


Admitad supports the following product feed formats:

- Google Merchant
- CSV (Comma\-Separated Values)


Click on a format name to see extended requirements.

- To make sure a Google Merchant feed is successfully uploaded to Admitad Partner Network and processed correctly by the system, your file must meet the following requirements:

	- [Google Merchant standard requirements](#standart-gm-requirements)
	- [Admitad Partner Network's additional requirements](#admitad-gm-requirements)## Google Merchant standard requirements


You can find the standard requirements for such feeds in Google Merchant's [Product data specification](https://support.google.com/merchants/answer/7052112?hl=en).

## Admitad's Google Merchant requirements


After the Google Merchant file is created, you need to check and refine it to ensure conformity with the Admitad's requirements.

	- [Markup specifics](#common-yml-admitad-requirements)
	- [Required attributes](#required-gm-attributes)
	- [Additional attributes supported by Admitad](#additional-gm-attributes)
	- [Google Merchant file example](#gm-example)### Markup specifics


The following markup requirements should be met.

	- Product info must be contained in attributes \<item\> or \<entry\>. The handler calls the feed and gets product info from these tags.
	- If the attributes \<size\>, \<gender\>, or \<color\> are in the product feed, they should be passed in the tag \<param\> (see [Example](#gm-example)).
	- The attributes in the file could be specified without the prefix "g:". The file will be processed correctly anyway.### Required attributes


Make sure the Google Merchant file contains all the elements required by Admitad.

| Attribute | Description |
| --- | --- |
| \<title\> | Product name. |
| \<link\> | Product page URL. |
| \<g:id\> | Product ID. |
| \<g:image\_link\> | Product photo. |
| \<g:price\> | Product price with currency in ISO 4217 format (UAH, USD, KZT). |
| \<google\_product\_category\> | Product category ID.Example: \<product\_type\> |

  

### Additional attributes supported by Admitad


If necessary, you can add some extra attributes to provide publishers with more product details.


Admitad can only process the attributes below.

| Attribute | Description |
| --- | --- |
| \<g:availability\> | Availability. |
| \<g:description\> | Product description. |
| \<g:brand\> | Product brand. |
| \<param\> | Product parameters. |

  

### Google Merchant file example

```
<item>  

   <link>https://test.by/smartwatch/apple-watch-series-6-gps-40mm-red-red-sport-band-m00a3</link>  

   <title>Apple Watch Series 6 GPS, 40mm, Red, Red Sport Band</title>  

   <g:description>Storage: 32 GB, NFC: YES, Dimensions: 40 mm,  

   Series: Apple watch series 6 gps, Manufacturer: Apple, State: Used</g:description>  

   <g:price>939.00 BYN</g:price>  

   <g:brand>apple</g:brand>  

   <g:image_link>https://test.by/storage/models/M00A3GK-A/large/j/200916180030597210.jpg</g:image_link>  

   <g:id>M00A3</g:id>  

   <g:availability>in stock</g:availability>  

   <g:condition>used</g:condition>  

   <g:identifier_exists>yes</g:identifier_exists>  

   <param name="Memory">32 GB</param>  

   <param name="NFC">Yes</param>  

   <param name="Size">40 mm</param>  

   <param name="Series">Apple watch series 6 gps</param>  

   <param name="Vendor">Apple</param>  

   <param name="Condition">Used</param>  

 </item>
	
```
- To make sure a CSV feed is successfully uploaded to Admitad and processed correctly by the system, your file must:

	- [Meet Admitad requirements](#admitad-csv-requirements)
	- [Contain required parameters](#csv-required-parameters)
If necessary, you can add some [extra parameters](#csv-additional-parameters) to provide publishers with more product details.

  

## Admitad requirements


Make sure your CSV file meets the requirements below.

	- Only one of divider types can be used between data files in the CSV file:
		
			- comma ( , )
			- semicolon ( ; )
			- vertical line ( \| )
			- horizontal tabulation ( tab )
			- double dash ( \-\- )
The character you selected as a divider can't be used for other purposes.  
If you selected comma ( , ) as a divider, there should be no commas in the product description.

  

	- You should pass every product's info in a separate row.  
	With that, all the rows must have the same number of values (parameter).  
	This is why if one of the products doesn't have the parameter value, it should be specified as "". Example: *"vitamins","","adult".*
	- You don't have to use "" to specify parameters in the CSV file.
Parameter names of the feed you want to upload to Admitad can be any, since our specialists process the file and transfer it to the system manually.

  

## Required parameters


Make sure the CSV file contains all the elements required by Admitad.

Some parameter names can differ from those below.


For example, the product page URL can be passed in url, link, or url\_address.

| Parameters | Description |
| --- | --- |
| category\_name | Product category name. |
| offer\_id | Product ID. |
| url | Product page URL. |
| price | Product price. |
| currencyId | Currency ID in ISO 4217 format (USD, UAH, KZT) |

  

## Additional parameters supported by Admitad


If necessary, you can add some extra parameters to provide publishers with more product details.


Admitad can only process the extra parameters below.

Some parameter names can differ from those below.


For instance, a link to the product photo can be passed via the picture, photo, or image parameter.


Though parameters name, picture, and description are additional parameters for CSV feeds, it's recommended to add them to the feed. This will make your feed more appealing and boost your sales. Users are more encouraged to buy products having an image and description.

| Parameter | Description |
| --- | --- |
| name | Product name. |
| picture | Link to product image. |
| description | Product description. |
| oldprice | Product price excluding discounts and promotions. |
| vendor | Product vendor. |
| available | Availability. |

  

## CSV file example


Parameter names can be any, this is why the fields in the example may differ from the parameters specified in the tables below.

```
"id","title","description","google product category","product type","link","image  

  link","condition","availability","price","currencyId","sale price","sale price effective  

  date","gtin","brand","mpn","item group id","gender","age  

  group","color","size","shipping","shipping weight" // product feed field names  

        

  "129914","Sunshine Nutrition Vitamin C Energy Apple Chewable Tablets 14's x 24","Sunshine  

  Nutrition Vitamin C Energy Apple Chewable Tablets 14's x 24","0","Vitamin C",  

  "https://www.testtest.com/product/sunshine-nutrition-vitamin-c-energy-apple-chewable-tablets-14-s-x-24",  

  "https://test-cdn.testtest.com/archieved-images/media/catalog/product/v/i/vit-c-apple.jpg","new",  

  "in stock","216","AED","","2022-02-22T10:58:55+04:00/2022-02-24T10:58:55+04:00",  

  "","SUNSHINE","","","","adult","","","","" // product 1 info  

        

  "125711","Loreal Infaillible Primer Pore  

  Refining","Loreal Infaillible Primer Pore Refining","0","0",  

  "https://www.testtest.com/product/lor-infaillible-primer-pore-refining",  

  "https://test-cdn.testtest.com/archieved-images/media/catalog/product","new",  

  "in stock","65","AED","21","2022-02-22T10:58:55+04:00/2022-02-24T10:58:55+04:00",  

  "","LOREAL MAKEUP","","","","adult","","","","" // product 2 info
    
	
```
