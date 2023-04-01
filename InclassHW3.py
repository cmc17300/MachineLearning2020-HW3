#import numpy
import numpy as np
# --- Question A -----------------
#array with range 1-20
print("------Question A--------")
print("array with range 1-20: ")
a = np.random.randint(1,21, size=15)
print(a)

print()

print("Reshaped to 3x5: ")
#reshaped to 3X5
b = np.reshape(a,(3,5))
print(b)

print()

print("print array shape: ")
#print array shape
print(a.shape)

# --------------------------------
# --------- Question A, pt 2-----------
print("----Question A, pt2---------")
print("2 dimensional array of size 4x3: ")
array = np.random.randint(1,10, size=(4,3))
print(array)
print("Array shape: ")
print(array.shape)
print("type of array: ")
print(type(array))
print("replace max in each row by 0: ")
x = array[array.argmax()] = 0
print(x)
# ------- Question B --------------
# compute eigenvalues and eigenvectors
print("---------Question B----------")
print("creating array to calculate eigenvalues and eigenvectors: ")
m = np.array([[3, -2],
             [1, 0]])
w , v = np.linalg.eig(m)

print("printing the eigenvalues of given array:\n", w)
print("printing right eigenvectors of given array:\n", v)

# ------ Question C ------------
# compute sum of the diagonal element of an array
print("------Question C----------")
print("creating the array: ")
c_array = np.array([[0,1,2],
                    [3,4,5]])
print(c_array)
trace = np.trace(c_array)
print("diagonal element of given array: ")
print(trace)

# ----- Question D ----------
# numpy program to create new shape into an array without changing the data
print("----Question D-----------")
d_array = np.array([[1,2,3], [4,5,6]])
print("reshape to 3x2: ")
d = np.reshape(d_array,(3,2))
print(d)
print("reshape to 3x2: ")
dd = np.reshape(d_array,(2,3))
print(dd)


# ------- Matplotlib problems -------

#-----Question 1 -------




