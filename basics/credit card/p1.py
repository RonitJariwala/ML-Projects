s=input()
if s[1:].isupper() or len(s)==1:
    r=s.swapcase()
    print(r)
else:
    print(s) 