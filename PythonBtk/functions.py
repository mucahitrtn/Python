#!/usr/bin/env python
# coding: utf-8

# In[1]:


benimadim= "Mucahit Ertano"


# In[2]:


benimadim.upper()


# In[4]:


help(benimadim.upper)


# In[5]:


def newFunc():
    print("My first function in python")


# In[6]:


newFunc()


# In[29]:


def funcwithparameter(a , s):
    print(f"ilk stringim: {s}  ilk integerim: {a}" )


# In[30]:


funcwithparameter(150 , "hello ")


# In[31]:


def sums(num1, num2):
       return num1+num2


# In[32]:


a= sums(10,20)


# In[33]:


a


# In[34]:


type(a)


# ##ARGS &KWARGS

# In[37]:


def yeniTopl(*args):
    return sum(args)


# In[39]:


a=yeniTopl(10,20)


# In[40]:


a


# In[43]:


def fun1(*args):
    return args


# In[45]:


a = fun1(10,20,30)


# In[46]:


type(a)


# In[53]:


def fun2(**kwargs):
    for x in kwargs:
        print (x)


# In[54]:


fun2(mucahit= 70, hello=25, yılmaz=120)


# In[ ]:




