# -*- coding: utf-8 -*-
'''
    Read MNIST DATA SET and write data into txt file
    @author: ICTwangbiao
    @date: 2014-08-05
'''

import numpy as np
from mnist import MNIST

# import mnist train dataset
mndata = MNIST('data')
mndata.load_training()
mndata.load_testing()

# write data into file like "feature1 feature2 ... featureN target"
print "Begin write..."

f = open('mnistTrain.txt', 'a')
for i in xrange(len(mndata.train_images)):
    for j in xrange(len(mndata.train_images[i])):
        f.write(str(mndata.train_images[i][j])+' ')
    f.write(str(mndata.train_labels[i])+'\n')
f.close()

f = open('mnistTest.txt', 'a')
for i in xrange(len(mndata.test_images)):
    for j in xrange(len(mndata.test_images[i])):
        f.write(str(mndata.test_images[i][j])+' ')
    f.write(str(mndata.test_labels[i])+'\n')
f.close()

print "End write!"