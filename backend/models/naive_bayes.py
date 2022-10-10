import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB 

def naive_bayes(X, y, response):

    print("Spliting data into training and testing")
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 0 )
  
    st_x= StandardScaler()    
    x_train= st_x.fit_transform(X_train)    
    x_test= st_x.transform(X_test)  

    lr = GaussianNB() 
    lr = lr.fit(x_train, y_train)
    y_pred = lr.predict(x_test)

    response["score"] = lr.score(x_test, y_test)

    return response