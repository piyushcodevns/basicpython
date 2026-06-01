arr=[3,-1,0,-5,8]

positive=0
negative=0

for num in arr:
    if num<0:
        positive+=1
    if num>0:
        negative+=1
        
print(f"Positive : {positive}, Negative : {negative}")