# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:07:51 2022

@author: M
"""
#Print Exercises
print("M")
print("i")
print("g")
print("u")
print("e")
print("l")
#No variables show up in the editor  

#Operation Exercises
#1
print(5/2)
print(5.0/2.0)
#They are displayed in the exact same way in the variable editor 
#2
print(6%5)
print(3%7)
print(14%36)
print(48%22)
#It displays the remainder from dividing the two numbers
#3
print(20//2)
print(32//8)
print(54//30)
#displays integer division 
#4
print(8+3+14*7/4)
#It does follow the order of operations

#Variable Exercises
letter1 = "M"
letter2 = "i"
letter3 = "g"
letter4 = "u"
letter5 = "e"
letter6 = "l"
letterx = letter1 
print(letterx)
print(letter1)

letter1 = "Z"
print(letterx)
print(letter1)

#2. The variables and their values appear
#3. No
#5. No 
#6. No, changes it then, not permanently

#Boolean Exercises
print(1 == 1.0)
#1. yes
#They are the exact same value even though one is in decimal form
#2.
print(5 == (3+2))
#Yes
#3.
print(1 == 1.0 and 1 == 1.0 and 5 == (3+2))
print(1 == 1.0 or 1 == 1.0 or 5 == (3+2))
print(1 == 1.0 and 1 == 1.0 or 5 ==(3+2))
print(1 == 1.0 or 1 == 1.0 and 5 == (3+2))
print(1 ==1.0 and not 1 == 1.0 or 5 ==(3+2))

#List Exercises
oddlist = [1, 3, 5, 7, 9]
#1. yes
#2. No issues
#3.
print(len(oddlist))
#It outputs "5"
#4. 
print(type(oddlist))
#<class 'list'>
#5.
intlist = range(101)
print(list(intlist))
#6. Yes

#Dictionary Exercises
#1.
nm = "Miguel"
yr = "24"
yos = "3"
ff = "food1, food2, food3"
about_me = {'name': nm, 'age': yr, 'stdyr':yos, 'favefood':ff}
#2.
print(about_me)
print(type(about_me))
#3.
print(len(about_me))
#By how how many variables are in the dictionary

#Array Exercises
import numpy as np
#1
mixnums = np.array([4, 9, 7, 8.5, 3.2, 1.8])
print(mixnums)
#The integers are spaced further apart and are succeeded by a dot
#The floats are closer together and aren't succeeded by anything 
#2
mixtypes = np.array([4, 8, 2.2, 4.5, "hello", "world"])
print(mixtypes)
#The array displays values as strings
#3
oddarray = np.arange(1,100,2)
print(oddarray)
#4
logarray = np.logspace(1,5,16)
print(logarray)






