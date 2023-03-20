from numpy import random
import matplotlib.pyplot as plt
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[4, 5, 6], [7, 8, 9]]])

print(arr1)
print(arr2)
print(arr3)
print(arr3[0, 1, 2])
print(arr1[:3])
print(arr1[1:3])
print(arr1[1:])

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr4 = arr.reshape(4, 3)
arr5 = arr.reshape(2, 3, 2)

print(arr4)
print(arr5)

arr6 = np.array([1, 2, 3, 4, 5, 6, 7])
arr7 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr6[1:5:2])
print(arr6[::2])
print(arr7[1, 1:4])
print(arr7[0:2, 2])
print(arr7[0:2, 1:4])

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
arr5 = np.array([[7, 8, 9], [10, 11, 12]])
arr6 = np.concatenate((arr4, arr5), axis=0)
arr7 = np.concatenate((arr4, arr5), axis=1)

print(arr3, arr6, arr7)

x1 = random.randint(100)
x2 = random.randint(100, size=(5))
x3 = random.randint(100, size=(3, 5))

print(x1, x2, x3)

# 5 numbers between 0 to 1 that is float x5 = random.rand(2,3)

x4 = random.rand(5)
print(x4)

x1 = random.normal(size=(2, 3))
x2 = random.normal(loc=1, scale=2, size=(2, 3))

print(x1)
print(x2)

xpoints = np.array([0, 2, 4, 6, 10])
ypoints = np.array([0, 5, 17, 37, 102])

plt.plot(xpoints, ypoints)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("X vs Y")
plt.grid()
plt.plot(xpoints, ypoints, linestyle="dotted", linewidth='10', color='r')

x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])
x3 = np.array([4, 5, 6])
x4 = np.array([1, 2, 3])

plt.subplot(1, 2, 1)
plt.plot(arr1, arr2)
plt.title("plot 1")

plt.subplot(1, 2, 2)
plt.plot(arr3, arr4)
plt.suptitle("my plot")
plt.title("plot 2")
plt.show()

def func(x, y): return (x*y)

print(func(2, 4))
for i in range(5):
    print(i)

a = 200
b = 198
if b > a:
    print('b>a')
elif a == b:
    print('a==b')
else:
    print('b>a')
