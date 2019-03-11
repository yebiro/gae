import numpy as np
import tensorflow as tf
from scipy.sparse import csr_matrix
import pickle
from networkx import to_numpy_matrix
import gzip

def load_data():
    with open('data/ind.WikiVote.graph') as f:
        with open('data/ind.Wiki.graph', 'wb') as fb:
            #print(type(f.read()))
            pickle.dump(f.read(), fb)

load_data()