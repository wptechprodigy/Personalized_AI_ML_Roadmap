import numpy as np

def run_numpy_bridge():
    print("\n--- The Physics to NumPy Bridge Lab ---")

    # 1. BROADCASTING: The "Force Field" Analogy
    # In Physics, you apply a constant force to all particles.
    # In NumPy, we add a scalar to a vector.
    points = np.array([10, 20, 30])  # Positions
    gravity = 9.8                    # Scalar force
    
    # NumPy 'stretches' the scalar to [9.8, 9.8, 9.8] automatically
    new_positions = points + gravity 
    print(f"Broadcasting Result: {new_positions} (Scalar added to Vector)")

    # 2. MATRIX SYNTAX: The Linear Algebra Mirror
    # A = [1, 2], B = [3, 4]
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    # Hadamard Product (Element-wise) - Rarely used for transformation
    element_wise = A * B 
    
    # Matrix Multiplication (Dot Product) - The standard for ML/Physics
    matrix_mult = A @ B 

    print(f"\nElement-wise (A * B):\n{element_wise}")
    print(f"Matrix Mult (A @ B):\n{matrix_mult}")

    # 3. MEMORY VIEWS: Changing the "Observer" not the "Reality"
    # Create a 1D array of 6 elements
    raw_data = np.arange(6) # [0, 1, 2, 3, 4, 5]
    
    # Reshape to 2x3. 
    # IMPORTANT: The data in memory HAS NOT MOVED. 
    # NumPy just changed how it 'reads' the index.
    matrix_view = raw_data.reshape(2, 3)
    
    print(f"\nRaw Data: {raw_data}")
    print(f"Matrix View (Reshaped):\n{matrix_view}")
    
    # Prove they share memory: Change the view, the raw data changes
    matrix_view[0, 0] = 99
    print(f"\nModified View -> Raw Data is now: {raw_data}")
    print("INSIGHT: Reshaping is 'free' in terms of performance.")

if __name__ == "__main__":
    run_numpy_bridge()
