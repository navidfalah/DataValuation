import numpy as np

def generate_synthetic_data(covariance_matrix, n_samples=1000):
    """Generate synthetic data given a covariance matrix."""
    mean = np.zeros(covariance_matrix.shape[0])
    data = np.random.multivariate_normal(mean, covariance_matrix, n_samples)
    return data

def calculate_eigenvalues(data):
    """Calculate eigenvalues of the covariance matrix derived from data."""
    covariance_matrix = np.cov(data, rowvar=False)
    eigenvalues, _ = np.linalg.eig(covariance_matrix)
    return eigenvalues

def calculate_diversity(buyer_eigenvalues, seller_eigenvalues):
    """Calculate the diversity between the buyer's and seller's eigenvalues."""
    return np.sqrt(
        (abs(buyer_eigenvalues[0] - seller_eigenvalues[0]) / max(buyer_eigenvalues[0], seller_eigenvalues[0])) *
        (abs(buyer_eigenvalues[1] - seller_eigenvalues[1]) / max(buyer_eigenvalues[1], seller_eigenvalues[1]))
    )

def calculate_relevance(buyer_eigenvalues, seller_eigenvalues):
    """Calculate the relevance between the buyer's and seller's eigenvalues."""
    return np.sqrt(
        (min(buyer_eigenvalues[0], seller_eigenvalues[0]) / max(buyer_eigenvalues[0], seller_eigenvalues[0])) *
        (min(buyer_eigenvalues[1], seller_eigenvalues[1]) / max(buyer_eigenvalues[1], seller_eigenvalues[1]))
    )

# Define the covariance matrices for the buyer and seller
buyer_covariance_matrix = np.array([[1, 0.1], [0.1, 0.25]])
seller_covariance_matrix = np.array([[0.5, 0.1], [0.1, 0.5]])

# Generate synthetic data
buyer_data = generate_synthetic_data(buyer_covariance_matrix)
seller_data = generate_synthetic_data(seller_covariance_matrix)

# Calculate the eigenvalues from the synthetic data
buyer_eigenvalues_from_data = calculate_eigenvalues(buyer_data)
seller_eigenvalues_from_data = calculate_eigenvalues(seller_data)

# Calculate diversity and relevance using eigenvalues from the synthetic data
diversity_from_data = calculate_diversity(buyer_eigenvalues_from_data, seller_eigenvalues_from_data)
relevance_from_data = calculate_relevance(buyer_eigenvalues_from_data, seller_eigenvalues_from_data)

# Output the results
print(f"Buyer Data Eigenvalues: {buyer_eigenvalues_from_data}")
print(f"Seller Data Eigenvalues: {seller_eigenvalues_from_data}")
print(f"Diversity from Data: {diversity_from_data}")
print(f"Relevance from Data: {relevance_from_data}")
