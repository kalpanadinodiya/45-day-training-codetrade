import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.arange(1, 11)

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

print("\nArray 1 Shape:", arr1.shape)
print("Array 1 Dtype:", arr1.dtype)
print("Array 1 Dimensions:", arr1.ndim)

print("\nArray 2 Shape:", arr2.shape)
print("Array 2 Dtype:", arr2.dtype)
print("Array 2 Dimensions:", arr2.ndim)

print("\nNegative Index:")
print(arr1[-1])

print("\nSlice:")
print(arr2[2:7])