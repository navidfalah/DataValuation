import os
import matplotlib.pyplot as plt


data_directory = "data"
os.makedirs(data_directory, exist_ok=True)

def plot_data_distribution(data, title, filename):
    plt.figure(figsize=(8, 6))
    plt.scatter(data[:, 0], data[:, 1], alpha=0.5)
    plt.title(title)
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.grid(True)
    filepath = os.path.join(data_directory, filename)
    plt.savefig(filepath)
    plt.close()

def plot_eigenvalues(eigenvalues, title, filename):
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(eigenvalues)), eigenvalues)
    plt.title(title)
    plt.xlabel('Eigenvalue Index')
    plt.ylabel('Eigenvalue')
    plt.grid(True)
    filepath = os.path.join(data_directory, filename)
    plt.savefig(filepath)
    plt.close() 
