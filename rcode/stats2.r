library(magrittr) #to use %>% notation
library(tidyverse)
library(dplyr)
library(plyr)
library(ggplot2)
library(car)
library(gridExtra)


#get csv paths of test folder
#csv_paths_test <- list.files(path="./data/test",
#           recursive=TRUE,
#           pattern="^Joule.*\\.csv",
#           full.names=TRUE)

aggr_memoized_file <- 'data/memoized/Aggregated_Results_Trepn.csv'
aggr_nonmemoized_file <- 'data/nonmemoized/Aggregated_Results_Trepn.csv'

m <- read_csv(aggr_memoized_file) %>%
  filter(grepl('test', subject)) %>%
  mutate(experiment="memoized", 
         parameters="memoized-noparams",
         experiment_noparams="memoized-noparams"
         )
n <- read_csv(aggr_nonmemoized_file) %>%
  filter(grepl('test', subject)) %>%
  mutate(experiment="nonmemoized",
         parameters="nonmemoized-noparams", 
         experiment_noparams="nonmemoized-noparams"
         )

new_column_names <- c("device", "subject", "browser", "bp_delta_uw", "bp_raw_uw", "cpu_load", "memory_usage_kb", "experiment", "parameters","experiment_noparams" ) #bp = battery power
colnames(m) <- new_column_names
colnames(n) <- new_column_names

m1 <- read_csv(aggr_memoized_file) %>%
  filter(!grepl('test', subject)) %>%
  mutate(experiment="memoized", 
         parameters="memoized-multipleparams",
         experiment_params="memoized-params")
n1 <- read_csv(aggr_nonmemoized_file) %>%
  filter(!grepl('test', subject)) %>%
  mutate(experiment="nonmemoized", 
         parameters="nonmemoized-multipleparams",
         experiment_params="nonmemoized-params")

new_column_names <- c("device", "subject", "browser", "bp_delta_uw", "bp_raw_uw", "cpu_load", "memory_usage_kb", "experiment", "parameters","experiment_params" ) #bp = battery power
colnames(m1) <- new_column_names
colnames(n1) <- new_column_names

#Experimenting with data transformations
combined_data_noparams <- bind_rows(m,m1) %>%
  mutate(memory_usage_mb = memory_usage_kb/1000,
         bp_delta_joule = (bp_delta_uw/1000000)*600,
         bp_delta_uw_log = log(bp_delta_uw),
         bp_delta_uw_sqrt = sqrt(bp_delta_uw),
         bp_delta_uw_reciprocal = 1/bp_delta_uw,
         cpu_load_log = log(cpu_load),
         cpu_load_sqrt = sqrt(cpu_load),
         cpu_load_reciprocal = 1/cpu_load,
         memory_usage_kb_log = log(memory_usage_kb),
         memory_usage_kb_sqrt = sqrt(memory_usage_kb),
         memory_usage_kb_reciprocal = 1/memory_usage_kb,)

#Experimenting with data transformations
combined_data_params <- bind_rows(n,n1) %>%
  mutate(memory_usage_mb = memory_usage_kb/1000,
         bp_delta_joule = (bp_delta_uw/1000000)*600,
         bp_delta_uw_log = log(bp_delta_uw),
         bp_delta_uw_sqrt = sqrt(bp_delta_uw),
         bp_delta_uw_reciprocal = 1/bp_delta_uw,
         cpu_load_log = log(cpu_load),
         cpu_load_sqrt = sqrt(cpu_load),
         cpu_load_reciprocal = 1/cpu_load,
         memory_usage_kb_log = log(memory_usage_kb),
         memory_usage_kb_sqrt = sqrt(memory_usage_kb),
         memory_usage_kb_reciprocal = 1/memory_usage_kb,)


combined_data <- bind_rows(combined_data_noparams,combined_data_params)

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
par(mfrow=c(2,2))

check_normality <- function(data) {
  plot(density(data))
  qqnorm(data)
  hist(data)
  shapiro.test(data)
}
#Shapiro-Wilk normality test. The p-value should be greater than 0.05, then it is a normal distribution.
a <- combined_data %>%
  filter(experiment == 'memoized') %>%
  select(bp_delta_joule) 
  #check_normality()
  

#$############################# 
mu <- ddply(combined_data, "experiment", summarise, grp.mean=mean(bp_delta_joule))
to_string <- as_labeller(c(`memoized` = "Memoized", `nonmemoized` = "Non-Memoized"))
p<-ggplot(combined_data, aes(x=bp_delta_joule))+ labs(title="Density Curves: Battery Power in Joule",x="Battery Power (Joule)", y = "Density") +
  geom_density(fill="gray")+facet_grid(experiment ~ ., labeller = to_string)

# Add mean lines
plot1 <- p+geom_vline(data=mu, aes(xintercept=grp.mean, color="red"),
             linetype="dashed")+theme(legend.position="none")

plot2 <- ggplot(combined_data, aes(sample=bp_delta_joule)) +labs(title="Q-Q Plots: Battery Power in Joule",x="Theoretical Quantiles", y = "Sample Quantiles") +
  stat_qq() +stat_qq_line(color="red") +facet_grid(experiment ~ ., labeller = to_string)

grid.arrange(plot1, plot2, ncol=2, nrow = 1)

#$#############################
mu <- ddply(combined_data, "experiment", summarise, grp.mean=mean(cpu_load))
to_string <- as_labeller(c(`memoized` = "Memoized", `nonmemoized` = "Non-Memoized"))
p<-ggplot(combined_data, aes(x=cpu_load))+ labs(title="Density Curves: CPU load in Percentage",x="CPU load (%)", y = "Density") +
  geom_density(fill="gray")+facet_grid(experiment ~ ., labeller = to_string)

# Add mean lines
plot1 <- p+geom_vline(data=mu, aes(xintercept=grp.mean, color="red"),
                      linetype="dashed")+theme(legend.position="none")

plot2 <- ggplot(combined_data, aes(sample=cpu_load)) +labs(title="Q-Q Plots: CPU load in Percentage",x="Theoretical Quantiles", y = "Sample Quantiles") +
  stat_qq() +stat_qq_line(color="red") +facet_grid(experiment ~ ., labeller = to_string)

grid.arrange(plot1, plot2, ncol=2, nrow = 1)

#$#############################
mu <- ddply(combined_data, "experiment", summarise, grp.mean=mean(memory_usage_mb))
to_string <- as_labeller(c(`memoized` = "Memoized", `nonmemoized` = "Non-Memoized"))
p<-ggplot(combined_data, aes(x=memory_usage_mb))+ labs(title="Density Curves: Memory Usage in mb",x="Memory Usage (mb)", y = "Density") +
  geom_density(fill="gray")+facet_grid(experiment ~ ., labeller = to_string)

# Add mean lines
plot1 <- p+geom_vline(data=mu, aes(xintercept=grp.mean, color="red"),
                      linetype="dashed")+theme(legend.position="none")

plot2 <- ggplot(combined_data, aes(sample=memory_usage_mb)) +labs(title="Q-Q Plots: Memory Usage in mb",x="Theoretical Quantiles", y = "Sample Quantiles") +
  stat_qq() +stat_qq_line(color="red") +facet_grid(experiment ~ ., labeller = to_string)

grid.arrange(plot1, plot2, ncol=2, nrow = 1)





#Experimenting with data transformations
# combined_data %>%
#   filter(experiment == 'memoized') %>%
#   select(bp_delta_uw_log) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'nonmemoized') %>%
#   select(bp_delta_uw_log) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'memoized') %>%
#   select(bp_delta_uw_sqrt) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'nonmemoized') %>%
#   select(bp_delta_uw_sqrt) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'memoized') %>%
#   select(bp_delta_uw_reciprocal) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'nonmemoized') %>%
#   select(bp_delta_uw_reciprocal) %>%
#   unlist() %>%
#   check_normality 

#CPU LOAD
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

#Experimenting with data transformations
# combined_data %>%
#   filter(experiment == 'memoized') %>%
#   select(cpu_load_log) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'nonmemoized') %>%
#   select(cpu_load_log) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'memoized') %>%
#   select(cpu_load_sqrt) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'nonmemoized') %>%
#   select(cpu_load_sqrt) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'memoized') %>%
#   select(cpu_load_reciprocal) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'nonmemoized') %>%
#   select(cpu_load_reciprocal) %>%
#   unlist() %>%
#   check_normality 

#MEMORY USGE
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

#Experimenting with data transformations
# combined_data %>%
#   filter(experiment == 'memoized') %>%
#   select(memory_usage_kb_log) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'nonmemoized') %>%
#   select(memory_usage_kb_log) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'memoized') %>%
#   select(memory_usage_kb_sqrt) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'nonmemoized') %>%
#   select(memory_usage_kb_sqrt) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'memoized') %>%
#   select(memory_usage_kb_reciprocal) %>%
#   unlist() %>%
#   check_normality 
# 
# combined_data %>%
#   filter(experiment == 'nonmemoized') %>%
#   select(memory_usage_kb_reciprocal) %>%
#   unlist() %>%
#   check_normality 

# mann whitney tests
wilcox.test(n$bp_delta_uw, m$bp_delta_uw)
wilcox.test(n$memory_usage_kb, m$memory_usage_kb)
wilcox.test(n$cpu_load, m$cpu_load)

# different syntax same result
wilcox.test(combined_data$bp_delta_joule~combined_data$experiment, data = combined_data, exact = FALSE)
wilcox.test(combined_data$memory_usage_mb~combined_data$experiment, data = combined_data, exact = FALSE)
wilcox.test(combined_data$cpu_load~combined_data$experiment, data = combined_data, exact = FALSE)

#--Assumption 3: Homogeneity in variances?
res.ftest <- var.test(bp_delta_uw ~ experiment, data = combined_data)
res.ftest #p-value should be greater than 0.05

res.ftest <- var.test(cpu_load ~ experiment, data = combined_data)
res.ftest #p-value should be greater than 0.05

