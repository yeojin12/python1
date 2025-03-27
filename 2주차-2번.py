N=int(input("범위를 입력하시오: "))

if 1<=N<=100:
    for i in range(1,N+1):
        if i%3==0:
            print(i) 