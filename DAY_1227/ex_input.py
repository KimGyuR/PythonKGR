'''
표준입력기능의 내장함수 => input()
- 문법 : input("요청 메시지")
- 결과 : 입력받은 데이터, 데이터 종류는 str
'''
# 이름을 입력 받기 ==> input
name = input("이름이 뭐니? ")

# 입력받은 데이터 출력하기 ==> print()
print("당신 이름은 ", name, "이군요")
print("당신 이름은 %s이군요"%name)
print(f'당신 이름은 {name}이군요')

# 나이 입력 받기 => input
age=input("몇 살이야?")

# 입력받은 나이와 타입 출력
print(age, type(age))

# 숫자 2개를 입력 받기 => input() 2개
num1=input('정수 1개 입력: ')
num2=input('정수 1개 입력: ')

print(num1, type(num1), num2, type(num2))

# ----------------------------------------------------------
# str ==> int 타입으로 형 변환 즉, 타입 캐스팅(Type casting)
# - 함수 : 타입명(데이터)
#         str(데이터) : 데이터를 str 타입으로 형변환
#         int(데이터) : 데이터를 int 타입으로 형변환
#         float(데이터) : 데이터를 float 타입으로 형변환
#         bool(데이터) : 데이터를 bool 타입으로 형변환
# ---------------------------------------------------------
# 입력받은 정수 2개 정수로 타입 변환
num1 = int(num1)
num2 = int(num2)

print(num1, type(num1), num2, type(num2))

# -----------------------------------------------------------
# 계산하기 => 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/)
# -----------------------------------------------------------
# [출력] 10 + 30 = 40
print(f'{num1}+{num2} = {num1+num2}')
print(f'{num1}-{num2} = {num1-num2}')
print(f'{num1}*{num2} = {num1*num2}')
print(f'{num1}/{num2} = {num1/num2}')

# -----------------------------------------------------------
# 계산하기 => 몫(//), 나머지(%)
# -----------------------------------------------------------
print(f'{num1}//{num2} = {num1//num2}')
print(f'{num1}%{num2} = {num1%num2}')

# -----------------------------------------------------------
# 계산하기 => 제곱근(**)
# -----------------------------------------------------------
print(f'{num1}**{num2} = {num1**num2}')
