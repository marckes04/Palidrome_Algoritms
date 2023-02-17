#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left_partition = [x for x in arr[1:] if x <= pivot]
        right_partition = [x for x in arr[1:] if x > pivot]
        return quick_sort(left_partition) + [pivot] + quick_sort(right_partition)
    
    
print(quick_sort([2,4,5,67,3,4,5,78,4,9]))

