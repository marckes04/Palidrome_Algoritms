#!/usr/bin/env python
# coding: utf-8

# In[3]:



def heapify(arr, n, i):
	largest = i 
	l = 2 * i + 1 
	r = 2 * i + 2 


	if l < n and arr[i] < arr[l]:
		largest = l


	if r < n and arr[largest] < arr[r]:
		largest = r


	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i]) 



		heapify(arr, n, largest)



def heapSort(arr):
	n = len(arr)


	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

# One by one extract elements

	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i]) 
		heapify(arr, i, 0)



arr = [12, 11, 13, 5, 6, 7, ]
heapSort(arr)
n = len(arr)
print('Sorted array is')
for i in range(n):
	print(arr[i])



# In[2]:


print(bubble_sort([1,4,6,3,5,6,3,9,9,5,6,7,9.4])


# In[ ]:




