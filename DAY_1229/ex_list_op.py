# -----------------------------------------------------------
# List 자료형의 연산 살펴보기
# - 산술연산
# - 비교연산
# - 멤버연산자
# -----------------------------------------------------------
# 1~50 범위의 2의 배수로 구성된 리스트 생성
nums = list(range(2,51,2))

# 산술연산 => 덧셈(+), 곱셈(*)
print(nums + ["a", "b"])

datas = nums + ["a","b"]
print(datas)

# list + str => list + list(str)
print(nums+list("ABC"))

# list + str => str(list) + str
print(str(nums)+"ABC")

# list * int => int만큼 원소를 반복해서 하나의 list
print(nums * 3)

# 멤버 연산 => in / not in
#         => 결과 : True/False
print("C" in datas)
print(1 in datas)