import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
import random
import globVars

def Score(WordList):
    training_ratio = 0.7
    X = []
    y = [globVars.Categories.index(label) for label in globVars.Labels]
    

    for headline in globVars.Headlines:
        headlineOneHot = [int(word in headline) for word in WordList]
        X.append(headlineOneHot)
    
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size = training_ratio, random_state = 0)
    
    clf = MLPClassifier(
        solver = 'lbfgs',
        hidden_layer_sizes = (50,),
        random_state = 1,
        activation = 'logistic',
        learning_rate = 'adaptive')

    clf.fit(Xtrain, ytrain)
    
    probs_of_each_category = clf.predict_proba(Xtest)
    predictions = [list(values).index(max(values)) for values in probs_of_each_category]

    correct = 0
    for i in range(0, len(ytest)):
        if predictions[i] == ytest[i]:
            correct += 1
    score = correct / len(ytest)
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
