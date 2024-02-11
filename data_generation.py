import numpy as np

def generate_synthetic_data(covariance_matrix, n_samples=1000):
    mean = np.zeros(covariance_matrix.shape[0])
    return np.random.multivariate_normal(mean, covariance_matrix, n_samples)
