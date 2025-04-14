#calculation of gross salary based on the basic salary and hra and da

basic_sal=int(input("enter your salary : "))
hra=0
da=0
if  basic_sal<20000:
    hra=(basic_sal*76)/100 
    da=(basic_sal*78)/100
elif basic_sal>30000:
    hra=(basic_sal*85)/100 
    da=(basic_sal*89)/100
else:
    hra=(basic_sal*79)/100 
    da=(basic_sal*82)/100
gross_sal=basic_sal+da+hra
print("your gross salary is : ",gross_sal)