#!/usr/bin/env python
# coding: utf-8

# # instance&attribute

# In[20]:


class SuperHero():
    
    
    
    def __init__(self, name, age, job):#__init__ parametre almıyorsa self ile çağrılmalıdır.
        print("HELLO init.")
        self.name= name
        self.age= age
        self.job= job
        
    def whatismyjob(self):
        print(f"I am a superhero and im a {self.job}")


# In[21]:


superman = SuperHero("Mucahit", 21, "Software Engineer")


# In[24]:


superman.whatismyjob()


# In[35]:


class Araba():
    
    def __init__(self, marka, yas, hacim):
        self.yas= yas
        self.hacim=hacim
        self.marka= marka
    
    def tiphesapla(self):
        if self.hacim/self.yas>=20:
            print (f"Arabaniz D sinifi modeliniz: {self.marka}")
        else:
            print(f"Arabaniz C sinifi modeliniz: {self.marka}") 


# In[36]:


yeniaraba= Araba("bmw",5,150)


# In[37]:


yeniaraba.marka


# In[38]:


yeniaraba.tiphesapla()


# In[39]:


araba= Araba("toyota",5,95)


# In[40]:


araba.tiphesapla()


# In[ ]:




