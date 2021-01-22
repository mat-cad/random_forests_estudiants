#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:44:37 2018

@author: joans
"""

import numpy as np
import matplotlib.pyplot as plt
# from mnist import init
# do init()it just once, to download the four .gz files
from mnist import load


Xtrain, ytrain, Xtest, ytest = load()
print('{} train and {} test samples with {} features per sample'
      .format(Xtrain.shape[0], Xtest.shape[0], Xtrain.shape[1]))

nrows, ncols = 28, 28

# show first 200 samples as images
plt.close('all')
plt.figure()
for i in range(10):
    for j in range(20):
        n_sample = 20 * i + j
        plt.subplot(10, 20, n_sample + 1)
        plt.imshow(np.reshape(Xtrain[n_sample], (28, 28)),
                   interpolation='nearest', cmap=plt.cm.gray)  # 0...255
        plt.title(str(ytrain[n_sample]), fontsize=8)
        plt.axis('off')


n_digits = 10
digits = []
projections_x = [] # vertical
projections_y = [] # horizontal
for lab in range(n_digits):
    print(lab)
    idx = np.where(ytrain==lab)[0][0]
    ima_digit = np.reshape(Xtrain[idx], (nrows, ncols))
    digits.append(ima_digit)
    projections_x.append(np.sum(ima_digit, axis=0)/255.)    
    projections_y.append(np.sum(ima_digit, axis=1)/255.)
    
plt.figure()
plt.subplot(3,n_digits,1)
max_val = 20.
for i in range(n_digits):
    plt.subplot(3,n_digits,i+1)
    plt.imshow(digits[i],cmap=plt.cm.gray,interpolation='nearest')
    plt.subplot(3,n_digits,n_digits+i+1)
    plt.bar(range(28),projections_x[i])
    plt.ylim([0,max_val])
    plt.subplot(3,n_digits,2*n_digits+i+1)
    plt.bar(range(28),projections_y[i])
    plt.ylim([0,max_val])

plt.show(block=False)
