import pandas as pd
import utilities.cleaning_data as cd
import utilities.encoding_data as ed
import models.linear_regression as linear_regression
import models.logistic_regression as logistic_regression
import models.decision_tree as decision_tree
import models.naive_bayes as naive_bayes
import models.random_forest as random_forest
import models.support_vector_machine as support_vector_machine
import seaborn as sns
import matplotlib.pyplot as plt

def drop_unwanted_columns(df, discarded_columns_array):
    df.dropna(inplace=True)
    # dropping unwanted columns
    print("Removing unwanted columns")
    if len(discarded_columns_array) > 0:
        for col in discarded_columns_array:
            df = df.drop(col, axis=1)
    return df

def seperating_numeric_nonnumeric(df):
    # seperating numerical and categorical columns
    print("seperating numerical and categorical columns")
    df_numeric, df_non_numeric = cd.seperating_columns(df)
    return df_numeric, df_non_numeric

def cleaning_data(df, cleaning_data_type, percent_num, df_numeric, df_non_numeric):
    # cleaning data
    print("Remove duplicate records")
    df = cd.remove_duplicate_records(df)
    print("Cleaning data")
    if cleaning_data_type == "drop_observations":
        pct_missing_df = cd.missing_values(df)
        df = cd.drop_observations(df, pct_missing_df)
    elif cleaning_data_type == "input_missing_values":
        df = cd.input_numerical_missing_values(df, df_numeric)
        df = cd.input_categorical_missing_values(df, df_non_numeric)
    elif cleaning_data_type == "remove_features":
        pct_missing_df = cd.missing_values(df)
        df = cd.remove_features(df, pct_missing_df, percent_num)
    return df

def encoding_data(df, encoding_type, label, df_non_numeric):
    # Encoding data
    print("Encoding data")
    if encoding_type == "dummy_encoding":
        df = ed.dummy_encoding(df, df_non_numeric)
    elif encoding_type == "leave_one_encoding":
        df = ed.leave_one_encoding(df, df_non_numeric, label)
    elif encoding_type == "target_mean_encoding":
        df = ed.target_mean_encoding(df, df_non_numeric, label)
    elif encoding_type == "frequency_encoding":
        df = ed.frequency_encoding(df, df_non_numeric)
    elif encoding_type == "count_encoding":
        df = ed.count_encoding(df, df_non_numeric)
    elif encoding_type == "binary_encoding":
        df = ed.binary_encoding(df, df_non_numeric)
    elif encoding_type == "hashing_encoding":
        df = ed.hashing_encoding(df, df_non_numeric)
    return df

def select_featured_columns(df, label):
    print("Selecting feature columns")
    feature_columns = []
    for col in df:
        if col != label:
            feature_columns.append(col)
    return feature_columns

def save_visuals(df, feature_columns, model_type, label):
    response = {}
    image_path = "results/"+model_type
    # to plot all the scatterplots in a single plot
    print("Saving scatter plots")
    sns.pairplot(df, x_vars=feature_columns, y_vars = label, height = 4, kind = 'scatter' )
    plt.savefig(image_path+"/scatterplots.png")
    response["scatter_plot"] = model_type+"/scatterplots.png"
    #To plot heatmap to find out correlations
    print("Saving heatmap")
    sns.heatmap(df.corr(), cmap = 'YlGnBu', annot = True )
    plt.savefig(image_path+"/heatmap.png")
    response["heatmap"] = model_type+"/heatmap.png"
    # to plot pairplots
    print("Saving pairplot")
    sns.pairplot(df)
    plt.savefig(image_path+"/pairplot.png")
    response["pairplot"] = model_type+"/pairplot.png"
    return response

def divide_column_x_y(df, feature_columns, label):
    print("Dividing column into X and y")
    X = df[feature_columns]
    X = pd.get_dummies(data=X, drop_first=True)
    y = df[label]
    return X, y

def choose_model(X, y, response, model_type):
    # Model type
    print("Working on model")
    if model_type == "linear_regression":
        response = linear_regression.linear_regression(X, y, response)
    if model_type == "logistic_regression":
        response = logistic_regression.logistic_regression(X, y, response)
    if model_type == "decision_tree":
        response = decision_tree.decision_tree(X, y, response)
    if model_type == "support_vector_machine":
        response = support_vector_machine.support_vector_machine(X, y, response)
    if model_type == "naive_bayes":
        response = naive_bayes.naive_bayes(X, y, response)
    if model_type == "random_forest":
        response = random_forest.random_forest(X, y, response)
    print("Model Complete")
    return response

def main(file_path, model_type, cleaning_data_type, percent_num, encoding_type, discarded_columns_array, label):

    df = pd.read_csv(file_path)

    df = drop_unwanted_columns(df, discarded_columns_array)

    df_numeric, df_non_numeric = seperating_numeric_nonnumeric(df)

    df = cleaning_data(df, cleaning_data_type, percent_num, df_numeric, df_non_numeric)

    df = encoding_data(df, encoding_type, label, df_non_numeric)

    feature_columns = select_featured_columns(df, label)

    response = save_visuals(df, feature_columns, model_type, label)

    X, y = divide_column_x_y(df, feature_columns, label)

    response = choose_model(X, y, response, model_type)

    return response
    