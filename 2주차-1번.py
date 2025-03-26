N=int(input("나이를 입력하세요: "))

if 0<=N<=120:
    if 0<=N<=12:
        print("500원")
    elif 13<=N<=18:
        print("1000원")
    elif 19<=N<=64:
        print("2000원") 
    else:
        print("무료")