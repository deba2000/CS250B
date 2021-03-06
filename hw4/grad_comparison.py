"""
grad_comparison.py

Compares the value of the derivatives calculated with backpropagation, versus 
an estimate calculated using a central difference approximation.
"""

import numpy as np
import matplotlib.pyplot as plt
from backprop import backprop,backprop_full
from training import full_j, compute_grad
from dataproc import format_data
from cross_validate import k_fold

def main():
    D = 4
    L = 2
    
    # randomly generate parameter values for testing
    np.random.seed(28031987)
    W1 = np.random.randn(D,2*D)
    b1 = np.random.randn(D)
    W2 = np.random.randn(2*D,D)
    b2 = np.random.randn(2*D)
    Wlabel = np.random.randn(L,D)
    
    # flattened arrays
    W1flat = W1.flatten()
    W2flat = W2.flatten()
    Wlabelflat = Wlabel.flatten()
    allflat = np.append(W1flat,b1)
    allflat = np.append(allflat,W2flat)
    allflat = np.append(allflat,b2)
    allflat = np.append(allflat,Wlabelflat)
    Np = len(allflat)
    
    # hyperparameters
    eps = 0.00000001
    lambda_reg = 0.0
    alpha = 0.2
    
    # get the data
    neg_list,pos_list = format_data()
    neg_list = neg_list[:1]
    pos_list = pos_list[:1]
    vocab = np.random.randn(268810,D)
    
    # do k_fold
    mean,SEM = k_fold(neg_list,pos_list,10,L,alpha,lambda_reg,vocab,normalized=False)
    exit(0)
    
    # calculate finite difference approximation to gradient
    numgrad = np.zeros(Np)
    for i in range(Np):
        print 'P ' + str(i)
        allflat[i] += eps
        fxpe = full_j(allflat,D,L,lambda_reg,alpha,neg_list,pos_list,
                      vocab,normalized=False)
        allflat[i] -= 2.0*eps
        fxme = full_j(allflat,D,L,lambda_reg,alpha,neg_list,pos_list,
                       vocab,normalized=False)
        allflat[i] += eps
        numgrad[i] = (fxpe - fxme)/(2.0*eps)
    
    # now use backprop
    bpgrad = compute_grad(allflat,D,L,lambda_reg,alpha,neg_list,pos_list,
                          vocab,normalized=False)
    
    print numgrad
    print bpgrad
    print numgrad-bpgrad

if __name__ == '__main__':
    main()
