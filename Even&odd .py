#print the no.of even digits and odd digits from the given number
num=783781
rem=0
ocount=0
ecount=0
esum=0
osum=0
while num!=0:
     rem=num%10
     if rem%2==0:
          esum=esum+rem
          ecount=ecount+1

     else:
          ocount=ocount+1
          osum=osum+rem
     num=num//10
print("Even counts:",ecount)
print("Odd counts:",ocount)
print(esum)
print(osum) 