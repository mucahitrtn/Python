#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn


# In[3]:


dataframe= pd.read_excel("maliciousornot.xlsx")


# In[4]:


dataframe


# In[5]:


dataframe.info()


# In[6]:


dataframe.describe()


# In[8]:


dataframe.corr()["Type"].sort_values()


# In[9]:


sbn.countplot(x="Type", data=dataframe)


# In[10]:


dataframe.corr()["Type"].sort_values().plot(kind="bar")


# In[11]:


y= dataframe["Type"].values


# In[12]:


x=dataframe.drop("Type", axis=1).values


# In[13]:


from sklearn.model_selection import train_test_split


# In[19]:


x_train, x_test, y_train, y_test= train_test_split(x,y, test_size=0.3, random_state=15)


# In[20]:


from sklearn.preprocessing import MinMaxScaler


# In[21]:


scaler = MinMaxScaler()


# In[22]:


scaler.fit(x_train)


# In[23]:


x_train= scaler.transform(x_train)
x_test= scaler.transform(x_test)


# In[24]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.callbacks import EarlyStopping


# In[28]:


model= Sequential()

model.add(Dense(units=30, activation= "relu"))

model.add(Dense(units=30, activation= "relu"))

model.add(Dense(units=30, activation= "relu"))

model.add(Dense(units=1, activation= "sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam")


# In[29]:


model.fit(x=x_train, y=y_train, epochs=700,validation_data=(x_test, y_test), verbose=1 )


# In[30]:


verikaybi= pd.DataFrame(model.history.history)


# In[31]:


verikaybi.plot()


# In[32]:


earlystopping= EarlyStopping(monitor="val_loss", mode="min", verbose=1, patience=25)


# In[36]:


model.fit(x=x_train, y=y_train, epochs=700,validation_data=(x_test, y_test), verbose=1 , callbacks=[earlystopping])


# In[37]:


verikaybi= pd.DataFrame(model.history.history)


# In[38]:


verikaybi.plot()


# In[41]:


model= Sequential()

model.add(Dense(units=30, activation= "relu"))
model.add(Dropout(0.6))
model.add(Dense(units=15, activation= "relu"))
model.add(Dropout(0.6))
model.add(Dense(units=15, activation= "relu"))
model.add(Dropout(0.6))
model.add(Dense(units=1, activation= "sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam")


# In[42]:


model.fit(x=x_train, y=y_train, epochs=700,validation_data=(x_test, y_test), verbose=1 , callbacks=[earlystopping])


# In[43]:


lossframe=pd.DataFrame(model.history.history)


# In[44]:


lossframe.plot()


# In[47]:


tahminler= model.predict_classes(x_test)


# In[48]:


tahminler


# In[49]:


from sklearn.metrics import classification_report, confusion_matrix


# In[50]:


print(classification_report(y_test, tahminler))


# In[53]:


confusion_matrix(y_test,tahminler)# ettiği tahminde 7 hatalı 84 doğru 


# In[ ]:




