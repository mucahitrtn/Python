#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


dataframe= pd.read_excel("bisiklet_fiyatlari.xlsx")


# In[8]:


dataframe.head()


# In[9]:


import seaborn as sbn
import matplotlib.pyplot as plt


# In[10]:


sbn.pairplot(dataframe)


# # splitting data into two pieces

# In[11]:


from sklearn.model_selection import train_test_split


# In[17]:


#y= wx + b    y= dffiyat
y=dataframe["Fiyat"].values

x=dataframe[["BisikletOzellik1","BisikletOzellik2"]].values

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.33, random_state=15)


# In[18]:


x_train


# In[19]:


x_train.shape


# In[21]:


x_test.shape #%33,3333 e %66,666666 olarak bölündü 


# In[22]:


y_train


# In[23]:


y_test


# # Scaling

# In[24]:


from sklearn.preprocessing import MinMaxScaler


# In[25]:


scaler= MinMaxScaler()


# In[26]:


scaler.fit(x_train)


# In[27]:


x_train= scaler.transform(x_train)
x_test = scaler.transform(x_test)


# In[29]:


x_train # Veriler 0,1 arasında scale edildi


# In[33]:


import tensorflow as tf


# In[34]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[66]:


model = Sequential()

model.add(Dense(6, activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(6, activation="relu"))

model.add(Dense(1))

model.compile(optimizer= "rmsprop", loss= "mse")


# In[67]:


model.fit(x_train, y_train, epochs=250)


# In[70]:


loss= model.history.history["loss"]


# In[71]:


sbn.lineplot(x=range(len(loss)), y= loss)


# In[72]:


trainloss= model.evaluate(x_train, y_train, verbose=0)


# In[73]:


testloss= model.evaluate(x_test, y_test, verbose=0)


# In[74]:


trainloss


# In[75]:


testloss


# In[76]:


testTahminleri = model.predict(x_test)


# In[77]:


testTahminleri


# In[78]:


tahmindf= pd.DataFrame(y_test, columns=["Gercek Y"])


# In[79]:


tahmindf


# In[80]:


testTahminleri = pd.Series(testTahminleri.reshape(330,))


# In[81]:


testTahminleri


# In[82]:


tahmindf= pd.concat([tahmindf,testTahminleri], axis= 1)


# In[83]:


tahmindf.columns= ["Gercek Fiyat", "Tahmini fiyat"]


# In[84]:


tahmindf


# In[90]:


sbn.scatterplot(data= tahmindf, x="Gercek Fiyat", y= "Tahmini fiyat")


# In[91]:


from sklearn.metrics import mean_absolute_error, mean_squared_error


# In[92]:


mean_absolute_error(tahmindf["Gercek Fiyat"], tahmindf["Tahmini fiyat"])


# In[93]:


mean_squared_error(tahmindf["Gercek Fiyat"], tahmindf["Tahmini fiyat"])


# In[ ]:




