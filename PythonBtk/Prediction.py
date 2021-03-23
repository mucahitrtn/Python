# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Btk pyhton ile makine ogrenmesi --1--
# kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
#Veri Yükleme
#verilerin bir dataFrame'e atanmasi
veriler= pd.read_excel("veri1.xlsx")
#print(type(veriler))

#print(veriler)

veriBoy= veriler[["boy"]]

#print(veriBoy)

#EKSIK VERILER- VERI YUKLEME- SORUNU COZME

#EKSIK VERILERE YAS KOLONU ORTALAMASI EKLENMESI

eksikveri= pd.read_excel("eksikveriler.xlsx")

#print(eksikveri)

imputer= SimpleImputer(missing_values=np.nan, strategy= 'mean')

yas= eksikveri.iloc[:,1:4].values

#print(yas)

imputer= imputer.fit(yas[:,1:4])
yas[:,1:4]= imputer.transform(yas[:,1:4])
#print(yas)

#eksikveri ICERISINDE NAN OLAN SATIRLARIN SILINMESI

droppedveri= eksikveri.dropna()

#print(droppedveri)

#ulke= np.array(droppedveri["ulke"])

##########################################################################################



#AYNI SEKILDE DIZI OLUSTURABILMEK ICIN
#SU METOD KULLANILABILIR

ulke1= eksikveri.iloc[:,0:1].values
#Bu kodda :, tum kolonu al demek, 0:1 ise 0. sadece 0. indexteki kolonu al dememk


#KATEGORİKİ VERİLERİN SAYISAL VERİLERE CEVRIMI GOSTERILMISTIR.

labelencoder= preprocessing.LabelEncoder()

ulke1[:,0]= labelencoder.fit_transform(eksikveri.iloc[:,0])

#print (ulke1)

ohe= preprocessing.OneHotEncoder()
ulke_ohe= ohe.fit_transform(ulke1).toarray()

#############################33
###cinsiyet encode
c = eksikveri.iloc[:,4:].values
labelencoder= preprocessing.LabelEncoder()

c[:,-1]= labelencoder.fit_transform(eksikveri.iloc[:,-1])

#print (ulke1)

c_ohe= ohe.fit_transform(c).toarray()



#print(c_ohe)

#####################################################

#PANDASTA DATAFRAMELERLE ISLEMLER VE CONCATENATE

res= pd.DataFrame(data= ulke_ohe, index= range(22), columns=["tr", "us","uk","rt","de","fr"])
#print(res)

res1= pd.DataFrame(data=yas, index= range(22) ,columns=["boy", "kilo", "yas"])
#print(res1)

res2= pd.DataFrame(data=c[:,:1], index=range(22), columns=["cinsiyet"])
#print (res2)

s= pd.concat([res,res1], axis=1)
s= pd.concat([s,res2], axis=1)

#print (s)

####################################################################

#OZNITELIK OLCEKLENDIRME

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(s, res2, test_size=0.33, random_state=15)

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

sc= StandardScaler()
lr= LinearRegression()

lr.fit(x_train, y_train)

y_predict= lr.predict(x_test)

boy= s.iloc[:, 6:7].values

#print (boy)

sol= s.iloc[:,:6]
sag= s.iloc[:,7:]

sagsol=pd.concat([sol, sag], axis=1)

x_train, x_test, y_train, y_test = train_test_split(sagsol, boy, test_size=0.33, random_state=15)

r2= LinearRegression()

r2.fit(x_train, y_train)

y_pred= r2.predict(x_test)

########### p-value

import statsmodels.api as sm

X= np.append(arr= np.ones((22,1)).astype(int), values=sagsol, axis=1)

Xl= sagsol.iloc[:,[0,1,2,3,4,5,7]].values

Xl= np.array(Xl,dtype=float)

model= sm.OLS(boy,Xl).fit()

print(model.summary())
















