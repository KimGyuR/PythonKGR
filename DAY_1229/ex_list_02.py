# -----------------------------------------------------
# 다양한 리스트 생성
# -----------------------------------------------------
# 실수 데이터로 구성된 리스트 생성
floatNums = [4., 2.1, 3.2, 5.01]

# str 데이터로 구성된 리스트 생성
strNums = ['33', '21', '25']

# bool 데이터로 구성된 리스트 생성
boolNums = [False, True, False, True, True]

# 다양한 데이터 타입으로 구성된 리스트 생성
nums = ['100', 98, False, 7.31, 'Apple', True]

# 빈 리스트 생성
nums = []

# 리스트 안에 리스트 데이터로 구성된 리스트 생성
nums = [10, 20, 30, ['A', 'B'], 100, 200]

# 리스트의 요소 출력
print(f'nums[0] => {nums[0]},{type(nums[0])}' )
print(f'nums[1] => {nums[1]},{type(nums[1])}' )
print(f'nums[2] => {nums[2]},{type(nums[2])}' )
print(f'nums[3] => {nums[3]},{type(nums[3])}' )
print(f'nums[4] => {nums[4]},{type(nums[4])}' )
print(f'nums[5] => {nums[5]},{type(nums[5])}' )

print(f'nums[3] => {nums[3][1]},{type(nums[3][1])}' )