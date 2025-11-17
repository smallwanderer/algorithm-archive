import numpy as np
import math

def normal_distribution(size = 4000):
    temp = []
    for i in range(size):
        x = np.random.randn()
        y = np.random.randn()
        if -1<=x<=1 and -1<=y<=1:
            temp.append((x, y))
    return temp

def uniform_distribution(size = 4000):
    temp = []
    for i in range(size):
        temp.append(np.random.uniform(-1, 1, 2))
    return temp

def monte_carlo_temp():
    inside = 0
    arr1 = normal_distribution()
    arr2 = uniform_distribution()

    for x, y in arr1:
        if x**2 + y ** 2 <= 1:
            inside += 1

    return inside/len(arr1) * 4

a = list("11111")
a[2] = '4'
print(a)