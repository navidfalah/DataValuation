import numpy as np

def calculate_eigenvalues(data):
    covariance_matrix = np.cov(data, rowvar=False)
    return np.linalg.eig(covariance_matrix)

def calculate_diversity(buyer_eigenvalues, seller_eigenvalues):
    return np.sqrt((abs(buyer_eigenvalues - seller_eigenvalues) / np.maximum(buyer_eigenvalues, seller_eigenvalues)).prod())

def calculate_relevance(buyer_eigenvalues, seller_eigenvalues):
    return np.sqrt((np.minimum(buyer_eigenvalues, seller_eigenvalues) / np.maximum(buyer_eigenvalues, seller_eigenvalues)).prod())
