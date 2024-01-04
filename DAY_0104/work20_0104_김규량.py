# 1~100 숫자 출력하기
for i in range(1, 101):
    print(i)

# 3의 배수일 때와 5의 배수일 때 처리하기
for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 3과 5의 공배수 처리하기
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 코드 단축하기
for i in range(1, 101):
    print('Fizz'* (i%3==0) + 'Buzz'*(i%5==0) or i)

# 연습문제
for i in range(1, 101):
    if i%22==0:
        print('FizzBuzz')
    elif i%2==0:
        print('Fizz')
    elif i%11==0:
        print('Buzz')
    else:
        print(i)

# 심사문제
num1, num2 = map(int, input().split())

if (num1<num2) and (num1>=1 and num1<=1000) and (num2>=1 and num2<-1000):
    for i in range(num1,num2+1):
        if i%35==0:
            print('FizzBuzz')
        elif i % 7 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
else:
    print('값의 범위를 넘어갔거나 첫번째 수가 두번째 수보다 큽니다.')