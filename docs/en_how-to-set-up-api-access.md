---
title: How to set up API access
category: takedeals
section: Getting+started.
language: en
source: https://support.mitgo.com/knowledge-base/article/how-to-set-up-api-access
---

# How to set up API access

This article explains how to set up API access to get tracking data and describes the API endpoints.


Before you begin, ensure your source is approved and its status is Active. You can check this in the My Sources section.


To set up API access for your source:


1\. Go to the My Sources section and copy the Source ID.


2\. Go to the API сonnection section and generate a token:


2\.1 Click Generate API access token.


2\.2 Enter token name and click Create.


2\.3 Copy the generated token and store it securely. It allows access to your data.


3\. Follow the API documentation and Swagger link. Swagger will open.


4\. Click Authorize, paste the API token you copied, and click Authorize.


After authorization, you can test endpoints.

## API endpoints overview


To edit an endpoint:

1. Click an endpoint to expand its details.
2. Click Try it out to enable editing.
3. Update endpoint parameters.
4. Click Execute to test the request.

### Endpoints description

/actions: Gets all your confirmed actions (conversions).


You can filter results by:

- from and to dates.
- status: approved, pending, declined.
- (optional) sub\_id, if you use subIDs in tracking links.

/merchants: Lists available merchants.


Requires your Source ID. You can filter results by:

- country: multiple values allowed, separated by commas.
- isLocalOnly: set to true to get merchants with location\-specific coupons.
- status: active or inactive merchants.

/coupons: Retrieves active coupons.


Requires your Source ID. Useful for retrieving available deals by merchant or country.

/resolve\-link: Generates tracking links.


Input a target URL (landing page). The system returns a tracking link that includes your source attribution.

/coupon\-categories: Lists coupon categories. Example: Fashion, Sport, Electronics.

/value\-categories: Gets categories of value types.


Helps users understand the value proposition of each offer. Example: Free shipping, Discount %. There are 5 predefined categories.
