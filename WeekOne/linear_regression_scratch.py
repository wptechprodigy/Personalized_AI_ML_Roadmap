import numpy as np
import matplotlib.pyplot as plt

def run_linear_regression():
    print("\n--- Task 2: Linear Regression from Scratch (Normal Equation) ---")
    np.random.seed(42)
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)
    X_b = np.c_[np.ones((100, 1)), X]
    theta_best = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
    intercept, slope = theta_best[0][0], theta_best[1][0]
    print(f"Calculated Intercept (Bias): {intercept:.4f} (Ideal: 4.0)")
    print(f"Calculated Slope (Weight):  {slope:.4f} (Ideal: 3.0)")

    X_new = np.array([[0], [2]])
    X_new_b = np.c_[np.ones((2, 1)), X_new]
    y_predict = X_new_b @ theta_best

    plt.figure(figsize=(10, 6))
    plt.plot(X_new, y_predict, "r-", linewidth=2, label="Predictions (Model)")
    plt.plot(X, y, "b.", alpha=0.5, label="Raw Data (Noisy)")
    plt.xlabel("Transactions per Second")
    plt.ylabel("Processing Latency (ms)")
    plt.title("FinTech System Performance Prediction")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig("regression_plot.png")
    print("SUCCESS: Model trained and plot saved.")

if __name__ == "__main__":
    run_linear_regression()
