export const Documents={
    models:[
        {
            key:"linear_regression",
            value:"Linear Regression",
            description:"Linear regression analysis is used to predict the value of a variable based on the value of another variable."
        },
        {
            key:"logistic_regression",
            value:"Logistic Regression",
            description:"Logistic regression is a statistical analysis method to predict a binary outcome, such as yes or no, based on prior observations of a data set."
        },
        {
            key:"decision_tree",
            value:"Decision Tree",
            description:"A decision tree is a graph that uses a branching method to illustrate every possible output for a specific input"
        },
        {
            key:"support_vector_machine",
            value:"Support Vector Machine",
            description:"A support vector machine (SVM) is a type of deep learning algorithm that performs supervised learning for classification or regression of data groups."
        },
        {
            key:"naive_bayes",
            value:"Naive Bayes",
            description:"Naïve Bayes is a simple learning algorithm that utilizes Bayes rule together with a strong assumption that the attributes are conditionally independent, given the class."
        },
        {
            key:"random_forest",
            value:"Random Forest",
            description:"The random forest is a classification algorithm consisting of many decisions trees."
        }
    ],
    cleaningModels:[
        {
            key:"drop_observations",
            value:"Drop Observations"
        },
        {
            key:"input_missing_values",
            value:"Input Missing Values"
        }
        // ,
        // {
        //     key:"remove_features",
        //     value:"Remove Features"
        // }
    ],
    encodingModels:[
        {
            key:"dummy_encoding",
            value:"Dummy Encoding"
        },
        {
            key:"leave_one_encoding",
            value:"Leave One Encoding"
        },
        {
            key:"target_mean_encoding",
            value:"Target Mean Encoding"
        },
        {
            key:"frequency_encoding",
            value:"Frequency Encoding"
        },
        {
            key:"count_encoding",
            value:"Count Encoding"
        },
        {
            key:"binary_encoding",
            value:"Binary Encoding"
        },
        {
            key:"hashing_encoding",
            value:"Hashing Encoding"
        }
    ],
    percentForCleaning:["remove_features"]
}