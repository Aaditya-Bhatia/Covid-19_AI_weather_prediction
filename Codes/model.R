rm(list=ls())
library(caret)
library(randomForest)
library(dplyr)
library(AUC)
library(ROCR)
library(Hmisc)




df = read.csv('/Users/aadityabhatia/Projects/Coronavirus/corona_model_features.csv')
df[is.na(df)] <- 0
df$Label = as.factor(df$Label)

print(colnames(df))
# drop <- c("date" ,"total_cases", "total_deaths", "incubationDateStart", "incubationDateEnd", "new_deaths", "location", "new_cases")
# df = df[,!(names(df) %in% drop)]

keep <- c("humidity", "tempC", "new_cases")
df = df[,(names(df) %in% keep)]



# correlation test
df_corrTest = sapply(df, as.numeric)
par(mfrow=c(1,1))
plot(varclus(df_corrTest, similarity="spearman"), type='n')
abline (h = 1 - 0.7 , col=" grey ", lty =2)


set.seed(311)
ind <- sample(2, nrow(df), replace = TRUE, prob = c(0.7, 0.3))
train <- df[ind ==1 ,]
test <- df[ind ==2 ,]



mseV = list()
impV = list()
for(i in 1:20){
  train_index<-sample(seq(1:nrow(df)),size=nrow(df),replace=T)
  test_index<-seq(1:nrow(df))[-train_index]
  train <- df[train_index ,]
  test <- df[test_index ,]
  
  rf <- randomForest(new_cases ~ .,
                     data=train,
                     importance =TRUE,
                     proximity = TRUE)
 impV[[i]] <- varImp(rf, type=1, scale=F, labels = lab)[[1]]
 mseV[[i]] <- summary(rf)[[4]]
}

lab = c("Humidity", "Temprature")
par(mfrow=c(1,1))
varImpPlot(rf, type=1, scale=F, labels = lab)

cor(df$new_cases, df$tempC, method = "pearson")
cor(df$new_cases, df$humidity, method = "pearson")
