#!/usr/bin/env python
# coding: utf-8

# In[11]:


import threading 
#this is for python 3.0 and above. 
from threading import*
import time


# In[12]:


d={} #the dictionary to store data


# In[17]:


def create(key,value,timeout=0):
    if key in d:
        print("this key already exists") #error 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("Memory limit exceeded!! ")#error 
        else:
            print("Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error


# In[18]:


def read(key):
    if key not in d:
        print("given key does not exist in database. Please enter a valid key") #error
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("time-to-live of",key,"has expired") #error
        else:
            stri=str(key)+":"+str(b[0])
            return stri


# In[19]:


def delete(key):
    if key not in d:
        print("given key does not exist in database. Please enter a valid key") #error
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("time-to-live of",key,"has expired") #error
        else:
            del d[key]
            print("key is successfully deleted")


# In[16]:


def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("given key does not exist in database. Please enter a valid key") #error 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("time-to-live of",key,"has expired") #error
    else:
        if key not in d:
            print("given key does not exist in database. Please enter a valid key") #error
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




