arr = [10, 5, 20, 8, 15]
max1 = max(arr)
max2 = -1
for x in arr:
    if x != max1 and x > max2:
        max2 = x
print("2nd max =", max2)
