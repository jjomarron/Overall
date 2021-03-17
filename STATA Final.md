# Time Series and ARIMA Models

## Overview
This is a copy of my final I completed for my graduate Econometrics course. The test was all under one dataset with a heavy focus on not only our STATA skills but also our understanding of Time Series Analysis. I will bold all questions and share my answers in bulleted, normal text.

The dataset was relatively simple consisting of the Dow Jones closing price, month, day, year, and day of week variables. It also included the number of reported Covid-19 cases in China and the number of reported Covid-19 cases in the rest of the world. The range of the dataset was from March 14,2019 to March 13, 2020)

My STATA code is available [here](Stata Final Code.md).

## Time Series Analysis
**1. Plot the closing price over the past year using a created time variable.**
  ![image](https://user-images.githubusercontent.com/80477575/111415651-55fde200-86b0-11eb-8635-4c6e70590445.png)\
**2. Is the natural log of the Dow Jones Industrial Average (DJIA) closing price stationary? How do you know?**
  * The natural log is not stationary. I conducted a Dickey-Fuller test and the natural log did not pass the statistical tests at the 10% level.\
  ![image](https://user-images.githubusercontent.com/80477575/111415730-834a9000-86b0-11eb-898d-c53acc0327f8.png)\
  
**3. If the natural log of the DJIA is non-stationary, transform it so that it is stationary and then present evidence that the new time series is stationary.**
  * I transformed the data by finding the daily change in the closing price. It is stationary as shown by the Dickey-Fuller test below. It is significant at the 1% level.\
  ![image](https://user-images.githubusercontent.com/80477575/111415784-9bbaaa80-86b0-11eb-9342-690c7654b2ce.png)\

**4. Model your stationary version of the time series as an AR(1), do the estimates imply that the DJIA follows a random walk? How do you know?**
  * I conducted an ARIMA test with an AR(1) model. It is negative which indicates that it is mean reverting since for each time period it keeps flipping signs.\
  ![image](https://user-images.githubusercontent.com/80477575/111415837-b7be4c00-86b0-11eb-9d46-e4a54725d6ce.png)\

**5. How is your answer in (d) influenced by the Covid-19 pandemic?  To answer this, simply limit the analysis to observations before the outbreak.**
  * Before the COVID-19 pandemic, the coefficient is not statistically different than 0. So, this means that before, the stock market was a random walk.\
  ![image](https://user-images.githubusercontent.com/80477575/111415925-e2a8a000-86b0-11eb-8098-24e498aa707d.png)\

**6. If you believe that your answers in (d) and (e) represent some “new normal,” what should you do the day after the stock market drops 5%.**
  * I should invest in the stock market since the new normal is mean reversion. If it goes down 5% one day, then it should go up as it reverts to the mean. If I invest on after it has gone down, I can capture the upswing and profit.

**7. What ARIMA model best fits the data?  How do you know?**
  * The ARIMA model that best fits the data is ARIMA (3,0,2). I know this by doing Akaike information criterion (AIC) and Bayesian information criterion (BIC) tests. The lowest value is the best fit and it corresponded with ARIMA (3,0,2).\
  ![image](https://user-images.githubusercontent.com/80477575/111416051-18e61f80-86b1-11eb-9012-3bf0724b6800.png)\

**8. Estimate whether the data exhibit weekend effects and turn of the month effects.  Interpret the results.**
  * I ran the regression and found that the data did not exhibit weekend effects. dow1 which corresponds with Monday is not statistically significant. None of the days are which suggests that there are no specific day effects on closing price in the Dow Jones. This is the same case for turn of the month effects (I created firstpart by looking at the last couple days of the previous month and the first few days of the current month like they did in the paper). It is not statistically significant which indicates that there is nothing different about the turn of the month than the rest of it.\
  ![image](https://user-images.githubusercontent.com/80477575/111416115-49c65480-86b1-11eb-9e61-eb58b343f088.png)\

**9. Another common anomaly in stocks is referred to the January effect, where stock returns are elevated in Janaury.  Is there evidence of a January effect?  How do you know?**
  * There is no evidence of a January effect based off of this data. None of the months are statistically different from the omitted variable December. So, there is no evidence that January (or any other month) provides an elevated stock return.\
  ![image](https://user-images.githubusercontent.com/80477575/111416155-5f3b7e80-86b1-11eb-8e6e-6da7aa3605f9.png)\

**10. Interpret the coefficients on covid19_china and covid19_row.**
  * The coefficient for covid19_china is statistically significant at the 5% level but for the rest of the world it is not statistically significant. For COVID-19 cases in China it means that for every 1000 cases, the daily change in the Dow Jones decreases by 0.01%\
  ![image](https://user-images.githubusercontent.com/80477575/111416425-e7ba1f00-86b1-11eb-973a-e602d94e43e9.png)\

**11. Do Covid-19 cases in China and Covid-19 cases in the rest of the world appear to be having the same effect on the DJIA. How do you know?**
  * The regression is evidence that cases in China do not have the same effect as in the rest of the world. I know this because in China, the coefficient is statistically significant while in the rest of the world it is not.
    *	However, I believe this model (and subsequently its analysis is incomplete). Both numbers are growing simultaneously and in China they are growing at a faster rate than in the rest of the world. With more variation because of the higher numbers, the OLS model will favor the China cases whereas the real effect on Dow Jones prices might be the growing cases outside of China and knowing that the exponential increase in cases will happen. 

**12. Now, estimate the distributed lag model, which includes two additional lags of covid19_china and covid19_row. Describe what your estimates say about how increased cases of Covid-19 in China and the rest of the world is affecting the change in the DJIA.**
  * In this model, the COVID-19 cases in China are not statistically significant. In the rest of the world they are significant at the 5% level. For every 1000 new COVID-19 cases two days prior, we would expect a decrease of 1% in the daily change of the Dow Jones. For the previous day, an increase in 1000 cases causes an increase of 1.3%. For the day of, an increase in 1000 cases would cause a 0.3% decrease.

**13. What's one reason why your estimates might follow the path described by the estimates in the distributed lag model.**
  * It might follow this model because the market is reacting to the exponential nature of COVID-19. Right now in the developing stage, the true effect of coronavirus is not how many people have it today but instead how many people will be infected from the people who have it right now. So from two days ago, the market will react negatively due to worrying reports. Yesterday’s reports and the positive coefficient might be a correction by the market to the overreaction. The day prior will always have a higher number of cases than two days prior (a positive) and the market corrections will be positive so the positive coefficient might just be explaining the correction from the day before. The current day’s reports are negative because the long run trend is expected to be negative as the economy slows down as the number of cases goes up.

**14. All of the previous estimates assume that the number of diagnosed cases of Covid-19 should affect the DJIA linearly. Using the static model, should these two variables be included linearly or both a linear and squared component (include the day and day of the week in the specification as well)?  How do you know?**
  * They should have both a linear and squared component. I know this because cases are growing at an exponential rate (illustrated by the graph below). Since cases are growing exponentially, the relationship between the Dow Jones and COVID-19 is not linear. In order to run an accurate regression with OLS, this needs to be accounted for by including a squared component.
  * Again, the COVID-19 cases in China are not statistically significant. For the rest of the world, the cases are significant at the 99.5% level. This output is saying that the COVID-19 cases are having a negative impact on the Dow Jones at an increasing rate. The Dow Jones might react this way because it is anticipating the exponential negative outputs of coronavirus so for each case, there is an added negative drag on the Dow Jones since it is understood that for each person that is reported they will infect more than one person (as modeled by the graph above).





