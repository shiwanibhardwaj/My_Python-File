name,age=input("enter your name and age:(seperate by comma): ").split(",")
age=int(age)
if name[0] == ('a' or 'A') and age<=10:
    print("You can watch coco movie")
else:
    print("sorry, you can't watch coco")