library(magrittr) #to use %>% notation
library(tidyverse)
library(dplyr)
library(ggplot2)
library(car)


#get csv paths of test folder
#csv_paths_test <- list.files(path="./data/test",
#           recursive=TRUE,
#           pattern="^Joule.*\\.csv",
#           full.names=TRUE)

aggr_memoized_file <- 'data/memoized/Aggregated_Results_Trepn.csv'
aggr_nonmemoized_file <- 'data/nonmemoized/Aggregated_Results_Trepn.csv'

m <- read_csv(aggr_memoized_file) %>%
  #filter(!grepl('test', subject)) %>%
  mutate(experiment="memoized")
n <- read_csv(aggr_nonmemoized_file) %>%
  #filter(!grepl('test', subject)) %>%
  mutate(experiment="nonmemoized")

new_column_names <- c("device", "subject", "browser", "bp_delta_uw", "bp_raw_uw", "cpu_load", "memory_usage_kb", "experiment" ) #bp = battery power
colnames(m) <- new_column_names
colnames(n) <- new_column_names

#Experimenting with data transformations
combined_data <- bind_rows(m,n) %>%
  mutate(bp_delta_uw_log = log(bp_delta_uw),
         bp_delta_uw_sqrt = sqrt(bp_delta_uw),
         bp_delta_uw_reciprocal = 1/bp_delta_uw,
         cpu_load_log = log(cpu_load),
         cpu_load_sqrt = sqrt(cpu_load),
         cpu_load_reciprocal = 1/cpu_load,
         memory_usage_kb_log = log(memory_usage_kb),
         memory_usage_kb_sqrt = sqrt(memory_usage_kb),
         memory_usage_kb_reciprocal = 1/memory_usage_kb,)

combined_data

#get data from csv files
#test_data <- csv_paths_test %>%
#  lapply(read_csv) %>%
#  bind_rows

#add new factor to data which are taken from the path (memoized an non_memoized)
#test_data['experiment'] <-csv_paths_test %>%
#  strsplit('/', fixed=TRUE) %>%
#  rapply(nth, n=4) %>%
#  factor()

#-Check assumptions
#--Assumption 1: Are the two samples independents? Yes

#--Assumption 2: Normal distribution in both groups?
par(mfrow=c(3,2))

check_normality <- function(data) {
  plot(density(data))
  qqnorm(data)
  hist(data)
  shapiro.test(data)
}
#Shapiro-Wilk normality test. The p-value should be greater than 0.05, then it is a normal distribution.
combined_data %>%
  filter(experiment == 'memoized') %>%
  select(bp_delta_uw) %>%
  unlist() %>%
  check_normality()

combined_data %>%
  filter(experiment == 'nonmemoized') %>%
  select(bp_delta_uw) %>%
  unlist() %>%
  check_normality 

#Experimenting with data transformations
combined_data %>%
  filter(experiment == 'memoized') %>%
  select(bp_delta_uw_log) %>%
  unlist() %>%
  check_normality 

combined_data %>%
  filter(experiment == 'nonmemoized') %>%
  select(bp_delta_uw_log) %>%
  unlist() %>%
  check_normality 

combined_data %>%
  filter(experiment == 'memoized') %>%
  select(bp_delta_uw_sqrt) %>%
  unlist() %>%
  check_normality 

combined_data %>%
  filter(experiment == 'nonmemoized') %>%
  select(bp_delta_uw_sqrt) %>%
  unlist() %>%
  check_normality 

combined_data %>%
  filter(experiment == 'memoized') %>%
  select(bp_delta_uw_reciprocal) %>%
  unlist() %>%
  check_normality 

combined_data %>%
  filter(experiment == 'nonmemoized') %>%
  select(bp_delta_uw_reciprocal) %>%
  unlist() %>%
  check_normality 

combined_data %>%
  filter(experiment == 'memoized') %>%
  select(cpu_load) %>%
  unlist() %>%
  check_normality 

combined_data %>%
  filter(experiment == 'nonmemoized') %>%
  select(cpu_load) %>%
  unlist() %>%
  check_normality 

combined_data %>%
  filter(experiment == 'memoized') %>%
  select(memory_usage_kb) %>%
  unlist() %>%
  check_normality 

combined_data %>%
  filter(experiment == 'nonmemoized') %>%
  select(memory_usage_kb) %>%
  unlist() %>%
  check_normality 

# mann whitney tests
wilcox.test(n$bp_delta_uw, m$bp_delta_uw)
wilcox.test(n$memory_usage_kb, m$memory_usage_kb)
wilcox.test(n$cpu_load, m$cpu_load)

# different syntax same result
wilcox.test(combined_data$cpu_load~combined_data$experiment, data = combined_data, exact = FALSE)

#--Assumption 3: Homogeneity in variances?
res.ftest <- var.test(bp_delta_uw ~ experiment, data = combined_data)
res.ftest #p-value should be greater than 0.05

res.ftest <- var.test(cpu_load ~ experiment, data = combined_data)
res.ftest #p-value should be greater than 0.05

res.ftest <- var.test(memory_usage_kb ~ experiment, data = combined_data)
res.ftest #p-value should be greater than 0.05

#-T-test is used to compare two means. var.equal is set to TRUE when the variance is equal.
res.ttest <- t.test(bp_delta_uw ~ experiment, data = combined_data, var.equal=TRUE)
res.ttest

res.ttest <- t.test(cpu_load ~ experiment, data = combined_data, var.equal=TRUE)
res.ttest

res.ttest <- t.test(memory_usage_kb ~ experiment, data = combined_data, var.equal=TRUE)
res.ttest

#effect size to see how big the effect is when the t.test resulting p-value is below 0.05
require(effsize)
cohen.d(bp_delta_uw ~ experiment, data = combined_data)
cohen.d(cpu_load ~ experiment, data = combined_data)
cohen.d(memory_usage_kb ~ experiment, data = combined_data)


# VISUALIZATION
# FOR BP_DELTA_UW - copy this for the other variables
ggplot(combined_data, aes(y=bp_delta_uw, x=experiment, fill=experiment)) + 
  #limits are possible
  #ylim(50, 55) +
  #add labels
  xlab("Experiment") + ylab("Battery Power Delta in uW") + 
  #interesting looking shape represents the distribution
  geom_violin(trim=FALSE, alpha=1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

#battery
ggplot(combined_data, aes(y=bp_delta_uw, x=experiment, fill=experiment)) + 
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

#cpu_load
ggplot(combined_data, aes(y=cpu_load, x=experiment, fill=experiment)) + 
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

#memory_usage_kb
ggplot(combined_data, aes(y=memory_usage_kb, x=experiment, fill=experiment)) + 
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

#qqplot with beautiful line
ggplot(combined_data, aes(sample=bp_delta_uw))+stat_qq(color="blue")+geom_qq_line(color="black")

##density plot
ggplot(combined_data, aes(x=bp_delta_uw)) + 
  geom_density()

