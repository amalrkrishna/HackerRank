library(utils)
library(data.table)

train <- fread('training_dataset.csv')
test <- fread('test_dataset.csv')

target <- train$opened
target[target=='false'] <- 0
target[target=='true'] <- 1
target <- as.numeric(target)
train$opened<-target
test$opened <- "NA"

train[,c("click_time","open_time","clicked","unsubscribe_time","unsubscribed"):=NULL]
total<- rbind(train, test)

Mode <- function(x) {
  ux <- x[!is.na(x)]
  ux[which.max(tabulate(match(x, ux)))]
}

Mean <- function(x) {
  if (all(is.na(x))){
    return(NA)
  }
  else{
    x<-as.numeric(x)
    ux <- x[!is.na(x)]
    return(mean(ux))
  }
}

total[ ,c("group_by_id_mean"):= Mean(opened), by = c("user_id")]
train <- total[1:nrow(train), ]
test <- total[-c(1:nrow(train)), ]


print(train)

train$hacker_confirmation <- as.integer(as.logical(train$hacker_confirmation))
test$hacker_confirmation <- as.integer(as.logical(test$hacker_confirmation))
#print(train$hacker_confirmation)
#print(train$hacker_confirmation)

library(randomForest)
print("MODEL FIT")
modelFit <- randomForest(as.factor(opened) ~ group_by_id_mean + sent_time + last_online + hacker_created_at + contest_login_count + contest_login_count_1_days + contest_login_count_7_days + contest_login_count_30_days + contest_participation_count + contest_participation_count_1_days + contest_participation_count_7_days + contest_participation_count_30_days + submissions_count_contest + hacker_confirmation,
                         data=train, 
                         ntree=10, 
                         mtry=5, 
                         importance=TRUE, na.action=na.roughfix)
print("MODEL FIT DONE")
model_pred <- predict(modelFit, test)
print("WRITING TO CSV")
write.csv(model_pred, file = "predR.csv")
