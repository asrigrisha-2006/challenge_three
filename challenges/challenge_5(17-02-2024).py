n=int(input("Enter the number of items : "))
weights=[]
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entry=[]
v=0
a=0
for i in range(n):
    weights.append(int(input("Enter the weight of item"+str(i+1)+":")))
    if weights[i]<0:
        invalid_entry.append(weights[i])
    elif weights[i]<=5 and weights[i]>=0:
        very_light.append(weights[i])
        v=v+1
    elif weights[i]<=25 and weights[i]>=6:
        normal_load.append(weights[i])
        v=v+1
    elif weights[i]<=60 and weights[i]>=26:
        heavy_load.append(weights[i])
        v=v+1
    elif weights[i]>60:
        overload.append(weights[i])
        v=v+1
print("Original weights:")
print("very-light :",very_light)
print("normal-load :",normal_load)
print("heavy-load :",heavy_load)
print("overload :",overload)
print("Invalid entry :",invalid_entry)
l=input("Enter your name : ")
li=len(l.replace(" ",""))
lpi=li%3
if lpi==0:
    for item in overload:
        invalid_entry.append(item)
        a+=1
    overload.clear()
elif lpi==1:
    a = len(very_light)
    very_light.clear()
elif lpi==2:
    a = len(very_light) + len(overload) + len(invalid_entry)
    very_light.clear()
    overload.clear()
    invalid_entry.clear()
print("the length of name(l) is:",li)
print("LPI is: ",lpi)
print("Total valid items: ",v)
print("Total items affected after applying LPI are :",a)
print("weights after applying LPI:")
print("very-light :",very_light)
print("normal-load :",normal_load)
print("heavy-load :",heavy_load)
print("overload :",overload)
print("Invalid entry :",invalid_entry)
