n=int(input("Enter the number of students: "))
marks=[]
v=0
f=0
for i in range(n):
    marks.append(int(input("Enter the marks of student {}: ".format(i+1))))
    if marks[i]>=90 and marks[i]<=100:
        print("Excellent")
        v=v+1
    elif marks[i]>=75 and marks[i]<=89:
        print("Very Good")
        v=v+1
    elif marks[i]>=60 and marks[i]<=74:
        print("Good")
        v=v+1
    elif marks[i]>=40 and marks[i]<=59:
        print("Average")
        v=v+1
    elif marks[i]>=0 and marks[i]<=39:
        print("Fail")
        v=v+1
        f=f+1
    else:
        print("Invalid marks")
print("Total valid students: ",v)
print("Total failed students: ",f)