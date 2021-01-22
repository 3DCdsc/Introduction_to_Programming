# **Objected Oriented Programming**

## 1. Functions

### 1.1. _What are functions and why do we need them?_

Lets say that you are watching TV. Every time you want to change the channel, you will use the same remote control. It would be quite inconvenient if you had to make a new remote control each time you wanted to change the channel. Similarly, in programming, you might want to write a piece of code that you need to re-use multiple times in different parts of your program.

For example, lets say that you write a program to find the largest number in a list:
```py
list_of_numbers = [32, 88, 3, 48, 87, 22]
max = list_of_numbers[0]

for number in list_of_numbers:
    if max < number:
        max = number
print(max)
```

But what if you need to find the largest value in 10 different lists? Would it be feasable to rewrite the same code again 10 different times? This is where functions come into the picture. They allow you to re-use the same piece of code again and again, however many times you might want.

More formally, A function is a block of code that allows you to to perform a specific action. It is modular, and re-usable as many times as you want. Some functions might even give you back a value.

For example, the same code written using functions would look something like:

```py
# this line is known as the function prototype.
# the variables inside the brackets are known as formal parameters or formal arguments
def max_value(list_of_numbers):

# the word 'def' is short for define. It means you are defining a function called 'max_value'

# In programming, it is a convention to write function names in 'snake case'
# snake case means that the each word is in lower case, and separated by underscores.
# Example: this_is_snake_case

    max = list_of_numbers[0]

    for number in list_of_numbers:
        if max < number:
            max = number

    # the word 'return' here tells python that this function needs to give you back the value of 'max'
    return max
list1 = [32, 88, 3, 48, 87, 22]
list2 = [44, 26, 56, 90, 12, 35]
list3 = [96, 43, 30, 12, 37, 26]


# this is known as a function call and the variables passed to the function are called actual parameters or actual arguments
max1 = max_value(list1)
max2 = max_value(list2)
max3 = max_value(list3)

print(max1)
print(max2)
print(max3)
```

A function does not have to necessarily return a value:

```py
def display_elements(a_list):
    for element in a_list:
        print(element)

list1 = [32, 88, 3, 48, 87, 22]
list2 = [44, 26, 56, 90, 12, 35]
list3 = [96, 43, 30, 12, 37, 26]

print(display_elements(list1))
print(display_elements(list2))
print(display_elements(list3))
```
Output:
```py
32
88
3
48
87
22
None
44
26
56
90
12
35
None
96
43
30
12
37
26
None
```

Why does it print a `None` between the elements of the lists? Remember, these functions don't return any values! Thus, `print(displayElementsOf(list1))` doesn't actually have something to print!

Note: A function does not execute the rest of its code if a return statement is encountered

```py
def function(number):
    return number*2
    print(number/2)

print(function(5))
```
Output:
```
10
```


### 1.2. _Excersise: Write a function to calculate the factorial of a number_

The factorial of a number n, represented by n! is given by n\*(n-1)\*(n-2)\*...\*1. For example, 5! = 5\*4\*3\*2\*1 = 120

### 1.3. _Different types of arguments_

In python, there are 6 different types of arguments that a function can take. They are:

1.3.1. Required Arguments: are arguments that MUST ALWAYS be passed to the function.

```py
def add(a, b):
    # a and b are required arguments
    return a+b

print(add(3, 5))
# prints 8
```

1.3.2. Optional Arguments: are arguments that may not be passed to the function.

```py
def add(a, b, c = 0):
    # a and b are required arguments while c is an optional argument. All arguments initialised with a default value are optional
    return a+b+c

print(add(3, 5))
# prints 8

print(add(3, 5, 5))
# prints 13
```

Note: All optional arguments are always written after the positional arguments in the function prototype

1.3.3. Positional Arguments: are arguments that are passed using their position to the function.

```py
def simple_interest(principle, rate, time):
    # principle, rate and time are all required arguments
    return principle*rate/100*time

# since they are passed to the function by their position, i.e. principle is 1000, rate is 15 and time is 5 
print(simple_interest(1000, 15, 5))
# prints 750.0
```

Note: In the example in point 2, the variable `c` is a positional argument that is optional!

1.3.4. Keword Arguments: are arguments that are passed using their name to the function.

