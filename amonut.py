#ATM machine distribution of notes based on the amount
five=0
two=0
one=0
amount=int(input("Enter your amount :"))
if amount%100==0:
    if amount>=500:
        five=amount//500
        print("500 notes are",five)
        amount=amount-(five*500)
    if amount>=200:
        two=amount//200
        print("200 notes are",two)
        amount=amount-(two*200)
    if amount>=100:
        one=amount//100
        print("100 notes are",one)
else:
    print("Please enter multiples of 100 ")
