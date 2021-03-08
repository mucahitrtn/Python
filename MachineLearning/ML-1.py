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

#print(ulke_ohe)

#####################################################

#PANDASTA DATAFRAMELERLE ISLEMLER VE CONCATENATE

res= pd.DataFrame(data= ulke_ohe, index= range(22), columns=["tr", "us","uk","rt","de","fr"])
#print(res)

res1= pd.DataFrame(data=yas, index= range(22) ,columns=["boy", "kilo", "yas"])
#print(res1)

res2= pd.DataFrame(data=eksikveri, index=range(22), columns=["cinsiyet"])
#print (res2)

s= pd.concat([res,res1], axis=1)

#print (s)

####################################################################

#OZNITELIK OLCEKLENDIRME

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(s, res2, test_size=0.33, random_state=15)

from sklearn.preprocessing import StandardScaler

sc= StandardScaler()

xtrain= sc.fit_transform(x_train)

xtest= sc.fit_transform(x_test)





