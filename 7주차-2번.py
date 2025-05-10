import random

numbers = list(range(1, 46))
random.shuffle(numbers)
lotto = sorted(numbers[:6])

print(f"이번 주의 추천 로또번호: {lotto}")
