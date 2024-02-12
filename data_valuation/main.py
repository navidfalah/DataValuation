import numpy as np
from covariance_analysis import calculate_eigenvalues, calculate_diversity, calculate_relevance
from visualization import plot_data_distribution, plot_eigenvalues
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def read_data(filename):
    try:
        data = np.loadtxt(filename)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except ValueError as e:
        raise ValueError(f"Error reading data from '{filename}': {e}")

def main(buyer_data_file, seller_data_file):
    buyer_data = read_data(buyer_data_file)
    seller_data = read_data(seller_data_file)

    buyer_covariance_matrix = np.cov(buyer_data, rowvar=False)
    seller_covariance_matrix = np.cov(seller_data, rowvar=False)

    buyer_eigvals, _ = np.linalg.eig(buyer_covariance_matrix)
    seller_eigvals, _ = np.linalg.eig(seller_covariance_matrix)

    diversity = calculate_diversity(buyer_eigvals, seller_eigvals)
    relevance = calculate_relevance(buyer_eigvals, seller_eigvals)

    print(f"Buyer Data Covariance Matrix:\n{buyer_covariance_matrix}")
    print(f"Seller Data Covariance Matrix:\n{seller_covariance_matrix}")
    print(f"Diversity: {diversity}")
    print(f"Relevance: {relevance}")

    plot_data_distribution(buyer_data, "Buyer Data Distribution", "buyer_data_distribution.png")
    plot_data_distribution(seller_data, "Seller Data Distribution", "seller_data_distribution.png")
    plot_eigenvalues(buyer_eigvals, "Buyer Eigenvalues", "buyer_eigenvalues.png")
    plot_eigenvalues(seller_eigvals, "Seller Eigenvalues", "seller_eigenvalues.png")

if __name__ == "__main__":
    buyer_data_file = 'matrixes/buyer_matrix.txt'
    seller_data_file = 'matrixes/seller_matrix.txt'
    try:
        main(buyer_data_file, seller_data_file)
    except Exception as e:
        print(f"An error occurred: {e}")
