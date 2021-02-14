#!/usr/bin/env python
# coding: utf-8

# # 1. Creating formulas
# Write the following mathematical formula in Python:
# 
# \begin{align}
#  result = 6a^3 - \frac{8b^2 }{4c} + 11
# \end{align}
# 

# In[3]:


a = 2
b = 3
c = 2


# In[6]:


# Your formula here:
result = (6*a**3) - (8*b**2)/(4*c)+11


# In[8]:



assert result == 50


# # 2. Floating point pitfalls
# Show that `0.1 + 0.2 == 0.3`

# In[12]:


# Your solution here
p=0.1+0.2
q=round(p,2)
assert q == 0.3
# This won't work:
# assert 0.1 + 0.2 == 0.3

