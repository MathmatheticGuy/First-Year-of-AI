# get position of all point
# evaluate it pivot. (center of all point)

import numpy as np


class KMeansClustering:
    
    def __init__(self, k=3):
        self.k = k;
        self.centroids = None
        
        
    # randomly find a centroid
    def fit(self, X, max_iterations=200):
        # uniform: phân bố
        self.centroids = np.random.uniform(np.amin(X, axis=0), np.amax(X, axis=0),
                                           size=(self.k, X.shape[1]))
        