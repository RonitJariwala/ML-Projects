import sys

def solve():
    input_dta=sys.stdin.read()
    if not input_dta:
        return
    t=int(input_dta[0])
    idx=1
    ot=[]
    for _ in range(t):
        n=int(input_dta[idx])
        idx+=1
        half_n=n//2
        if half_n%2!=0:
            ot.append('NO')
        else:
            ot.append('YES')
            evens=[]
            odds=[]
            for i in range(1,half_n+1):
                evens.append(i*2)
            for i in range(1,half_n):
                odds.append(i*2-1)
            last_odd=(half_n*2-1)+half_n
            odds.append(last_odd)
            ans=evens+odds
            ot.append(" ".join(map(str,ans)))
    print('\n'.join(ot))

if __name__=='__main__':
    solve()