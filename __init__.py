import numpy as np

a1 = np.array([1, 1, 0, 0, 0,
               0, 1, 1, 0, 0,
               0, 1, 0, 0, 0,
               1, 0, 0, 0, 0,
               0, 0, 0, 0, 0])

a2 = np.array([1, 1, 0, 0, 0,
               0, 0, 1, 0, 0,
               1, 0, 0, 0, 0,
               0, 0, 1, 0, 0,
               0, 0, 0, 0, 0])

a3 = np.array([0, 1, 0, 0, 0,
               1, 1, 0, 0, 0,
               1, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               0, 0, 0, 0, 0])

a4 = np.array([1, 1, 0, 0, 0,
               1, 0, 1, 0, 0,
               0, 1, 0, 1, 0,
               0, 0, 0, 0, 0,
               0, 0, 1, 0, 0])

a5 = np.array([0, 1, 1, 0, 0,
               1, 1, 0, 0, 1,
               0, 1, 0, 0, 0,
               0, 0, 1, 0, 0,
               0, 0, 0, 0, 0])

b1 = np.array([0, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               0, 0, 0, 1, 0,
               0, 0, 0, 0, 1,
               0, 0, 1, 1, 1])

b2 = np.array([0, 0, 0, 0, 0,
               1, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               1, 0, 1, 0, 1,
               0, 1, 0, 1, 1])

b3 = np.array([0, 1, 0, 0, 0,
               0, 0, 0, 1, 0,
               1, 0, 0, 1, 0,
               0, 0, 0, 1, 1,
               0, 0, 0, 1, 0])

b4 = np.array([1, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               0, 0, 1, 0, 0,
               0, 0, 0, 1, 1,
               0, 1, 0, 1, 0])

b5 = np.array([0, 0, 0, 0, 0,
               0, 1, 0, 0, 1,
               0, 0, 0, 0, 1,
               0, 0, 0, 0, 0,
               0, 0, 1, 1, 1])

targets = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])

list = []
list.append(a1)
list.append(a2)
list.append(a3)
list.append(a4)
list.append(a5)

list.append(b1)
list.append(b2)
list.append(b3)
list.append(b4)
list.append(b5)

sample1 = np.array([1, 0, 0, 0, 0,
                    1, 0, 1, 0, 1,
                    0, 0, 0, 0, 0,
                    0, 0, 1, 1, 1,
                    0, 0, 0, 1, 0])

sample2 = np.array([1, 1, 1, 0, 0,
                    1, 1, 1, 0, 0,
                    0, 0, 1, 1, 0,
                    0, 0, 0, 0, 0,
                    1, 0, 1, 0, 0])

sample3 = np.array([0, 0, 0, 0, 1,
                    0, 0, 0, 0, 1,
                    0, 0, 0, 1, 1,
                    0, 0, 0, 0, 1,
                    0, 1, 0, 1, 1])

sample4 = np.array([0, 1, 1, 0, 0,
                    1, 1, 0, 0, 0,
                    0, 1, 1, 0, 0,
                    0, 1, 0, 0, 1,
                    0, 0, 0, 0, 0])

sample5 = np.array([1, 0, 0, 0, 1,
                    0, 0, 0, 0, 0,
                    0, 0, 1, 0, 0,
                    0, 0, 0, 0, 0,
                    1, 0, 0, 0, 1])

samples = []
samples.append(sample1)
samples.append(sample2)
samples.append(sample3)
samples.append(sample4)
samples.append(sample5)
samples_ndarray = np.asarray(samples)

# list_2 = []
# for nparray in list:
#     nparray = np.reshape(nparray, (5, 5))
#     print nparray

data_set = np.asarray(list)

# X = np.array([
#     [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
# ])

X = np.array([
[1,1,0,1,0,0,0,0,1,0],
[1,1,1,1,1,0,0,1,0,0],
[0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,1,1,1,0,1,0,0,0],
[1,0,1,0,1,0,0,0,0,1],
[1,1,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,1,0,0,0,0,1],
[0,1,1,0,0,0,0,1,0,0],
[1,0,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0],
[0,0,0,1,0,1,0,1,0,0],
[0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,1,0,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0],
[0,0,0,0,0,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,1,0],
[0,0,0,1,0,1,0,0,0,1],
[0,0,0,0,0,1,1,1,1,1],
[0,0,0,0,0,1,1,0,0,1]
])
from naive_bayes_classifier import MultinomialNB

X = X.T
nb = MultinomialNB(alpha=1.0, fit_prior=True)
nb = nb.fit(X, targets)
print nb.predict(samples_ndarray)
print nb.conditional_prob



# nb = MultinomialNB(alpha=1.0,fit_prior=True)
# nb = nb.fit(X,y)
#
# print X
# print nb.predict(np.array([2,4]))