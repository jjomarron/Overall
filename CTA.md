# Doors Closing: How have rideshares and demographic changes affected CTA ridership?
This project was developed in my Public Sector Economics graduate class at DePaul University. Many thanks to Professor Gabriella Bucci for the phenomenal class and especially for helping improve the conciseness of my economic writing.

## Overview
This project came out of personal interest for me inspired by a few changes I had witnessed. After two years away in the Peace Corps, I came back to see some of the familiar places I had known and loved in Chicago had been transformed and gentrified. I saw people not as familiar with the transit system as Ubers and Lyfts became more popular. I also was personally affected by cuts to our transit system in high school. I knew these changes were not happening in silos so I wanted to explore the relationship between rideshares, demographics, and Chicago Transit Authority (CTA) ridership as a proxy or initial understanding of how gentrification might be affecting our transit system.

## Key facts/concepts to know (Tableau graphs to be included later)
* Real median income has trended down in Chicago over the last 20 years
* Chicago's Black population has decreased substantially since 2000
  * CTA claimed in 2009 that 60% of their ridership identifies as a minority
  * Latino, White, and Asian populations are growing their shares of the total population
* Real operating expenses have increased steadily since 2006
* The "death spiral" is a concept in transit literature that identifies a funding/ridership crisis on public transit systems
  * A "death spiral" can occur from a loss of funding, worse service, or a loss of ridership. The three contribute to a hard-to-stop cycle
    * A loss of riders means less funding. Less funding means worse service. Worse service means less riders. The cycle continues until the system is extremely limited or until an intervention occurs

## Research Question
My driving research question was: **How have rideshares and demographic changes affected CTA ridership?** After determining those impacts, I also wanted to explore how certain neighborhoods might have been affected in order to understand the shifts in equity behind any of the ridership effects.

## Data Collection and Cleaning
For this project, I compiled a unique dataset utilizing the City of Chicago Data Portal, the American Community Survey, and CTA's annual Budget Recommendations. Data collection was more laborious than data cleaning which I will explore in this section. My data cleaning and compilation codes are available at the end of this section.
<sub>I had intended to use the robust rideshare data that Chicago now collects but unfortunately it did not cover the rise of rideshares in the city. So, instead I had to use indicator variables for both Uber and Lyft's launch date in Chicago in my regression model.</sub>

### City of Chicago Data Portal
The City of Chicago Data Portal's CTA Daily Boarding Totals and L-station Daily Boarding Totals made up the bulk of my dataset. CTA Daily Boarding Totals is an aggregate count of all the rides taken in a day, split between bus and train. This was useful in identifying the difference in effects between train and bus. The L-station Daily Boarding Totals was strictly train rides split by each train station. I grouped the stations by area of the city (more on this split later) to help understand how different parts of the city might have been affected at least by train. Unfortunately, the bus data was not available.

### American Community Survey
The American Community Survey (ACS) provided me with valuable demographic data about Chicago. The data was city-wide and included the racial demographic percentages, median income, and median age. I used the city-wide numbers because it captures at-large trends and not double count the neighborhood changing and the overall city changes that are occuring behind the scenes.

### CTA Budget Recommendation
The CTA releases a Budget Recommendation each year where they record last year's final budget. I used these reports to populate the annual operating expenses as a proxy for quality and commitment to sound transit service.

### Seasonality
It is well documented and apparent that transit has seasonal and weekly changes. Weekdays bring more riders as do the summer months. In order to account for this, I conducted a preliminary regression that removed the seasonality components. This allowed me to run a regression considering purely non-seasonal variables. 

The data cleaning code is available [here](.md).

The seasonality adjusting code is [here](.md).

## Model
### Initial Model
After conducting a literature review and considering the aims of my project, my initial regression model was the following:

**𝑅𝑖𝑑𝑒𝑠<sub>𝑡</sub>=𝛽0+𝛽1𝑈𝑏𝑒𝑟<sub>𝑡</sub>+𝛽2𝐿𝑦𝑓𝑡<sub>𝑡</sub>+𝛽3𝑀𝑒𝑑𝑖𝑎𝑛𝐴𝑔𝑒<sub>𝑡</sub>+𝛽4𝑃𝑜𝑝𝑢𝑙𝑎𝑡𝑖𝑜𝑛𝑃𝑒𝑟𝑐𝑒𝑛𝑡𝑎𝑔𝑒𝑠<sub>𝑡</sub>+𝛽5𝑎𝑑𝑗𝑇𝑟𝑎𝑖𝑛𝐹𝑎𝑟𝑒<sub>𝑡</sub>+𝛽5𝑎𝑑𝑗𝐵𝑢𝑠𝐹𝑎𝑟𝑒<sub>𝑡</sub>+𝛽6𝑎𝑑𝑗𝑀𝑒𝑑𝑖𝑎𝑛𝐼𝑛𝑐𝑜𝑚𝑒<sub>𝑡</sub>+𝛽7𝑎𝑑𝑗𝑂𝑝𝑒𝑟𝑎𝑡𝑖𝑛𝑔𝐸𝑥𝑝𝑒𝑛𝑠𝑒𝑠<sub>𝑡</sub>+𝛽8𝑃𝑜𝑝𝑢𝑙𝑎𝑡𝑖𝑜𝑛<sub>𝑡</sub>+𝛽9𝑑𝑎𝑦𝑡𝑦𝑝𝑒<sub>𝑡</sub>+𝛽9𝑑𝑎𝑦_𝑜𝑓_𝑤𝑒𝑒𝑘<sub>𝑡</sub>+𝛽10𝑚𝑜𝑛𝑡ℎ<sub>𝑡</sub>+𝛽11𝑑𝑎𝑦_𝑜𝑓_𝑚𝑜𝑛𝑡ℎ<sub>𝑡</sub>+ε<sub>𝑡</sub>**

