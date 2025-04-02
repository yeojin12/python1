n=int(input())

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

if 0<=n<=12:
    print(factorial(n))
else:
    print("0<=n<=12")