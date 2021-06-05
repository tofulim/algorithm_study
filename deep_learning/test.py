import random

seed=42
random.seed(seed)
n = random.randint(1, 100)
print(n)
n = random.randint(1, 100)
print(n)
n = random.randint(1, 100)
print(n)

# # (1) 숫자리스트 샘플링
# numlist = [1,2,3,4,5,6,7,8,9]
# s = random.sample(numlist, 3)
# print(s)  # [1, 2, 8]
# s = random.sample(numlist, 3)
# print(s)  # [1, 2, 8]
# s = random.sample(numlist, 3)
# print(s)  # [1, 2, 8]
 
# # (2) 튜플 샘플링
# frutes = ('사과', '귤', '포도', '배')
# s = random.sample(frutes, 2)
# print(s)  # ['배', '사과']