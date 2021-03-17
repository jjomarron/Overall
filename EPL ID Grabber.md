```python
## General
import time
import shutil, os
from pathlib import Path
from datetime import date, timedelta
import datetime

path=r'C:\Users\Jack\Documents\Misc\Friend Help\Fantasy Soccer'

## Excel
import pandas as pd
from io import StringIO
import numpy as np
import os
import win32com.client

#Selenium/Firefox
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) 
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', r'C:\Users\Jack\Documents\Work\Chicago Stars\Python.Line Up')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

browser = webdriver.Firefox(profile)
browser.implicitly_wait(10)

browser.get('https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/8228/Stages/18685/PlayerStatistics/England-Premier-League-2020-2021')

browser.find_element_by_css_selector("#apps > dd:nth-child(2) > a:nth-child(1)").click()

l=[]

table = browser.find_elements_by_css_selector("#top-player-stats-summary-grid")


for x in range(0,51,1):
    hold = browser.find_elements_by_xpath("//*[@id='top-player-stats-summary-grid']//*[@class='player-link']")

    try:
        for i in hold:
            l.append(i.get_attribute("href"))
            time.sleep(.5)

        browser.find_element_by_css_selector("#next").click()
        time.sleep(.5)

    except StaleElementReferenceException:
            pass

browser.quit()

len(l)

df= pd.DataFrame(l,columns=['temp'])

df['temp']=df['temp'].str[34:]

df[['ID','show','Name']]=df.temp.str.split('/',expand=True)

df['Name'] = pd.Series(df['Name'], dtype="string")

df[['First','Last1']]=df.Name.str.split('-',1,expand=True)

df = df.drop(['temp','show','Name'],axis=1)

df.to_csv('test.csv', index=False, encoding='utf-8')
```
