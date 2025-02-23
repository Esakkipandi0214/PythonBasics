# Variables are containers for storing data values .

"""
1. Python  is dynamically typed , which means you don't have to specify the type of a variable .
2. It is determined automatically based on the assigned value .
"""
# Python has no commands for declaring a variable .


""" Below Example for create a vairable and print in Terminal """

x = 5; # create variable "X" and assign a value 5 to it using "=" assignment operator 
y= "Pandi" # similar to above but a string value .

# to print the variables use "print" statement .
print(x);
print(y);

# to excecute use command below in your terminal
#  syntax ->  python PythonVariables/PythonVariables.py


""" Assign Multiple Values """

#  Python allows you to assign values to multiple variables in one line .

a,b,c = 1001,2001,3001 ;

print(a)
print(b)
print(c)

""" One value to Multiple Variables """

# You can assign the same value to multiple variables in one line .

d = e = f = 4001;

print(d)
print(e)
print(f)

""" Unpack a collection """

# Python allows you to extract the values into variables . 
# This is called "unpacking" .

fruits = ["Apple","Orange","Cherry"]
g,h,i = fruits # destructuring -> means unpacking a collection for data from a variable and assign to multiple seperate variables .

# we can use "+" operator on string to concate .
print(g + h + i)

# For number, they work as mathametical operation .


"""===================================== More Info ================================================"""

# to specify the data type of a variable , this can be done with casting .

X = str(5)
print(X);

# you can the print for line 28 show the number in string format .
# to get the type of a variable , we can use ` type(variabe) `

print(type(X)); #this print the type of the variable .
#  like <class 'str'>  , str -> represnt string type .


# Also python is case sensitive .
#  you see the above variables x and X are assigned seperately and printed seperately .
