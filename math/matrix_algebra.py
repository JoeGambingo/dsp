# Matrix Algebra

# J. Gambino
# Metis Pre-work
# August 27, 2017

# Below is the download of the Jupyter Notebook I used:



# coding: utf-8

# In[1]:

import numpy as np


# #### Given Matrices

# In[2]:

A = np.matrix([[1,2,3], [2,7,4]])
B = np.matrix([[1, -1],[0,1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])


# In[17]:

u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([1, 8, 0, 5])
w = w.T


# #### Shape of each matrix

# In[18]:

A.shape


# In[19]:

B.shape


# In[20]:

C.shape


# In[21]:

D.shape


# In[22]:

u.shape


# In[23]:

w.shape


# #### Vector Operations

# In[24]:

u + v


# In[25]:

u - v


# In[26]:

alpha = 6
alpha*u


# In[27]:

u


# In[28]:

v


# In[31]:

np.dot(u, v)


# In[34]:

np.sqrt(np.dot(u, u))


# #### Matrix Operations

# In[42]:

# A+C is not defined


# In[43]:

A - C.T


# In[44]:

C.T + 3*D


# In[45]:

B*A


# In[46]:

# B*A.T is not defined


# #### Optional Exercises

# In[48]:

# B*C is not defined


# In[49]:

C*B


# In[50]:

B**4


# In[51]:

A*A.T


# In[52]:

D.T*D


# In[ ]:
