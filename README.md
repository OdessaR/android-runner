# GoGreen Experiment Replication Package
This repository intends to be the Replication Package for the Green-Lab experiment with the title _What is the impact of memoization on the energy efficiency of mobile web apps?_ which was contucted at the Vrije Universiteit Amsterdam 2020. The actual report is available [here](https://github.com/OdessaR/android-runner/blob/master/documentation/GoGreen_Report.pdf).


## Structure
This Replication Package contains all necessary files and data to reproduce the entire experiment. To achieve this, the repository is based on a fork of [AndroidRunner](https://github.com/S2-group/android-runner) and is extended by all other experiment relevant files. This might lead to a more complex structure, but only by providing all necessary files, a replication is ensured. The repository is structured as follows and described acording to the experiment architecture (see next section):

```
    android-runner
     .
     |
     |--- AndroidRunner/    [AndroidRunner] Program core files
     |--- MonkeyPlayer/     [AndroidRunner] Android Record and Replay UI Testing Framework
     |--- documentation/    [All] Figures and PDFs for documentation
     |--- examples/         [AndroidRunner] Example configurations and experiments
     |
     |--- gogreen/          [Data Mining] Files for generating the experiment input data
     |      |
     |      |--- experiment-files/          [Data Mining] Resuls after executing the Data Mining process. Represents the actual experiment input data.
     |      |       |
     |      |       |--- lib/               Contains the memoization library
     |      |       |--- memoizedExec/      HTML files for the memoized experiment
     |      |       |--- normalExec/        HTML files for the non-memoized experiment
     |      |       |--- websites/          Extracted JS functions for the experiment
     |      |
     |      |--- generate.py                Helper file to create the memoized HTML files
     |
     |--- gogreenExperiment/    [Experiment Exectuion] Configuration files for the AndroidRunner and Trepn experiment
     |
     |--- rcode/                [Data Analysis] R-Script and experiment results in raw format
     |      |
     |      |--- data/          [Data Analysis] Experiment results in raw format (ZIP)
     |      |--- stats.r        [Data Analysis] Statistical analysis in R
     |
     |--- selenium/             [Data Mining] Automatically scripts for extracting pure JS functions from the Tranco list
     |
     |--- tests/                [AndroidRunner] Test cases
     |
     |--- <otherFiles>          <mostly relevant for AndroidRunner>
```

## Experiment Architecture
The experiment itself is structured into three different major parts:

### Data Mining
Since the experiment is based on real-world JavaScript functions, the [Tranco List](https://tranco-list.eu/) is used as groundwork. Based on this, several steps are computed to extract only pure JavaScript functions. The result of this process are several JavaScript files which contain only pure JavaScript functions.

### Experiment Execution
The actual experiment uses the pure JavaScript functions to measure i) energy consumption, ii) CPU utilization, and iii) memory utilization of pure JavaScript function with the respect to memoized vs. non-memoized functions. To measure the three metrics, the Trepn Power Profiler from Qualcomm is used. The experiment is performed on an Asus Nexus 7 phone. The result of this process are measurement values—for memoized and non-memoized functions—produced by AndroidRunner.

### Data Analysis
The results are analyzed by using R for the statistical tests. The data are examined if they follow a normal distribution and statistical tests are used for the hypothesis tests. The results of this step are different visualizations like BoxPlots and different numeric values to analyze our hypothesis.


<p align="center">
    <img src="./documentation/experimentArch.png" alt="GoGreen Experiment Architecture" width="300"/>
</p>




## Source Code

### Data Mining

- [[Selenium](https://github.com/OdessaR/android-runner/tree/master/selenium)] To extract pure JavaScript functions from real-world applications, Selenium and Node.js is used to store all websites from the Tranco List locally, remove non-pure JavaScript functions, and format the functions in a readable manner.
- [[Websites](https://github.com/OdessaR/android-runner/tree/master/gogreen/experiment-files/websites)] The actual selection process for the final 100 pure JavaScript functions was two-fold:
    - 50 pure JavaScript functions were selected with zero parameters. This selection process was done in an automatic process. (see [Generator](https://github.com/OdessaR/android-runner/tree/master/gogreen/experiment-files/normalExec/generator))
    - 50 pure JavaScript functions were selected with 1 or more parameters. This selection process was done in a manual process. This means, that 50 functions with parameters were extracted by the authors best knowledge in a random Trial & Error process.

### Experiment Execution

### Data Analysis


## Data


## Figures


## Steps to Reproduce