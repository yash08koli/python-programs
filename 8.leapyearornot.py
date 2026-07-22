#check whether the year is leap year or not 
year = int(input("Enter a year: "))

   
if (year % 4 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")
