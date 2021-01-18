# Day 4

Now that we roughly understand how applications interact over the internet, we might also want to understand how these applications are able to run, on what hardware and also find out what _servers_ exactly are.

## What are servers?

Let me quickly dissipate any confusion as to what servers might/might not be. They are computers. Whenever someone uses the term _servers_ what they really mean is a computer is doing the work.

> then why call them servers?

The main difference between _servers_ and _computers_ is that the former is assumed to not have any graphical interface to interact with- it is just the computer hardware but without the screen. Of course, there are other nuances but we will not delve into that.

For now, just understand that servers are really also just computers. Both will take in the same code and punch out the same information.

## How do application backends work?

When we use the term **backend**, we refer to the computational logic that processes data. Conversely, **frontend** refers to the display of data to the end-user through HTML, CSS, and Javascript.

So to understand how application backends work, we might want to answer the following questions:

1. How do they parse requests?
2. Where does information get stored?
3. How do we retrieve this information?

Essentially what’s happening is that your app server “listens on a port for incoming activity. When it does receive a request, it takes the data and does some processing and returns the response.

A-ha! I used a new word here, _port_. What is a port? It might be helpful to think about USB-ports, shipping ports, and all sorts of ports to kind of grapple with what it is.

## Where does information get stored?

When we write code, sometimes we store data in variables.
`a = 1` In this case, the computer stores the relation of `a` holding the value of `1` in memory. When we end the program, or shut the computer down, the memory is cleared and we lose the information.

For applications like Facebook, Netflix, and many more, it is thus important to have some kind of **persistent** storage of information that will be able to keep our data safe, secure and available for use the next time we access the application.

We call these data stores **databases**.

Databases are collections of information that allow you to store, update, delete and manage data. When we write information to a database, this database is assumed to be sitting in some server, and the information we store in it is not stored in memory but actually written to disk.

Think about it like saving a file to your Desktop. The file is written to your hard disk so that on bootup, the data will still be available.

## Types of databases

There are many types of databases. The two common ways to delineate databases is: SQL and NoSQL. Specifically, **relational** and **non-relational** databases.

In a relational database, information is stored in tables, neatly structured in terms of rows and columns. Much like Excel spreadsheets, the data **relates** to each other through their attributes.

| id  |  Name   | Gender |
| --- | :-----: | -----: |
| 1   | Raphael |      M |
| 2   |  Alex   |      F |
| 3   |   Ben   |     NA |

In a non-relational database, information is stored in nestable, key-value pairs. Much like Python's dictionaries.

A document database looks very much like JSON. Instead of tables and rows, we have nested “dictionary”-like structures that allow us to query for data using key-values.

```
{
  users: [
    {
      id: 1,
      first_name: Ben,
      last_name: Bitdiddle,
      Gender: M
    },
    {
      id: 2,
      first_name: Alyssa P.,
      last_name: Hacker,
      Gender: F
    },
  ]
}
```

## What is deployment?

After writing a piece of software, your app is available locally on your computer. But what if you want it to be available over the internet?

Deployment is the process of putting your app on cloud servers, allowing your app to be accessed over the internet. Once deployed, your application is able to receive requests over the web!

Common cloud-providers are AWS, Microsoft Azure, Google Cloud Platform, Heroku, DigitalOcean, and more. All of them help you manage the hardware servers that will host your application so that you only have to worry about your code.
