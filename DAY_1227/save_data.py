"""
데이터를 메모리에 저장하는 방법
=> 파이썬 문법 : 변수명 = 저장할 데이터
=> 파이썬의 변수는 힙영역에 저장된 데이터 주소를 저장하는 변수
=> 참조 변수
"""
# 나이를 메모리에 저장하기
# => 나이 : 정수 int ===> 힙 영역
# => 변수 ==> age
age=100
#'age'=100

# 이름을 메모리에 저장하기
# => 이름 : 문자 str ===> 힙 영역
# => 변수 ==> name
_name="김규량"
name="김규량"
my_name="김규량"
name99="김규량"
# 99name="김규량"   <== X 숫자는ㄴ 변수이름으로 첫 번째 불가

# 메모리에 저장은 됨 => 저장된 데이터 위치 알 수 없음 => 다시 사용 불가
2024
"hppy"

year=2024       # 2024 데이터가 저장된 주소를 year 이름이 붙은 메모리 저장
print(year)

# ----------------------------------------------------------------------
# 데이터의 주소를 확인하는 내장함수 => id( 실제 데이터) / id( 변수명 )
# ----------------------------------------------------------------------
print( id(2024) )
print( id(year) )

year=2023
print( id(year) )

year='2023'
print( id(year) )

# ----------------------------------------------------------------------
# 변수가 저장하고 있는 데이터의 종류 즉, 데이터 타입을 알려주는 함수
# => type(데이터) 또는 type(변수명)
# ----------------------------------------------------------------------
print(type(2024))
print(type(4.))
print(type('4.'))
