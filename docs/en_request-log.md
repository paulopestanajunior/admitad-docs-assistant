---
title: Request log
category: admitad-advertisers
section: technical-integration
language: en
source: https://support.mitgo.com/knowledge-base/article/request-log_2
---

# Request log

This section contains logs of requests with information about the actions performed in your program. 


At the integration stage, here you can see if the test orders data was correctly passed from your side to the Admitad side, and after the program is launched, the section can be used to identify errors, if some of the orders did not get in the statistics or loaded with incorrect data.


For each request, the following information is specified:

- the time of sending a request,
- the text of a request itself,
- the text of an error.


A dash in the Result field means the request has been passed correctly.


Below is the description of errors that are caused by incorrect tracking settings and must be fixed.

| Error text | Error description | Solution |
| --- | --- | --- |
| UIDDoesNotExist | There is no *admitad\_uid* in the request, or it has an invalid value. | Check *admitad\_uid*, correct, or add its value to the request. |
| ActionCodeDoesNotExist | No *action\_code (ac)* in the request. | Add *action\_code* to the request. |
| ActionDoesNotExist | Invalid *action\_code*. | Correct the value in the request. |
| TariffDoesNotExist | In the request, there is no *tariff\_code* (also *"tc"*), or it has an invalid value. | Correct or add the parameter *tariff\_code*. |
| PaymentExistError | Action with this *order\_id (oid)* already exists in the system. | Check *order\_id*. |
| PixelTrackingNotAllowed | Pixel requests are not allowed.The error occurs in programs that are integrated via tracking code. | If the program was first integrated via tracking code, but then shifted to another type of integration, the error can be ignored.If the program is still integrated via tracking code, contact a specialist of the tracking department, he will correct the settings. |
| PostbackNotAllowed | The error is similar to the previous one but occurs in programs with integration via postback requests. | If the program was first integrated via postback requests, but then shifted to another type of integration, the error can be ignored.If the program is still integrated via postback requests, contact a specialist of the tracking department, he will correct the settings. |
| PostbackAuthorizationError | Postback request authentication failed.The error can be caused by an invalid value or the absence of *postback\_key*. Also, the system will return an error if you have a list of authorized IP addresses from which postback requests can be sent, and the address of this request does not belong to the list. | Check for the presence and correctness of *postback\_key*. |
| PaymentAlreadyCollected | A request with information about this action has already been received. The error can occur only for action type "sale" (payment\_type\=sale). | If the order is in the statistics and the data is correct, there is no need to fix anything. Otherwise, check the order amount, *position\_id,* and *position\_count*. |
| FingerprintError | The error is similar to the previous one, but is typical for action type "lead" (payment\_type\=lead). | Check the statistics. If the lead is there, the data is correct, then nothing needs to be changed. |


After the error is fixed, do not forget to run a test to make sure that all data is now passed correctly.


Below are the errors that are caused not by incorrect tracking, but by other reasons. You do not need to fix them.

| Error text | Error description |
| --- | --- |
| RateDoesNotExist | No rate.   The error occurs most often in programs where rates are set by regions. It indicates that the request came from a country for which the rate is not defined. |
| CookiesIsExpired | The cookies have expired. It is also indicated how long ago they have expired. For example, CookiesIsExpired: 102 days, 1:31:07\. |
| EarlyRegistrationError | The error is caused by a delay in the transmission of requests. Wait a few minutes and the data will load. |
| WebsiteDoesNotExist | The ad space is not found. |
| WebsiteAdvCampaignDoesNotExist | This publisher is not joined to your program. |


If you cannot localize the error or face other difficulties, contact a specialist of the tracking department.
