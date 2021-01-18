# Day 1
## What you will be learning today:



- What is Coding? Why Python?
- Variables and simple data types
- Operators
- Strings
- Introduction to Lists
- Dictionaries
- Tuples
- Sets
- **If** statements 
- loops: **while** and **for**



## What is Coding?


Computer coding is the use of computer **programming** **languages**  to give computers and machines as **set** **of** **instructions** on what actions to perform. It’s how humans communicate with machines.
  
Allows us to create computer software like programs, operating systems, and mobile apps.

Without coding, computers would literally do nothing. They would be completely useless. That’s because source code is the set of instructions that tells the computer what to do. Computers have no free will, after all, so without explicit instruction, they’re just sophisticated hunks of metal.

Think of anything you’ve ever done with a computer:

- Play a video game.
- Send an email.
- Search for something on Google.
- Write a word document.
- Take a selfie on your smartphone (also a computer).
- Buy something on Amazon.
- Watch a movie on Netflix.

All of those applications are software written in code.



## Why Python?

1. Incredibly efficient language

2. "Clean code"

3. EASY to read, debug, build up and extend
 

following is the the Python code that literally tells the computer to print 'I am awesome':

```python linenums="1"
print("I am awesome")
```

when in Java it is

```java linenums="1"
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("I am awesome");
    }
}
```

And in C++ it is:

``` c++ linenums="1"
#include <iostream>

int main() {
  std::cout << "I'am awesome.\n";
}
```  

## Variables

Variables are often described as boxes you can store values in.
This idea can be helpful the first few times you use a variable, but it’s much better to think of variables as labels that you can assign to values. 
You can also say that a variable references a certain value.

**Data type**  is an attribute of data which tells the compiler or interpreter how the programmer intends to use the data.
          
A variable can be assigned to different types of values. 



Some basic data types in Python are:

- **int** : integer data type. Stores numbers without decimal points 
- **float** : float data type. Stores decimal numbers with floating points
- **str** : sequences of character data. We will be going into further detail later.
- **boolean** : Objects of Boolean type may have one of two values, True or False


Composite data types in Python :
 We will be exploring these data types in detail

- **list** : A list is a collection of items in a particular order
- **dict**: A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key
- **tuple** : A tuple looks just like a list except you use parentheses instead of square
brackets. 
- **set** : Sets are used to store multiple items in a single variable
- **frozenset** :frozenset is same as set except its elements cannot be changed.



### Variable Assignment

Now let's see how to assign a variable the right way!

Rules for Variable Names: 

-  Variable names can contain only letters, numbers, and underscores.
They can start with a letter or an underscore, but not with a number.
For instance, you can call a variable message_1 but not 1_message.

The following special symbols also cannot be used in a variable name: 

    :'",<>/?|\!@#%^&*~-+


-  Spaces are not allowed in variable names, but underscores can be used
to separate words in variable names. For example, *greeting_message*
works, but *greeting message* will cause errors.

-	 Avoid using Python keywords and function names as variable names.  Keywords are words that Python has reserved for a particular programmatic purpose. Some examples of keywords are : **print**, **input**, **type**. 


- Variable names should be short but descriptive. For example, name is better than n, student_name is better than s_n, and name_length is better
than length_of_persons_name.

- Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.

**NOT ALLOWED: Will throw error**

   5five = 10 (Starting with a number)

   my var = 10 (Using spaces)

   my_var* = 10 (Using special symbols)


## Some in-built functions
**print()** : the print() function is an in-built function of Python which is used to print the specified message to the screen or other standard output device.

```python
print("Hello, World!")
```

let's assign a variable and print it!

```python
message = 2
print(message) # this prints the value stored in the variable message 

#you can print more than one variable at a time by:
second_message = 1
print(message, second_message) 
```
What if you want to know what data type is the variable?

**type()** : this in-built function is used to determine the data type of the variable
```python
print(type(message))
type(2) 
```
 
Suppose you don't know what value should be assigned to your variable and want to ask the user for the value. you can do this using **input()**

**input()** method reads a line from input, converts into a string and returns it.

```python
message = input()
print("You entered: " , message)

#Suppose you want to print a message to the user for asking the value
second_message = input("Please enter a number")
print(second_message)
```



## Converting data types

Data types can be converted from one form to another using in-built functions like int(), str(), float().
However, do note that **not** every conversion is possible!

Can you convert an int type to a string type? 

```python

#using the in-built function str()
num = 1
num= str(num)
print(num)
print(type(num))

```

How about converting str to int?

```python
letter = 'A'
letter = int(letter) 

letter1 = '3'
letter1 = int(letter1)
print(type(letter1))
```

## Operators 

**Arithmetic Operators:**

```python
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)
```

**Comparison Operators:**
```python
x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)

```

**Logical Operators :**
```python

x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

```

**Shorthand Assignment operators:** 

In normal mathematics expressions:

var = 0

var = var +1   would mean 0 = 1

But in python, the same expression has a different meaning .
It means that the value of var is incremented by one and then assigned back to var. 

Thus the expression would store the value of 1 in var. 

## Strings

A string is a series of characters. Anything inside quotes is considered
a string in Python, and you can use single or double quotes around your
strings :

- I told my friend, "Python is my favorite language!"'

- "The language 'Python' is named after Monty Python, not the snake."

- "One of Python's strengths is its diverse and supportive community."



### String indexing and slicing

Strings are a sequence, which means Python can use indexes to call parts of the sequence. 

**Indexing** - Retrieving one letter from the string

**Slicing** - Retrieving multiple letters (Sub-string) from the string

In Python, we use brackets [] after an object to call its index. We should also note that indexing starts at 0 for Python. Let's create a new object called s and then walk through a few examples of indexing.

Syntax for []: Starting Index (Inclusive), End Index (Exclusive), Step Size

```python

# Outputs the first letter. Remember: In Python, index starts from '0'
print(my_var[0])

# Outputs the first to fourth letter. Indexing works by INCLUDING left bound but EXCLUDING right bound
print(my_var[0:4])

# Outputs the first and third letter.
print(my_var[0:4:2])

# Reversing a string
print(my_var[::-1])
```
**Practice 1 :**

Print 'I Love Coding' from the string below
s = "3DC'20 - I Love Coding!"



### Strings are immutable
This means that once a string is created, the elements within it can not be changed or replaced. For example:
```python
s = "I love coding"

#try changing the first letter to x
s[0] = "x"
#What do you get?
```
### String Concatenation
Dictionary definition of concatenation: "the action of linking things together in a series, or the condition of being linked in such a way"

Layman term: Joining 2 or more strings together
```python
s
```
```python
#we can reassign the new string back to s
s = s + " concatenate me"
print(s)
```

How does the multiplication operator behave with strings ? 
```python
length = "z"
print(length *3)
```
          
**Practice 2:**

Suppose you had a person's name in a variable:

myName = "Kenny Carney"

However, you want the surname Carney first and then the first name of Kenny. Use slicing to print out Carney Kenny.

Remember: you can use the plus symbol and spaces to concatenate:  print(surname + " " + firstName)


**Advanced Practice : Palindromes**

Given a string, write a code to check if it is palindrome or not.
A string is said to be palindrome if the reverse of the string is the same as string.
For example, “radar” is a palindrome, but “radix” is not a palindrome.

## Introduction to Lists

A list is a collection of items in a particular order.

In Python, square brackets ([ ]) indicate a list, and individual elements in the list are separated by commas

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```
### Accessing Elements

Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired

- Python considers the first item in a list to be at position 0, not position 1.
        
```python
print(bicycles[0])
``` 

- To access elements from the back of a list, use a negative index.

An index of -1 would access the last element, -2 would access the second last element and so on. 
```python
a = [1, 1.0, 'python', True]
print( a[-1])
print( a[-2] )
```

### Lists are mutable
You do this by referencing the element of the list and assigning a new object to it. 
```python
a = [1, 1.0, 'python', True] 
a[2] = 'SUTD'
print(a)
```

### len() function

The length of a list is the number of elements that it contains. 

Use the ```len``` function to check its length. 
```python
a = [1, 1.0, 'python', True] 
print(len(a))
```
### Creating a list

An empty list has a length of zero. 

You can either use the ```list()``` function or ```[]``` to create an empty list. 
```python
a = list()
b = []
print(a, b)
print(len(a), len(b))
```

Using **range()**

range() function is used to produce numbers using a start, stop, step 

range(2,10,1) will produce numbers starting from 2, incrementing by 2, till it becomes 10. 

Note that it DOES NOT include 10 


As the ```range()``` function is not a list, you need to pass it to the ```list()``` function to create a list. 

```python
 ls = list( range(10))
 print(ls)
```

### **Methods** of Lists

The term **method** refers to a function that is attached to a data type. 

A list object has functions attached to it. 

These are called **methods**. You access methods using the dot operator.
 
Note: **All of the below functions are applied directly to the original list**

- append() : add elements to the back of a list.

```python
a = [1, 1.0, 'python', True] 
a.append( 'five')
print(a)
```
        
- pop() : Removes the last element from the list.
```python
# Remove the last element from the list
ls = [1,2,3,4,5,"This will be removed from the list"]
print(ls)
ls.pop() # Note that .pop() is applied directly to the list I.e. There is no need to do ls = ls.pop()
print(ls)
```

- reverse() : Reverses the order of all elements in the list.
```python
# Reverses the order of the list
ls.reverse()
print(ls)
```

### List Slicing

The **in** Keyword
```python
a = ['horse', 'cat', 'dog', 'chicken', 'rat','duck', 'pigeon']
print('cat' in a)
print('donkey' in a)
```

The "+", " * " and "=="  operators with lists 

Recall that the "+" operator behaves differently with two numbers compared to two strings. 

The "+"and " * "  operators behave differently with lists, compared to the numeric datatypes. 

- The "+" operator performs concatenation when both its operands are lists. 
```python
a = [1, 2, 3]
b = [7, 8, 9]
c = a + b
print(c)
```

- The " * " operator works with a list and an integer. 
```python
a = [1, 2, 3]
c = a*3
print(c)
```

- The " == " operator checks the equality of two lists. This includes the length and all the elements in the list
```python
a = [1, 2, 3]
b = [3, 1, 2]
c = [1, 2, 3]
print(a == b)
print(a == c)
```

### Copying a list

By writing ```b=a``` in the example below, we are not creating a copy of a list. 

Recall that the ```=``` operator is an assignment operator. 

What the code does below is **aliasing**. The same set of data that is referenced by variable ```a``` is also referenced by ```b```.

In other words, both variables ```a``` and ```b``` refer to the same set of information. 

```python
a = [1,2,3]
b = a
```


Hence, what would we see on the screen if we had the following code? 

```python
a = [1,2,3]
b = a
b[2] = 5
print(a)
print(b)
```

### The ```is``` operator 

The ```is``` operator checks if aliasing is happening. 
```python
a = [1,2,3]
b = a
print(a is b)
```

### A list slice creates a copy of a list. 

List slicing can be used to create a copy of a list 
```python
a = [1,2,3]
b = a[:]
print(a is b)
print(a == b)
```

**Practice 3**
```python
#1. What will the below code produce?

x = [0,1,2,3,4,5]
x == x[:3] + x[3:]
```

**Practice 4**

Given a list, write a code that swaps the list elements at indices index1 and index2.

It does not modify the original list, but returns a new list.

Important note : Do keep in mind that the indices given could be *negative* as well

I have started the code for you 
```python
      ls = [3, 6, 8, 2]
      index1 = int(input(" Enter index 1 value :"))
      index2 = int(input(" Enter index 2 value:")) 
```

## Dictionaries

We've been learning about sequences in Python but now we're going to switch gears and learn about mappings in Python. If you're familiar with other languages you can think of these Dictionaries as hash tables.

So what are mappings?

**Mappings** are a collection of objects that are stored by a key, unlike a sequence that stores objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.

A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.

### Constructing a dictionary
```python
# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}
```
### Accessing a value
```python
# Access a value by inputting its key
my_dict["key1"]

# Dictionaries, like lists, can hold different data types
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
```
### Dictionaries are **mutable**
```python
# The values can be reassigned
my_dict["key1"] = 456

# New values can be assigned
my_dict["key4"] = "New Value"

print(my_dict)
```
### Nested Dictionaries
```python
# Accessing nested dictionaries
d = {'k1': [1,2,{'k2':[["Hello!"]]}]}
d['k1'][2]['k2'][0][0]
```
**Practice 5:**

Retrieve 'Coding is fun unless you're doing it wrong'
```python
d = {'k1':[1,2,{'k2':['pls do not do this',{'have fun':[1,2,['Coding is fun unless you\'re doing it wrong', 1, 2]]}]}]}
```

## Tuples

In Python tuples are very similar to lists, however, unlike lists they are **immutable** meaning they can not be changed.

You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar. 

You'll have an intuition of how to use tuples based on what you've learned about lists. 


### Constructing Tuples

The construction of a tuples use `()` with elements separated by commas. For example:
```python
tup = ("This will not change", True)

print(tup)
```

### Immutability

It can't be stressed enough that tuples are immutable.
**No variable reassignment!**

To drive that point home:
```python
tup[0] = "This will not work

print(tup[0])
```

## Sets
Sets are an **unordered collection of *unique* elements**. We can construct them by using the set() function.

What's the purpose? One main reason is to **identify unique elements from a list**

```x = set()```

```x.add(1)```

```x```

Note the curly brackets. This does not indicate a dictionary! Although you can draw analogies as a set being a dictionary with only keys.

We know that a set has only unique entries. So what happens when we try to add something that is already in a set?

```x.add(1)```

```x # Notice how there is still only 1 element? ```

## Conditionals : if, else and elif

Programming often involves examining a set of conditions and deciding which action to take based on those conditions.

Python’s if statement allows you to examine the current state of a program and respond appropriately to that state.
```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title())

```
```python
car ='bmw'
car =='bmw'  # What is the difference between the two operators?
```

Checking for inequality :
```python
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
  print("Hold the anchovies!")
  ```

### If-else block

An if-else block is similar to a simple if statement, but the else statement allows you to define an action or set of actions that are executed when the conditional test fails.
```python
age = 17
if age >= 18:
  print("You are old enough to vote!")
  print("Have you registered to vote yet?")
else:
  print("Sorry, you are too young to vote.")
  print("Please register to vote as soon as you turn 18!")
```
!!! note "NOTE" 
         The else block is a catchall statement. It matches any condition that wasn’t matched by a specific if or elif test, and that can sometimes include invalid or even malicious data.

        If you have a specific final condition you are testing for, consider using a final elif block and omit the else block.

        As a result, you’ll gain extra confidence that your code will run only under the correct conditions.


## for Loop
A ```for``` loop acts as an iterator in Python; it goes through items that are in a *sequence* or any other iterable item. 

Objects that we've learned about that we can iterate over include strings, lists, tuples, and even built-in iterables for dictionaries, such as keys or values.

Here's the general format for a  ```for``` loop in Python:

```python
    for item in object:
        statements to do stuff
```

## while loop

A bit similar to for loop, but it keeps running until the condition is false

The main difference between for loop and while loop is 

- for loop is used in situations where you know the number of iterations to go through

- while loop is used in situations where you do not know the number of iterations to go through but you know what is the condition that it should stop
    
```python
# Only when the condition behind the while statement is True, then only  it will enter the loop
# So do remember to update the condition for you to exit the while loop.
# Unless you want it to run forever

index = 1
while index < 5:
  print('This statement is printed {} times'.format(index))
  index += 1
print(index)
```
**Practice 7:**
one of the important application of while loop is to validate input from user
prompt the user to input their gender and if its not M or F you will notify them that its wrong input and ask them to input again
              
              
## Some more hands-on to end!

1. Write a function to print the following pattern using for/ while loops : 
            *
            
            **
            
            ***
            
            ****
            
            *****
             
2. Factorial of a number n is represented by n! and is equal to 1 * 2 * 3 * .... * (n-1) * n

    5! = 5 * 4 * 3 * 2 * 1 = 120
    
    Write a program to calculate the factorial of a number given by the user
    
            
  
    




