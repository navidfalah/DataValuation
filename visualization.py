import matplotlib.pyplot as plt

def plot_data_distribution(data, title):
    plt.figure(figsize=(8, 6))
    plt.scatter(data[:, 0], data[:, 1], alpha=0.5)
    plt.title(title)
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.grid(True)
    plt.show()

def plot_eigenvalues(eigenvalues, title):
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(eigenvalues)), eigenvalues)
    plt.title(title)
    plt.xlabel('Eigenvalue Index')
    plt.ylabel('Eigenvalue')
    plt.grid(True)
    plt.show()
