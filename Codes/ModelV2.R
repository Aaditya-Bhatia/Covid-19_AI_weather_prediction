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

rf <- randomForest(new_cases ~ .,
                   data=train,
                   importance =TRUE,
                   proximity = TRUE)

# test_ = test
# test_$new_cases = NULL
# rf_p_test <- predict(rf, type="prob",newdata = test_)[,2]
# rf_pr_test <- prediction(rf_p_test, test$Label)
# r_auc_test <- performance(rf_pr_test, measure = "auc")@y.values[[1]] 
# print(r_auc_test)
# 
# # Accuracy
# p1 <- predict(rf, test_)
# confusionMatrix(p1, test$Label)

lab = c("MinTempMedian", "MaxTempMedian", "HumidityMedian", 
        "WindChillMedian", "TempMedian", "FeelsLikeMedian", 
        "HeatIndexMedian")
par(mfrow=c(1,1))
varImpPlot(rf, type=1, scale=F, labels = lab)
varImpPlot(rf, type=1, scale=F)

varImpPlot(rf.boston,n.var=nvar, sort = F,
           labels = rep("random variable name",5))

cor(df$new_cases, df$tempC, method = "pearson")
cor(df$new_cases, df$humidity, method = "pearson")

# fit <- glm(Label~.,data=df,family=binomial(), control = list(maxit = 50))

