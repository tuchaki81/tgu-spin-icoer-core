# Núcleo do Spin Informacional
import numpy as np

def spin_resonance(input_vector, epsilon=1e-5):
    norm = np.linalg.norm(input_vector)
    if norm < epsilon:
        return 0.0
    return np.dot(input_vector, input_vector) / norm
