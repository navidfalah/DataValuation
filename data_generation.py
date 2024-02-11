import numpy as np

def generate_synthetic_data(covariance_matrix, n_samples=1000, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)

    mean = np.zeros(covariance_matrix.shape[0])
    synthetic_data = np.random.multivariate_normal(mean, covariance_matrix, n_samples)
    return synthetic_data