res.ftest <- var.test(memory_usage_kb ~ experiment, data = combined_data)
res.ftest #p-value should be greater than 0.05

#added check for difference in parameters
res.ftest <- var.test(bp_delta_uw ~ experiment_noparams, data = combined_data)
res.ftest #p-value should be greater than 0.05

res.ftest <- var.test(bp_delta_uw ~ experiment_params, data = combined_data)
res.ftest #p-value should be greater than 0.05

#-T-test is used to compare two means. var.equal is set to TRUE when the variance is equal.
res.ttest <- t.test(bp_delta_uw ~ experiment, data = combined_data, var.equal=TRUE)
res.ttest

res.ttest <- t.test(cpu_load ~ experiment, data = combined_data, var.equal=TRUE)
res.ttest

res.ttest <- t.test(memory_usage_kb ~ experiment, data = combined_data, var.equal=TRUE)
res.ttest

#added check for difference in parameters
res.ttest <- t.test(bp_delta_uw ~ experiment_noparams, data = combined_data, var.equal=TRUE)
res.ttest

res.ttest <- t.test(bp_delta_uw ~ experiment_params, data = combined_data, var.equal=TRUE)
res.ttest

#effect size to see how big the effect is when the t.test resulting p-value is below 0.05
require(effsize)
VD.A(bp_delta_joule ~ experiment, data = combined_data)
VD.A(cpu_load ~ experiment, data = combined_data)
VD.A(memory_usage_mb ~ experiment, data = combined_data)


VD.A(bp_delta_joule ~ experiment_noparams, data = combined_data)

# VISUALIZATION
# FOR BP_DELTA_UW - copy this for the other variables
ggplot(combined_data, aes(y=bp_delta_joule, x=experiment, fill=experiment)) + 
  #limits are possible
  #ylim(50, 55) +
  #add labels
  xlab("Experiments") + ylab("Battery Power Delta in uW") + 
  #interesting looking shape represents the distribution
  geom_violin(trim=FALSE, alpha=1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  #stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

#battery
ggplot1 <- ggplot(combined_data, aes(y=bp_delta_joule, x=experiment, fill=experiment)) + 
  labs(title="Boxplots: Comparison of Energy Consumption in Joule between experiments") +
  xlab("Combined") + 
  ylab("") + 
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

ggplot2 <- ggplot(subset(combined_data, !is.na(experiment_noparams)), aes(y=bp_delta_joule, x=experiment_noparams, fill=experiment_noparams, na.rm = TRUE), na.rm = TRUE) + 
  xlab("No Parameter Functions") +  ylim(0,800) +
  ylab("") + 
  #points
  geom_jitter(width=.1, show.legend = FALSE, na.rm = TRUE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE, na.rm = TRUE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE, na.rm = TRUE)

ggplot3 <- ggplot(subset(combined_data, !is.na(experiment_params)), aes(y=bp_delta_joule, x=experiment_params, fill=experiment_params, na.rm = TRUE)) + 
  xlab("Multiple Parameter Functions") + 
  ylab("") + 
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

grid.arrange(ggplot1, ggplot2, ggplot3, ncol=1, nrow = 3, left= "Energy Consumption (Joule)")

#cpu_load
ggplot(combined_data, aes(y=cpu_load, x=experiment, fill=experiment)) + 
  xlab("Experiments") + ylab("CPU Load (%)") + 
  labs(title="Boxplots: Comparison of CPU Load in Percentage between experiments") +
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

#memory_usage_kb
ggplot(combined_data, aes(y=memory_usage_mb, x=experiment, fill=experiment)) + 
  xlab("Experiments") + ylab("Memory Usage (mb)") + 
  labs(title="Boxplots: Comparison of Memory Usage in mb between experiments") +
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

#qqplot with beautiful line
#ggplot(combined_data, aes(sample=bp_delta_joule))+stat_qq(color="blue")+geom_qq_line(color="black")

##density plot
#ggplot(combined_data, aes(x=bp_delta_joule)) + 
#  geom_density()

#memory_usage_kb
plot1 <- ggplot(combined_data, aes(y=bp_delta_joule, x=parameters, fill=parameters)) + 
  xlab("") + ylab("Battery Power (joule)") + 
  labs(title="Boxplots: Comparison of multiple parameters against no parameters") +
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

#memory_usage_kb
plot2 <- ggplot(combined_data, aes(y=cpu_load, x=parameters, fill=parameters)) + 
  xlab("") + ylab("CPU load (%)") + 
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

#memory_usage_kb
plot3 <- ggplot(combined_data, aes(y=memory_usage_mb, x=parameters, fill=parameters)) + 
  xlab("Parameters") + ylab("Memory Usage (mb)") + 
  #points
  geom_jitter(width=.1, show.legend = FALSE) +
  #add boxplots
  geom_boxplot(show.legend = FALSE) +
  #add points
  stat_summary(fun=mean, color='black', geom ='point', show.legend = FALSE)

grid.arrange(plot1, plot2, plot3, ncol=1, nrow = 3)
