a,b,c=map(int,input().split())
if -1000<=a<=1000 and -1000<=b<=1000 and -1000<=c<=1000:
    t=(a,b,c)
    print(t.index(max(t)))