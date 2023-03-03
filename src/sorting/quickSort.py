
def quicksort(arr):
    """
    QuickSort algorithm implementation.
    """
    if len(arr) <= 1:
        return arr

    # Choose the pivot element
    pivot = arr[len(arr) // 2]

    # Divide the array into three parts: elements smaller than the pivot,
    # elements equal to the pivot, and elements greater than the pivot
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right parts
    return quicksort(left) + equal + quicksort(right)
