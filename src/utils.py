"""
utils.py
Purpose: Helper functions for plotting, evaluation, etc.
"""

import matplotlib.pyplot as plt

def plot_actual_vs_predicted(y_actual, y_pred, title="Actual vs Predicted"):
    plt.figure(figsize=(8,6))
    plt.scatter(y_actual, y_pred)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title(title)
    plt.show()
