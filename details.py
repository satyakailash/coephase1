name=int(input("Enter your name: "))
mobile_number=int(input("Enter your mobile number: "))
email=int(input("Enter your email: "))
password=int(input("Enter your password: "))
if name.isalpha():
    if len(name)<3 and len(name)<=15:
        print("valid")
    else:
        print("invalid")
if mobile_number.isdigit() and mobile_number.startswith("9") or index(0)=="8" or index(0)=="7" or index(0)=="6" :