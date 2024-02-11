import numpy as np
from data_generation import generate_synthetic_data
from covariance_analysis import calculate_eigenvalues, calculate_diversity, calculate_relevance
from visualization import plot_data_distribution, plot_eigenvalues
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


buyer_covariance_matrix = np.array([[1, 0.1], [0.1, 0.25]])
seller_covariance_matrix = np.array([[0.5, 0.1], [0.1, 0.5]])

buyer_data = generate_synthetic_data(buyer_covariance_matrix)
seller_data = generate_synthetic_data(seller_covariance_matrix)

buyer_eigvals, buyer_eigvecs = calculate_eigenvalues(buyer_data)
seller_eigvals, seller_eigvecs = calculate_eigenvalues(seller_data)

diversity = calculate_diversity(buyer_eigvals, seller_eigvals)
relevance = calculate_relevance(buyer_eigvals, seller_eigvals)

print(f"Buyer Data Eigenvalues: {buyer_eigvals}")
print(f"Seller Data Eigenvalues: {seller_eigvals}")
print(f"Diversity: {diversity}")
print(f"Relevance: {relevance}")

plot_data_distribution(buyer_data, "Buyer Data Distribution", "buyer_data_distribution.png")
plot_data_distribution(seller_data, "Seller Data Distribution", "seller_data_distribution.png")
plot_eigenvalues(buyer_eigvals, "Buyer Eigenvalues", "buyer_eigenvalues.png")
plot_eigenvalues(seller_eigvals, "Seller Eigenvalues", "seller_eigenvalues.png")

