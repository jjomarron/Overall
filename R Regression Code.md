```r
#ECO 520 HW8

source("http://bigblue.depaul.edu/jlee141/econdata/R/func_lib.R")
gse <- read.csv("http://bigblue.depaul.edu/jlee141/econdata/fannie_mae/Fannie_Mort_IL_2007.csv")
str(gse)

indata <- subset(gse,select=-c(fstimebuyer,state,orgyear))
# Exclude unusual zip_3 
indata <- indata[indata$zip_3 != 800,]   
indata$zip_3 <- as.factor(indata$zip_3)
indata$delinq <- as.factor(indata$delinq)
str(indata)

# Split the data into train and test data
set.seed(44044277)
train_idx <- sample(nrow(indata),round(.8*nrow(indata)))
train <- indata[train_idx,]
test  <- indata[-train_idx,]
testy <- test$delinq

#Linear Probability Model#
lpm0 <- lm(delinq~ . , data=train)
summary(lpm0)
yhat0 <- predict (lpm0, newdata=test)
conf_table(yhat0,testy,"LPM")
auc_plot(yhat0, testy, "LPM")

lpm1 <- lm(delinq~ orig_rt+orig_amt+orig_trm+num_bo+dti+cscore_b, data=train)
summary(lpm1)
yhat1 <- predict (lm1, newdata=test)
conf_table(yhat1,testy,"LPM")
auc_plot(yhat1, testy, "LPM")

lpm2 <- step(lm(delinq~ . , data=train), direction="both")
summary(lpm2)
yhat2 <- predict (lm2, newdata=test)
conf_table(yhat2,testy,"LPM")
auc_plot(yhat2, testy, "LPM")

#Logistic model
logit0 <- glm(formula=delinq~ . ,data=train,
              family=binomial(link=logit))
summary(logit0)
loghat0 <- predict(logit0, newdata=test, type="response")
conf_table(loghat0,testy,"LPM")
auc_plot(loghat0, testy, "LOGIT")

logit1 <- glm(formula=delinq~ orig_rt+orig_amt+ orig_trm+ num_bo+ dti+ cscore_b,data=train,
              family=binomial(link=logit))
summary(logit1)
loghat1 <- predict(logit1, newdata=test, type="response")
conf_table(loghat1,testy,"LPM")
auc_plot(loghat1, testy, "LOGIT")

logit2 <- step(glm(formula=delinq~ . ,data=train,
                   family=binomial(link=logit)), direction="both")

summary(logit2)

loghat2 <- predict(logit2, newdata=test, type="response")
conf_table(loghat2,testy,"LPM")
auc_plot(loghat2, testy, "LOGIT")
               
#Random Forest Model
rf1<-randomForest(formula=delinq~.,data=train,mtry=5,ntree=500)
summary(rf1)
rfhat1<-predict(rf1,newdata=test,type="prob")
rfhat1<-rfhat1[,2]
conf_table(rfhat1,testy,"RANDOMFOREST")
auc_plot(rfhat1,testy,"RANDOMFOREST")
               
#find the best mtry
oob.values<-vector(length=12)
for(i in 1:12){
               temp.model <-randomForest(formula=delinq~.,data=train,mtry=i,ntree=500)
               oob.values[i]<-temp.model$err.rate[nrow(temp.model$err.rate),1]
}
cbind(1:12,oob.values)
               
#Found mtry=2

#find the best ntree
rf_tree<-randomForest(formula=delinq~.,data=train,mtry=2,ntree=1000)
Trees<-rep(1:nrow(rf_tree$err.rate))
Error.rate<-rf_tree$err.rate[,"OOB"]
plot(Trees,Error.rate,col="red")

#tree might be 100 or 350
rf2<-randomForest(formula=delinq~.,data=train,mtry=2,ntree=100)
summary(rf2)
rfhat2<-predict(rf2,newdata=test,type="prob")
rfhat2<-rfhat2[,2]
conf_table(rfhat2,testy,"RANDOMFOREST")
auc_plot(rfhat2,testy,"RANDOMFOREST")

rf3<-randomForest(formula=delinq~.,data=train,mtry=2,ntree=450)
summary(rf3)
rfhat3<-predict(rf3,newdata=test,type="prob")
rfhat3<-rfhat3[,2]
conf_table(rfhat3,testy,"RANDOMFOREST")
auc_plot(rfhat3,testy,"RANDOMFOREST")

par(mfrow=c(3,3))
auc_plot(yhat0,testy,"LPM all")
auc_plot(yhat1,testy,"LPM specified")
auc_plot(yhat2,testy,"LPM stepwise")
auc_plot(loghat0,testy,"Logistic Regression all")
auc_plot(loghat1,testy,"Logistic Regression specified")
auc_plot(loghat2,testy,"Logistic Regression stepwise")
auc_plot(rfhat1,testy,"RANDOMFOREST mtry=5 ntree=1000")
auc_plot(rfhat2,testy,"RANDOMFOREST mtry=3 ntree=100")
auc_plot(rfhat3,testy,"RANDOMFOREST mtry=3 ntree=450")
par(mfrow=c(1,1))

#final decision
dec_logit1<-ifelse(loghat0>.3,1,0)
table(testy,dec_logit1)


#save the best algorithm
saveRDS(loghat0,file="C:/Users/Jack/Documents/School/Business Analytics.520/loghat2,hw8_jackjomarron.rds")
```
