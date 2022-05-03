# Innis-Retention-Project

This repo is a compilation of work done to explore Data from a Large College in the Western United States to identify drivers over retention.

## About the Project

### Project Goals

The goal of this project is to identify drivers of retention for a large University in the Western United States. 

### Project Description

College continues to be a large expense for adults in America. Ensuring students have every oppurtunity to finish their education should be of upmost importance to every University. In this project I will explore possible drivers that can help Universities identify which students are at risk of not returning year over year.

### Initial Questions

1)  Does the students class status (Freshman, Sophmore,etc..) vs the years since a student started affect retention?

2)  Does whether a student was enrolled between the retention semester affect retention?

3) Does a students term gpa affect retention?

4) Does the students w_count affect retention?

5) Does a students full time or part time status affect retention?

### Summary of Findings

- Through exploration and modeling whether a student was enrolled in the semester between the retention calculation and the base semester showed the most drastic retention difference. Freshman students showed a much lower retention then the other classes. Lastely term_gpa was much lower in students that were not retained.

### Project Report

https://github.com/mwboiss/retention-project/blob/main/report.ipynb

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

5. CSV file must remain private for purposes of anonymity.

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

1)  Does the students class status (Freshman, Sophmore,etc..) vs the years since a student started affect retention?

2)  Does whether a student was enrolled between the retention semester affect retention?

3) Does a students term gpa affect retention?

4) Does the students w_count affect retention?

5) Does a students full time or part time status affect retention?

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

3) Develop models to predict

4) Fit the models to Train data

5) Evaluate on Validate data to ensure no overfitting

6) Evaluate top model on test data

#### Report

1) Create report ensuring well documented code and clear summary of findings as well as next steps to improve research

#### Summary of Questions and Conclusions

Question 1: Does the students class status (Freshman, Sophmore,etc..) vs the years since a student started affect retention?

Question 1 Summary: Freshman by far have the lowest retention across the yrs. Juniors and Seniors have the highest. Further exploration could be done with enrollment type to see how first time students compare to transfer students. As well populations can be seperated by full time and part time status. 

Question 2: Does whether a student was enrolled between the retention semester affect retention?

Question 2 Summary: If a student was not enrolled between the retention semester it seems to be the biggest indicator that they will not be retained. According to the Chi^2 test mid semester enrollment is not independent of retention.

Question 3: Does a students term gpa affect retention?

Question 3 Summary: Term gpa seems to be a decent predictor. Bottom 75 % of students in the not retained category had a term_gpa less than the bottom 50 % of those retained. Also note for later analysis hs_gpa does not change with a student over time but term_gpa does.

Qestion 4: Does the students w_count affect retention?

Question 4 Summary: 70 percent of students did not have a w_count in the base semester of the retention calculation, out of those students the retention rate was higher than the average. The 30 percent of students with at least one withdraw had a much lower retention rate of 55 percent.

Question 5: Does a students full time or part time status affect retention?

Question 5 Summary: It does look as though full time students are more likely to be retained. The chi^2 test does show that there is a statistically significant relationship between time_status and retention.