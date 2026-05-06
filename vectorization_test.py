import numpy as np
import time

def run_performance_test():
    num_points = 1_000_000
    points = np.random.rand(num_points, 3)
    theta = np.radians(45)
    c, s = np.cos(theta), np.sin(theta)
    rotation_matrix = np.array([
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1]
    ])

    print(f"\n--- M1 Pro Performance Report: {num_points:,} Points ---")
    start_loop = time.time()
    loop_result = np.zeros_like(points)
    for i in range(num_points):
        loop_result[i] = np.dot(rotation_matrix, points[i])
    end_loop = time.time()
    loop_time = end_loop - start_loop
    print(f"Method A (Looping): {loop_time:.4f} seconds")

    start_vec = time.time()
    vec_result = points @ rotation_matrix.T 
    end_vec = time.time()
    vec_time = end_vec - start_vec
    print(f"Method B (Vectorized): {vec_time:.4f} seconds")

    speedup = loop_time / vec_time
    parity = np.allclose(loop_result, vec_result)
    
    print("-" * 45)
    print(f"Speedup Factor: {speedup:.1f}x faster")
    print(f"Mathematical Parity Check: {'PASSED' if parity else 'FAILED'}")
    print("-" * 45)

if __name__ == "__main__":
    run_performance_test()
