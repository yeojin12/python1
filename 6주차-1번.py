N = int(input())
name = input().split()

list1 = sorted(name, key=lambda x: (len(x), x))

print(" ".join(list1))