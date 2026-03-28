---
title: Setting up auto-verification via postback
section: technical-integration
source: https://support.mitgo.com/knowledge-base/article/setting-up-auto-verification-via-postback_2
---

# Setting up auto-verification via postback

> Read about the verification and its types in [this article](https://support.admitad.com/hc/en-us/articles/4405920549905).

Auto\-verification via postback is similar to [auto\-verification via XML](https://support.admitad.com/hc/en-us/articles/4405926808081). However, in this case, the advertiser’s server itself sends the request with the data about the processed actions to the Admitad server. Such a method is considered more secure and thus is popular among financial programs.

Auto\-verification via postback allows updating the Admitad statistics more promptly because the data is sent at the moment of changing the action status or every 2–3 hours (depending on the auto\-verification settings) rather than once per day as in case of the verification via XML.

Only pending orders can be verified.

> Confirming an order means you’re ready to pay a reward to the publisher for the order. After you confirm the order, the publisher can withdraw the reward from the system, so we strongly recommend that you check everything you need to check before confirming.

Verification can be done in two ways:

- [by request signature](#verification-by-request-signature).
- [by key and IP address](#postback-request-example).

## Verification by request signature

This method is convenient for those who don’t need to specify an IP address and is suitable if you use a dynamic IP range.

To sign verification requests, use the HMAC\-SHA1 algorithm for campaign\_code and order\_id (your program and order IDs written as a single string without spaces or special characters between the two values). All strings should be in UTF\-8\. An example in Python 3\.7/2\.7 (IPython):

```
In [16]: import hmac

In [17]: import hashlib

In [18]: campaign_code = u'campaign_code'.encode('utf-8')

In [19]: order_id = u'my_order_id_here'.encode('utf-8')

In [20]: revision_secret_key = u'0123456789acbdef'.encode('utf-8')

In [22]: revision_sign = hmac.new(revision_secret_key, campaign_code + order_id, hashlib.sha1).hexdigest()

In [23]: print(revision_sign)

'01ae14a1c4ef90e6ce48c65525833e3f8a1f0228'

In [24]:

```

 

### Required parameters

Employees of the tracking department will give you the values for campaign\_code and revision\_secret\_key during the auto\-verification setup process.

- campaign\_code — the code of an affiliate program (a string value, 10 symbols);
- revision\_secret\_key — a secret key for verification via requests (a string value, 40 symbols);
- revision\_sign — an output signature (see example above);
- order\_id — an order number (a string value, 1\-100 symbols).
- status — the order status may have the following values:
	- pending
	- approved
	- declined
- amount — amount of the order (a decimal number with a period as a decimal separator);
- reward — reward of a publisher (a decimal number with a period as a decimal separator);
- currency\_code *(optional)* — the currency (3\-letter code) for values in the "amount" (order amount) and "reward" (publisher's reward) parameters;

- if you don't pass currency\_code, the currency specified in the affiliate program will be used for currency\_code by default;
- If you pass currency\_code and the currency in it differs from the affiliate program currency, the amounts in the "amount" and "reward" parameters will be converted to the program currency using the exchange rate in the system at the moment when the target action was recorded.

- comment — the reason for declining an order (a string value, 0\-30 characters).

### Example of a postback request

```
https://ad.admitad.com/rp?campaign_code=8f803552ea&
revision_sign=01ae14a1c4ef90e6ce48c65525833e3f8a1f0228&order_id=&status=&comment=
```

 

## Verification by key and IP address

### Required parameters

Employees of the tracking department will give you the values for campaign\_code and revision\_key during the auto\-verification setup process. Give them the IP address(es) from which requests will come.

- campaign\_code — the code of an affiliate program (a string value, 10 symbols);
- revision\_key — a secret key for verification via requests (a string value, 32 symbols);
- order\_id — an order number (a string value, 1\-100 symbols).
- status — the order status may have the following values:
	- pending
	- approved
	- declined
- amount — amount of the order (a decimal number with a period as a decimal separator);
- reward — reward of a publisher (a decimal number with a period as a decimal separator);
- comment — the reason for declining an order (a string value, 0\-30 characters).

### Example of a postback request

```
https://ad.admitad.com/rp?campaign_code=8f803552ea&
revision_key=3b9e06d28835AA872AE9cb6fc1186d1E&order_id=&status=&comment=
```

 

### Testing

After the setup is finished, specialists of the Admitad tracking department carry out testing. They make two test orders. You should approve one of them and change the order amount, and decline the second one and add a comment. If the data is correct (the order statuses are correct, the order amount has changed, and a comment exists), testing is considered successful, and auto\-verification is activated.

 

## Error notification

After a request is sent, a JSON message with the results of the validation of the request is sent in reply:

- If it was successful: {"success":true}, "message": "request is processing." This means the request has passed preliminary validation but could still be declined in the course of internal checks.
- If it was declined: {"errors":\["length revision\_key must be no more than 32"],"success":false}, with the reasons the order was declined given in “errors.”

If possible, set up a notification for yourself for responses containing {“errors”} with the logging of these responses. If errors start appearing, tell your manager at Admitad.
