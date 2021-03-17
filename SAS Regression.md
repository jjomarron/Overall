# Regression Analysis
This code is sharing fairly straightforward regression concepts while also exploring goodness of fit concepts. This was originally an assignment for a class where we spent time learning about various analytic tools across SAS and R.

## Overview
The assignment provides generally straightforward directions to practice skills in the SAS language with a few conceptual questions included. Questions will be bolded and my answers are bulleted, normal text.

**1. Use sgscatter function for multivariate scatter plots to find a potential variables to have nonlinear relationship with price. If necessary, create some squared variables to analyze the potential nonlinear relationships. For example, square of rooms, square of bathrooms, etc.**
  * I created squared variables for review score ratings, beds, and bathrooms based on their relationship. There is a quadratic relationship for these independent variables and the dependent variable (price). I also considered number of reviews as the relationship appears to be quadratic but not squared (more like square root).\
   ![image](https://user-images.githubusercontent.com/80477575/111419307-3d44fa80-86b7-11eb-9110-fb59cd973086.png)\
   
**2. Carefully explain why we want to transform some variables as logarithmic variables. From the variables in the data what are the variables you want to consider to transform as logarithmic variables?**
  * We want to transform some variables as logarithmic variables if they’re distribution is not normal. This particularly happens with some bounded independent variables. By transforming logarithmically, we can fix some of these distribution problems by still having a solid interpretation of the variables.
  * In this case, I would look to transform reviews scores rating (however, in this exercise I decided that squaring was a better fit than logging) as well as number of reviews. Also, price is popularly transformed due to its generally non-normal distribution.

**3. Perform a regression analysis on the following base model
proc reg data=Airbnb2 ;
   model price = accommodates ;  
   model logprice = logaccommodates ;  
run ;
Compare the models and explain the meanings of the coefficient of b1 for each model.**
  * In the first model (price=accommodates), the B1 coefficient is 23.47648. This means that for every 1 extra person the Airbnb accommodates, the expected price increases by $23.48.\
  ![image](https://user-images.githubusercontent.com/80477575/111419496-8d23c180-86b7-11eb-846d-b4653b39ac36.png)
  * In the second model (logprice = logaccomodates), the B1 coefficient is 0.74935. This means that for every 1 percent increase in people the Airbnb can accommodate, the expected price increases by .75%.
  ![image](https://user-images.githubusercontent.com/80477575/111419556-ab89bd00-86b7-11eb-94f8-909725cb308a.png)
  
**4. From the models in 3, we want to consider if the hostclass influence the price along with the accommodates. Since the hostclass is an ordinal variable, we cannot include the variable in the regression model directly. Estimate the model using “proc reg” and “proc glm”. Explain if the hostclass is a significant variable to the price.**
  * Based off of the following proc glm model, I determined hostclass to not be a significant variable to price. I determined this after observing the Type III chart that provides a partial analysis of the categorical variables in relation to the dependent variable.\
  ![image](https://user-images.githubusercontent.com/80477575/111419624-cceaa900-86b7-11eb-8746-df2419b40d6f.png)
  * However, when I ran the model with log price and log accommodates I found a significant relationship again based on the Type III sum of squared errors. This would direct me to using the log-log model in my final model.
  ![image](https://user-images.githubusercontent.com/80477575/111419641-d2e08a00-86b7-11eb-90f0-1cf18379990d.png)\
  
**5. Using Airbnb2 data, let’s use 70% as a training data and 30% as a testing (validating) with the seed number as 123456. Estimate some regression models as the dependent variable of logprice using the training data with the following options in the regression.**
  * Adjusted R-squared--iterating for every possible model variation and finding the model with the highest adjusted R<sup>2</sup>\
  ![image](https://user-images.githubusercontent.com/80477575/111419741-fc011a80-86b7-11eb-80dd-ad22d0c058f6.png)
  * Stepwise--adding another variable if the adjusted R-squared increases. A variable is not added if the adjusted R-squared does not increase\
  ![image](https://user-images.githubusercontent.com/80477575/111419759-058a8280-86b8-11eb-8512-29081efc531b.png)\
  * Your own model different from 1) and 2)--Based on observing the other models, I included key variables that I thought would provide the best results\
  ![image](https://user-images.githubusercontent.com/80477575/111419772-0d4a2700-86b8-11eb-84a2-474d64988435.png)\
  
**6.	Perform the out of sample prediction for the observations using the testing data. Find the following statistics and compare the results. Which model is the best performed model in terms of the following statistics?**
  * Mean Squared Error
    * The best model here is the 1st one (which is the Adjusted R-Squared model)\
    ![image](https://user-images.githubusercontent.com/80477575/111420093-995c4e80-86b8-11eb-9e4d-dbfa836cdcfb.png)
  * Root Mean Squared Error
    * The best model here is the 2nd one (which is the stepwise model)\
    ![image](https://user-images.githubusercontent.com/80477575/111420104-9feac600-86b8-11eb-896c-621b65691890.png)
  * Mean Percentage Error
    * The best model here is the 2nd one (which is the stepwise model)\
    ![image](https://user-images.githubusercontent.com/80477575/111420128-a9742e00-86b8-11eb-9b7e-3cc14ebc5f66.png)
  * Mean Absolute Error
    * The best model here is the 2nd one (which is the stepwise model)\
    ![image](https://user-images.githubusercontent.com/80477575/111420149-b2fd9600-86b8-11eb-946b-a0a0ec318bdb.png)
  * Predicted value plots
    * The sgscatter plots also show that the first two models are better fits based on the tighter scatter of predicted and actual y values.\
    ![image](https://user-images.githubusercontent.com/80477575/111420166-b7c24a00-86b8-11eb-8e19-0f385a3431e9.png)






