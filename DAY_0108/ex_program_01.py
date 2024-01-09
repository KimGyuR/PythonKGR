# -----------------------------------------------------------
# 나의 프로그램 - 계산기
# [계산기]
# 0. 입력
# 1. 덧셈
# 2. 뺄샘
# 3. 곱셈
# 4. 나눗셈
# 5. 종료
# -----------------------------------------------------------
# 사용자 정의 함수 ---------------------------------------------
# 함수 기능 : 연산 결과 리스트에서 검색어에 해당하는 데이터만 출력
# 함수 이름 : searchRes
# 매개 변수 : search
# 함수 결과 : None
# -----------------------------------------------------------
def searchRes(search):
    cnt = 0
    for calc in calclist:
        if search in calc:
            print(calc)
            cnt += 1
    print(f'{cnt}개의 검색결과 확인' if cnt else '검색결과가 없습니다.')


# 계산 기록 저장할 전역변수 선언
# -----------------------------------------------------------
calclist=[]

while True:
    print('[나의 계산기]')
    print('0. 입력')
    print('1. 덧셈')
    print('2. 뺄셈')
    print('3. 곱셈')
    print('4. 나눗셈')
    print('5. 기록보기')
    print('6. 검 색')
    print('7. 삭 제')
    print('8. 종료')
    choice = input('Select menu: ')
    if choice.isdecimal():
        if choice == '0':
            data=input('2개 정수 (예: 10 20) : ')
            n1, n2 = list(map(int, data.split()))

        elif choice =='1':
            calclist.append(f'덧셈: {n1} + {n2} = {n1+n2}')
            print(f'{calclist[-1]}\n')
        elif choice =='2':
            calclist.append(f'뺄셈: {n1} - {n2} = {n1-n2}')
            print(f'{calclist[-1]}\n')
        elif choice =='3':
            calclist.append(f'곱셈: {n1} * {n2} = {n1*n2}')
            print(f'{calclist[-1]}\n')
        elif choice =='4':
            calclist.append(f'나눗셈: {n1} / {n2} = {n1/n2 if n2 else "None"}')
            print(f'{calclist[-1]}\n')
        elif choice =='5':
            print("계산기록")
            calclist.sort(reverse=True)
            for calc in calclist:
                print(calc)
        elif choice == '6':
            search=input("검 색 : ")
            searchRes(search)
        elif choice == '7':
            calclist.clear()
            print('모든 계산 기록이 삭제 되었습니다.')
        elif choice =='8':
            print("프로그램 종료")
            break
        else:
            print('메뉴 0 ~ 8 선택가능합니다.')
    else:
        print('NO menu list')