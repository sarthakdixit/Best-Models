import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

def logistic_regression(X, y, response):

    print("Spliting data into training and testing")
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 0 )
  
    st_x= StandardScaler()    
    x_train= st_x.fit_transform(X_train)    
    x_test= st_x.transform(X_test)  

    lr = LogisticRegression(random_state=0)
    lr = lr.fit(x_train, y_train)
    y_pred = lr.predict(x_test)

    intercept_arr = lr.intercept_
    response["intercept"] = intercept_arr[0]

    response["score"] = lr.score(x_test, y_test)

    response["rmse"] = np.sqrt( mean_squared_error( y_test, y_pred ))

    response["r-squared"] = r2_score( y_test, y_pred )

    return response