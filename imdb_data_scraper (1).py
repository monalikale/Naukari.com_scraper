#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as bs
import json


# In[15]:


imdb = 'https://www.imdb.com/'
driver = webdriver.Chrome()
driver.get(imdb)


# In[16]:


#Xpath of menu button
menu = '//label[@id="imdbHeader-navDrawerOpen"]'
#click menu
menu_button = driver.find_element(By.XPATH,menu)
menu_button.click()


# In[14]:


tab='//*[@id="imdbHeader"]/div[2]/aside[1]/div/div[2]/div/div[1]/span/div/div/ul/a[3]'
menu_button = driver.find_element(By.XPATH,tab)
menu_button.click()


# In[21]:


driver.find_element(By.XPATH,("//*[text()='Most Popular TV Shows']")).click()


# In[38]:


titles = driver.find_elements(By.XPATH,'//a[@class="ipc-title-link-wrapper"]/h3')
ratings = driver.find_elements(By.XPATH,'//div[@class="sc-e2dbc1a3-0 ajrIH sc-be6f1408-2 dAeZAQ cli-ratings-container"]/span')
link=driver.find_elements(By.XPATH,'//a[@class="ipc-title-link-wrapper"]')

title = []
year = []
rating = []
links=[]
for x in link:
    #list of texts title, year 
    a = x.get_attribute("href")
    links.append(a)
    
for x in titles:
    #list of texts title, year 
    a = x.text
    title.append(a)

#get rating    
for y in ratings:
    b = y.text
    rating.append(b.replace("\n", ""))
#compile list to single Data Frame    
popular_shows = pd.DataFrame(list(zip(title,rating,links)), columns = ["title","rating","links"])


# In[40]:


popular_shows.to_csv("Most_popular_movises.csv")


# In[ ]:




