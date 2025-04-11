'''1. Food – Smart Restaurant Billing with Meal Plans
Scenario:
A restaurant offers multiple meal plans (Veg, Non-Veg, Combo) and discounts on festivals.
 
Requirements:
 
Take user input: meal type, quantity, is today a festival (yes/no)
 
Pricing:
 
Veg: ₹150
 
Non-Veg: ₹200
 
Combo: ₹300
 
Festival day → 10% discount
 
If total bill > ₹1000 → add free dessert
 
Add 5% GST on total'''

'''veg = 150
nonveg = 200
combo = 300
bill = 0

meal = input("Enter the meal (veg/nonveg/combo): ")
quantity = int(input("Enter the quantity per person: "))
festival_input = input("Is it a festival : ")
festival = festival_input == "yes"

if meal == "veg":
    bill = veg*quantity
elif meal == "nonveg":
    bill = nonveg*quantity
else:
    bill = combo*quantity
if festival:
    bill -= (bill*10)/100
if bill == 1000:
    print("You got free dessert")
totalbill = bill+(bill * 5) / 100

print("Total bill",totalbill)'''

'''2. Education – Scholarship Eligibility Evaluator
Scenario:
University grants scholarships based on students’ marks and family income.
 
Requirements:
 
Input: student name, % in 10th, 12th, UG, family income
 
Rules:
 
85% in all and income < 3 LPA → Full Scholarship
 
70% in UG and income < 5 LPA → Partial Scholarship
 
Else → Not eligible'''

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
