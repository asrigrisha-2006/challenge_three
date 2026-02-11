n=int(input("Enter the number of marks"))
marks=[]
for i in range(n):
    marks.append(input("Enter mark"))
c = 0
for i in range(n):
    str1 = marks[i]
    if str1.isdigit():
        if int(str1) >= 0 and int(str1) <= 100:
            print("valid marks")
        else:
            print("invalid marks")
            c = c + 1
    else:
        print("invalid marks")
        c = c + 1
print("the no of invalid marks are:", c)
