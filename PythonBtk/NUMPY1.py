#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


np.random.randn()


# In[4]:


np.random.randn(5,5)


# In[5]:


np.random.randn(3,3
               )


# In[7]:


type(np.random.randn(3,3))


# In[17]:


list1=np.random.randint(1,21,5)


# In[14]:


list= np.random.randn(5,5)


# In[15]:


list


# In[16]:


type(list)


# In[18]:


type(list1)


# In[19]:


list.reshape(5,5
            )


# In[20]:


list.max()


# In[21]:


list1.max()


# In[22]:


list1.argmax()


# In[23]:


list1.shape


# In[24]:


list.shape


# #  NUMPY OPERTIONS
# 

# In[34]:


nplist= np.arange(0,15)


# In[26]:


list[3]


# In[27]:


list[3,2]


# In[28]:


list[3][2]


# In[29]:


nplist[3]


# In[35]:


slicelist= nplist[3:7]


# In[36]:


slicelist


# In[37]:


slicelist[:]=100


# In[38]:


nplist


# In[ ]:




