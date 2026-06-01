arr=[2,4,1,3,6]#2 6 7 10 16
left=int(input("Enter the number: "))
right=int(input("Enter the number: "))

prefix=[]
total=0

for num in arr:
    total+=num
    prefix.append(total)

if left==0:
    print(prefix[right])
else:
    print(prefix[right]-prefix[left-1])