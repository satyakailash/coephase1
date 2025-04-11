internal=int(input("Internal Score"))
external=int(input("External Score"))
project=int(input("Project"))
if internal>=50 and external >=50 and project >=50:
    sum=internal+external+project
    print("Total score :",sum)
    grade=((70/100*project) + (20/100*external) + (10/100*internal))
    print("Average :",grade)
    if grade >=90:
        print("Grade is A")
    elif grade >=70:
        print("Grade is B")
    else:
        print("Grade is C")
