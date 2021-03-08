#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn


# In[2]:


dataframe= pd.read_excel("merc.xlsx")


# In[3]:


dataframe


# In[4]:


dataframe.describe()


# In[7]:


dataframe.isnull().sum()#NULL OLAN VERİLER KONTROL EDİLMİŞTİR


# In[8]:


sbn.distplot(dataframe["price"])


# In[11]:


sbn.countplot(dataframe["year"])


# In[12]:


dataframe.corr()


# In[13]:


dataframe.corr()["price"].sort_values()


# In[16]:


sbn.scatterplot(data= dataframe)


# In[17]:


sbn.scatterplot(x="mileage", y="price", data= dataframe)


# In[20]:


dataframe.sort_values("price", ascending= False).head(20)


# In[21]:


dataframe.sort_values("price", ascending= True).head(20)


# In[22]:


len(dataframe)


# # Data setinden veri cikarmak

# In[23]:


dataframe.sort_values("price", ascending=False).iloc[100:]


# In[24]:


# İlk yüz araba atlanılarak yeni frame oluşturuldu


# In[26]:


yeniframe=dataframe.sort_values("price", ascending=False).iloc[100:]


# In[28]:


yeniframe.describe()


# In[29]:


dataframe.describe()


# In[30]:


plt.figure(figsize=(7,5))
sbn.displot(yeniframe["price"])


# In[31]:


dataframe=yeniframe


# In[32]:


dataframe= dataframe[dataframe.year!= 1970]


# In[34]:


dataframe.groupby("year").mean()["price"]


# In[35]:


dataframe=dataframe.drop("transmission", axis=1)


# In[36]:


dataframe


# In[37]:


y= dataframe["price"].values
x= dataframe.drop("price", axis=1).values


# In[38]:


from sklearn.model_selection import train_test_split


# In[39]:


x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.3, random_state=10)


# In[40]:


len(x_test)


# In[42]:


len(x_train)


# In[43]:


from sklearn.preprocessing import MinMaxScaler


# In[44]:


scaler = MinMaxScaler()


# In[45]:


x_train= scaler.fit_transform(x_train)


# In[47]:


x_test=scaler.fit_transform(x_test)


# In[48]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[50]:


x_train.shape


# In[51]:


model = Sequential()

model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))

model.add(Dense(1))

model.compile(optimizer="adam", loss="mse")


# In[52]:


model.fit(x=x_train, y=y_train, validation_data=(x_test, y_test),batch_size=250 ,epochs=300)


# In[53]:


kayipveri= pd.DataFrame(model.history.history)


# In[54]:


kayipveri


# In[55]:


kayipveri.plot()


# In[56]:


from sklearn.metrics import mean_squared_error, mean_absolute_error


# In[57]:


tahmin= model.predict(x_test)


# In[58]:


mean_absolute_error(y_test, tahmin)


# In[63]:


plt.scatter(y_test, tahmin)
plt.plot(y_test,y_test, "g-*")


# In[ ]:




