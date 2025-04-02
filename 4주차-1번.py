N=int(input("학생 수: "))
if 1<=N<=100:
    dic={}
    for i in range(N):
        name,score=input().split()
        score=int(score)
        dic[name]=score
    ans=input()
    if ans in dic:
        print(dic[ans])
    else:
        print("학생을 찾을 수 없습니다.")
else:
    print("N의 크기를 확인해주세요")
