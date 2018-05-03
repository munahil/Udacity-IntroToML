def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    from sklearn.naive_bayes import GaussianNB 
    clf=GaussianNB() # initialise
    clf.fit(features_train,labels_train) # as input of our function "classify" are features_train, labels_train
    return clf # return value from the function
    