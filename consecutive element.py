a=[1,2,1,5,1,3,2,4]
k=3
n=len(a)
if k>n:
    print("Not possible")
else:
    currentsum=0
    for i in range(k):
        currentsum+=a[i]
    maxsum=currentsum
    maxpos=0
    for i in range(k,n):
        currentsum=currentsum+a[i]-a[i-k]
        if currentsum>maxsum:
            maxsum=currentsum
            maxpos=i
    print("Answer=",maxsum,a[maxpos:maxpos+k])