library(magrittr) #to use %>% notation
library(tidyverse)
library(dplyr)
library(ggplot2)

#get csv paths of test folder
csv_paths_test <- list.files(path="./data/test",
           recursive=TRUE,
           pattern="^Joule.*\\.csv",
           full.names=TRUE)

#get data from csv files
test_data <- csv_paths_test %>%
  lapply(read_csv) %>%
  bind_rows

#add new factor to data which are taken from the path (memoized an non_memoized)
test_data['experiment'] <-csv_paths_test %>%
  strsplit('/', fixed=TRUE) %>%
  rapply(nth, n=4) %>%
  factor()

#battery_data <- ...
#cpu_data <- ...
#memory_data < ...

#-Check assumptions
#--Assumption 1: Are the two samples independents? Yes
#--Assumption 2: Normal distribution in both groups?
par(mfrow=c(2,2))

check_normality <- function(data) {
  plot(density(data))
  qqnorm(data)
  shapiro.test(data)
}
#Shapiro-Wilk normality test
test_data %>%
  filter(experiment == 'memoized') %>%
  select(Joule_calculated) %>%
  unlist() %>%
  check_normality #p-value should be greater than 0.05

test_data %>%
  filter(experiment == 'non_memoized') %>%
  select(Joule_calculated) %>%
  unlist() %>%
  check_normality #p-value should be greater than 0.05


#--Assumption 3: Homogeneity in variances?
res.ftest <- var.test(Joule_calculated ~ experiment, data = test_data)
res.ftest #p-value should be greater than 0.05


#-T-test is used to compare two means
res.ttest <- t.test(Joule_calculated ~ experiment, data = test_data)
res.ttest

#effect size?
require(effsize)
cohen.d(Joule_calculated ~ experiment, data = test_data)

ggplot(test_data, aes(y=Joule_calculated, x=experiment, fill=experiment)) + 
    #limits are possible
    #ylim(50, 55) +
    #add labels
    xlab("Experiment") + ylab("Joule calculated") + 
    #interesting looking shape represents the distribution
    geom_violin(trim=FALSE, alpha=1, show.legend = FALSE) +
    #add boxplots
    geom_boxplot(show.legend = FALSE) +
    #add points
    stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)
 
ggplot(test_data, aes(y=Joule_calculated, x=experiment, fill=experiment)) + 
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

#qqplot with beautiful line
ggplot(test_data, aes(sample=Joule_calculated))+stat_qq(color="blue")+geom_qq_line(color="black")

##density plot
ggplot(test_data, aes(x=Joule_calculated)) + 
  geom_density()
