# -----------------------------------------------------------
# 전역변수(Global Variable)와 지역 변수(Local Variable)
# -
# -----------------------------------------------------------
# 사용자 정의 함수 ---------------------------------------------
def currnetDate(todays):
    # todays => 년, 월, 일을 원소로 담고 있는 데이터 타입, 리스트
    print(f'Today : {todays[0]}/{todays[1]:0>2}/{todays[2]:0>2}')

# 전역 변수 -----------------------------------------------------
year, month, day = 2024, 1, 8
todayList=[year, month, day]

# 함수 사용 즉 함수 호출 ------------------------------------------
print(f'year : {year}, month : {month}, day : {day}')

currnetDate(todayList)

# 변수 값 확인 출력
print(f'year : {year}, month : {month}, day : {day}')