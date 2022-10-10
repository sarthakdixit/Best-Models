import pandas as pd
import numpy as np



def remove_duplicate_records(df):
    # dropping duplicates by considering all columns other than ID
    cols_other_than_id = list(df.columns)[1:]
    df.drop_duplicates(subset=cols_other_than_id, inplace=True)

    return df



def input_categorical_missing_values(df, df_non_numeric):
    df_non_numeric = df.select_dtypes(exclude=[np.number])
    non_numeric_cols = df_non_numeric.columns.values
    for col in non_numeric_cols:
        missing = df[col].isnull()
        num_missing = np.sum(missing)
        if num_missing > 0:  # impute values only for columns that have missing values
            mod = df[col].describe()['top'] # impute with the most frequently occuring value
            df[col] = df[col].fillna(mod)
    
    return df



def input_numerical_missing_values(df, df_numeric):
    df_numeric = df.select_dtypes(include=[np.number])
    numeric_cols = df_numeric.columns.values
    for col in numeric_cols:
        missing = df[col].isnull()
        num_missing = np.sum(missing)
        if num_missing > 0:  # impute values only for columns that have missing values
            med = df[col].median() #impute with the median
            df[col] = df[col].fillna(med)
    
    return df



def remove_features(df, pct_missing_df, percent_num):
    # dropping columns with more than percent_num% null values
    pct_missing_cols_list = list(pct_missing_df.loc[pct_missing_df.pct_missing > percent_num, 'col'].values)
    df.drop(columns=pct_missing_cols_list, inplace=True)

    return df



def drop_observations(df, pct_missing_df):
    # removing rows 
    less_missing_values_cols_list = list(pct_missing_df.loc[(pct_missing_df.pct_missing < 0.5) & (pct_missing_df.pct_missing > 0), 'col'].values)
    df.dropna(subset=less_missing_values_cols_list, inplace=True)

    return df



def missing_values(df):
    # % of values missing in each column
    values_list = list()
    cols_list = list()
    for col in df.columns:
        pct_missing = np.mean(df[col].isnull())*100
        cols_list.append(col)
        values_list.append(pct_missing)
    pct_missing_df = pd.DataFrame()
    pct_missing_df['col'] = cols_list
    pct_missing_df['pct_missing'] = values_list

    return pct_missing_df



def seperating_columns(df):
    # numeric data
    df_numeric = df.select_dtypes(include=[np.number])

    # categorical data
    df_non_numeric = df.select_dtypes(exclude=[np.number])

    return df_numeric, df_non_numeric