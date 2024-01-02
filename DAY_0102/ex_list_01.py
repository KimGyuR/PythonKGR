# ---------------------------------------------------------------
# List => 여러 개의 데이터를 저장하는 데이터 타입
# - 문법 => [데이터1, 데이터2, ...., 데이터n]
# - 원소/요소 => 식별하기 위해서 인덱스(Index) : 파이썬에 명명
# - 인덱싱 기능/슬라이싱 기능 모두 사용 가능
# ---------------------------------------------------------------
# 1~50 범위의 7의 배수에 해당하는 정수로 구성된 리스트 생성
# => 7, 14, 21, 28, 35,42, 49
# => 시작 7
# => 간격 7
# => 끝 49
# 7의 배수 정수 범위 객체
sevens = range(7,50,7)

# => range ==> list 형변환
sevens = list(sevens)

print(sevens)

# str 데이터 타입 => 인덱싱 ---->요소 변경 X
# 제일 첫번째 인덱스에 있는 원소 삭제
# ===> del 삭제하고 싶은 데이터 또는 del(삭제하고 싶은 데이터)
del sevens[0]
del (sevens[0])
print(sevens)

# del sevens # 리스트 객체 주소를 저장하는 변수 삭제

# str 데이터 타입 => 인덱싱 ---->요소 추가
# 리스트에 인덱싱 방식으로 원소/요소 데이터 변경 가능
# 요소 갯수 5개 => 0 ~ 4
sevens[4] = 56
print(f'sevens => {sevens}')
