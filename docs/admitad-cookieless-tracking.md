---
title: Admitad Cookieless Tracking
section: technical-integration
source: https://support.mitgo.com/knowledge-base/article/admitad-cookieless-tracking_2
---

# Admitad Cookieless Tracking

In order to track actions on advertisers’ websites and attribute them to the right publishers, Admitad normally sets a tracking cookie in users’ browsers.


However, the GDPR and ITP rules state that a cookie can be placed only if the user consents and users may prefer not to use cookies at all and opt out.


To comply with GDPR and ITP requirements and preserve tracking at the same time, Admitad has come up with a cookieless tracking solution.

## How does it work


1\. An affiliate link contains a GET parameter with the [*admitad\_uid*](https://support.admitad.com/hc/en-us/articles/4403304880529#admitad_uid-en) value.  
When a user clicks an affiliate link and comes to your site, you should collect and store this value.


2\. When the user converts, transmit the same *admitad\_uid* value together with the order data.


3\. Based on *admitad\_uid*, Admitad will assign the conversion to a publisher.

## How do I set up cookieless tracking


1\. Collect the *admitad\_uid* value sent in a special GET parameter. Store it using any method you like:

- Preserve *admitad\_uid* in a GET parameter across all pages, from the page a user arrives at after clicking the affiliate link right up to the conversion page.
- Store *admitad\_uid* in the database.
- Save *admitad\_uid* in session storage.
- Any other method that works for this purpose.


Note that the stored value must be updated, if a new *admitad\_uid* value is supplied.


2\. When a user performs an action, pass on the same *admitad\_uid* value to Admitad.

Query string example

```
https://ad.admitad.com/r?campaign_code=your_campaign_code&postback=1&postback_key=your_postback_key&uid=03b374fa9c2f34069e8df0bda61b8627&action_code=1&order_id=123456&tariff_code=1&currency_code=USD&price=20000&quantity=2&position_id=1&position_count=3&product_id=11&client_id=&payment_type=sale   

```

If you want to use a front\-end solution, contact your account manager. You’ll be provided with a custom solution.


3\. Make sure you’ve set up tracking correctly by carrying out [this test procedure](https://support.admitad.com/hc/en-us/articles/4405926814865-Integration-via-postback-request#how-to-test-postback-request).


4\. After that:

- If you have an account manager, confirm with them that the test went through successfully and that the conversion appeared in Admitad reports.  
If the test is failed, follow your manager's instructions.
- If you manage the affiliate program yourself, contact the tech support (support@admitad.com) to confirm that the test went through successfully and that the conversion appeared in Admitad reports.  
If the test is failed, try to go through the set\-up steps described in [the guide](#cookieless-tracking-setup) once again and return to the support team for confirmation.
