# Neural Networks
Neural networks is a form of machine learning that tries to uncover underlying relationships in data by mimicking the human brain albeit at machine-capable levels. In this case, this assignment was to introduce us to neural networks and create our own in R.

# Overview
The goal of this project was to identify which variables might best predict people who will go delinquent on their loans. The questions are bolded and my answers (which are mostly graphs of the neural networks conducted) are in normal text.

The dataset can be found [here](http://bigblue.depaul.edu/jlee141/econdata/fannie_mae/Fannie_Mort_US_2017.csv).
My code can be found [here](Neural Networks Code.md)

**1. Estimate the following neural network models with different hidden layers**
  * hidden=c(5)\
  ![image](https://user-images.githubusercontent.com/80477575/111425405-21465680-86c1-11eb-9eaa-9329ac8c8b37.png)\
  Error: 876.335932	Steps: 93442
  ![image](https://user-images.githubusercontent.com/80477575/111425416-260b0a80-86c1-11eb-8689-93b01b4fb86c.png)\
  Error: 866.486453	Steps: 221227
  * hidden=c(5,2)
  ![image](https://user-images.githubusercontent.com/80477575/111425532-489d2380-86c1-11eb-90da-b06f288ae3cc.png)\
  Error: 861.84366	Steps: 219532\
  ![image](https://user-images.githubusercontent.com/80477575/111425553-50f55e80-86c1-11eb-8a4c-e504e78ed11c.png)
  * hidden=c(7,3)
  ![image](https://user-images.githubusercontent.com/80477575/111425590-62d70180-86c1-11eb-9b6c-21962dc36a70.png)\
  Error: 830.846066	Steps: 1536057
  ![image](https://user-images.githubusercontent.com/80477575/111425607-6a96a600-86c1-11eb-8fa9-20d7f9e0c635.png)
  * Your own choice of hidden layer that can beat the above models hidden=c(3)\
  ![image](https://user-images.githubusercontent.com/80477575/111425620-6ff3f080-86c1-11eb-883b-75fa60666681.png)
  

**2. Find the best performing model from 1), and answer the following questions. Suppose you setup a
rule that if a person’s predicted probability is higher than 30%, then you classified the person as a
possible case of delinquency. Create the confusion table and answer the following questions:**

   **i. What is the probability that the model correctly predicted the persons who were delinquent on mortgage loans?**\
  True positives / Total positives -- 14/(306+14)=0.04375 ⇒ 4.38%\
  **ii. What is the probability that the model correctly predicted the persons who were not delinquent on mortgage loans?**\
  True negatives / Total negatives -- 846/(846+34)=0.96136364 ⇒ 96.14%\
  **iii. What is the probability that the model makes false positives?**\
  False positive rate = False positives / (True negatives + False positives) -- 34/(846+34)=0.03863636 ⇒ 3.86%\
  **iv. What is the probability that the model makes false negatives?**\
  False negatives / (False negatives + True positives) -- 306/(306+14)=0.95625 ⇒ 95.625%\
  **v. What is the total accuracy of your neural network model?**\
  Total accuracy=(846+14)/(846+14+306+34)=0.71667 ⇒ 71.67%
  