*<sub>Model had three iterations: one with total CTA rides, one with only train, and another with only bus</sub>

**<sub>PopulationPercentages are 4 separate variables consisting percentage of Latino, White, Black, and Asian residents </sub>

***<sub>All prices (fare, median income, etc.) are in 2019 USD</sub>

### Model Testing
#### VIF
To test my model, I took 25% of the dataset as a sample to test my specification. The initial model showed an extremely Variance Inflation Factor (VIF) which suggests multicollinearity between my independent variables. 

![image](https://user-images.githubusercontent.com/80477575/111392806-5634b800-8685-11eb-90d1-e36690d3707e.png)

In order to combat this, I conducted a stepwise regression and correlation pairwise. I decided to drop day of the week and train fare as they heavily correlated with day type and bus fare, respectively. I still had issues with multicollinearity with bus fare so I took the first difference. There was also obvious issues including all the percentages of the population so I kept the white percentage of the population as the variable to evaluate regarding demographic change.

![image](https://user-images.githubusercontent.com/80477575/111395763-9a2abb80-868b-11eb-85d5-8533620405cc.png)


These new VIF numbers are much lower and all under the critical numbers of 10.

#### Autocorrelation
I tested for autocorrelation and recorded a Durbin-Watson statistic of 1.57 which suggests slight negative autocorrelation but not enough to be worried about.

#### Goodness of Fit
Finally, I tested the goodness of fit of my adjusted model on the Total dataset and the Test dataset and found my model was a good fit for the data I had compiled. The Root Mean Squared Errors were close with perhaps a slight overfit but nothing worrisome.

![image](https://user-images.githubusercontent.com/80477575/111393871-97c66280-8687-11eb-831c-b246e53f028e.png)

### Final Model
After my testing and consideration of different variables, my final model was the following:

**𝑅𝑖𝑑𝑒𝑠<sub>𝑡</sub>=𝛽0+𝛽1𝑈𝑏𝑒𝑟<sub>𝑡</sub>+𝛽2𝐿𝑦𝑓𝑡<sub>𝑡</sub>+𝛽3𝑀𝑒𝑑𝑖𝑎𝑛𝐴𝑔𝑒<sub>𝑡</sub>+𝛽4𝑊ℎ𝑖𝑡𝑒𝑃𝑒𝑟𝑐𝑒𝑛𝑡𝑎𝑔𝑒<sub>𝑡</sub>+𝛽5𝑎𝑑𝑗𝐹𝑎𝑟𝑒<sub>𝑡</sub>+𝛽6𝑎𝑑𝑗𝑀𝑒𝑑𝑖𝑎𝑛𝐼𝑛𝑐𝑜𝑚𝑒<sub>𝑡</sub>+𝛽7𝑎𝑑𝑗𝑂𝑝𝑒𝑟𝑎𝑡𝑖𝑛𝑔𝐸𝑥𝑝𝑒𝑛𝑠𝑒𝑠<sub>𝑡</sub>+𝛽8𝑃𝑜𝑝𝑢𝑙𝑎𝑡𝑖𝑜𝑛<sub>𝑡</sub>+ε<sub>𝑡</sub>**

The code for this regression is available [here](CTA Final Regression.md)

## Hypotheses
Ultimately, there is a lot that might affect CTA ridership so I considered each variable I included in my regression. Here are my hypotheses for each variable.

* **Uber/Lyft** - Rideshares have both complementary and substitution effects on transit. Rideshare advocates say they provide final connections and can enhance existing transit infrastructure. Critics claim that rideshares are pulling away riders and putting transit systems in threat of the death spiral. I believe in Chicago's case, the substitution effect will outweigh its complement and cause a decrease in Uber/Lyft.
* **Median Age** - Older Chicagoans are less likely to be acclimated to rideshare companies so I believe a younger Chicago would cause a decrease in CTA rides as they are more familiar with the technology. Also, the young workforce that is moving to Chicago is not as familiar with the CTA and might prefer to use rideshares than adjust to our transit system. 
* **White Percentage** - CTA's core riders are minorities so I would expect an increase in the share of white Chicagoans to reflect a severe negative adjustment in CTA rides.
* **Adjusted Bus Fare** - As bus fare increases, I would expect less riders as people might transition to other forms of transportation (walking, bikes, cars, etc.). One exception to this might be if the fares are well spent and result in higher quality service which should be captured by the Adjusted Operating Expenses. 
* **Adjusted Median Income** - As income increases, I would anticipate seeing a decrease in ridership as people might be more willing to drive and incur more costs.
* **Adjusted Operating Expenses** - I expected an increase in ridership since operating expenses can serve as a proxy for quality. This is not always the case but something to hypothesize about.
* **Population** - Population should increase ridership as more people move in and need to travel for work and life.

## Results

### Bus and Train

![image](https://user-images.githubusercontent.com/80477575/111395419-d3aef700-868a-11eb-98d0-313c7975cbca.png)

### Train Ridership by Neighborhood

![image](https://user-images.githubusercontent.com/80477575/111395447-dd385f00-868a-11eb-8967-30d3d98101d1.png)

## Takeaways
* Increased ridership has many positive benefits
  * Environmental, cultural, equitable, etc.
* If we can better identify why ridership is declining, we can better fix lagging ridership
* How policy choices in different areas might affect public transportation
  * Death spiral



## Gaps and Further Questions
* Crime data on the CTA
* Rideshare regressors are just indicator variables
  * Model would benefit from ride counts per day, especially growth over time
* Expand on Neighborhood Analysis
  * Cluster based on key variables (income, demographics, etc.)
  * Bus ridership
