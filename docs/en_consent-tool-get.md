---
title: Consent Tool (GET)
category: admitad-publishers
section: gdpr
language: en
source: https://support.mitgo.com/knowledge-base/article/consent-tool-get_5
---

# Consent Tool (GET)

According to the GDPR and [Admitad Privacy Policy](https://www.admitad.com/en/privacy/) (paragraph 2\.3\.2\), you are obliged to inform visitors of your website that your ad space uses cookies, including those placed by Admitad Partner Network, and obtain their consent.

In addition, we need you to pass the information on visitors’ choices to Admitad Partner Network, as only in case of consent Admitad Partner Network is allowed to track the users’ actions, and you can get the reward for them.

To facilitate this process for you, we have created a ready\-to\-use solution that works by appending a special parameter to affiliate links at your ad space.  
 

### How the tool works

1\. First of all, you need to have an already configured mechanism of collecting consent from visitors of your website. The most popular solution is a cookie consent banner, that informs visitors that your website uses cookies, describes the reasons and purposes of their use, and requests consent.

2\. Access to our tool is granted at request. If you want to use it, create a ticket for the Admitad Partner Network support team with the subject “GDPR Consent Tool (GET)”, and we will activate it for you.

3\. When the tool is activated, we will notify you about it in the ticket. After that, add the parameter “ct” to all your affiliate links. The value of this parameter will indicate the status of users’ consents:

| Parameter value | Meaning |
| --- | --- |
| 1 | a user gave cookie consent, Admitad Partner Network is allowed to track the user’s actions on advertisers’ websites. |
| 0 | a user declined the use of cookies, Admitad Partner Network checks if the user opted out at the [Admitad Privacy Policy](https://www.admitad.com/en/privacy#optout-widget) page. |

> Example
> 
> 
> https://ad.admitad.com/g/6agwoaxtyzc20f67753f69b07947bf/?ct\=1

Note:

- The parameter values are accepted only in case the tool is activated on the Admitad Partner Network side. If you have added the “ct” parameter to your links but have not sent the request for tool activation, the parameter will be ignored.
- If the tool is enabled, but you do not transmit the “ct” parameter to Admitad Partner Network or its value is not “0” or “1”, then the parameter will be ignored, too. The decision on tracking the user’s actions will be made based on whether the user opted out at the [Admitad Privacy Policy](https://www.admitad.com/en/privacy#optout-widget) page.
- The consent status in the parameter has a one\-time effect, i.e. applies only to this particular click. If later the user clicks an affiliate link again, you will need to pass the consent status anew.
- The parameter is valid only if the user's IP belongs to the EU. Otherwise, the parameter is ignored, and Admitad Partner Network continues to track the user's actions.

### The list of the EU countries

| Austria | Estonia | Italy | Portugal |
| --- | --- | --- | --- |
| Belgium | Finland | Latvia | Romania |
| Bulgaria | France | Lithuania | Slovakia |
| Croatia | Germany | Luxembourg | Slovenia |
| Cyprus | Greece | Malta | Spain |
| Czechia | Hungary | Netherlands | Sweden |
| Denmark | Ireland | Poland | United Kingdom |
