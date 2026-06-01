arr=[7,3,9,1]
def smallest_element(arr):
    smallest=arr[0]
    for i in arr:
        if i<smallest:
            smallest=i
    return smallest
print(smallest_element(arr))