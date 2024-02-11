# Diversity and Relevance Analysis Package

This Python package provides tools for generating synthetic data based on covariance matrices, computing eigenvalues, and calculating the diversity and relevance of datasets in the context of covariance matrix analysis. It also includes visualization tools for plotting the data distributions and eigenvalues.

## Package Structure

The package is organized as follows:

div_rel_package/
│
├── init.py
│
├── data_generation.py
│ └── generate_synthetic_data
│
├── covariance_analysis.py
│ ├── calculate_eigenvalues
│ ├── calculate_diversity
│ ├── calculate_relevance
│
├── visualization.py
│ ├── plot_data_distribution
│ ├── plot_eigenvalues
│
└── main.py
└── Main execution script


### Modules

- `data_generation.py`: Contains functions related to the generation of synthetic data from a given covariance matrix.
- `covariance_analysis.py`: Includes functions for calculating eigenvalues, diversity, and relevance from data.
- `visualization.py`: Provides functions for visualizing data distributions and eigenvalues.
- `main.py`: The main script that uses functions from the other modules to perform the analysis and output results.

## Usage

To run the analysis, execute the `main.py` script. This will generate synthetic data, calculate the corresponding eigenvalues, and output the diversity and relevance measures. Additionally, it will produce plots for both the data distributions and the eigenvalues.

Ensure that you have `numpy` and `matplotlib` installed in your environment to handle calculations and visualizations, respectively.

## Installation

Clone this repository or download the package, navigate to the package directory, and install the required dependencies:

