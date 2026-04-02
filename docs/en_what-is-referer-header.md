---
title: What is Referer header
category: takeads
section: account-and-settings_2
language: en
source: https://support.mitgo.com/knowledge-base/article/what-is-referer-header_2
---

# What is Referer header

The 
`Referer` (a misspelling of Referrer) HTTP header is a request\-type header that identifies the address of the previous webpage linked to the current webpage or requested resource. [Read more](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)

We use your 
`Referer`


 to identify if our tracking links are located on your website. We may also share your 
`Referer`


 with our partners, such as affiliate networks and/or advertisers, upon your request.

No other information will be transferred to our partners. Read more about the 
`Referer`


 Policy in [Section 4\.3 of our Terms of Use](https://takeads.com/terms-of-use/)

Main features of the 
`Referer`

header:

- The 
`Referer`

 contains the absolute or partial address from which the user requested the resource.
- The 
`Referer`

 allows a server to identify referring pages users come from or where requested resources are used. You can use this data for analytics, logging, optimized caching, and more.
- When users click a link on any page, the 
`Referer`

 contains the address of the page that includes the link.
- The
`Referer`

 can contain an *origin*, *path*, *query string*, and may not contain URL fragments (i.e \#section) or username:password information.
- The request referrer policy defines the data that can be included in the 
`Referer`

header.


The usage of the header increases the risk of privacy and security breaches on the website. It’s important to handle it with care. [Read more](https://www.geeksforgeeks.org/http-headers-referer/)

## How it looks

Here, *https://example.com/page?q\=123* is the address of the previous webpage the user came from:

```

Referer: https://example.com/page?q=123

```

Takeads webpage example:

## How to set Referer to your website

You can set referrer policies inside HTML. For example, you can set the referrer policy for the entire document with the \<meta\> tag with the name of 
`referer`


:

```

<meta name="referrer" content="origin" />

```

There are many different types of `content`

 associated with the \<meta\> element. We are only interested in `origin`


. For example, a document at *https://example.com/page.html* will send the referrer *https://example.com/.* [Read more](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy#origin_2)

Also, you can specify the`referrerpolicy`

attribute for \<a\>, \<area\>, \<img\>, \<iframe\>, , \<link\> tags to set referrer policies for individual requests:

```

<a href="http://example.com" referrerpolicy="origin">…</a>

```

### Referer setup rules

Follow these rules to ensure tracking of your users’ actions:

- Do not set the`noreferrer`

link relation for \<a\>, \<area\>, \<link\> tags that contain our tracking links:

```

⛔ <a href="https://tatrck.com/.../" rel="noreferrer">…</a>

```

- Do not set the referrer policy for the entire document with the \<meta\> tag:

```

⛔ <meta name="referrer" content="no-referrer">

```

`Referer`
