"""
Purpose: pandas functions that are useful for machine learning


.iloc: indexes with integers
ex: df_test.iloc[:5] --> gets first 5 rows
.loc: indexes with strings
Ex: df_test.loc[df.columns,df.columns[:5]]
"""
    
import pandas as pd
import numpy as np
    
def df_no_target(df,target_name):
    return df[[k for k in df.columns if k != target_name]]

def n_features(df,target_name=None):
    return len(pdml.df_no_target(df,target_name).columns)

def X_y(df,target_name):
    return pdml.df_no_target(df,target_name),df[target_name]

def feature_names(df,target_name=None):
    return np.array(list(pdml.df_no_target(df,target_name).columns))

def df_column_summaries(df):
    return df.describe()

def filter_away_nan_rows(df):
    return df[~(df.isna().any(axis=1))]

def dropna(axis=0):
    """
    More straight forward way for dropping nans
    """
    return df.dropna(axis)

def correlations_by_col(df,
                           correlation_method = "pearson"):
    """
    will return a table that has the correlations between
    all the columns in the dataframe
    
    other correlations methods: "pearson","spearman",'kendall'
    
    """
    return df.corr(correlation_method)

def correlations_to_target(df,
                           target_name = "target",
                            correlation_method = "pearson",
                           verbose = False,
                           sort_by_value = True,
                          ):
    """
    Purpose: Will find the correlation between all
    columns and the 
    """
    #1) gets the correlation matrix
    corr_df = pdml.correlations_by_col(df,
                                     correlation_method = correlation_method)
    
    #2) only gets the last row (with the target)
    corr_with_target = corr_df.loc[target_name][[k for k in df.columns if k != target_name]]
    
    if sort_by_value:
        corr_with_target= corr_with_target.sort_values(ascending=False)
    
    return corr_with_target


def df_mean(df):
    return df.mean()

def df_std_dev(df):
    return df.std()

def center_df(df):
    return df - df.mean()

def hstack(dfs):
    return pd.concat(dfs,axis = 1)
    
    
import pandas_ml as pdml