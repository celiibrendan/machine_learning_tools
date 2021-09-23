"""
Functions used on data before
models analyze the data

Application: 
1) Lasso Linear Regression should have all columns on the same scale
so they get regularized the same amount


Useful link explaining different sklearn scalars for preprocessing: 

http://benalexkeen.com/feature-scaling-with-scikit-learn/
"""
import sklearn.preprocessing as sklpre

available_scalars = dict(
    normal_dist = sklpre.StandardScaler, #will ensure all rows are normalized with 0 mean, std dev 1 (should only be if data already normal)
    min_max = sklpre.MinMaxScaler, #subtracts the min and then divides by the (max - min) [subjecdt to outliers]
    min_max_q1_q3 = sklpre.RobustScaler, #same as min max except min = Q1, max = Q3 [better for outliers]
    within_unit_sphere = sklpre.Normalizer, #makes sure all data is inside an n dimensional sphere of radius 1 of origin
)


def get_scaler(scaler):
    """
    Purpose: To return the appropriate scalar option
    
    """
    if type(scaler) != str:
        return scaler()
    if scaler not in available_scalars.keys():
        return getattr(sklpre,scaler)()
    else:
        return available_scalars[scaler]()
    
import pandas_ml as pdml
import pandas as pd
def scale_df(df,
             scaler="StandardScaler",
            target_name =  None,
            verbose = False):
    """
    Purpose: 
    To apply a preprocessing scalar
    to all of the feature columns of a df

    1) Get the appropriate scaler
    
    Ex: 
    import preprocessing_ml as preml
    preml.scale_df(df,
    target_name=target_name,
    scaler = "RobustScaler",
    verbose = False)
    """


    scaler = preml.get_scaler(scaler)

    if verbose:
        print(f"scaler = {scaler}")

    df_features = pdml.feature_names(df,target_name)
    scaler_df = scaler.fit_transform(df[df_features])
    scaler_df = pd.DataFrame(scaler_df,columns = df_features)
    scaler_df
    
    return scaler_df

import preprocessing_ml as preml