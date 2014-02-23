"""
runclassic400.py

Run script to perform LDA sampling on Classic 400 data.
"""

import numpy as np
import scipy.io

# First, load in the data
datadict = scipy.io.loadmat('../data/classic400.mat')

# Extract count data from dict, split into lists
classic400data = datadict['classic400']
doc_idx, vocab_idx = classic400data.nonzero()  # load doc, vocab indices
counts = classic400data.data  # load counts

K = 3  # cardinality of topic space

# Now randomly initialize q,n based on data
q = np.zeros(len(counts),K)
n = np.zeros(

for bi,count in enumerate(counts):
    
