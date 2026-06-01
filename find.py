arr=[2,3,2,5,2]
target=2
found=False
positions=[]
for i in range(len(arr)):
    if arr[i]==target:
        positions.append(i)
        found=True
if found:
    print(f"{target} found at indices {positions}")
else:
    print(f"{target} not found")