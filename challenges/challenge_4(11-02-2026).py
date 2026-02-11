num=int(input("enter the number of elements in the list: "))
list1=[]
number_list=[]
string_list=[]
n=0
s=0
for i in range(num):
    list1.append(input("enter the elements {}: ".format(i+1)))
    if list1[i].isdigit():
        number_list.append(int(list1[i]))
        n=n+1
    elif list1[i].isalnum() and list1[i] != "":
         string_list.append(list1[i])
         s=s+1
reg=int(input("Enter the last four digits of your registration number: "))
print("the original number list is :",number_list)
print("the original string list is :",string_list)
a=reg%10
if a%2==0:
    number_list.reverse()
    print("the number list after personalized check :",number_list)
else:
    string_list.reverse()
    print("the string list after personalized check :",string_list)
print("Total numbers: ",n)
print("Total strings: ",s)


