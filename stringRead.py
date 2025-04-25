str="hey well man my no is 8008 @!@#"
a=0
d=0
s=0
sp=0
v=0
for i in str:
    if i.isdigit():
        d=d+1
        
    elif i.isalpha():
        a=a+1
        
    elif i.isspace():
        s=s+1    
    elif i== 'a'or'e'or'i'or'o'or'u' or 'A'or'E'or'I'or'O'or'U':
        v=v+1
    else:
        sp+=1
print("No.of digits :",d )
print("No.of alphabets :",a )
print("No.of spaces :",s )
print("No of vowels:",v)
print("No.of special characters :",sp )





