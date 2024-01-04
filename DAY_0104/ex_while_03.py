# --------------------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해지지 않은 경우
# --------------------------------------------------------------
# [요청] 사용자가 'x'입력 전까지 입력받은 데이터를 저장해 주세요.
# => 몇 번 입력할지 알 수 없음 ==> 무한 입력 받기
# => 종료 조건 ==> 사용자 'x' 입력
while True:
    data=input("저장하고 싶은 데이터 입력 (종료 x,X) : ")
    # 종료 검사
    # => break : 키워드가 있는 부분에서 비로 반복 종료, 아래 코드 실행 안됨
    # if data == 'x' or data == 'X':
    if data in ('x', 'X'): break

    print('ok')

print("프로그램 종료")

# -----------------------------------------------------------------
# [요청] 사용자로 부터 x/X 입력 전까지 계속 정수를 입력
#       입력 받은 정수 만큼 알파벳을 출력
# [예시] 출력 원하는 알파벳 수 입력 : 5
#       abcde
#       출력 원하는 알파벳 수 입력 : 1
#       a
#       출력 원하는 알파벳 수 입력 : 10
#       abcdefghij
#       출력 원하는 알파벳 수 입력 : 27
#       abcdefghijlmnopqrstuvwxyz 종료
#       출력 원하는 알파벳 수 입력 : x
#       종료
#  -----------------------------------------------------------------
# while True:
#     num = input("출력 원하는 알파벳 수 입력 : ")
#
#     # 무한 입력 반복 종료 조건
#     if num in ('x', 'X'): break  # 즉시 종료
#
#     num = int(num)
#     aCode=ord('a')
while True:
    count = input("출력 원하는 알파벳 수 : ")
    # 종료 코드
    if count in ('x', 'X'):
        print('프로그램 종료')
        break

    if count.isdecimal():
        count = int(count)

        aCode = ord('A')
        for value in range(count):
            value += aCode
            if value == ord('Z'): break
            print(f'value => {value}, {chr(value)}')

    else:
        print("정확한 데이터 아닙니다.")

print("--- 코드 끝 부분 ---")

isEnd=False

for n in range(100):
    if isEnd:
        print("프로그램 종료합니다")
        break

    print(f'out -> {n}')

    for n2 in range(100):
        if n2>10:
            isEnd=True
            break
        print(f'in -> {n2} ===> {n}번째')

# [요청] 내부에 반복문에서 데이터가 10초과되면 프로그램 종료 =====
outNum=1
isEnd=False

while outNum<=100:
    # 종료 조건 검사
    if isEnd:
        print("프로그램 종료")
        break
    print(f'outNum => {outNum}')

    # 내부 while
    inNum = 1
    while inNum<=100:
        if inNum>10:
            print("내부 종료")
            isEnd=True
            break
            print(f'inNum -> {outNum} ===> {outNum}번째')
            inNum += 1
    outNum += 1