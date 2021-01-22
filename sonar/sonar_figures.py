#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 12:27:20 2018

@author: joans
"""
import numpy as np
import matplotlib.pyplot as plt


def load_sonar():
    """
    Loads the UCI Sonar dataset described here :
    https://archive.ics.uci.edu/ml/datasets/Connectionist+Bench+%28Sonar,+Mines+vs.+Rocks%29
    and contained in file sonar.all-data (need to append .csv extension)
    """
    from csv import reader
    X = []
    y = []
    with open('sonar.all-data.csv', 'r') as f:
        csv_reader = reader(f)
        for row in csv_reader:
            # print(row)
            X.append([float(s) for s in row[:-1]])
            if row[-1] == 'M':
                y.append(0)
            elif row[-1] == 'R':
                y.append(1)
            else:
                assert False

    X = np.array(X)
    y = np.array(y).astype(np.int)
    print('Dataset sonar from sonar.all-data.csv')
    print('loaded {} samples of dimension {}, {} samples of mineral (label 0) and {} of rock (label 1)'
          .format(X.shape[0], X.shape[1], np.sum(y == 0), np.sum(y == 1)))
    return X, y


def plot_sonar(X, y, n_samples=10):
    """
    Plots a few first samples of each of the two classes
    """
    plt.figure()
    lines_mineral = plt.plot(X[y == 0][:n_samples].transpose(), 'b')
    lines_rock = plt.plot(X[y == 1][:n_samples].transpose(), 'r')
    plt.legend([lines_mineral[0], lines_rock[0]], ['mineral', 'rock'])
    plt.title(str(n_samples)+ ' samples per class')
    
    plt.figure()
    plt.plot(X[y == 0].transpose(), 'b:')
    plt.title('all samples for class mineral')

    plt.figure()
    plt.plot(X[y == 1].transpose(), 'r:')
    plt.title('all samples for class rock')

    plt.show(block=False)


if __name__ == '__main__':
    X_sonar, y_sonar = load_sonar()
    print('{} samples, {} dimensions per sample'\
          .format(X_sonar.shape[0], X_sonar.shape[1]))
    print('{} samples of class 0 and {} of class 1'\
          .format(np.sum(y_sonar == 0), np.sum(y_sonar == 1)))
    plt.close('all')
    plot_sonar(X_sonar, y_sonar)
