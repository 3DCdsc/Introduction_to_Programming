# Day 3

## Overview

Those who are new to programming may find it trivial to understand small lines of code, yet find difficulty in wrapping their heads around how applications, web applications in particular, work in general.

This course was written to help the novice reader better understand, at least in abstract, how simple applications communicate and "work" over the internet. The intended outcome of this exercise is not for you to be able to understand the intricacies of transport layer protocols or how things work down to the wire, but to gain insight into the mental models of abstraction that allow us to understand the web.

## How does the web work?

The fundamental question that underpins internet connected applications. Although it seems rather mysterious, the novice reader might do well to **break the problem down**. Then, they might find that their methods of inquiry are more effective than they would think. Indeed, this question, and the problem, is rather tractable even for beginners.

We know that:

1. data must be passed around from one remote computer to another.
2. This data should be processed and results returned.

So following which, we can setup the problem by asking the following questions:

- How do we retrieve and send information?
- What tools do we use to exchange information?
- How do these programs communicate?
- How do humans accomplish the tasks above?

By answering any one of the questions above, we are able to get closer to a high-level understanding of how web applications works.

Spoiler alert: By the end of your inquiries, you will come to the realization that what the web pretty much boils down to, is an **exchange of information**. Choosing what to do with the information is entirely up to us and is written in code. First, we need to figure out how to move this information around.

## How do we move information?

Let's try to understand how information is being moved around and what we will need to make that exchange of information happen.

#### Push or pull

First, it's important for us to think about what _moving information_ means.

In general, we can think of moving information in terms of **pushing** and **pulling**.

**Pushing** is when we would like to send information.
**Pulling** is when we would like to receive information.

We can think of the act of _publishing an article_ as analogous to pushing information while _reading an article_ is like pulling information.

Similarly, when we **post** mail, we think: push. When we **get** mail, we think: pull.

While in both ways information is being transferred, the directionality helps us understand which side of the exchange is likely intending to do more processing on the information.

#### Request/Response

An important concept in programming is the idea of requests and responses. To initiate an exchange of information, first there must be some _request_ for information followed by a _response_ that finalizes the exchange.

Simply: **A request is a question and a response is an answer.**

The answer may have useful information or it may not. Some requests may not get an answer… in which case we say that the `requested resource is not found`.

It is also helpful to understand requests as capable of being both **push** and **pull**. Rather, the _requests_ that we think as analogous to questions, can be both _asking for information_ and also _sending information_. So they are not _questions_ in the sense that they always ask for information, but more like questions in the sense that they initiate an exchange of information from one person to another, in either direction.

```
** Pull **
Person A: How many books are in the library?
Person B: 23.
```

```
** Push **
Person A: I'd like to donate this book to the library.
Person B: Okay, we will accept it.
```

## What makes a request?

Not all requests look like this, but for the sake of simplicity, we will be looking at RESTful HTTP requests.

We can break down the parts of request as follows:

- **Type**
  The request type is just a way of categorizing requests according to function. It is helpful to know the request type because it will help us understand the purpose of the request.

  - GET - used when **pulling** information
  - POST - used when **pushing** information
  - PUT - **pushing**, but with the intent to update existing information
  - DELETE - **pushing**, but with the intent to delete existing information

  \
  You may notice that POST, GET, PUT, DELETE follow the CREATE, READ, UPDATE, DELETE (CRUD) paradigm.

- **URL**
  The URL is a string that contains information about the request. You can think of the URL as a house address on steroids. It is a way to locate the address of the receiver, transmit information about how to transport the data and even what to do with the request.

  - Scheme - HTTP/HTTPS is **how** the request is transported
  - Domain - `youtube.com` is the address of the recipient
  - Path - `/search` tells us the _unit number_ of the receiver
  - Query Parameters - `?query=dog+videos` data (we'll cover this later)

- **Payload**
  - The data we are sending across

## Responses

We note that responses are tied to a request. Meaning that while responses also carry information, they are not “push” requests; you do not _initiate_ a response the same way you initiate a request.

It is useful to think of it that once a request is sent, it “picks up” the response on its way back to the computer who initiated it.

Responses, like requests, also contain information.

- **Status Codes**
  They give us semantic information about a request. Whether a request succeeds, fails, whether there was an error, a request was malformed or even if the resource being requested for is not found. Assuming the server provides accurate status codes, we can use this in our code logic to decide whether or not to take a certain action, retry the request or abort the operation.

- **Payload**
  Like requests, responses can contain data being returned to the client who initiated the request. This must be so- when we make a `GET` request, don't we want to receive information in return?

## What is HTML/CSS?

According to [W3C](https://www.w3.org/standards/webdesign/htmlcss.html):

> HTML (the Hypertext Markup Language) and CSS (Cascading Style Sheets) are two of the core technologies for building Web pages. HTML provides the structure of the page, CSS the (visual and aural) layout, for a variety of devices. Along with graphics and scripting, HTML and CSS are the basis of building Web pages and Web Applications.

Simply put, HTML contains the instructions on how to structure a web page and CSS provides information on styling (eg. colour, width, height...).

## Putting it all together

Now that we understand request/responses, we can roughly see how a web browser works. A web browser, is like a graphical user interface (GUI) for making requests over the internet!

1. Browser makes a GET request for `https://www.youtube.com`
2. Youtube's servers return HTML, Javascript and CSS for the front page.
3. Browser loads the HTML, Javascript and CSS.
4. Voila, you see the frontpage.
