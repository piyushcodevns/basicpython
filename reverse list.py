arr=[1,2,3,4]
def reverse_list(arr):
    reversed_array=[]
    for i in range(len(arr)-1,-1,-1):
        reversed_array.append(arr[i])
    return reversed_array
print(reverse_list(arr))