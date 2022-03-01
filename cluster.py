import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

class cluster:

    def __init__(self, k=5, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
    
    def fit(self, X):
        #randomly select centroids 

        for i in range(self.max_iterations):
            self.labels_ = [np]
