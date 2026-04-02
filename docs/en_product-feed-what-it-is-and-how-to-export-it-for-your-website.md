---
title: Product feed: what it is and how to export it for your website
category: admitad-publishers
section: tools
language: en
source: https://support.mitgo.com/knowledge-base/article/product-feed-what-it-is-and-how-to-export-it-for-your-website_4
---

# Product feed: what it is and how to export it for your website

A product feed is a file containing information about the products displayed on the advertiser's website. This information is collected and organized with the help of special attributes and parameters that depend on the file format: XML, CSV, or Google Merchant.  
  

## Benefits of product feeds

You can use product feeds to:

- Upload to your website information about all the advertiser's products at a time.
- Timely update product info (price, availability, specs, etc.) on your website.
- Create price comparison services, online stores, affiliate stores, and email newsletters with product descriptions and images.

 

## How to use and manage product feeds

To use a product feed of the selected program, you need to do the following:

1\. [Export the feed](#how-export-feed) in the target format.

2\. Modify it (if necessary): rename columns, change data format, etc.

3\. Upload the product feed to your website using:

- A plugin
- A proprietary or ready\-to\-use parser.

 

## How to export a product feed

You can export a feed:

- [From your account](#export-from-personal-account)
- [From the affiliate program page](#export-from-catalog)

### Exporting a product feed from the personal account

1\. In your account, click Product Feeds → Original.

2\. In the form that opens, fill out the following fields:

- Ad space. Choose the ad space for which you are going to use the product feed.
- Advertiser. Choose the affiliate program associated with the products you are going to place on your website.  
The list contains the programs that have product feeds available for exporting.
- Feed. Choose a feed that you are going to export.  
If the program has several feeds, choose the most suitable one by name. The name contains the attribute that determines how products are added to the file: GEO, currency, product category.
- Export template. If you already have an export template for this program, choose it and jump to [Step 3](#step-3). The fields added to the template will be added automatically.  
If there is no template, you can create one following [this guide](#how-create-template).

By default, the exported file contains all the parameters added by the advertiser. If you select an export template, the product feed will only contain the parameters that you set in the template.  
Also, if you use a template, you won't need to customize the settings manually every time you download the feed.

- Currency. From the dropdown list, choose the currency in which product prices will be displayed in the feed and on your website.
- Catalog format. Choose the export format: XML, CSV, or Google Merchant.
- Discounted products only. Check this box if you want to only export the discounted products.
- Date and time of last import. Enter the date and time to only export the products that were modified and/or deleted after the specified date and time.  
*Example: If you specify February 10, 2023 12:00 PM, the feed will only contain the products modified after the specified date and time.*

3\. Click Generate.

A product feed link will appear in the Generated Link field.

4\. Copy this link and paste it to the URL bar of your browser. The feed file will be automatically downloaded to your computer.

Download time depends on the number of products in the feed. It may take a few minutes.

If downloading seems too long, you can download your feed with:

- [Postman](https://www.postman.com/downloads/)
- [S3 download manager](https://addons.mozilla.org/ru/firefox/addon/s3download-statusbar/) for Firefox
- [Free Liquid Studio Community Edition](https://www.liquid-technologies.com/liquid-community-edition)

 

### Exporting a product feed from the affiliate program page

1\. In the [Admitad Store](https://store.admitad.com/en/catalog/) catalog, find the programs that have product feeds. For that, choose Product Feed in the tools filter.

 

2\. Choose an appropriate program and go to its page. In the left\-side menu, choose Product Feeds.

 

3\. Fill out the following fields:

- For ad space. Choose the ad space where you are going to publish product info.
- For a feed. Choose the feed that you want to export.  
If the program has several feeds, choose the most suitable one by name. The name contains the attribute that determines how products are added to the file: GEO, currency, product category.

After that, the links to the CSV and XML files will be generated automatically.

4\. Copy the link and paste it to the URL bar of your browser. The feed file will be automatically downloaded to your computer.

Download time depends on the number of products in the feed. It may take a few minutes.

If downloading seems too long, you can download your feed with:

- [Postman](https://www.postman.com/downloads/)
- [S3 download manager](https://addons.mozilla.org/ru/firefox/addon/s3download-statusbar/) for Firefox
- [Free Liquid Studio Community Edition](https://www.liquid-technologies.com/liquid-community-edition)

 

## How to create a product feed export template

1\. Choose the following in your account:

- Product Feeds → Export templates → \>Add new template (upper\-right corner)

or
- Product Feeds → Original → Add new template (next to the Export template field)

2\. In the new form, fill out the following fields:

- Template name. Enter the template name.
- Advertiser. From the dropdown list, choose the advertiser for whose program you are creating a template.
- Feed. Choose the feed available for the program.
- Export format. Choose the suitable one: XML or CSV.  
*If you choose CSV*, *select the divider type in the corresponding field.*
- Encoding. Choose the encoding option.
- Currency. Choose the currency in which product prices will be displayed in the feed and on your website.
- Discounted products only. Check this box if you want to only export the discounted products.
- Format of updating date. Enter the date and time to only export the products that were modified and/or deleted after the specified date and time.  
*Example: If you specify February 10, 2023 12:00 PM, the feed will only contain the products modified after the specified date and time.*
- SubID. Specify the SubID that will be added to all affiliate links to the products in the feed.

3\. In the Available fields (1\) area, choose the parameters that will be uploaded to the feed with this template, and move them to the Selected fields (2\) using the arrows (3\).

Be sure to add the following parameters to the product feed:

- `categoryId`
- `currencyID`
- `name`
- `picture`
- `price`
- `url`

If necessary, you can rename the selected parameters (4\).

- The parameters are displayed in the alphabetical order.

| Parameter | Description |
| --- | --- |
| \<article\> | Item number. |
| \<adult\> | A product that is associated to sexual needs or exploits the interest in sex. |
| \<barcode\> | Barcode provided by the vendor. |
| \<categoryId\> | Product category identifier that helps automate product categorization on the website.The parameter value is an integer number, up to 18 characters long. A product can only belong to one category. |
| \<currencyId\> | Product currency identifier (RUB, USD, UAH, KZT). |
| \<delivery\> | Delivery availability. |
| \<description\> | Product description. |
| \<local\_delivery\_cost\> | Local delivery price. |
| \<model\> | Product model. |
| \<name\> | Product name. |
| \<oldprice\> | Previous product price (i.e., price before the discount or sale). This parameter is usually used to calculate a discount. Possible options: \<old\_price\>, \<price\_old\>. |
| \<param\> | Product specs: color, dimensions, composition, etc. |
| \<pickup\> | Reservation and pickup availability. |
| \<picture\> | Link to product image. |
| \<price\> | Product price. |
| \<sales\_notes\> | Additional product info: minimum order amount, minimum batch, advance payment, deals, discounts, and sales. |
| \<store\> | Availability at a retail store. |
| \<typePrefix\> | Product group or category. |
| \<url\> | Product page URL. |
| \<vendor\> | Product vendor. |
| \<vendorCode\> | Product code, vendor code. |

4\. Click Save template.  
Done! You have created an export template for the selected affiliate program.

After that, you can change or delete it in Export templates.

 

### How to manage export templates

In your account, go to Product Feeds → Export templates.

In Export templates you will see a table with your templates.

In the Tools column, click:

- — to get a link to the product feed exported with this template
- — to edit the selected template
- — to delete the template

 

## FAQ

### How often is information in product feeds updated?

Information in this section is updated on a daily basis.

To learn the time when the product feed was last updated, you can:

- Go to the affiliate program page, open the Product Feeds section and find the update date in the Updated by advertiser field (bottom\-right corner).
- In your account, go to Product Feeds → Original. In the Feed field, select the target feed. You will see the update date in the Updated field.

 

### What happens if a product is removed from the website?

Once products are added to or removed from the advertiser's website, they are added to or removed from the product feeds that you can export.

 

### Can I set up automatic exporting of a product feed?

You can set up automatic product feed exports via API. [Learn more](https://developers.admitad.com/hc/en-us/articles/7930565454353-Affiliate-programs#list-for-ad-space)
