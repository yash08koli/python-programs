#evaluate student performance 
percentage = float(input("Enter the student's percentage: "))


if percentage > 90:
    print("Performance: Excellent")
elif percentage > 80:
    print("Performance: Very Good")
elif percentage > 70:
    print("Performance: Good")
elif percentage > 60:
    print("Performance: Average")
else:
    print("Performance: Poor")
