# GoGreen Experiment Replication Package
This repository represents the Replication Package for the Green-Lab experiment with the title _'What is the impact of memoization on the energy efficiency of mobile web apps?'_, which was conducted at the Vrije Universiteit Amsterdam 2020. The actual report is available [here](https://github.com/OdessaR/android-runner/blob/master/documentation/GoGreen_Report.pdf).


## Structure
This Replication Package contains all necessary files and data to reproduce the entire experiment. To achieve this, the repository is based on a fork of [AndroidRunner](https://github.com/S2-group/android-runner) and is extended by all other relevant files. This might lead to a more complex structure, but only by providing all necessary files, a replication is ensured. The repository is structured as follows and described according to the experiment architecture (see next section):

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
     |      |--- experiment-files/          [Data Mining] Results after executing the Data Mining process. Represents the actual experiment input data.
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
The experiment itself is structured into three different main parts:

### Data Mining
Since the experiment is based on real-world JavaScript functions, the [Tranco List](https://tranco-list.eu/) is used as groundwork. Based on this, several steps are computed to extract only pure JavaScript functions. The results of this process are several JavaScript files that contain only pure JavaScript functions.

### Experiment Execution
The actual experiment uses the pure JavaScript functions to measure i) energy consumption, ii) CPU utilization, and iii) memory utilization of pure JavaScript function with the respect to memoized vs. non-memoized functions. To measure the three metrics, the Trepn Power Profiler from Qualcomm is used. The experiment is performed on an Asus Nexus 7 phone. The results of this process are measurement values—for memoized and non-memoized functions—produced by AndroidRunner.

### Data Analysis
The results are analyzed by using R for the statistical tests. The data are examined if they follow a normal distribution and statistical tests are used for the hypothesis tests. The results of this step are different visualizations like BoxPlots and different numeric values to analyze our hypothesis.


<p align="center">
    <img src="./documentation/experimentArch.png" alt="GoGreen Experiment Architecture" width="300"/>
</p>




## Source Code
The relevant source code is explained and structure according to the experiment architecture.

