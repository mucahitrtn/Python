#!/usr/bin/env python
# coding: utf-8

# In[1]:


liste = [0,1,2,3,4,5,6,]


# In[2]:


#RANGE


# In[3]:


range(15)


# In[5]:


list(range(10
          ))


# In[6]:


for x in list(range(5)):
    print (x*5)


# In[8]:


list(range(2, 25, 3))


# In[9]:


##ENUMERATE


# In[14]:


i=0
for x in list(range(2,25,3)):
    print(f"güncel numara: {x} güncel index:{i}")
    i+=1


# In[15]:


for x in enumerate(list(range(5,25))):
    print(x)


# RANDOM

# In[16]:


from random import randint


# In[17]:


randint(0,1000)


# In[18]:


randint(0,1000)


# In[19]:


from random import shuffle


# In[20]:


listem= list(range(10,1500,27))


# In[24]:


shuffle(listem)


# In[ ]:





# # ZİP

# In[27]:


yemek= ["muz", "elma", "armut0", "ananas"]
kalori= ["100", "150", "250", "217"]
gun= ["pazartesi", "sali", "cars", "pers"]


# In[28]:


listelerim= list(zip(yemek,kalori,gun))


# In[29]:


type(listelerim)


# In[30]:


listelerim


# In[31]:


ornek = []
benimStr= "Mucahit Ertano"

for harf in benimStr:
    ornek.append(harf)


# In[32]:


ornek


# In[33]:


newList = [x for x in benimStr]


# In[34]:


newList


# In[35]:


secondList = [x ** 3 for x in list(range(5,10))]


# In[36]:


secondList


# In[ ]:




