import pandas as pd
import numpy as np
from math import sqrt
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import wrangle as w
from sklearn.model_selection import train_test_split
import sklearn.preprocessing
from sklearn.metrics import mean_squared_error


# create functions for evaluate.py
def plot_residuals(df,y,yhat):
    '''This function will plot the residual plot'''
    plt.plot(df['y'], df['yhat'], 'o')
    
def regression_errors(y,yhat):
    '''returns the sum of squared errors, explained sum of squares, 
    total sum of squares, mean squared error, root mean squared error'''
    
    #calculate mean squared error 
    MSE = mean_squared_error(y, yhat)
    print("Mean Squared Error:",{MSE})
    
    #calculates sum of squared errors
    SSE = MSE*len(y)
    print("Sum of Squared errors:",{SSE}) 
    
    #calculate explained sum of squares 
    ESS = sum((yhat - y.mean()**2).sum())
    print("Explained Sum of Squares:",{ESS}) 
    
    #calculate total sum of squares 
    TSS = ESS + SSE
    print("Total Sum of Squares:",{TSS})
    
    #calculate root mean squared error 
    RMSE = sqrt(MSE)
    print("Root Mean Squared Error:",{RMSE})
        
def baseline_mean_errors(y):
    '''returns the sum of squared errors, explained sum of squares, 
    total sum of squares, mean squared error, root mean squared error
    for baseline model'''
    
    #calculates sum of squared errors
    baseline = np.repeat(y.mean(), len(y))
    print("Sum of Squared errors for Baseline model:",{SSE})
        
    #calculate mean squared error 
    MSE_baseline = mean_squared_error(y, baseline)
    print("Mean Squared Error for Baseline model:",{MSE})
    
    #calculates sum of squared errors
    SSE_baseline = MSE_baseline*len(y)
    print("Sum of Squared errors:",{SSE}) 
              
    #calculate root mean squared error
    RMSE_baseline = MSE**.5 
    print("Root Mean Squared Error for Baseline model:",{RMSE_baseline})

def better_than_baseline(y,yhat):
    '''this function will determine which model is better
        based on the value of SSE'''
        SSE, ESS, TSS, MSE, RMSE = regression_errors(y, yhat)
              
        SSE_baseline, MSE_baseline, RMSE_baseline = baseline_mean_errors(y)
    if SSE > SSE_baseline:
        print('My Linear Regression model performs worse than the baseline')
    else:
        print('My Linear Regression model performs better than the baseline')