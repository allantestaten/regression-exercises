# Preventing Customer Churn 
 
# Project Description
I am taking the opportunity to demonstrate my skills learned in codeup to impress the Zillow Data Science team in hopes of recieving an opportunity to interview for a position at their company. I will build a model to predict values of single unit properties based on Zillow data from 2017. 
 
# Project Goal
* Identify which features are drivers for predicting the value of a single unit property
* Develop and use machine learning model that accurately predict value of properties in 2017.
* Deliver a report that explains what steps were taken and why there were taken.

 
# Initial Thoughts
 
Customer churn is more likely to occur based on the services they recieve and contract type. 

# The Plan
 
* Acquire data from Codeup database using mySQL Workbench
 
* Prepare data
   * Created columns representing anticipated drivers that are easy for machine learning model to process
       * has_churned
       * tech_support_Yes
       * contract_type_One year
       * contract_type_Two year
       * internet_service_type_Fiber optic
 
* Explore data in search of drivers of propety value
   * Answer the following initial questions
       * How often do customers churn?
       * Is there an association between churn and Internet Service?
       * Is there an association between churn and fiber optic internet?
       * How often do customers with tech support churn?
       * How often do customers with only phone service churn?
       * Is there an association between churn and contract type?
      
* Develop a Model to predict an accurate value of the property
   * Use drivers supported by statistical test results to build predictive models
   * Evaluate all models on train 
   * Evaluate top models on validate data 
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions
 
# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|Has Churned| True or False, The status of the customer|
|Internet Service Type| The type of internet service the customer has: none, Fiber Optic, DSL|
|Tech Support| True or False, The customer does or does not have technical support|
|Phone Service| True or False, The customer does or does not have phone service|
|Contract Type| The customer has a contract length of month to month, one year or two years|

# Steps to Reproduce
1) Clone this repo
2) Acquire the data from mySQL workbench database 
3) Create env file with username, password and codeup host name 
4) Include the function below in your env file
def get_db_url(db, user = username, host = host, password = password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
5) Put the data in the file containing the cloned repo
6) Run notebook
 
# Takeaways and Conclusions
* 26% of customers churn 
* There is not an association between phone service and churn 
* Statistical evidence supports an association between tech support and churn 
* Statistical evidence supports an association between intertnet service type and churn 
* There is evidence to support an association between fiber optic internet and churn 
* Evidence supports an association between contract type and churn 
* The drivers I used were supported by statistical tests and I believe this is why my final model was able to perform above the baseline


 
# Recommendations
* Recommendations are actions the stakeholder should take based on your insights
* Gather qualitative and quantitative data from customer's about the performance of the fiber optic internet 
* Solicit for quantitative and qualitative data on why customer's select month to month contracts 
* Review incentives offered for each contract type. 