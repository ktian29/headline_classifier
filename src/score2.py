from sklearn.linear_model import LogisticRegression

def OneHot(row):
    output = []
    index = row.index(max(row))
    for i in range(len(row)):
        if i==index:
            output.append(1)
        else:
            output.append(0)
    return output

def Convert(array):
    Output = []
    for row in array:
        Output.append(OneHot(list(row)))
    return np.array(Output)


def Score2(WordList):
    
    training_ratio = 0.7
    X=[]
    y=[]
    
    for (headline, label) in globVars.zipped:
        headlineOneHot = [1 if word in headline else 0 for word in WordList]
        labelOneHot = [1 if label==category else 0 for category in globVars.Categories]
        X.append(headlineOneHot)
        y.append(labelOneHot)
    
    train, test = sample(list(zip(X,y)),training_ratio)

    Xtrain = []
    ytrain = []
    for (X,y) in train:
        Xtrain.append(X)
        ytrain.append(y)
     
    Xtrain = np.array(Xtrain)
    ytrain = np.array(ytrain)

    ytrainBUS = ytrain[:,0]
    ytrainENT = ytrain[:,1]
    ytrainHEA = ytrain[:,2]
    ytrainNAT = ytrain[:,3]
    ytrainSCI = ytrain[:,4]
    ytrainSPO = ytrain[:,5]
    ytrainTEC = ytrain[:,6]
    ytrainWOR = ytrain[:,7]
        
    Xtest= []
    ytest = []
    for (X,y) in test:
        Xtest.append(X)
        ytest.append(y)

    Xtest = np.array(Xtest)
    ytest = np.array(ytest)

    


    logisticRegrBUS = LogisticRegression()
    logisticRegrBUS.fit(Xtrain, ytrainBUS)
    predBUS = logisticRegrBUS.predict_proba(Xtest)[:,1]

    logisticRegrENT = LogisticRegression()
    logisticRegrENT.fit(Xtrain, ytrainENT)
    predENT = logisticRegrENT.predict_proba(Xtest)[:,1]

    logisticRegrHEA = LogisticRegression()
    logisticRegrHEA.fit(Xtrain, ytrainHEA)
    predHEA = logisticRegrHEA.predict_proba(Xtest)[:,1]

    logisticRegrNAT = LogisticRegression()
    logisticRegrNAT.fit(Xtrain, ytrainNAT)
    predNAT = logisticRegrNAT.predict_proba(Xtest)[:,1]

    logisticRegrSCI = LogisticRegression()
    logisticRegrSCI.fit(Xtrain, ytrainSCI)
    predSCI = logisticRegrSCI.predict_proba(Xtest)[:,1]

    logisticRegrSPO = LogisticRegression()
    logisticRegrSPO.fit(Xtrain, ytrainSPO)
    predSPO = logisticRegrSPO.predict_proba(Xtest)[:,1]

    logisticRegrTEC = LogisticRegression()
    logisticRegrTEC.fit(Xtrain, ytrainTEC)
    predTEC = logisticRegrTEC.predict_proba(Xtest)[:,1]

    logisticRegrWOR = LogisticRegression()
    logisticRegrWOR.fit(Xtrain, ytrainWOR)
    predWOR = logisticRegrWOR.predict_proba(Xtest)[:,1]


    predictions = np.array(list(zip(predBUS, predENT, predHEA, predNAT, predSCI,\
                                    predSPO, predTEC, predWOR)))

    OneHotPredictions = Convert(predictions)


    diff = ytest-OneHotPredictions

    total_error = np.sum([np.sum(np.abs(row)) for row in diff])
    
    size = len(diff[:,0])*len(diff[0,:])
    score = total_error/size

    return score