### Data Mining
- [[Selenium](https://github.com/OdessaR/android-runner/tree/master/selenium)] To extract pure JavaScript functions from real-world applications, Selenium and Node.js is used to store all websites from the Tranco List locally, remove non-pure JavaScript functions, and format the functions in a readable manner. The result of this process can be found in this [ZIP file](https://github.com/OdessaR/android-runner/blob/master/gogreen/experiment-files/websites/pure.zip).
- [[Websites](https://github.com/OdessaR/android-runner/tree/master/gogreen/experiment-files/websites)] The actual selection process for the final 100 pure JavaScript functions was two-fold:
    - 50 pure JavaScript functions were selected with zero parameters. This selection process was done in an automatic process. (see [Generator](https://github.com/OdessaR/android-runner/tree/master/gogreen/experiment-files/normalExec/generator)) The selected JavaScript functions are not part of this repository, since the functions were selected in an automatic process.
    - 50 pure JavaScript functions were selected with 1 or more parameters. This selection process was done in a manual process. This means, that 50 functions with parameters were extracted to the authors' best knowledge in a random Trial & Error process. The selected JavaScript functions can be found [here](https://github.com/OdessaR/android-runner/tree/master/gogreen/experiment-files/websites)

### Experiment Execution
- [[Android Runner - Trepn](https://github.com/OdessaR/android-runner/tree/master/gogreenExperiment/trepn)] The experiment configuration are split in two configurations.
    - [[Non-Memoized Config](https://github.com/OdessaR/android-runner/blob/master/gogreenExperiment/trepn/config_web_gogreen_normal.json)] JSON configuration file which contains all pure JavaScript functions __without__ memoization.
    - [[Memoized Config](https://github.com/OdessaR/android-runner/blob/master/gogreenExperiment/trepn/config_web_gogreen_memoized.json)] JSON configuration file which contains all pure JavaScript functions __with__ memoization.

### Data Analysis
- [[R-Script](https://github.com/OdessaR/android-runner/blob/master/rcode/stats.r)] The data analysis is based on one single R-Script which executes the data transformations, normality tests, hypothesis tests, and performs different visualizations.


## Data
The relevant data is explained and structure according to the experiment architecture.

### Data Mining
#### Input
- [[Tranco List](https://tranco-list.eu/)] The official (standard) Tranco list serves as initial input for the data mining process. The list represents 1 million real-world domains.

#### Output
- [[Websites](https://github.com/OdessaR/android-runner/blob/master/gogreen/experiment-files/websites/pure.zip)] After applying the mining process (see Selenium step), the results are JavaScript files, structured according to their domain (Tranco list). The actual website resources (HTML, CSS, media content) were removed as well as non-pure JavaScript functions.
- [[Pure JavaScript Functions](https://github.com/OdessaR/android-runner/tree/master/gogreen/experiment-files/websites)] After the selection process (automatic and manuel - see Source Code Data Mining), 50 pure JavaScript functions __without__ paramesters and 50 pure JavaScript functions __with__ 1 to N parameters are available.

### Experiment Execution
#### Input
- [[non-memoized HTML/JS](https://github.com/OdessaR/android-runner/tree/master/gogreen/experiment-files/normalExec)] non-memoized HTML files which uses the pure JavaScript functions for the actual experiment execution.
- [[memoized HTML/JS](https://github.com/OdessaR/android-runner/tree/master/gogreen/experiment-files/memoizedExec)] memoized HTML files which uses the pure JavaScript functions for the actual experiment execution in their memoized version.

All HTML files follow the same structure:

__non-memoized:__

```html
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="utf-8">
</head>

<body>
    <!-- ==> CONF: WEBSITE -->
    <script src="../websites/myWebsite/main.js"></script>

    <!-- exectution -->
    <script type="text/javascript">

        while (true) {

            /* ==> CONF: FUNCTION EXECUTION WITH PARAMS */
            for (x = 0; x < 40; x++) {
                // memo
                myJSfunction(x)
            }

        }
    </script>
</body>
</html>
```

__memoized:__

```html
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="utf-8">
</head>

<body>
    <!-- memoization lib -->
    <script src="../lib/memoization.js"></script>
    <!-- ==> CONF: WEBSITE -->
    <script src="../websites/myWebsite/main.js"></script>

    <!-- exectution -->
    <script type="text/javascript">

        /* ==> CONF: MEMOIZE FUNCTION */
        const memoFunc = memoizer(myJSfunction);

        while (true) {

            /* ==> CONF: FUNCTION EXECUTION WITH PARAMS */
            for (x = 0; x < 40; x++) {
                // memo
                memoFunc(x)
            }

        }
    </script>
</body>
</html>
```

#### Output
- [[Experiment Results](https://github.com/OdessaR/android-runner/blob/master/rcode/data/data_memoized_non-memoized.zip)] Raw measured values from Trepn and aggregated values by AndroidRunner. Contains the results from both runs, non-memoized and memoized.

### Data Analysis
#### Input
- [[Experiment Results](https://github.com/OdessaR/android-runner/blob/master/rcode/data/data_memoized_non-memoized.zip)] Raw measured values from Trepn and aggregated values by AndroidRunner. Contains the results from both runs, non-memoized and memoized.

#### Output
The output of the data analysis is the actual statistical result and the visualizations. See 'Figures' and the [report](https://github.com/OdessaR/android-runner/blob/master/documentation/GoGreen_Report.pdf).

## Figures

__TODO! @Wouter @Sven put figures into folder './documentation/report_figures/'__

[[Figures](https://github.com/OdessaR/android-runner/tree/master/documentation/report_figures)] Figures from the statistical analysis and the actual results.


## Steps to Reproduce
### Data Mining (Selenium)

```
npm -g install js-beautify npm -g install purecheck

pip install -r requirements.txt

python3.6 selenium/main.py
```

### Experiment Execution (AndroidRunner)

```
python3.6 android-runner android-runner/gogreenExperiment/trepn/config_web_gogreen_normal.json

python3.6 android-runner android-runner/gogreenExperiment/trepn/config_web_gogreen_memoized.json
```

### Data Analysis (RStudio)

```
open and execute ./rcode/stats.r in RStudio
```