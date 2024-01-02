'''
논리 연산자 => and, or, not
- 결과 : True, False
- 동작방식
    * and => A and B : A, B 모두 True일때만 True
    * or  => A or B : A, B 중 하나 이상 True가 되면 True
    * not => not A : 현재 A의 상태를 반대로 => not True --> False, not False --> True : 토글링(toggle)
'''
no1=10
no2=3
#no1, no2 = 10, 3 이것도 됨

# and 연산자 -------------------------------------
# no1은 no2보다 크고 그리고 100보다 큰 수
print(no1>no2, no1>100)
print(no1>no2 and no1>100)
print(no1>no2 and no1>100 and no1>0)

# or 연산자 ------------------------------------------
# 1개 이상만 True가 되면 True로 결정
no1=10
no2=3

print(no1>no2, no1>100)
print(no1>no2 or no1>100)
print(no1>no2 or no1>100 or no1>0)

# not 연산자 -----------------------------------------
# 현재 값을 반대로 즉, True => False, False => True
# False => 0, True => 1 / 0이 아닌 모든 숫자
print(not False, not True)
print(not 0, not 1)
print(not 2, not -3, not 0.0)

'''
객체 비교 연산자 => is, is not
- 결과 : True, False
- 동작방식
    * is => A is B : A, B가 동일한 데이터 타입의 객체 여부
    * is not => A is not B : A, B가 서로 다른 데이터 타입의 객체 여부
'''
print(f'10 is 10 => {10 is 10},  10 == 10.0 => {10 == 10}')
print(f'10 is 10.0 => {10 is 10.0}, 10 == 10.0 => {10 == 10.0}')

# -----------------------------------------------------------------
# [실습1] 2개 숫자 데이터 입력 받은 후 2개의 값을 산술 연산 결과를 출력해 주세요
# [출력예시] 10+4=14
# ------------------------------------------------------------------
num1 = int(input('숫자 입력: '))
num2 = int(input('숫자 입력: '))
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2}')
print(f'{num1}//{num2}={num1//num2}')
print(f'{num1}%{num2}={num1%num2}')
print(f'{num1}**{num2}={num1**num2}')

# -----------------------------------------------------------------
# [실습2] [실습1]에서 입력받은 숫자 데이터를 활용하여 비교연산결과를 출력하세요
# [출력예시] 10>4 => True
#           10==4 => False
# ------------------------------------------------------------------
print(f'{num1}>{num2} => {num1>num2}')
print(f'{num1}<{num2} => {num1<num2}')
print(f'{num1}>={num2} => {num1>=num2}')
print(f'{num1}<={num2} => {num1<=num2}')
print(f'{num1}=={num2} => {num1==num2}')
print(f'{num1}!={num2} => {num1!=num2}')

# -----------------------------------------------------------------
# [실습3] [실습1]에서 입력 받은 숫자 데이터를 활용하여
# 최대값과 최소값을 추가로 입력 받은 후 논리 연산 결괄 출력하세요
# [출력예시] 10>4 and 10>최대값  => True
#           10>4 and 10>최소값  => True
#           not 10            => False
# ------------------------------------------------------------------
maxi = int(input('최대값 입력: '))
mini = int(input('최소값 입력: '))

# and 연산자 => 왼쪽/오른쪽 모두 True인 경우만 True가 됨
print(f'{num1}>{num2} and {num1}>{maxi} => {num1>num2 and num1>maxi}')
print(f'{num1}>{num2} and {num1}>{maxi} => {num1>num2 and num1>maxi}')

# or 연산자 => 왼쪽/오른쪽 모두 False인 경우만 False가 됨
print(f'{num1}>{num2} or {num1}>{maxi} => {num1>num2 or num1>maxi}')
print(f'{num1}>{num2} or {num1}>{maxi} => {num1>num2 or num1>maxi}')

# not 연산자 => not 데이터/변수명/연산식
print(f'not {num1} => {not num1}')
print(f'not {num2} => {not num2}')