```py
def simple_interest(rate, time, principle = 100):
    # rate and time are all required arguments while principle is an optional argument with a default value of 100
    return principle*rate/100*time

# since they are passed to the function 
print(simple_interest(rate = 15, principle = 1000, time = 5))
# prints 750.0

print(simple_interest(15, 5))
# prints 75.0

print(simple_interest(15, principle = 1000, time = 5))
# prints 750.0
```

Note1: Keyword arguments are always passed to the function after positional arguments!

Note2: An argument cannot be called as both a positonal and a keyword argument IN THE SAME function call! `simple_interest(15, 5, rate = 15)` would not be valid since it calls rate as both a positional and a keyword argument

1.3.5. Arbitrary Arguments(*args): When an unknown or "arbitrary" number of arguments are passed to a function, they are known as Arbitrary arguments

```py
def add_multiply(*nums, multiply = 1):
    # nums is a required argument. the * denotes that it will accept an arbitrary number of arguments.
    # nums will be a list of all the arguments provided
    sum = 0
    for num in nums:
        sum+=num
    return sum*multiply

# add up all these numbers
print(add_multiply(5, 6, 2, 4, 2))
# prints 19

# add up all these numbers and also multiply by 2
print(add_multiply(5, 6, 2, 4, 2, 3, 5, multiply = 2))
# prints 54
``` 

Note1: Other arguments may follow an arbitrary argument but then that argument MUST ALWAYS be called as a keyword argument

Note2: Other positional arguments may preceed an arbitrary argument

Note3: An arbitrary argument CANNOT be called as a keyword argument!

1.3.6. Arbitrary Keyword Arguments(**kwargs): When an unknown or "arbitrary" number of keyword arguments are passed to a function, they are known as Arbitrary arguments

```py
def display_works(author, **works):
    # works is a required argument. the ** denotes that it will accept an arbitrary number of keyword arguments.
    # works will be a dictionary of all the keyword arguments and their values provided.
    for key in works:
        print(f"({key}, {works[key]})")
    print(author)

display_works("Roald Dahl", book1="Charlie and the Chocolate Factory", book2="Matilda")
``` 

Note1: No arguments can follow arbitrary keyword arguments.

Note2: Any number of keyword or positional arguments can preceed arbitrary keyword arguments.

```py
def add_multiply(*nums, multiply = 1):
    # nums is a required argument. the * denotes that it will accept an arbitrary number of arguments.
    # nums will be a list of all the arguments provided
    sum = 0
    for num in nums:
        sum+=num
    return sum*multiply

# add up all these numbers
print(add_multiply(5, 6, 2, 4, 2))
# prints 19

# add up all these numbers and also multiply by 2
print(add_multiply(5, 6, 2, 4, 2, 3, 5, multiply = 2))
# prints 54
``` 

### 1.4 _What is recursion, and why do we need it?_

Lets take the factorial from the previous excersie as an example.

We have learnt that n! = n\*(n-1)\*(n-2)\*...\*1

Similarly, (n-1)! = (n-1)\*(n-2)\*...\*1

But, notice that from these two equations we can actually write that n! = n\*(n-1)!

So if you were being introduced to the factorial for the first time, and you were just told that n! = n\*(n-1)! would this be enough information to find out the factorial of any number? Try computing 3! just by using the definition that n! = n*(n-1)!.

If you actually tried to do that, you would realise that its actually not possible because with that definition, you don't know when to stop!

3! = 3*2!

2! = 2*1!

1! = 1*0!

0! = 0*(-1)!

...

This means that other than the fact that n! = n*(n-1)! we also need a point to stop at. Lets say that you are now told that 0! = 1. With that information in mind, we can actually compute 3!

3! = 3*2!

2! = 2*1!

1! = 1*0!

and now, we know that 0! = 1, so now we use that in the last equation and work our way back up!

1! = 1 and then using this, 2! = 2, and then using this, it is found that 3! = 6

This process of defining a process in its own terms is known as recursion! The "stopping point" at which we stop going down and start to work back up is known as the base case! So can we do something like this with functions? Yes!

```py
def factorial(number):

    # remember to write a base case!
    # If you forget, you're program will be stuck in an infinite loop of recursion!
    if number == 0:
        return 1
    # the recursive case:
    return number*factorial(number-1)
```

### 1.5 _Excersise: What does this piece of code output?_

```py
def function(number):
    if number >= 1:
        print(number)
        function(number-1)
    print(number)

function(3)
```
Remember: A function will always execute ALL of its code UNLESS a return statement is encountered.

## 2. Classes and Objects

### 2.1. _What is Object Oriented Programming, and why do we need it?_

We come across a lot of different objects in our daily life. Each object has its own properties, some features that define it.

Lets take a pen for example. What are the properties of a pen? Its colour, its size, its kind (ball-point, fountain-point, gel-ink) and maybe the name of its owner.

Another example is a textbook. A textbook has a size, it has a subject, it has a length (the number of pages) and it has some information inside of it. Now the information inside a textbook is organised into named chapters.

For example, a maths text book might contain chapters like "sets", "trigonometery", "calculus" and so on, and if you want someone to read or go through a chapter, you'd say something like "go through the chapter on calculus".

Now imagine that you are a programmer who wants to write code that describes a pen, or a textbook... how could you go about writing code that expresses these properties discussed above?

You might try writing code that looks similar to this:

```py
pen_colour = "red"
pen_size = 0.5
pen_kind = "ball"
pen_owner = "John"

# wouldn't you want a way to see the info about your pen? Lets write a function to do that!
def display_information(colour, size, kind, owner):
    print("Colour : " + colour)
    print("Size   : " + str(size))
    print("Kind   : " + kind)
    print("Owner  : " + owner)
    print()

display_information(pen_colour, pen_size, pen_kind, pen_owner)
```
Sure, that would work for one pen, but some questions one might have are:

1. What if you wanted to make an unknown number of pens? How would someone know how many variables to declare?
2. What if you had a more complicated object with 100 properties? Would it be feasable to manually declare 100 variables for every object that you might need to create?

This is where classes come into the picture. So far we have learnt about the primitive data types in python, primitive meaning that they are in-built, simple data types which python provides to us. Now we are moving on to custom data types, data types that are defined by you, the programmer!

### 2.2. _What are classes, and why do we need them?_

So now, we want to create our own data types, a data type that would allow us to describe a pen, or any other object effectively, using code. This is exactly what a class allows us to do!

A class is basically a blue-print for creating an object, it tells us the defining properties of the object, and it also tells us what functions the object can perform. Following the class blue-print allows us to create "instances" of that class.

An object of a class, the realisation of the blueprint, is known as an instance of the class.

```py
class Pen:

    # remember the properties of the pen we discussed? A colour, a size, a kind, an owner
    
    def __init__(pen, col, sz, knd, own):
        pen.colour = col
        pen.size = sz
        pen.kind = knd
        pen.owner = own

    # This special function __init__ is known as a constructor, this is the "method" by which the object will be "constructed",
    # this is the essence of the blue-print!


    # wouldn't you want a way to see the properties of a pen you made as well?
    # you can write functions in a class that can work with the instances of the class. These functions are known as 'member
    # functions' of the class or 'methods'.
    def display_information(pen):
        print("Colour : " + pen.colour)
        print("Size   : " + str(pen.size))
        print("Kind   : " + pen.kind)
        print("Owner  : " + pen.owner)
        print()

# But a class is just a blue-print for creating a pen, it tells us which properties a pen is supposed to have
# But it is NOT the pen itself!
# To actually create a pen, we need to use the blue-print and specify all the properties of the specifc pen we want to create:

A = Pen("red", 0.5, "marker", "John")
# When we do this, python calls the constructor and says, hey constructor,
# construct me a Pen with its colour as "red", its size as 0.5, its kind as "marker" and let its owner be "John"
# this process of creating an object from its class is known as instantiation

A.display_information()
# display this marker's information

# And now that we actually have a pen class, remember that we can make AS MANY pens as we want!
B = Pen("blue", 0.1, "ball", "John")
C = Pen("black", 0.2, "fountain", "Robin")
D = Pen("red", 0.1, "gel", "Joe")
E = Pen("green", 0.1, "gel", "Robert")

# since a method works on a particular instance of a class, it must be called by using the dot operator, on that specific object.
B.display_information()
C.display_information()
D.display_information()
E.display_information()
```

### 2.3. _Classes, conventionally_

