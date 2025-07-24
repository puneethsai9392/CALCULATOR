def my_fun(y):
    if y%400==0:
        return f"the leap year is{format(y)}"
    elif(y%4==0) and (y%100!=0):
        return f"the leasp is{format(y)} "
    else:
        return f"it is not leap year{format(y)}"
year=int(input("enter the year in loop year"))
mn=my_fun(year)
print(mn)
 