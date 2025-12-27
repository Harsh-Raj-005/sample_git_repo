import numpy as np

#Your code for Question 1 here

arr1=np.array([0,1,2,3,4,5,6,7,8,9])
print(arr1)

#Your code for Question 2 here

arr2 = np.array([10, 20, 30, 40, 50])
arr2_multiplied = arr2*3
print(arr2_multiplied)

# Your code for Question 3 here

matrix =np.array([1,2,3,4,5,6]).reshape(2,3)
matrix_reshaped =matrix.reshape(3,2)

print(matrix_reshaped)


# Your code for Question 4 here

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

second_row =data[1:2,:]
last_column =data[:,2:3]

print("Second row:", second_row)
print("Last column:", last_column)


# Your code for Question 5 here

scores = np.array([85, 92, 78, 60, 95, 70])

high_scores =scores>80

print(high_scores)


# Your code for Question 6 here

angles = np.array([0, np.pi/2, np.pi])

sine_angles =np.sin(angles)

print(sine_angles)


# Your code for Question 7 here

data_points = np.array([1.5, 2.3, 0.8, 3.1, 4.0])

mean_val =np.mean(data_points)
std_dev =np.std(data_points)

print("Mean:", mean_val)
print("Standard Deviation:", std_dev)

# Your code for Question 8 here

zeros_matrix =np.zeros((3,3))
ones_matrix =np.ones((2,4))

print("Zeros Matrix:\n", zeros_matrix)
print("Ones Matrix:\n", ones_matrix)


# Your code for Question 9 here

col_vec = np.array([[10], [20], [30]])
row_vec = np.array([1, 2, 3])

broadcast_sum =col_vec+row_vec

print(broadcast_sum)


# Your code for Question 10 here

mat_A = np.array([[1, 2], [3, 4]])
mat_B = np.array([[5, 6], [7, 8]])

mat_C =np.dot(mat_A,mat_B)

print(mat_C)