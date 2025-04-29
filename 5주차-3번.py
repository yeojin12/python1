try:
    a=input("입력할 파일의 이름: ")
    f=open(a,'r')
    s=f.read()
    print(s)
except FileNotFoundError:
    print("{} 파일이 존재하지 않습니다.".format(a))
finally:
    try:
        f.close()
    except:
        pass