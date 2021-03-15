# Fantasy Soccer Overview
As mentioned before, this project's goal is to automatically update an Excel spreadsheet with each player (15) on each team (10). The data we use to evaluate all comes from WhoScored.com which is a fantastic website with super in-depth soccer statistics. The only problem is that the statistics need to be found after each match on either the match page or the updated player page. It is relatively tedious and can add up especially later in the season when game weeks are shifted around as European competitions are in full swing.

## EPL ID Grabber
First, I had to know this type of project was possible. After quickly browsing the web site , I realized that the format of the website was www.whoscored.com/Players/######/Show/Player-Name where ###### is a unique identification number (UIN). After a quick check, I realized that I could access the player page by just using the www.whoscored.com/Players/######. So, my first idea was set--I had to see if I could collect the ID number for each of the Premier League Players. I figured if I could collect this, I could use the UIN in our spreadsheet to match and update the appropriate statistics. There is a page on WhoScored where I could select the Player ID from the html. There were 51 pages on the table so I iterated over the table and clicked next page 51 times. 
Here is the code:
```ruby
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
As you can see in the picture below, I was able to successfully return an ID for all 510 EPL players listed on WhoScored.com. This was an initial proof of concept for the project about Selenium accessing the WhoScored website as well as gathering the necessary IDs in order to match those and update the statistics later. However, as you can also still see I am still struggling to adjust the unicode text format and need to figure out away to adjust for the accent marks in player names better. I skipped past this part for now as it will likely be an option/a few lines of code so I wanted to continue into the bulk of the project.
![image](https://user-images.githubusercontent.com/80477575/111106557-4c933f00-8523-11eb-9345-2aea84a1c8a8.png)

## Auto Update Initial Check
In this part, I wanted to prove I could access the stats so I kept the first 9 names from the test.csv file that I had gather the EPL IDs. The result is here below:
![image](https://user-images.githubusercontent.com/80477575/111106962-07234180-8524-11eb-82d0-74a5de8afa47.png)

I was able to succesfully populate the table! However, this was only for the most recent game played which means that I would still run into problems as game weeks are played out of order.

# Moving Forward
* I need to solve the unicode issue
* I need to add a gameweek/date variable to match as well so the data is populating appropriately
* I need to learn .csv to Google Sheets functionality
