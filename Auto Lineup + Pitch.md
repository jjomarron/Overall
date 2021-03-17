# Automate Lineup and Pitch Counts
This project is my most substantial Python undertaking and where I was able to access many different modules including Selenium, Pandas, Pathlib, time, and more. This project was also my first one and where I developed the skills that I have subsequently used in other projects. It was slow going with ups and downs but I am proud to have finished a project that brings together many different skills into one simple, easily understood result.

## Inspiration/Foundation
Ultimately, this project is a brainchild between myself and the head of the youth baseball organization I work with. Inspired by Moneyball and professional sabermetrics, we wanted to bring a level of analytics to our youth program to provide a more competitive edge for our teams and our players. We had been using [GameChanger](https://gc.com/) which kept track of our teams' statistics. A parent or coach would track every pitch of the game and GameChanger would compile pretty in-depth information about our players. However, most of this data was wasted beyond our players bragging about their HRs, batting average, or RBIs. This is our initial attempt to utilize data to help our teams perform better.

## Calculations
### Lineup
#### Order
The guiding philosophy behind our lineup generation was that we wanted to design an order that would avoid any true rally killers. Most baseball lineups are set up with the best hitters at the top and the worst at the bottom in order to provide the most plate appearances to the best hitters. This works well at the top but often times good pitchers can easily pass through the rest of the lineup with very little exertion thus making it further into the game. Our idea is to provide a lineup that does not provide three weak hitters in a row while still maintaing general lineup integrity in order to force their starting pitchers out of the game earlier.

The lineup was then agreed to be the following (numbers refer to relative strength of hitters): 1-2-3-4-7-10-5-8-11-6-9. This order would largely avoid three weak hitters in a row while still affording our best hitters the most plate appearances. The problem now is working on how to evaluate the strength of the hitters 

#### Evaluation
Borrowing from sabermetric literature as well as our own team philosophy we identified key areas in which we would evaluate our hitters. Those statistics were On Base Percentage, Contact Percentage, Batting Average on Balls in Play, Fly Ball Percentage, and Walk to Strikeout Ratio. We generated a relative strength index for each statistic by finding the team average and subtracting that from the individual's result. From there we divided that number by the team average and added 1 to avoid negatives and ranked the hitters in each statistic. We weighted each statistic equally and multiplied them all by each other to get one final number that we would use to evaluate the hitter's effectiveness. 

This is not a perfect calculation but we have a limited sample size, large performance variation, as well as inconsistent scoring. I am looking into more sabermetric literature to improve this calculation and thus improve our evaluation method. For now this is how we are ranking hitters and we are plugging them into the lineup order mentioned in the previous section.

### Pitch Counts
Another issue in youth baseball is pitch counts. Overuse can lead to long-term issues. Teams and leagues are looking to limit this by putting in weekly pitch limits. However, keeping track of these game to game is not always easily done. In order to preserve the integrity of our players' arms, I wanted to include a pitch counting segment that would allow coaches to know how many pitches they could plan for each player before the game started. This would allow coaches to create better plans and contingencies while also protecting our players. This process eliminates human error, keeps us in line with league protocol, and provides accountability to our coaches and their players.

## Code
```python
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
ElemE.send_keys('*********')

ElemP = browser.find_element_by_css_selector('#login_password')
ElemP.send_keys('*******')
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
```
Here you can see the final result combined with my [SMS Trigger Project](SMS Trigger.md)(certain information blocked out to protect identities):\
![image](https://user-images.githubusercontent.com/80477575/111109312-8581e280-8528-11eb-939e-da981cda2a1d.png)

## Moving Forward
* I need to globalize this code for each of our ~10 teams
* I need to make sure the file path naming conventions are consistent
* I need to create a way to schedule this to run nightly in order to save locally (for why see: [SMS Trigger](SMS Trigger.md))
* The code is a little long. There might be ways for me to shorten this and be better with coding conventions
