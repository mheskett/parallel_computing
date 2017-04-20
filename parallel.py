import multiprocessing
import os


a = [0]*1000
a = [a]*1000
for i in range(0,1000):
	for j in range(0,1000):
		a[i][j] = 0.0005 * (i+1) + 0.0005 * (j+1)

print(a)
print(multiprocessing.cpu_count())