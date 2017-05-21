
# coding: utf-8

# In[2]:

#weather
import requests
from bs4 import BeautifulSoup
import re
from termcolor import colored

res=requests.get("https://www.msn.com/en-us/weather")

bsobj=BeautifulSoup(res.text,"lxml")
weather=bsobj.find("span",{"class":"current"})
acc=bsobj.find("a",{"href":re.compile(r'(day=1)$')})
print("\n\t\t")
print colored(weather.attrs["aria-label"],"blue")
print("\n")
print colored(acc.attrs["aria-label"],"blue")


# In[ ]:



