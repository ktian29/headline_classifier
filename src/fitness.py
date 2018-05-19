import numpy as np
from sklearn.neural_network import MLPClassifier
import globVars
import random

shuffle = False

def Score(WordList):
    training_ratio = 0.7
    num_headlines = 6000
    X=[]
    y=[]
    
    sample = globVars.sample(num_headlines)
    raw_x, raw_y = zip(*sample)
    unique = np.unique(raw_y)
    for (headline, label) in globVars.sample(num_headlines):
        headlineOneHot = [1 if word in headline else 0 for word in WordList]
        # remove the headlines where no words match
        if sum(headlineOneHot) > 0:
            labelOneHot = [1 if label==category else 0 for category in unique]
            X.append(headlineOneHot)
            y.append(labelOneHot)
    
    
    #for headline in raw_x:
    #    headlineOneHot = [1 if word in headline else 0 for word in WordList]
    #    X.append(headlineOneHot)
    
    #for label in raw_y:
    #    labelOneHot = [1 if label==category else 0 for category in unique]
    #    y.append(labelOneHot)
    
    clf = MLPClassifier(
        solver = 'sgd',
        alpha = 1e-5,
        hidden_layer_sizes = (800,),
        random_state = 1,
        activation = 'logistic',
        learning_rate = 'adaptive')
    print('Fitting %d points...' % len(y))
    num_training = int(len(y) * training_ratio)
    
    clf.fit(X[0:num_training], y[0:num_training])   

    print('Validating....')
    prediction = clf.predict(X[num_training:])
    
    diff = y[num_training:]-prediction
    
    total_error = np.sum([np.sum(np.abs(row)) for row in diff])
    
    size = len(diff)*len(diff[0])
    score = total_error/size
    print('Accuracy =', score)
    return score



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
