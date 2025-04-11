
prev=int(input("Enter Prev units"))

pres=int(input("Enter Pres units"))
 
units=pres-prev 

bill=0

if units<=50:

    bill=units*0.50

elif units<=150:

    bill= 50*0.50+(units-50)*0.75

elif units<=250:

    bill=50*0.50+(100*0.75)+(units-150)*1.25

else:

    bill=50*0.50+(100*0.75)+(100*1.25)+(units-250)*2.50
 
 
bill=bill+(bill*18)/100
print(bill)