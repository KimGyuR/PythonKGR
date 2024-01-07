# -------------------------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수 (1)
# - 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 형태 : def 함수명( *data ):
# - 가변 인자 함수
# - 매개변수 개수 : 0 ~ N개
# -------------------------------------------------------------------
# 2개 정수를 덧셈 후 결과를 반환 하는 함수 생성 ----------------------------
def plusTwo(a, b):
    return a+b

# 5개 정수를 덧셈 후 결과를 반환 하는 함수 생성 ----------------------------
def plusFive(a, b, c, d, e):
    return a+b+c+d+e

# 3개 정수를 덧셈 후 결과를 반환 하는 함수 생성 ----------------------------
def addThree(a, b, c):
    return a+b+c

# 7개 정수를 덧셈 후 결과를 반환 하는 함수 생성 ----------------------------
def plusSeven(a, b, c, d, e, x, y):
    return a+b+c+d+e+x+y

# -------------------------------------------------------------------
# 함수 기능 : 전달 받은 숫자를 모두 덧셈한 결과 반환 기능
# 함수 이름 : addNumber
# 매개 변수 : *num
# 반 환 값 : 계산 결과
def addNumber(*num):
    print(type(num))
    nums = 0
    for n in num:
        nums+=n
    return nums

# 함수 사용 즉 함수 호출
print(addNumber(1,2,3))
print(addNumber(10))
print(addNumber())
print(addNumber(1,2,3,4,5,6,7,8,9))

# *시퀀스/반복이 가능한 객체 => 내부에 모든 원소를 하나씩 풀어서 전달 : 언팩킹
print(addNumber(*range(1,11)))

a = [11,22,33,44]
aTuple='a', 'b', 'c'
aDict={'name':'Hong', 'age':100}

print(a, aTuple, aDict)
print(*aDict, sep=' ')