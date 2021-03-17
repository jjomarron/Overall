```r
#R code in bigblue: 

gse <- read.csv("http://bigblue.depaul.edu/jlee141/econdata/fannie_mae/Fannie_Mort_US_2017.csv")
str(gse)

indata <- subset(gse,select=-c(fstimebuyer,state,orgyear,zip_3,relo_flg))
str(indata)

# Convert any factor variable to numeric variable 
# if necessary, you can create multiple dummy variables for multiple categories
# Simple conversion of a factor variable using ifelse
indata$purpose  <- ifelse(indata$purpose == "P",1,0)
indata$occ_stat <- ifelse(indata$occ_stat == "P",1,0)
str(indata)

# Neural Network Analysis requires to normalize the data 
zindata <- min_max_nor(indata)

# Split the data into train and test data
set.seed(44044277)
train_idx <- sample(nrow(indata),round(.8*nrow(indata)))
ztrain    <- zindata[train_idx,]
ztest     <- zindata[-train_idx,]
testy     <- ztest$delinq

# The dependent variable needs to be a factor to be a classification 
ztrain$delinq    <- as.factor(ztest$delinq)

# Now estimate the neural network models and make predictions
library(neuralnet)

# Your code to estimate the neural network models from here
# Be patience since the neural network needs much longer computational time
# Your grade will be also based on the performance of the model (ROC and AUC)

nnet1a <- neuralnet(delinq~., data=ztrain, hidden=c(5),stepmax=1000000)
pred1a <- predict(nnet1a,ztest)
pred1a <- pred1a[,2]
head(pred1a)

nnet1b <- neuralnet(delinq~., data=ztrain, hidden=c(5,2),stepmax=1000000)
pred1b <- predict(nnet1b,ztest)
pred1b <- pred1b[,2]
head(pred1b)

nnet1c <- neuralnet(delinq~., data=ztrain, hidden=c(7,3),stepmax=1000000)
pred1c <- predict(nnet1c,ztest)
pred1c <- pred1c[,2]
head(pred1c)

nnet1d <- neuralnet(delinq~., data=ztrain, hidden=c(4,3,2,1),stepmax=1000000)
pred1d <- predict(nnet1d,ztest)
pred1d <- pred1d[,2]
head(pred1d)

nnet1e <- neuralnet(delinq~., data=ztrain, hidden=c(6,3,2,2),stepmax=1000000)
pred1e <- predict(nnet1e,ztest)
pred1e <- pred1e[,2]
head(pred1e)

nnet1f <- neuralnet(delinq~., data=ztrain, hidden=c(8,2,2),stepmax=1000000)
pred1f <- predict(nnet1f,ztest)
pred1f <- pred1f[,2]
head(pred1f)

nnet1g <- neuralnet(delinq~., data=ztrain, hidden=c(5,5,2,2),stepmax=1000000)
pred1g <- predict(nnet1g,ztest)
pred1g <- pred1d[,2]
head(pred1g)

nnet1h <- neuralnet(delinq~., data=ztrain, hidden=c(6,4,1,2),stepmax=1000000)
pred1h <- predict(nnet1d,ztest)
pred1h <- pred1h[,2]
head(pred1h)

par(mfrow=c(3,3))
auc_plot(pred1a,testy,"NNA")
auc_plot(pred1b,testy,"NNA")
auc_plot(pred1c,testy,"NNA")
auc_plot(pred1d,testy,"NNA")
auc_plot(pred1e,testy,"NNA")
auc_plot(pred1f,testy,"NNA")
auc_plot(pred1g,testy,"NNA")
auc_plot(pred1h,testy,"NNA")
par(mfrow=c(1,1)

conf_table(pred1h,testy,"NNA") # Use 30% probability as the cut off

dec_NN <- if else(pred1h > 0.3, 1, 0)
table(testy,dec_NN)

```
