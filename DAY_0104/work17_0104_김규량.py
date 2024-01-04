# while 반복문 형식(증가)
import random

i = 0       # 초기식
while i<10: # while 조건식
    print('Hello') # 반복할 코드
    i += 1 # 변화식

# while 반복문 형식(감소)
i = 10       # 초기식
while i>0: # while 조건식
    print('Hello') # 반복할 코드
    i -= 1 # 변화식

# 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while i < count:
    print('Hello', i)
    i += 1

count = int(input('반복할 횟수를 입력하세요: '))

while count>0:
    print('Hello', count)
    count -= 1

# random 모듈
print(random.random())
print(random.randint(1,6))

import random

i = 0
while i != 3:
    i = random.randint(1,6)
    print(i)

# while 무한 루프
while True:
    print("hello")

# 연습문제
i = 2
j = 5

while i<=32 or j>0:
    print(i, j)
    i *= 2
    j -= 1

# 심사문제
won = int(input())

while won>0:
    won -= 1350
    if won>=0:
        print(won)
    else:
        print("잔액이 부족합니다.")
