## General
import time
import shutil, os
from pathlib import Path
from datetime import date, timedelta
import datetime

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

#Download File Path
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) 
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', r'C:\Users\Jack\Documents\Work\Chicago Stars\Python.Line Up')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')  #skips popup

browser = webdriver.Firefox(profile)
browser.implicitly_wait(10)


## Access online database
browser.get('https://gc.com')

browser.find_element_by_css_selector(".gcButtonSmall").click()

ElemE = browser.find_element_by_css_selector('#email')
ElemE.send_keys('*************')

ElemP = browser.find_element_by_css_selector('#login_password')
ElemP.send_keys('*************')
ElemP.submit()

browser.find_element_by_css_selector(".teamsLink").click()

browser.find_element_by_css_selector("ul.withDividers:nth-child(5) > li:nth-child(1) > h2:nth-child(1) > a:nth-child(1)").click()

browser.find_element_by_css_selector("#statsnav").click()

## Download the datataset for LineUp
browser.find_element_by_css_selector(".jsExportStatsCSVContainer").click()

browser.find_element_by_css_selector("li.team_stat_nav_link:nth-child(3) > a:nth-child(1)").click()
browser.find_element_by_css_selector(".right").click()

######PITCHING

today=date.today()
month=today.strftime('%m')
day=today.strftime('%d')
year=today.strftime('%Y')

for x in range(8,0,-1):
    try:
        #front=date.today()-timedelta(x)
        front=datetime.date(2019,5,3)-timedelta(x)  ##Loop test
        date1=front.strftime("%b %d").lstrip("0").replace(" 0", " ")
        browser.find_element_by_xpath("//select//option[contains(.,'" + date1 + "')]").click()

        table = browser.find_elements_by_css_selector("table.gcTable")

        for row in table:
            print(row.text)
	
        df = pd.read_csv(StringIO(row.text),sep=' ')
        df = df.filter(['#','Roster','#P'])
        df = df.drop('Totals')
        #df = 80-df['#P'] ####Suggested weekly pitch count
        df = df.sort_values(by=['#P'],ascending=False)
        df = df.astype(str)

        df['Final'] = df['#'] + " " + df["Roster"] + " " + df['#P']

        pitch_list=df['Final'].values.tolist()
        f = '{:<8}|{:<15}' # formatting

        if pitch_list:
            break

    except NoSuchElementException:
            continue

browser.quit()

#df = pd.read_csv((r'C:/Users/Jack/Documents/Work/Chicago Stars/Python.Line Up/gc-'+year+'-welles-park-14u-red_spring-'+year+'_Qualified_SeasonStats-'+year+'-'+month+'-'+day+'.csv'), header=1)

#df = pd.read_csv((r'C:/Users/Jack/Documents/Work/Chicago Stars/Python.Line Up/gc-2019-welles-park-14u-red_spring-2019_Qualified_SeasonStats-'+year+'-'+month+'-'+day+'.csv'), header=1) #14u depending on team and change based on download date

#FILENOTFOUNDERROR

df = pd.read_csv((r'C:/Users/Jack/Documents/Work/Chicago Stars/Python.Line Up/gc-2019-welles-park-14u-red_spring-2019_Qualified_SeasonStats-'+year+'-'+month+'-15.csv'), header=1)

#os.unlink(r'C:/Users/Jack/Documents/Work/Chicago Stars/Python.Line Up/gc-'+year+'-welles-park-14u-red_spring-'+year+'_Qualified_SeasonStats-'+year+'-'+month+'-'+day+'.csv')

os.unlink(r'C:/Users/Jack/Documents/Work/Chicago Stars/Python.Line Up/gc-2019-welles-park-14u-red_spring-2019_Qualified_SeasonStats-'+year+'-'+month+'-15.csv')


#######LOO Calculation########
df=df.filter(['Number','Last','First', 'OBP', 'C%', 'BABIP','FLB%','BB/K'])
ur_row = df[df['Number']=='Team'].index.tolist()
df=df.iloc[:ur_row[0]]
df['FLB%'] = df['FLB%'].str.rstrip('%')
df=df.apply(pd.to_numeric,errors='ignore')
df.loc['mean'] = df.mean(axis=0,skipna=True)

df['aOBP']=(df['OBP']-df.loc['mean','OBP'])/df.loc['mean','OBP']+1
df['aC%']=(df['C%']-df.loc['mean','C%'])/df.loc['mean','C%']+1
df['aBABIP']=(df['BABIP']-df.loc['mean','BABIP'])/df.loc['mean','BABIP']+1
df['aFLB%']=(df['FLB%']-df.loc['mean','FLB%'])/df.loc['mean','FLB%']+1
df['aBB/K']=(df['BB/K']-df.loc['mean','BB/K'])/df.loc['mean','BB/K']+1

df = df.drop('mean')
df['LOO']=df['aOBP']*df['aC%']*df['aBABIP']*df['aFLB%']*df['aBB/K']

df = df.sort_values(by=['LOO'],ascending=False)
df.insert(1,"LineUp",["1", "2", "3", "4", "7", "10", "5", "8", "11", "6", "9"],True)
df=df.apply(pd.to_numeric,errors='ignore')
df = df.sort_values(by=['LineUp'],ascending=True)

df1 = df.filter(['First','Last'])
df1["Full Name"] = df1["First"] + " " + df1["Last"]


lineup_list=df1["Full Name"].values.tolist()
f = '{:<8}|{:<15}' # formatting
str_lineup = 'Lineup:\n' + '\n'.join([str(elem) for elem in lineup_list])

try:
    str_pitchers = 'Pitch Count:\n' + '\n'.join([str(elem) for elem in pitch_list])
except NameError:
    str_pitchers=''

final = str_lineup + '\n\n' + str_pitchers

print(final)

textfile = open('C:\\Users\\Jack\\Documents\\Work\\Chicago Stars\\Python.Line Up\\14u.txt', 'w') #Change for the 
textfile.write(final)
textfile.close()
