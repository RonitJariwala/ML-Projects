n = int(input())
st=list(map(int,input().split()))
crime_count = 0
police_available = 0
for i in st:
    if i==-1:
        if police_available>0:
            police_available-=1
        else:
            crime_count+=1
    else:
        police_available+=i
print(crime_count)            