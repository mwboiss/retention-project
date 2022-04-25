# Innis-Retention-Project

This repo is a compilation of work done to explore Data from a Large College in the Western United States to identify drivers over retention.

## About the Project

### Project Goals

The goal of this project is to identify drivers of retention

### Project Description


### Initial Questions

1) 

2) 

3) 

4) 

5) 

### Summary of Findings

- 
- 

### Project Report



### Data Dictionary

|Column Name|Column Description|
|:-:|:--|
|id|Proxy student ID|
|retained|Y/N flag for whether a student was retained fall-fall or spring-spring|
|enrolled_between|Y/N flag for whether a student was enrolled in the fall or spring semester in between the retained span|
|race_ethn|Race/ ethnicity|
|sex|Sex|
|time_status|Full or part time status based on credits attempted|
|fgen|First generation student status|
|student_year|Student Classification (freshmen, sophomore,etc)|
|pell_ever|Whether or a not a student has ever been Pell grant eligible|
|efc|Expected Family Contribution (null where no FAFSA received)|
|hs_gpa|High School GPA where available|
|term_gpa|Term grade point average in base semester of retention calculation|	
|enroll_type|A student's original student type when beginning at the university|
|cip|2 digit classification of instrucitonal program|
|age_at_start_term|Age at the start of the term for the base semester of the retention calculation|
|act|ACT score bucket where available|
|academic_standing|Academic standing bucket (here grouped into good or issue bins)	|
|fa_recd|Whether or a not a student received financial aid in the base semester of retention calculation|
|depend_status|Students' financial dependency status|
|w_count|Count of W grades received in base semester of retention calculation|
|yr_since_start|Groupings of years between when a student began and the start date of the base semester of the retention calculation|
|reg_before_start|Number of days between when a student registered for the base semester of the retention calculation and that semester's start date|

### Steps to Reproduce

1. A locally stored env.py file containing hostname, username and password for the mySQL database containing the zillow dataset is needed.

2. Data Science Libraries needed: pandas, numpy, matplotlib.pyplot, seaborn, scipy.stats, sklearn

3. All files in the repo should be cloned to reproduce this project.

4. Ensuring .gitignore is setup to protect env.py file data.

## Plan of Action

### Wrangle Module

1) Create and test acquire functions

2) Add functions to wrangle.py module

3) Create and test prepare functions

4) Add functions to wrangle.py module

##### Missing Values

1) Explore data for missing values

2) Add code to prepare function to remove values

3) Test function in notebook

##### Outliers

1) Assess data for outliers

2) Remove outliers if needed

3) Create function to remove outliers

4) Add function to wrangle.py module

##### Scale Data

1) Scale data appropriately

2) Create function to scale data

3) Add function to wrangle.py module

##### Data Split

1) Write code needed to split data into train, validate and test

2) Add code to prepare function and test in notebook

##### Explore

###### Each Feature Individually

###### Pairs of Variables

###### Multiple Variables

###### Questions to Answer

1) 

2) 

3) 

4) 

5) 

###### Explore through visualizations

1) Create visualizations exploring each question

###### Statistics tests

1) Run statistics test relevant to each question

###### Explore through Clustering

1) Test clusters as features, visualizations and possible samples for modeling.

###### Summary 

1) Create a summary that answers exploritory questions

#### Modeling

1) Evaluate which metrics best answer each question

2) Evaluate a basline meteric used to compare models to the most present target variable

3) Develop models to predict .

4) Fit the models to Train data

5) Evaluate on Validate data to ensure no overfitting

6) Evaluate top model on test data

#### Report

1) Create report ensuring well documented code and clear summary of findings as well as next steps to improve research