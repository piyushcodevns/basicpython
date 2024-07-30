month=5

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    noofdays=31
elif month==4 or month==6 or month==9 or month==11:
    noofdays=30
elif month==2:
    noofdays="28/29"
else:
    noofdays="Invalid "

print(noofdays)