All programmers mutually agree to follow some rules, called conventions that are not necessary, but nice to follow while writing classes and make your code more readable to a usual programmer:

```py
class Pen:

    # typically, the object is called "self" in the functions that work with it
    # it is also common to give the same names to the function parameters as the properties of the object itself
    def __init__(self, colour, size, kind, owner):
        self.colour = colour
        self.size = size
        self.kind = kind
        self.owner = owner

    def display_information(self):
        print("Colour : " + self.colour)
        print("Size   : " + str(self.size))
        print("Kind   : " + self.kind)
        print("Owner  : " + self.owner)
        print()
```

### 2.4. _Excersise: Write a class that describes a bicycle object_

Which properties should a bicycle object have?

1. Colour (red, blue, white, etc)
2. Material (steel, aluminum, plastic, wood, etc)
3. Size (small, medium, large)
4. Height of the seat (in m)
5. Gear ratio (1, 2.5, 4, etc)
6. Diameter of the wheels (in cm)
7. Does it have a basket
8. Does it have a Bell
9. Do its wheels have sufficient air
10. Is the chain of the bicycle routed properly

What functions should a bicycle have?

1. Change gear ratio
2. Adjust seat height
3. Route chain
4. Pump air into the wheels
5. Find the speed of the bicycle (in m/s) when a peddling speed (in rpm) is provided

    (Hint: The speed of a bicycle with a peddling speed in rpm is given by:
    `(peddling_speed/60)*gear_ratio*((2*π*wheel_diameter/2)/100)`)

Would you make this with or without using a class?

### 2.5. _What makes classes so good?_

1. Reusability: The same class can be used to make as many objects as you want
2. Modularity: The code becomes incredibly modular, and it is easy for a programmer to debug the code in case there are any bugs
3. Clarity of code: Due to the code being modular, it is easier for others to read and understand the code
4. Better organisation: The data can be clearly and neatly organised for more complex objects
5. Data Abstraction: This is the process of hiding the implementation details from the user, allowing them to focus on the functionality instead.

    Example: you don't need to know a smartphone works internally to be able to use it. The details about its circuits, its workings are hidden from you, the user! Instead, the smartphone provides you with functions (call, message, surf the internet) only.

    Example in python:
    The functions like `math.sin()` and `math.cos()` can be used to find out the sine or cosine of an angle, but they do not tell you how the calcualtion is actually done. Those implementation details are hidden from you, the user and you only need to focus on the functionality!

### 2.6. _An object can also have other objects as its properties_

```py
class Pen:
    def __init__(self, colour, size, kind, owner):
        self.colour = colour
        self.size = size
        self.kind = kind
        self.owner = owner
    def display_information(self):
        print("Colour : " + self.colour)
        print("Size   : " + str(self.size))
        print("Kind   : " + self.kind)
        print("Owner  : " + self.owner)
        print()
class Pencil:
    def __init__(self, colour, shade, owner):
        self.colour = colour
        self.shade = shade
        self.owner = owner
    def display_information(self):
        print("Colour : " + self.colour)
        print("Shade  : " + str(self.shade))
        print("Owner  : " + self.owner)
        print()

class Stationary:
    def __init__(self, pen, pencil):
        self.pen = pen
        self.pencil = pencil
    def display_information(self):
        print("The Pen: ")
        self.pen.display_information()
        print("The Pencil: ")
        self.pencil.display_information()

A = Stationary(Pen("blue", 0.1, "ball", "John"), Pencil("black", "HB", "John"))
A.display_information()
```

## 3. Inheritance

### 3.1. _What is inheritance, and why do we need it?_

Lets say that there is a Person. Now each person has some defining properties, like their name, age, sex, height, weight. A person could be a student and in that case, they would have some additional defining properties, for example the school they attend, their id number, their year, their section and their seat number.

Now imagine that you are a programmer trying to describe a student using code... how could you go about writing code that expresses these properties discussed above? Keep in mind that a `class Person` with the properties name, age, sex, height and weight already exists.

You might think of a few different things that can be done here:

One option is to have a `person` object as a part of the `student` object, like so:

```py
class Person:
    def __init__(self, name, age, sex, height, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight

    def display_information(self):
        print("Name   : " + self.name)
        print("Age    : " + str(self.age))
        print("Sex    : " + self.sex)
        print("Height : " + str(self.height))
        print("Weight : " + str(self.weight))

class Student1:
    def __init__(self, person, school, id_no, seat_no, year, section):
        self.person = person
        self.school = school
        self.id_no = id_no
        self.seat_no = seat_no
        self.year = year
        self.section = section
    
    def display_information(self):
        self.person.display_information()
        print("School  : " + self.school)
        print("ID      : " + str(self.id_no))
        print("Seat    : " + str(self.seat_no))
        print("Year    : " + str(self.year))
        print("Section : " + self.section)
        print()
    
        
A = Student1(Person("John", 15, "male", 160, 60), "SUTD", 1024, 32, 2, "A")

print(A.person.name+"'s age: "+str(A.person.age))
A.display_information()
```

Another option might be to declare all of the properties of a `person` again along with the additional properties of a `student`
```py
# class Person here is unused, basically making the already existing class redundant
class Person:
    def __init__(self, name, age, sex, height, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight

    def display_information(self):
        print("Name   : " + self.name)
        print("Age    : " + str(self.age))
        print("Sex    : " + self.sex)
        print("Height : " + str(self.height))
        print("Weight : " + str(self.weight))

class Student2:
    def __init__(self, name, age, sex, height, weight, school, id_no, seat_no, year, section):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.school = school
        self.id_no = id_no
        self.seat_no = seat_no
        self.year = year
        self.section = section

    def display_information(self):
        print("Name   : " + self.name)
        print("Age    : " + str(self.age))
        print("Sex    : " + self.sex)
        print("Height : " + str(self.height))
        print("Weight : " + str(self.weight))
        print("School  : " + self.school)
        print("ID      : " + str(self.id_no))
        print("Seat    : " + str(self.seat_no))
        print("Year    : " + str(self.year))
        print("Section : " + self.section)
        print()

# when there are a lot of function parameters, it is nice to specify which parameters correspond to what
# values for better readability and clarity
B = Student2(name = "Robert", age = 14, sex = "male", height = 160, weight = 65, school = "SUTD", id_no = 1025, seat_no = 12, year = 1, section = "A")
print(B.name+"'s age: "+str(B.age))
B.display_information()
```
The first approach works, but the syntax looks a bit unintuitive, doesn't it?

This is because to create a student object, you have to first make a Person object and then provide that person object to the student constructor, like so `A = Student1(Person("John", 15, "male", 170, 70), "SUTD", 1024, 32, 2, "A")`

Also, to access a student's name and age, you have to do `A.person.name` and `A.person.age`... wouldn't `A.name` and `A.age` make more sense?

The 2nd approach fixes this issue but it is also a bit tedious because you have to manually declare all properties of a person inside the student constructor... What if there were not 5, but 100 different properties associated with a person? It would be too unfeasable to manually rewrite them.

This is where inheritance comes into the picture. Inheritance literally allows us to "inherit" the properties of one class (called the super class) into another class (called the sub class)

```py

# Super/Parent class
class Person:
    def __init__(self, name, age, sex, height, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight

    def display_information(self):
        print("Name   : " + self.name)
        print("Age    : " + str(self.age))
        print("Sex    : " + self.sex)
        print("Height : " + str(self.height))
        print("Weight : " + str(self.weight))

# Base/Sub class
class Student(Person):
    def __init__(self, name, age, sex, height, weight, school, id_no, seat_no, year, section):
        Person.__init__(self, name, age, sex, height, weight)
        self.school = school
        self.id_no = id_no
        self.seat_no = seat_no
        self.year = year
        self.section = section

    def display_information(self):
        Person.display_information(self)
        print("School  : " + self.school)
        print("ID      : " + str(self.id_no))
        print("Seat    : " + str(self.seat_no))
        print("Year    : " + str(self.year))
        print("Section : " + self.section)
    
# when there are a lot of function parameters, it is nice to specify which parameters correspond to what
# values for better readability and clarity
A = Student(name = "Robin", age = 16, sex = "male", height = 180, weight = 75, school = "SUTD", id_no = 1023, seat_no = 3, year = 3, section = "A")
print(A.name+"'s age: "+str(A.age))
A.display_information()
```

## 3.2 Excersise: