from category_encoders import OneHotEncoder, TargetEncoder, LeaveOneOutEncoder, CountEncoder, BinaryEncoder, HashingEncoder



def hashing_encoding(df, df_non_numeric):
    for column in df_non_numeric:
        HashingEncoder(cols=[column]).fit(df).transform(df)

    return df



def binary_encoding(df, df_non_numeric):
    for column in df_non_numeric:
        BinaryEncoder(cols=[column]).fit(df).transform(df)

    return df



def count_encoding(df, df_non_numeric):
    for column in df_non_numeric:
        CountEncoder(cols=[column]).fit(df).transform(df)

    return df



def frequency_encoding(df, df_non_numeric):
    for column in df_non_numeric:
        CountEncoder(cols=[column], normalize=True).fit(df).transform(df)

    return df



def target_mean_encoding(df, df_non_numeric, label):
    for column in df_non_numeric:
        TargetEncoder(cols=[column], smoothing=1.0).fit(df, df[label]).transform(df)

    return df



def leave_one_encoding(df, df_non_numeric, label):
    for column in df_non_numeric:
        LeaveOneOutEncoder(cols=[column]).fit(df, df[label]).transform(df)

    return df



def dummy_encoding(df, df_non_numeric):
    for column in df_non_numeric:
        OneHotEncoder(cols=[column]).fit(df).transform(df)

    return df