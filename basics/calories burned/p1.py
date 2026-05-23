t=int(input())
while t>0:
    n,k=map(int,input().split())
    a = list(map(int, input().split()))
    if k in a:
        print('YES')
    else:
        print('NO')
    t-=1    
