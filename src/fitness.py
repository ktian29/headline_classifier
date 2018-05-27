import numpy as np
from sklearn.neural_network import MLPClassifier
import random
import globVars

def sample(data,ratio):
    random.shuffle(data)
    split = int(len(data)*ratio)
    train = data[:split]
    test = data[split:]
    return train, test

def Score(WordList):

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
        
    Xtest= []
    ytest = []
    for (X,y) in test:
        Xtest.append(X)
        ytest.append(y)

        
    clf = MLPClassifier(
        solver = 'sgd',
        alpha = 1e-5,
        hidden_layer_sizes = (20,),
        random_state = 1,
        activation = 'logistic',
        learning_rate = 'adaptive')
    print('Fitting %d points...' % len(y))
    
    clf.fit(Xtrain, ytrain)   

    print('Validating....')

    prediction = clf.predict(Xtest)
    
    diff = ytest-prediction
    
    total_error = np.sum([np.sum(np.abs(row)) for row in diff])
    
    size = len(diff)*len(diff[0])
    score = total_error/size
    print('Accuracy =', score)
    return score

# Currently creates subset to test and train on based on the existance of any 
# of the "500 words", should train on all 500 and test on all the rest

# (We know that W should be 0.1 and b 0.3, but Tensorflow will
# figure that out for us.)
#W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
#b = tf.Variable(tf.zeros([1]))
#y = W * x_data + b

# Minimize the mean squared errors.
#loss = tf.reduce_mean(tf.square(y - y_data))
#optimizer = tf.train.GradientDescentOptimizer(0.5)
#train = optimizer.minimize(loss)

# Before starting, initialize the variables. We will 'run' this first.
#init = tf.global_variables_initializer()


# Launch the graph.
#sess = tf.Session()
#sess.run(init)
# Fit the line.
#for step in range(201):
#    sess.run(train)
#    if step % 20 == 0:
#       print(step, sess.run(W), sess.run(b))
# Learns best fit is W: [0.1], b: [0.3]
