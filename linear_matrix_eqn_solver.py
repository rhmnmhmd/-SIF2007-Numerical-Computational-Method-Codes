import numpy as np
import math

A = [[14, 14, -9, 3, -5],
     [14, 52, -15, 2, -32],
     [-9, -15, 36, -5, 16],
     [3, 2, -5, 47, 49],
     [5, 32, 16, 49, 79]
     ]

b = [-15, -100, 106, 329, 463]

solution = np.linalg.solve(A, b)

print(solution)


























