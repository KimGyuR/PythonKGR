# 'Hello, world!' 문자열 100번 출력
print('Hello world!')
print('Hello world!')
print('Hello world!')
print('Hello world!')
print('Hello world!')
print('Hello world!')
print('Hello world!')
print('Hello world!')
print('Hello world!')
print('Hello world!')
print('Hello world!')
# ... 정성껏 복사+붙이기해서 하면 100번 적을 수 있음

''' for 변수 in range(횟수):
        반복할 코드
'''
for i in range(100):
    print("Hello world!")

# for 변수 in range(시작, 끝):
for i in range(5, 12):
    print("Hello world!", i)

# for 변수 in range(시작, 끝, 증가폭):
for i in range(0, 10, 2):
    print("Hello, world")

# for 숫자 감소시키기
for i in range(10, 0):
    print('Hello, world!', i)
# 기본변수가 증가하는 값이라 감소값을 넣어줘야 감소시키는 출력문을 낼 수 있음

for i in range(10, 0, -1):
    print('Hello, world!', i)

for i in reversed(range(10)):
    print('Hello, world!', i)

# 입력한 횟수대로 반복하기
count = int(input("반복할 횟수를 입력하세요: "))

for i in range(count):
    print('Hello, world!', i)

# 시퀀스 객체로 반복하기
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in 'Python':
    print(letter, end=' ')

for letter in reversed('Python'):
    print(letter, end=' ')

# 연습문제
x = [49, -17, 25, 102, 8, 62, 21]
for nx in x:
    print(nx*10, end=' ')

# 심사문제
num = int(input())
for i in range(1,10,1):
    print(f'{num} * {i} = {num*i}')