def isLeap(a):
    if(a%400 == 0):
        print(a,"is a leap year")
    elif(a%4 == 0 and a%100 != 0):
        print(a,"is a leap year")
    else:
        print(a,"is not a leap year")
year = int(input("Enter the year:"))
isLeap(year)


