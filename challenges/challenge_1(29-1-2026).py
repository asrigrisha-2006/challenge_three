name=input("Enter your full name")
mail=input("Enter your email id")
number=input("enter your phone number")
age=int(input("enter your age"))
c=0
if name.count(" ")<1:
    c=1
elif name[0]==' ' or name[-1]==' ':
    c=1
if '@' not in mail or '.' not in mail:
    c=1
elif mail[0]=='@':
    c=1
if len(number)!=10:
    c=1;
elif not number.isdigit():
    c=1
elif number[0]=='0':
    c=1
if age<18 or age>60:
    c=1
if(c==0):
    print("Your profile is valid")
else:
    print("Your profile is invalid")
