n=int(input("Enter the number of songs"))
duration=[]
s=0
l=0
for i in range(n):
    d=int(input("Enter duration of song "+str(i + 1)+" in seconds: "))
    duration.append(d)
for i in range(n):
    if duration[i]<=0:
        print("Invalid Playlist")
        exit()
sum1=sum(duration)
length=len(duration)
duration.sort()
print("Total Duration : ",sum1)
print("Total songs : ",length)
repetitive=False
for i in range(length - 1):
    if duration[i]==duration[i+1]:
        repetitive=True
        break
if repetitive:
          print("Category: Repetitive Playlist")
          print("Recommendation: Add variety")
elif sum1<300:
        print("Category: Too short Playlist")
        print("Recommendation: add some more songs")
elif sum1>3600:
        print("Category: Too long Playlist")
        print("Recommendation: Reduce the duration")
else:
        print("Category: Balanced Playlist")
        print("Recommendation: Good listening session")










