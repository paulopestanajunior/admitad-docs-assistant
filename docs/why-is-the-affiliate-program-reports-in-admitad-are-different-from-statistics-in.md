---
title: Why is the affiliate program reports in Admitad are different from statistics in GA4?
section: faq
source: https://support.mitgo.com/knowledge-base/article/why-is-the-affiliate-program-reports-in-admitad-are-different-from-statistics-in-ga4_1
---

# Why is the affiliate program reports in Admitad are different from statistics in GA4?

If you use Google Analytics 4 (GA4\), you might have noticed that the statistics in GA4 are not exactly the same to the affiliate program reports in [Admitad](https://admitad.useresponse.com/knowledge-base/article/how-to-view-admitad-affiliate-program-reports_6-%D0%9A%D0%B0%D0%BA-%D0%BF%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D1%83-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81%D0%B2%D0%BE%D0%B5%D0%B9-%D0%BF%D0%B0%D1%80%D1%82%D0%BD%D0%B5%D1%80%D1%81%D0%BA%D0%BE%D0%B9-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D0%B2-Admitad). The reason lies in the fundamental attribution differences and other specifics:

1. By default, GA4 sets the data\-driven attribution model that doesn't rely on the last traffic source but determines every participant's contribution (as a percentage) to the final conversion. This is why data\-driven attribution isn't suitable for CPA networks, where other attribution models are used, including Last Click and Last Paid Click. You can choose the most optimal attribution model in settings. Read the [guide](https://support.google.com/analytics/answer/10597962#zippy=%2Cin-this-article) to learn how to do that.
2. GA4 automatically identifies the traffic source by the transition link and click referrer, unless utm\_source and utm\_medium are not specified in the URL parameters. Therefore, in case of a click on a free source's click, GA4's parameters Source and Medium may have unexpected values that attribute events to wrong sources.
3. GA4 treats organic traffic from Google search results as paid traffic, applying the Last Non\-Direct Click attribution model. This means that, if a user clicked the Admitad link and then visited the website again, but this time from search, GA4 will attribute this user's order to Organic, not to Admitad.
4. GA4 tracks returning users using a common cookie for all subdomains, though subdomains may belong to different advertising campaigns (e.g., if a free online store building platform is used). Thus, if a user visits a website with a URL like my.site.com, the cookie will be attributed to the .site.com domain. GA4 will identify the user who moved to another subdomain, another.site.com, as a returning user, but actually—and in terms of Admitad reports—this user is a new user.
5. Using cookies with GA4 is subject to certain restrictions that affect the accuracy of data collection. This happens because a cookie is associated with a certain device and browser: 1 cookie — 1 device — 1 browser. A user might block cookies or just delete them. In this case, a new cookie—with a new Client ID—will be created during the next visit, and GA4 will recognize the user as a new visitor. But actually—and in terms of Admitad reports—this user will be the same user.

With properly set parameter, the affiliate program reports in Admitad usually differ from GA4 statistics by 10\-20%. Such a share of discrepancy is considered healthy.

If the difference makes more 20%, you may try to reduce it. For that, in GA4:

1. Use the Last Click attribution model as a global setting for GA4 reports. This model is very similar to the attribution model adopted by Admitad. Read the [guide](https://support.google.com/analytics/answer/10597962?hl=en) to learn how to choose attribution settings in GA4\.
2. Add irrelevant traffic sources to exceptions. Mainly, irrelevant traffic sources are domains of external payment systems through which the user can make an online payment. Read the [guide](https://support.google.com/analytics/answer/10327750?hl=en) to learn how to add irrelevant traffic sources to exceptions.
3. In reports, select Attribution → Source to correctly identify the last paid source from which the transaction was led.
