import numpy as np


# Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)    ## numpy.arange(start, end, gap)
#print("Original Vector:", vector)

# Reverse the vector using slicing
reversed_vector = vector[::-1]    ## [start:limit:gap] | slicing from 'start' to 'limit' with 'gap'
#print("Reversed Vector:", reversed_vector)



# Create a 1D array of 20 consecutive even numbers starting from 2
even_array = np.arange(2, 42, 2)
#print("Original 1D Array of even numbers:", even_array)

# Extract every third element starting from the second element
sliced_array = even_array[1::3]
#print("Every third element starting from the second:", sliced_array)



# Create 2D array of shape (5,5) with values from 1 to 25
matrix = np.arange(1, 26).reshape(5, 5)
#print("Original 2D Array:\n", matrix)

# Extract a subarray that includes only the 2nd and 4th rows and the 3rd and 5th columns
subarray = matrix[[1, 3], :][:, [2, 4]]
#print("Extracted Subarray:\n", subarray)



# Create two constant 1D arrays with 5 elements each
array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])

# Add the two arrays element-wise, and then multiply the result by 2
sum_array = np.add(array1, array2)
#print("Element-wise Sum:", sum_array)

mul_array = np.multiply(sum_array, 2)
#print("Multiplied by 2:", mul_array)

# Calculate the mean of the resulting array
mean_value = np.mean(mul_array)
#print("Mean of the Resulting Array:", mean_value)



# Define the 2D arrays
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8], 
              [9, 10], 
              [11, 12]])

# Perform element-wise multiplication between A and the transpose of B
element_wise_product = A * B.T    # must match dimensions
#print("Element-wise multiplication (A * B.T):\n", element_wise_product)

# Perform matrix multiplication (dot product) between A and B
dot_product_matrix = np.dot(A, B)
#print("Matrix multiplication (A dot B):\n", dot_product_matrix)

# Calculate the sum of all elements in the resulting dot product matrix
sum_of_elements = np.sum(dot_product_matrix)
#print("Sum of all elements in the dot product matrix:", sum_of_elements)



# Broadcasting
A = np.array([1, 2, 3])
B = np.array([[4, 5, 6], 
              [7, 8, 9], 
              [10, 11, 12], ])
result = B - A
#print("Result of broadcasting (B - A):\n", result)



# Define 1D array X and column vector Y
X = np.array([1, 2, 3])
Y = np.array([[10], [20], [30]])

# Use broadcasting to multiply X and Y
result = Y * X
print("Result of broadcasting (Y * X):\n", result)



A = np.array([[4, 7], 
              [2, 6]])

# Compute the inverst of array A
inverse_A = np.linalg.inv(A)
#print("Inverse of A:\n", inverse_A)

# Multiply the original array A with its inverse
identity_matrix = np.dot(A, inverse_A)
#print("A * inverse(A) (should be the identity matrix):\n", identity_matrix)