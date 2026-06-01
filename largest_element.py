arr=[3,9,2,8]
def largest_element(arr):
    largest=arr[0]
    for i in arr:
        if i>largest:
            largest=i
    return largest
print(largest_element(arr))