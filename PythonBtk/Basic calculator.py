#!/usr/bin/env python
# coding: utf-8

# In[5]:




def toplama(num1,num2):
    return int(num1)+int(num2)
    
def cikarma(num1,num2):
    return int(num1)-int(num2)
    
def carpma(num1,num2):
    return int(num1)*int(num2)

def bolme(num1,num2):
    return int(num1)/int(num2)

def hesapmakines():
    
    print("+ Toplama")
    print("- Cikarma")
    print("/ Bolme")
    print("* Carpma")
    a= input ("yapacaginiz islemi secin.")
    num1= input("Sayi 1= ")
    num2= input("Sayi 2= ")
    sonuc=0
    if a=="+":
        sonuc=toplama(num1,num2)
    elif a=="-":
        sonuc=cikarma(num1,num2)
    elif a=="*":
        sonuc=carpma(num1,num2)
    elif a=="/":
        sonuc=bolme(num1,num2)    
    
    print(sonuc)

hesapmakines()
    


# In[ ]:




