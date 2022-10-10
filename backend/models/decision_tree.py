import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn import metrics

def decision_tree(X, y, response):
    print("Spliting data into training and testing")
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 0 )

    lr = DecisionTreeClassifier(max_depth=3)
    lr = lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)

    response["score"] = lr.score(X_test, y_test)

    return response