#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[15]:


#Generation of random 5x5 ndarray
x=np.random.random((5,5))
x


# In[16]:


#Storing mean and std deviation for formula
mean=np.mean(x)
std=np.std(x)

#Formula for normalization
x_normalized=(x-mean)/std

#Output
x_normalized


# In[18]:


#Saving of file
np.save("x_normalized.npy",x_normalized)


# ### Problem 2

# In[28]:


#Generation of 10x10 array of squares of integers from 1 to 100
X=np.arange(1,101)**2
Y=X.reshape(10,10)
Y


# In[29]:


#Output of Y so it is more pleasant to look at
print(Y)


# In[30]:


#Elements divisible by 3
div_by_3 = Y[Y % 3 == 0]
div_by_3


# In[32]:


#Cleaner output
print(div_by_3)


# In[35]:


#Saving of file
np.save("div_by_3.npy",div_by_3)


# In[ ]:




