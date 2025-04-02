N=int(input("숫자를 입력하시오: "))

if 1<=N<=150:
    for i in range(1,N+1):
        if i%7==0:
            continue
        if i>100:
            break
        print(i)