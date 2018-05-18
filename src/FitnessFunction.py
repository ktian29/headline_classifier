import numpy as np
from sklearn.neural_network import MLPClassifier


def FitnessScore(WordList, Headlines, Labels):    

    X=[]
    for headline in Headlines:
        headlineOneHot = [1 if word in headline else 0 for word in WordList]
        X.append(headlineOneHot)

    y=[]
    for category in np.unique(Labels):
        labelOneHot = [1 if label==category else 0 for label in Labels]
        y.append(labelOneHot)

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes=(10, 10), random_state=1)
    clf.fit(X, y)   
    prediction = clf.predict(X)
    
    diff = y-prediction
    
    total_error = np.sum([np.sum(np.abs(row)) for row in diff])
    
    size = len(diff)*len(diff[0])
    score = total_error/size

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