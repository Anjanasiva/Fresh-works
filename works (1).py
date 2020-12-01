#!/usr/bin/env python
# coding: utf-8

# In[82]:


import Freshworks as x


# In[96]:


x.create("Anjana",25)#creates key with key_name,value given and with no time-to-live property


# In[97]:


x.create("Siva",26,3600)# creates  key with key_name,value given and with  time-to-live property


# In[98]:


x.read("Anjana")#returns the value of the respective key in Jasonobject format 'key_name:value'


# In[99]:


x.read("Siva")
#returns the value of the respective key in Jasonobject format 'key_name:value' byconsidering time-to-live property


# In[100]:


x.create("Anjana",50)#gives error because keyname already existed in database


# In[101]:


x.modify("Anjana",55)#modifies the keyname in db


# In[102]:


x.delete("Anjana")#it deletes the respective key and its value from the database


# In[103]:


import threading 
#this is for python 3.0 and above. 
from threading import*
import time
import Freshworks as x

t1=Thread(target=(x.create or read or delete),args=("keyname",1,0)) #as per the operation
t1.start()
time.sleep(5)
t2=Thread(target=(x.create or read or delete),args=("key",5,0)) #as per the operation
t2.start()
time.sleep(5)
#and so on upto tn


# In[ ]:





# In[ ]:




