import numpy as np

# Masking
arr = np.array([10, 20, 30, 40, 50])

mask = arr > 25

print("Original Array:")
print(arr)

print("\nMasked Values:")
print(arr[mask])

# Broadcasting
scaled = arr + 5

print("\nBroadcasting (+5):")
print(scaled)

# Cosine Similarity
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

vector1 = np.array([1, 2, 3])
vector2 = np.array([1, 2, 3])

vector3 = np.array([1, 0, 0])
vector4 = np.array([0, 1, 0])

print("\nCosine Similarity (vector1, vector2):")
print(cosine_similarity(vector1, vector2))

print("\nCosine Similarity (vector3, vector4):")
print(cosine_similarity(vector3, vector4))