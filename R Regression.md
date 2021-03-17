# Regression Analysis
This code contains various different regression analyses conducted in the R programming language. This was a homework assignment that took the regression analysis skills I had developed in my other classes and applied them to the R language. This code contains Linear Probability Models, Logistic Regression Models, and Random Forest Models. I also calculate area under the curve and use a confusion matrix to determine the best model.

## Overview
This assignment seeks to find the best performing model to determine the likelihood if an individual will default on a Fannie Mae mortgage payment. Questions are bolded and my answers are in bulleted, normal text.

The dataset can be found [here](http://bigblue.depaul.edu/jlee141/econdata/fannie_mae/Fannie_Mort_IL_2007.csv).
My code can be seen [here](R Regression Code.md).

## Fannie Mae Mortgage Performance
**1. Set 80% as training set and 20% as test set** 
  ```ruby set.seed(44044277)
train_idx <- sample(nrow(indata),round(.8*nrow(indata)))
train <- indata[train_idx,]
test  <- indata[-train_idx,]
testy <- test$delinq
```
**2. Use the training data set to estimate all models and compare the performance using test data
by the Receiver Operating Characteristic (ROC) and Area Under Curve (AUC)**\
![image](https://user-images.githubusercontent.com/80477575/111421741-8139fe80-86bb-11eb-85e5-c667da5faea8.png)\
**3. Find the best suitable threshold probability, and explain the performance using confusion
matrix.**
  * The best suitable threshold probability is 0.3. I determined this by looking at the ROC/AUC graph as well as the confusion matrix. 0.3 provides a good balance of an effective detection rate (0.6174) and a lower false positive rate (0.245). The confusion matrix substantiates what the initial table shows that 0.3 is a satisfactory threshold probability for the “Logit all” model I selected.\
  ![image](https://user-images.githubusercontent.com/80477575/111421751-872fdf80-86bb-11eb-9038-1fced9df62af.png)\
  ![image](https://user-images.githubusercontent.com/80477575/111421762-8b5bfd00-86bb-11eb-8494-e26676466465.png)\
  
**4. Save the best performing algorithm**
```ruby
saveRDS(loghat0,file="C:/Users/Jack/Documents/School/Business Analytics.520/loghat2,hw8_jackjomarron.rds")
```






