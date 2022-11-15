import pandas as pd
import numpy as np
from env import get_db_url
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data
from sklearn.model_selection import train_test_split


# train test split from sklearn
from sklearn.model_selection import train_test_split
# imputer from sklearn
from sklearn.impute import SimpleImputer

#------------------- ACQUIRE OR GET ZILLOW DATA -------------------#
def new_zillow_data():
    '''
    This function reads the zillow data from the Codeup db into a df.
    '''
    # Create SQL query.
    sql_query = """SELECT bedroomcnt,bathroomcnt,calculatedfinishedsquarefeet, yearbuilt, taxvaluedollarcnt,taxamount,fips
                FROM properties_2017
                LEFT JOIN propertylandusetype as pl using (propertylandusetypeid)
                WHERE pl.propertylandusetypeid = '261'"""
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_db_url('zillow'))
    
    return df

def get_zillow_data():
    '''
    This function reads in zillow data from local copy as a df
    '''
        
    # Reads local copy of csv 
    df = pd.read_csv('zillow.csv')

    # renaming column names to more readable format
    df = df.rename(columns = {'bedroomcnt':'bedrooms', 
                              'bathroomcnt':'bathrooms', 
                              'calculatedfinishedsquarefeet':'area',
                              'taxvaluedollarcnt':'property_value', 
                              'yearbuilt':'year_built',})
    
    return df
def remove_outliers(df, k, col_list):
    ''' remove outliers from a list of columns in a dataframe 
        and return that dataframe
    '''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df

def prepare_zillow(df):
    ''' Prepare zillow data for exploration'''

    # removing outliers
    df = remove_outliers(df, 1.5, ['bedrooms', 'bathrooms', 'area', 'property_value', 'taxamount'])
    
    # drop nulls 
    df = df.dropna()
    
    # train/validate/test split
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)      
    
    return train, validate, test   

def wrangle_zillow():
    '''Acquire and prepare data from Zillow database for explore'''
    train, validate, test = prepare_zillow(get_zillow_data())
    
    return train, validate, test