name=input("Enter your good name: ")
tenth=float(input("Enter your 10th per :"))
twelth=float(input("Enter your 12th per :"))
ug=float(input("Enter your UG per :"))
income=int(input("Enter your family income per Annum :"))

if tenth>85 and twelth>85 and ug>85 and income<=300000:
    print("your are Eligible for Full scholarship")
elif ug>70 and income<=500000:
    print("your are Eligible for partial scholarship")
else:
    print("your not Eligible for Scholarship")
