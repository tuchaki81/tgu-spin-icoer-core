# Índice de Coerência Informacional (ICOER) v7.0
from collections import Counter
import math

def icoer_from_pos_tags(pos_tags):
    counts = Counter(pos_tags)
    total = sum(counts.values())
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    normalized = 1 - entropy / math.log2(len(counts)) if len(counts) > 1 else 1.0
    return round(normalized, 4)
