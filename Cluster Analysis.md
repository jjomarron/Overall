# Cluster Analysis

This page is sharing a homework assignment I completed in my Master's program where I conducted a cluster analysis to discern logical groups in Big Data. I really enjoyed learning about the different clustering methods and plan on utilizing this in my future data analysis to help better extract meaningful conclusions from large datasets.

## Overview

This assignment was split into 2 parts. Both sections ask to perform the same tasks except across different sections. The first section is based on Customers and the second is based on item purchased. Questions are bolded while my answers can be found in normal text.

The original dataset can be found [here](http://bigblue.depaul.edu/jlee141/econdata/eco520/online_retail.csv).
My code is available [here](Cluster Analysis Code.md).

## First Part: Customer Summary--Three Variable Clustering Analysis (Vars = Freq., Rec., Mone.)
**1. Potential outlier issues or problem with the data (remove only extreme outliers if necessary)**
    
   * Frequency—I have decided to drop one outlier based on the Frequency variable analysis. While there are a fair amount of observations that are outside the 99th percentile, they are plausible (high volume buyers). The 4967 is an extreme outlier which would skew the data heavily, so I decided to drop it.\
   ![image](https://user-images.githubusercontent.com/80477575/111412204-fef50e80-86a9-11eb-9064-e0a3e9a9fc1b.png)
   * Recency—I have decided to not drop any outliers based on Recency variable analysis. The maximum and minimum values are not outside far from the 5-95% range and there are a high number of observations for all values.\
   ![image](https://user-images.githubusercontent.com/80477575/111412236-0f0cee00-86aa-11eb-8a31-3ad14b126020.png)
   * Monetary—After going back and forth, I decided to not drop any observations based on Monetary variable analysis. While there are not a lot of observations for the higher values, the higher values are not far outside of the range so I decided to keep them.\
   ![image](https://user-images.githubusercontent.com/80477575/111412300-2ba92600-86aa-11eb-8a79-bc92d148242e.png)\
**2. Show the best number of clusters using various settings of clusters**
   * The best number of clusters is 3. I based this on the R2 analysis as well as the elbow method.\
   ![image](https://user-images.githubusercontent.com/80477575/111412367-50050280-86aa-11eb-87e9-ff5213604383.png)\
   ![image](https://user-images.githubusercontent.com/80477575/111412383-54312000-86aa-11eb-8c8d-a519b62e5650.png)\
**3. Conduct one hierarchical Model and one K-Means Model and compare the differences**
   * I did a Ward Clustering Procedure for my hierarchical model and conducted a K-means procedure as well. There were slight differences in how observations were clustered but overall, they had very similar mean values as listed below.\
   ![image](https://user-images.githubusercontent.com/80477575/111413011-737c7d00-86ab-11eb-818a-5a77c3d5cb1d.png)\
**4. Use graphs to illustrate the different clusters**
   ![image](https://user-images.githubusercontent.com/80477575/111413043-83945c80-86ab-11eb-885a-18716574965c.png)\
   ![image](https://user-images.githubusercontent.com/80477575/111413052-85f6b680-86ab-11eb-856f-bf3f64e9c9b8.png)\
   ![image](https://user-images.githubusercontent.com/80477575/111413064-8abb6a80-86ab-11eb-9016-0ffe774d3c71.png)\
**5. Name each group using the summary statistics by cluster**
   * The 1st cluster is a group of items which on average were bought 190 days ago, 2.6 times and a log(totalsale) value of 3.3.
   * The 2nd cluster is a group of items which on average were bought 331 days ago, 1.86 times, and a log(totalsale) value of 2.9 (lower performing items).
   * The 3rd cluster is a group of items which on average were bought 59 days ago, 5.58 times (a popular group item), and with a log(totalsale) value of 3.84 (higher performing items).\
   ![image](https://user-images.githubusercontent.com/80477575/111413107-a4f54880-86ab-11eb-8128-dac27a67c44e.png)

## Second Part: Item Summary--Three Variable Clustering Analysis (Vars = Freq., Rec., Mone.)
**1. Potential outlier issues or problem with the data (remove only extreme outliers if necessary)**
   * After analyzing each variable I decided to not remove any observations because there were no extreme outliers. I used the proc univariate and proc sgplot codes to determine this.
   * Frequency\
   ![image](https://user-images.githubusercontent.com/80477575/111413340-1208de00-86ac-11eb-82bb-d48d099d11d3.png)
   * Recency\
   ![image](https://user-images.githubusercontent.com/80477575/111413354-1b924600-86ac-11eb-8565-354d46ea45c9.png)\
   * Monetary\
   ![image](https://user-images.githubusercontent.com/80477575/111413375-23ea8100-86ac-11eb-8156-c54637788b73.png)\
**2. Show the best number of clusters using various settings of clusters**
   * The best number of clusters is 4 based on an R2 analysis as well as the elbow method. While 5 is also for consideration, the magnitude of jumps (double digits to single digits changes between 4 and 5 so I decided on 4 clusters.\
   ![image](https://user-images.githubusercontent.com/80477575/111413412-382e7e00-86ac-11eb-8e34-691968030a4d.png)\
**3. Conduct one hierarchical Model and one K-Means Model and compare the differences**
   * I conducted a clustering based on a hierarchical model and a K-Means model. The results are listed below in the following 2 charts. Overall, the numbers were not very similar in their clustering which suggests that my choosing of 4 may have been incorrect.\
   ![image](https://user-images.githubusercontent.com/80477575/111413449-48465d80-86ac-11eb-8767-ab61dd045083.png)\
**4. Use graphs to illustrate the different clusters**
   ![image](https://user-images.githubusercontent.com/80477575/111413512-62803b80-86ac-11eb-8951-c1a17edbf993.png)\
   ![image](https://user-images.githubusercontent.com/80477575/111413531-69a74980-86ac-11eb-9bda-6e3b7022fe31.png)\
   ![image](https://user-images.githubusercontent.com/80477575/111413563-76c43880-86ac-11eb-99eb-88874a6a1220.png)\
**5. Name each group using the summary statistics by cluster**
   * The 1st cluster was a group that was bought 92 days ago, 27 times and with a log(totalsale) value of 4.9.\
   * The 2nd cluster was a group that was bought 288 days ago, 7 times and with a log(totalsale) value of 3.5.\
   * The 3rd cluster was a group that was bought 178 days ago, 199 times and with a log(totalsale) value of 8.3.\
   * The 4th cluster was a group that was bought 197 days ago, 39 times and with a log(totalsale) value of 5.6.
   ![image](https://user-images.githubusercontent.com/80477575/111413620-95c2ca80-86ac-11eb-81a7-f6010cda1950.png)





 
