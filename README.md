# ![Android Malware Threat Predictor]()

The Android Malware Threat Predictor is a data app with a Streamlit dashboard that can predict threat levels for certain types of malware. At the heart of the app, a machine learning algorithm trained on a dataset, predicts threat levels for Adware, Scareware, SMS Malware and Benign on Android devices. 

The live website link can be found here ![Android Malware Threat Predictor](https://pp5-android-malware-detector.onrender.com)

## Dataset Content
The Dataset is sourced from ![Kaggle - Android Malware Detection](https://www.kaggle.com/datasets/subhajournal/android-malware-detection). It was chosen based on the business case and the idea to create an Andorid Malware Predictor. The dataset separates the types of malware into four labels -  Android_Adware, Android_Scareware, Android_SMS_Malware and Benign - which fit well with the wish to predict types of malware. At the time of access, the dataset consisted of 355630 entries or instances (rows) with 85 columns and had the following label distribution: 

Android_Adware =>147443
Android_Scareware => 117082
Android_SMS_Malware => 67397
Benign => 23708

After choosing the dataset and conducting further analysis on the data, it was found that the other variables - features - were quite technical in origin and not easy to understand which led to some challenges and complications in working with the data. 

## Business Requirements
As a Data Scientist working with cybersecurity stakeholders, you are tasked with developing a predictive system to classify Android applications into malware categories. The client — a cybersecurity firm — seeks to automate malware threat detection and gain insights on prevalent malware types to enhance security monitoring and response strategies.

1. The client wants to understand the characteristics and distribution of different malware types within their dataset to prioritize threat management effectively.

2. The client needs an automated classification model that can accurately categorize new Android applications into malware classes such as Adware, SMS Malware, Scareware, or mark them as Benign, facilitating real-time threat detection and mitigation.

3. The client desires actionable insights on feature importance and behavior patterns that differentiate malware classes to inform defensive strategies and guide further security research.


## Hypothesis and how to validate?
1. Hypothesis: Specific static or behavioral features extracted from Android apps strongly correlate with particular malware types, enabling accurate classification.

    * Validation: Perform exploratory data analysis and correlation studies on features against malware classes. Use feature importanceto further explore how features correlate with malware types.

2. Hypothesis: A supervised machine learning model trained on labeled malware data can achieve high accuracy and balanced performance across malware classes, enabling reliable classification.

    * Validation: Train and evaluate various classification models using metrics such as accuracy, balanced accuracy, and F1-score. Validate performance on hold-out test data to confirm generalization.

3. Hypothesis: The distribution of predicted probabilities for each malware class reveals actionable thresholds for threat levels, which can inform risk-based alerting systems.

    * Validation: Analyze prediction probability distributions per class, and consult with domain experts to set meaningful threat level thresholds.


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* Business Requirement 1: Malware Characterization and Distribution Analysis

    * Use exploratory data analysis (EDA) visualizations to show class distribution and feature correlations.

    * Employ summary statistics and plots to highlight key malware characteristics.

* Business Requirement 2: Malware Classification Modeling

    * Develop and compare classification models (e.g., Random Forest, XGBoost) to identify the best-performing algorithm.

    * Use classification metrics (accuracy, balanced accuracy, F1-score) to evaluate model effectiveness.

* Business Requirement 3: Feature Importance and Threat Level Interpretation

    * Generate feature importance plots to reveal features driving model decisions.

    * Create interactive dashboards that allow users to select malware classes and view threat probabilities, supporting risk assessment and decision-making.


## ML Business Case
Malware Classification
Classification Model

* We want an ML model to classify Android applications into one of four classes: Adware, SMS Malware, Scareware, or Benign, based on static and behavioral features extracted from the apps. The target variable is categorical with 4 classes.

* We consider a supervised multi-class classification model with single-label output:

    * 0: Adware

    * 1: SMS Malware

    * 2: Scareware

    * 3: Benign

* Our ideal outcome is to provide cybersecurity analysts and automated systems with reliable and fast malware type detection, enabling efficient threat response and risk management.

* The model success metrics are:

    * At least 80% balanced accuracy on train and test sets to ensure fairness across classes.

    * F1-score greater than 0.75 for each malware class, especially focusing on minimizing false negatives for malware classes (classes 0,1,2).

* The ML model is considered a failure if:

    * The false negative rate for any malware class exceeds 20%, leading to undetected threats.

    * The model’s overall accuracy on unseen data falls below 75%, implying poor generalization.

* The model output is defined as a predicted malware class label and associated class probability, which can be integrated into automated threat alert systems or analyst dashboards.

* Input features should be extracted from user input via an interactive dashboard. Predictions are made on the fly. 

* Heuristics: Currently, manual or signature-based detection is used, which is slower and less adaptive to new threats.

* The training data comes from a publically available dataset from Kaggle. It contains 355630 entries split into four classes. 
    * Train data - target: Label(classes); features: all other variables, but Flow ID, Source IP, Destination IP, Timestamp and Unnamed: 0


## Dashboard Design (Streamlit App User Interface)

### Page 1: Project Summary
* Quick project summary
    * Describe project dataset
    * State business requirements & hypotheses
    * Link readme file

### Page 2: Exploratory Data Analysis
* Overview of overall data analysis
    * Explain purpose
    * Display EDA visualisations 
    * State conclusion 
    * Answer business requirements & hypotheses if possible

### Page 3: Malware Threat Predictor
* Overview of model development
    * Explain purpose
    * Display prediction model functionality with: 
        * Interactive threat level prediction for types of malware
        * Interactive threat type prediction for feature inputs
    * State conclusion 
    * Answer business requirements & hypotheses if possible

### Page 4: Project Evaluation
* Overview of project evaluation
    * Explain purpose
    * Display evaluation visualisations 
    * State conclusion 
    * Answer business requirements & hypotheses if possible

## Bugs

### Unfixed Bugs

* PPScore install issue 2: 
    * When trying to install the ppscore library, a dependency conflict with other libraries arose with the required pandas version. PPscore required a pandas version <2.0.0>=1.0.0 whereas feature-engine requires pandas >=2.2.0
    * Solution 1: Prioritise feature-engine vs. ppscore and refrain from using ppscore
    * Active: PPScore cannot be used in the current set up 

### Fixed Bugs 

* VSCode install issue: 
    * When creating Pandas Profiling Reports, missing installs of ipywidgets prevented it from rendering. The install worked fine in the terminal but not in the notebook. 
    * Solution: Run install directly in the notebook once before removing code snippet

* PPScore install issue 1: 
    * When trying to install the ppscore library, an error indicated that Microsoft Visual C++ needed to be updated.
    * Solution 1: Run installer for Microsoft C++ Build Tools to update version

* Rounding issues: 
    * When running the EvaluateMissingData function, rounding settings
 
## Further Improvements

### Model Enhancement

* Currently, the best trained model has a balanced accuracy of 45%, failing the business requirements. It is possible, that deep feature engineering could enhance the model performance, although the tried methods did the opposite and worsened the performance. 

### Code Enhancement

* Set reusable file paths at the top of each notebook to reduce repeated code segments and increase reusability of code
* Additionally increase reusability of code by refactoring code into pipeline processes instead of modular code blocks
* Possibly refactor code functions into separate python files to allow access from all directories and notebooks

## Deployment

### Render

* The app was deployed on Render, with the live link found here [Android Malware Threat Predictor](https://pp5-android-malware-detector.onrender.com)
* The following guides from Code Institute were followed for the deployment steps:
    * Creating an account on Render [CI Render Account Creation Guide](https://code-institute-students.github.io/deployment-docs/03-render/render-01-sign-up)
    * Deploying app on Render [CI Render App Deployment Guide](https://code-institute-students.github.io/deployment-docs/42-pp5-pa/pp5-pa-01-preparing-for-render)

### Heroku

* Originally the app was supposed to be deployed via Heroku. Due to large file contraints, this was not possible.

## Main Data Analysis and Machine Learning Libraries
* [Imblearn](https://imbalanced-learn.org/stable/): Used for SMOTE 
* [Sklearn](https://scikit-learn.org/stable/): Used for algorithms and model training like RandomForestClassifier and GridSearchCV
* [Xgboost](https://xgboost.readthedocs.io/en/release_3.0.0/): Used for algorithms and model training like XGBClassifier

## Credits 

### Code 

* The [Code Institute Churnometer Walkthrough](https://github.com/Code-Institute-Solutions/churnometer) was used as a guide and source for custom functions (e.g EvaluateMissingData) which have been adapted to fit this project.
* The [Code Institute PP5 Template](https://github.com/Code-Institute-Solutions/milestone-project-bring-your-own-data) has been used for general project setup and readme template.

### Official Documentation

The official documentation of used libraries were often used to see sample code and how to build and use different functionality.

* [Numpy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [Plotly](https://plotly.com/)
* [Pandas](https://pandas.pydata.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Streamlit](https://streamlit.io/)
* [Imblearn](https://imbalanced-learn.org/stable/)
* [Sklearn](https://scikit-learn.org/stable/)
* [Xgboost](https://xgboost.readthedocs.io/en/release_3.0.0/)

### Code Assistance 

* Many code problems and questions were solved by searching for answers on [W3Schools](https://www.w3schools.com/), [Stack Overflow](https://stackoverflow.com/questions) & [Google](https://www.google.com)



