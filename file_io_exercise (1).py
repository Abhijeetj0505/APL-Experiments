#!/usr/bin/env python
# coding: utf-8

# In[3]:


# EXECUTE THIS ONE FIRST!

import os

# Constants for the exercises:
WORKING_DIR = os.getcwd()
DATA_DIR = os.path.join(os.path.dirname(WORKING_DIR), 'data')


# # 1. Sum numbers listed in a file
# Fill ____ pieces of the code below. `sum_numbers_in_file` function takes a input file path as argument, reads the numbers listed in the input file and returns the sum of those numbers. You can assume that each line contains exactly one numeric value.

# In[3]:


def sum_numbers_in_file(in_file):
    sum_ = 0  # A common way to use variable names that collide with built-in/keyword words is to add underscore
    with open (in_file,'r') as f:
        for line in f:
            line = line.strip()  # Remove potential white space 
            sum_+= float(line)
    return sum_


# In[4]:


in_file = os.path.join(DATA_DIR, 'numbers.txt')
assert sum_numbers_in_file(in_file) == 189.5


# # 2. Reading first word from each line of a file
# Implement `find_first_words` function which takes an input file path as argument. The function should find the first word of each line in the file and return these words as a list. If a line is empty, the returned list should contain an empty string for that line.

# In[28]:


# Your implementation here
#s1=[]
def find_first_words(str):
    s1=[]
    with open(str,'r') as f:
        for line in f:
            line=line.strip()
            s1.append(line.split(" ",1)[0])
    return s1


# In[29]:


in_file1 = os.path.join(DATA_DIR, 'simple_file.txt')
in_file2 = os.path.join(DATA_DIR, 'simple_file_with_empty_lines.txt')

expected_file_1 = ['First', 'Second', 'Third', 'And']
assert find_first_words(in_file1) == expected_file_1

expected_file_2 = ['The', '', 'First', 'nonsense', '', 'Then']
assert find_first_words(in_file2) == expected_file_2


# In[30]:


in_file1 = os.path.join(DATA_DIR, 'simple_file.txt')


# In[31]:


find_first_words(in_file1)


# In[32]:


find_first_words(in_file2)

