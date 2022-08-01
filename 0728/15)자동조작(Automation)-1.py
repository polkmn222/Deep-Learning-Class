#!/usr/bin/env python
# coding: utf-8

# Selenium WebDriver
# ----------------------
# We need to figure it out
# What is WebDriver?
# 
# * WebDriver is One of the component in selenium.
# * WebDriver is module
# 
# * Kind of browser engine
#     
#     >firefox browser ---> Firefox()
#     >
#     >Chrome Browser ---> Chrome()
#     >
#     >Edge ---> Edge()
# 
# * WebDriver is an API (APPlication Programming Interface)

# ### The structure of WebDriver

# ![image-3.png](attachment:image-3.png)

# Architecture of WebDriver
# -----------------------
# Selenium 3
# 
# Selenium Language bindings -- JSON Wire protocal --> Browser drivers --- w3c --> Browsers
# 
# Selenium 4
# 
# Selenium Language bindings -- w3c --> Browser drivers --- w3c --> Browsers

# ## Pre-requisites:
# 
# Python
# 
# IDE(Jupyter Notebook or Pycharm or VScode :: whatever you want)

# #### 1) Download browser specific drivers by using below links.......

# In[1]:


# https://pypi.org/project/selenium/


# >chrome: https://chromedriver.chromium.org/downloads
# > 
# >Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# >
# >Firefox: https://github.com/mozilla/geckodriver/releases
# >
# >Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/

# Once you downloaded, extract .zip files then you can use .exe files in python

# #### 2) setup selenium webdriver

# In[4]:


# !pip install selenium == 4.0.0.b4
# !pip install selenium


# ### Test Case
# 
# 1) Open Web Browser(Chrome/FF/Edge)
# 
# 2) Open URL https://admin-demo.nopcommerce.com/login
# 
# 3) Provide Email (admin@yourstore.com).
# 
# 4) Provide password (admin). 
# 
# 5) Click on Login.
# 
# 6) Capture title of the dashboard page. (Actual title)
# 
# 7) Verify title of the page: "Dashboard /  nopCommerce administration" (Expected)
# 
# 8) close browser

# Test site address::https://opensource-demo.orangehrmlive.com/

# In[10]:


# selenium 3

from selenium import webdriver

driver = webdriver.Chrome('D://Leon_Park//Crawling_test//chromedriver.exe')
driver.get('https://opensource-demo.orangehrmlive.com/')

driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id('btnLogin').click()


# check the title
act_title = driver.title
exp_title ='OrangeHRM'

if act_title == exp_title:
    print('Login Test is Okay')
else:
    print('Login Test Failed')
    
driver.close()


# In[11]:


# selenium 4
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Servicevice('D://Leon_Park//Crawling_test//chromedriver.exe')
driver = webdriver.Chrome(service = serv_obj)

driver.get('https://opensource-demo.orangehrmlive.com/')

# driver.find_element_by_name("txtUsername").send_keys("Admin")
# 위와 같은 형태의 selenium 4 변형
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,'btnLogin').click()


# check the title
act_title = driver.title
exp_title ='OrangeHRM'

if act_title == exp_title:
    print('Login Test is Okay')
else:
    print('Login Test Failed')
    
driver.close()


# In[ ]:


# end of test file


# In[ ]:




