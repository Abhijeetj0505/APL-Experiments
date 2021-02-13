#!/usr/bin/env python
# coding: utf-8

# # APL EXP 1
#     

# Python Basics
# Content:
# Primitive types: int, float, variables, operators, expressions, statements,input/output statements
# Conditionals & loops: if, while and for loops

# Aim – Write a menu-Driven text Applications to solve five problems as a menu-driven textbased application. It presents the user with a set of choices ( that, e.g., (1) sum of input numbers, (2) average of input numbers, (3) mean of input numbers, (4)median of input numbers, (2) mode of input numbers and (X) Quit. The user makes a selection, which is then executed. The program exits when the user chooses the “quit” option. The great advantage of a program like this is that it allows the user to run as many iterations of your solutions without necessarily having to restart the same program over and over again

# Theory:-
# 
# Primitive Types:-
# 1)Int:- By default,the int data type is a 32-bit signed two's complement integer, which has a minimum value of -231 and a maximum value of 231-1. In Java SE 8 and later, you can use the int data type to represent an unsigned 32-bit integer, which has a minimum value of 0 and a maximum value of 232-1. Use the Integer class to use int data type as an unsigned integer. See the section The Number Classes for more information. Static methods like compareUnsigned, divideUnsigned etc have been added to the Integer class to support the arithmetic operations for unsigned integers
#         
# 2)float:- The float data type is a single-precision 32-bit IEEE 754 floating point. Its range of values is beyond the scope of this discussion, but is specified in the Floating-Point Types, Formats, and Values section of the Java Language Specification. As with the recommendations for byte and short, use a float (instead of double) if you need to save memory in large arrays of floating point numbers. This data type should never be used for precise values, such as currency. For that, you will need to use the java.math.BigDecimal class instead. Numbers and Strings covers BigDecimal and other useful classes provided by the Java platform        
#         
# 3)Variables:-Variables are containers for storing data values.Python has no command for declaring a variable.A variable is created the moment you first assign a value to it.Variables do not need to be declared with any particular type, and can even change type after they have been set.
# 
# 4)Operators:-Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators
#                 
# 5)Menu Driven Program:- A program that obtains input from a user by displaying a list of options – the menu – from which the user indicates his/her choice. Systems running menu-driven programs are commonplace, ranging from icroprocessor controlled washing machines to bank cash dispensers. In the case of the cash dispenser, single keys are pressed to indicate the type of transaction (whether a receipt is wanted with the cash, or if a statement of the bank balance is required) and with many, a single key is pressed to indicate the amount of money required
# 
# 6)MEAN,MODE and MEDIAN OF NUMBERS:-
# 1.Avarage/Mean= (sum of input numbers/n)
# 2.Mode=If the total number of observations (n) is an odd number, then the formula is given below:
#         Median=((n+1)/2)th observation
# If the total number of the observations (n) is an even number, then the formula is given below:
#         Median=((n/2)th observation+(n/2+1)th observation)/2
# 3.Mode=Most Frequently Occuring Value/input number is Mode.        

# In[17]:


import statistics
#asking users how many numbers they want to add in the list .
n=int(input("Enter the number of elements to be inserted: "))
#our list of numbers is stored here...
a=[]
#for loop for appending elements in list as we get input from user...
for i in range(0,n):
    Ele=int(input("Enter element: "))
    a.append(Ele)
Add=sum(a)
#while loop starts here .while true is used because we want this loop to run forever.
while True:
    #below list will be displayed to the users to pick from also called menu.
    print("1.Addition of Numbers")
    print("2.Avarage of Numbers")
    print("3.Mean of Numbers")
    print("4.Median of Numbers")
    print("5.Mode Of Numbers")    
    print("6.QUIT")
    #asking users about there choice or which action they want to perform on this program.
    choice=int(input("Enter your choice:"))
    #addition of numbers displayed here.
    if choice==1:
        print("Sum of elements is:",Add)
    #avarage of numbers.   
    elif choice==2:
        avg=Add/n
        print("Avarage is:",avg)
     #Mean of numbers or avarage.  
    elif choice==3:
        mean=Add/n
        print("Mean is:",mean)
     #median of numbers for odd and even number of lists.   
    elif choice==4:
        a.sort()  
        #median for Even n  
        if n % 2==0:
            a1=a[n//2]#floor division discards the fractional part
            a2=a[n//2-1]
            median=(a1+a2)/2
        else:
            #Median for odd n
            median=a[n//2]
        print("Median is: " + str(median))  
        #mode used predefined function mode and imported statistics library
    elif choice==5:
        print("Mode of given data set is % s" % (statistics.mode(a)))
    else:
        break


# In[ ]:




