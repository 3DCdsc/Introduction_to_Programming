# Day 1
## What you will be learning today:



*   What is Coding? Why Python?
*   Variables and simple data types
*   Operators
*   Strings
*   Introduction to Lists
*   Dictionaries
*   Tuples
*   Sets
*   **If** statements 
*  loops: **while** and **for**



## What is Coding?


> Computer coding is the use of computer **programming** **languages**  to give computers and machines as **set** **of** **instructions** on what actions to perform. It’s how humans communicate with machines.
  
> Allows us to create computer software like programs, operating systems, and mobile apps.


## Why Python?

> Incredibly efficient language

> "Clean code"

> EASY to read, debug, build up and extend

## Variables

Variables are often described as boxes you can store values in.
This idea can be helpful the first few times you use a variable, but it’s muchbetter to think of variables as labels that you can assign to values. 
You can also say that a variable references a certain value.

A variable can be assigned to different types of values. 

What are the basic data types?


> Some basic data types in Python are:

*   **int** : integer data type. Stores numbers without decimal points 
*   **float** : float data type. Stores decimal numbers with floating points
*   **str** : sequences of character data. We will be going into further detail later.
*   **boolean** : Objects of Boolean type may have one of two values, True or False


> Composite data types in Python :
We will be exploring these data types in detail

*   **list** : A list is a collection of items in a particular order
*   **dict**: A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key
*   **tuple** : A tuple looks just like a list except you use parentheses instead of square
brackets. 
*   **set** : Sets are used to store multiple items in a single variable
*   **frozenset** :frozenset is same as set except its elements cannot be changed.



### Variable Assignment

Now let's see how to assign a variable the right way!

Rules for Variable Names: 

•  Variable names can contain only letters, numbers, and underscores.
They can start with a letter or an underscore, but not with a number.
For instance, you can call a variable message_1 but not 1_message.

The following special symbols also cannot be used in a variable name: 

    :'",<>/?|\!@#%^&*~-+


•	 Spaces are not allowed in variable names, but underscores can be used
to separate words in variable names. For example, *greeting_message*
works, but *greeting message* will cause errors.

•	 Avoid using Python keywords and function names as variable names

!!! note "What are **keywords**? "
        They are words that Python has reserved for a particular programmatic purpose. Some examples of keywords are : **print**, **input**, **type**. 


•	 Variable names should be short but descriptive. For example, name is
better than n, student_name is better than s_n, and name_length is better
than length_of_persons_name.

•	 Be careful when using the lowercase letter l and the uppercase letter O
because they could be confused with the numbers 1 and 0.

!!! note "NOT ALLOWED: Will throw error"

         5five = 10 (Starting with a number)
         my var = 10 (Using spaces)
         my_var* = 10 (Using special symbols)


## Some in-built functions
* **print()** : the print() function is an in-built function of Python which is used to print the specified message to the screen or other standard output device.
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

* **type()** : this in-built function is used to determine the data type of the variable
    ```python
    print(type(message))
    type(2) 
     ```
* Suppose you don't know what value should be assigned to your variable and want to ask the user for the value. you can do this using **input()**

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

> Can you convert an int type to a string type? 
```python

#using the in-built function str()
num = 1
num= str(num)
print(num)
print(type(num))
```
> How about converting str to int?
```python
letter = 'A'
letter = int(letter) 

letter1 = '3'
letter1 = int(letter1)
print(type(letter1))
```



