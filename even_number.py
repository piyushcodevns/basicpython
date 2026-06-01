arr=[1,2,3,4,5,6,7]
def even_number(arr):
    even_number=[]
    count=0
    for i in arr:
        if i%2==0:
            even_number.append(i)
            count+=1
    return count
print(even_number(arr))