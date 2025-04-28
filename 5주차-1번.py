try:
    a=input("첫 번째 숫자: ")
    b=input("두 번째 숫자: ")
    c=input("연산자(+, _, *, /): ")

    if c == '+':
        result = int(a) + int(b)
    elif c == '-':
        result = int(a) - int(b)
    elif c == '*':
        result = int(a) * int(b)
    elif c == '/':
        result = int(a) / int(b)

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자만 입력 가능합니다.")
else:
    print("결과: ", result)
finally:
    print("종료")