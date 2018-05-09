#This should all be recognisable to you by now

#install.packages("class")
library(class)
library(ggplot2)

setwd("C:/Users/tknow/Desktop/datasets")

RawBCD <- read.table("BreastCancerData.data", sep = ',')    #read.table is being used due to it
                                                            #having the unusual .data extension

#In case the V1-32 labels aren't descriptive enough for you, you can use the VariablesNames
#file to label the data

names(RawBCD) <- c("ID","Result","Mean_Radius","Mean_Texture","Mean_Perimeter",
                   "Mean_Area","Mean_Smoothness","Mean_Compactness", "Mean_Concavity",
                   "Mean_ConcavePoints", "Mean_Symmetry","Mean_FractalDimension",
                   "SE_Radius","SE_Texture","SE_Perimeter","SE_Area","SE_Smoothness",
                   "SE_Compactness","SE_Concavity","SE_ConcavePoints","SE_Symmetry",
                   "SE_FractalDimension","Worst_Radius","Worst_Texture","Worst_Perimeter",
                   "Worst_Area","Worst_Smoothness","Worst_Compactness","Worst_Concavity",
                   "Worst_ConcavePoints","Worst_Symmetry","Worst_FractalDimension")

#Let's remove the ID Variable - R has an index built-in, so a second one is extraneous
#Besides, we don't want to feed ID in as a parameter to our KNN

BCD_NoID <- RawBCD[,-1]

#We also need a subset of the BCD data set without the Result column
#This allows it to be used for normalisation and validation purposes

BCD_NoResults <- BCD_NoID[,-1]

#There are many Feature Scaling functions defined in CRAN, but to learn the maths, it is
#good to built one yourself, like so:

FeatureScaling <- function(x) { ((x - min(x)) / (max(x) - min(x))) }
#This corresponds to the equation given in the slides

BCD_Normalised <- as.data.frame(lapply(BCD_NoResults, FeatureScaling))
#Now our data has been normalised according to our function

#This is a good time to split our data. Let's go for a 75:25 (ish) split.
BCD_Training <- BCD_Normalised[1:450,]  #Leave the value after the comma empty to
                                        #capture all columns

BCD_Test <- BCD_Normalised[451:569,]

#Finally, let's compute a k-Value to use with the classifier
#The rule of thumb is the square root of the number of observations
#trained with, so let's use that for now

K_Value <- floor(sqrt(length(BCD_Training[,1])))  #Result is floored, as k must be
                                                  #a whole number

#Now we can use the KNN Algorithm that comes with the 'class' package to classify our data
#This is done all at once, in a single function

BCD_Predictions <- knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1], k=K_Value)

#Now, let's view the performance of our KNN
#This is expressed in terms of {True Positives   False Positives}
#                              {False Negatives  True Negatives}

#First, subset the reference data into its own data frame

BCD_Reference <- BCD_NoID[451:569,1]

#Then, we can tabulate the two

table(BCD_Predictions,BCD_Reference)

#Further analysis of the results can give further insights into the suitability
#of the model, and of its parameters

#Type '?knn' into the console, and observe the various parameters
#You can adjust the parameters to empirically determine which k-Value and which
#geometry works best for this data set

#Also, explore the class package for similar models

####################################

#Below is the working example for if the trainees struggle to complete the
#assigned workbook tasks

big_error1 <-   table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=1),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=1),BCD_Reference)[2,1]

big_error2 <-   table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=2),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=2),BCD_Reference)[2,1]

big_error5 <-   table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=5),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=5),BCD_Reference)[2,1]

big_error10 <-  table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=10),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=10),BCD_Reference)[2,1]

big_error15 <-  table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=15),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=15),BCD_Reference)[2,1]

big_error20 <-  table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=20),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=20),BCD_Reference)[2,1]

big_error25 <-  table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=25),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=25),BCD_Reference)[2,1]

big_error30 <-  table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=30),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=30),BCD_Reference)[2,1]

big_error40 <-  table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=40),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=40),BCD_Reference)[2,1]

big_error50 <-  table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=50),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=50),BCD_Reference)[2,1]

big_errors <- c(big_error1,big_error2,big_error5,big_error10,
                big_error15,big_error20,big_error25,big_error30,
                big_error40,big_error50)

kValues <- c(1,2,5,10,15,20,25,30,40,50)

big_errors_df <- data.frame(kValues,big_errors)

names(big_errors_df) <- c("k-Value","Error Value")

ggplot(big_errors_df, aes(x = kValues, y = big_errors)) +   geom_point(data = big_errors_df, colour = big_errors, size = 3) +
                                                            geom_smooth(method = "loess",colour = "blue", size = 1) + 
                                                            ggtitle("Error vs k-Value for Breast Cancer Data") +
                                                            xlab("k-Values") +
                                                            ylab("Error") +
                                                            scale_colour_gradient(low = "yellow", high = "red") +
                                                            theme(axis.text.x=element_text(angle=-45, vjust=0.5)) +
                                                            theme(axis.text.y=element_text(angle=-45, hjust=-0.1, vjust=-0.5))

big_errors <- c()

kValues <- c()

for(i in c(1:100)) {
  
  next_error <-  table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=i),BCD_Reference)[1,2] +
                table(knn(BCD_Training,BCD_Test,BCD_NoID[1:450,1],k=i),BCD_Reference)[2,1]
  
  big_errors <- c(big_errors, next_error)
  
  kValues <- c(kValues, i)
}

big_errors_df <- data.frame(kValues,big_errors)

names(big_errors_df) <- c("k-Value","Error Value")

ggplot(big_errors_df, aes(x = kValues, y = big_errors)) +
  #geom_point() +
  geom_smooth(method = "loess",colour = "blue", size = 1) + 
  ggtitle("Error vs k-Value for Breast Cancer Data") +
  xlab("k-Values") +
  ylab("Error") +
  theme(axis.text.x=element_text(angle=-45, vjust=0.5)) +
  theme(axis.text.y=element_text(angle=-45, hjust=-0.1, vjust=-0.5)) +
  scale_colour_manual(values = c("red","blue"))

#BCD_Small <- read.table("BreastCancerData.data", sep = ',')[1:200,]

#write.csv(BCD_Small, "BCD_Small.data")
