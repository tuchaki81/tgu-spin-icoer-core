# Treinador Fractal de Ressonância
def spin_sync_loop(data, spin_func):
    result = []
    for item in data:
        coherence = spin_func(item)
        result.append(coherence)
    return result
