#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Elma():
    
    def __init__(self, isim):
        self.isim=isim
        
    def bilgiver(self):
        return self.isim+ " 150 kalori"


# In[12]:


class Muz():
    
    def __init__(self, isim):
        self.isim=isim
        
    def bilgiver(self):
        return self.isim+ " 100 kalori"


# In[13]:


elma = Elma("elma")
muz = Muz("muz")


# In[14]:


meyveListesi = [elma, muz]


# In[15]:


for meyve in meyveListesi:
    print(meyve.bilgiver())


# # Ozel Methodlar

# In[24]:


class Meyve():
    def __init__(self, isim, kalori):
        self.isim= isim
        self.kalori= kalori
        
    def __str__(self):
        return f"{self.isim} şu kadar kaloriye sahiptir: {self.kalori}"
    def __len__(self):
        return self.kalori


# In[25]:


muz = Meyve("Muz", 186)


# In[26]:


print(muz)


# In[27]:


len(muz)


# # Exception Handling

# In[ ]:


while True:
    try:
        i= int(input("Numaranizi giriniz: "))
    except:
        print("Lutfen gecerli numara giriniz.")
        continue
    else:
        print("Tesekkurler.")
    finally:
        print("finally...")    


# In[ ]:




