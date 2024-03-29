# ---------------------------------------------------------
# [실습1] 임의의 숫자 데이터 7개를 저장한 리스트를 생성
#        리스트에 원소를 하나씩 화면에 한 줄에 한개씩 출력하세요
# ---------------------------------------------------------
nums = [25, 30, 21, 24, 28, 33, 38]
print(f'nums[0] => {nums[0]}')
print(f'nums[1] => {nums[1]}')
print(f'nums[2] => {nums[2]}')
print(f'nums[3] => {nums[3]}')
print(f'nums[4] => {nums[4]}')
print(f'nums[5] => {nums[5]}')
print(f'nums[6] => {nums[6]}\n')
# ---------------------------------------------------------
# [실습2] 아래 리스트에서 원소를 화면에 한 줄에 한개씩 출력하세요
# ---------------------------------------------------------
datas = [[10,20], [40,50], [70,80,90]]
print(f'0번째 원소 : {datas[0]}')
print(f'1번째 원소 : {datas[1]}')
print(f'2번째 원소 : {datas[2]}\n')

print(f'0-0번째 원소 : {datas[0][0]}')
print(f'0-1번째 원소 : {datas[0][1]}\n')

print(f'1-0번째 원소 : {datas[1][0]}')
print(f'1-1번째 원소 : {datas[1][1]}\n')

print(f'2-0번째 원소 : {datas[2][0]}')
print(f'2-1번째 원소 : {datas[2][1]}')
print(f'2-2번째 원소 : {datas[2][2]}\n')
# ---------------------------------------------------------
# [실습3] 좋아하는 계절과 월(month)을 입력 받은후 각각 변수에
#        저장하세요. 변수명은 season, month 입니다.
# ---------------------------------------------------------
word = input("좋아하는 계절과 월: ").split()

season = word[0]
month = word[1]

print(f'좋아하는 계절: {season}')
print(f'좋아하는 월: {month}월\n')

# ---------------------------------------------------------
# [실습4] 1~20으로 구성된 정수 리스트를 생성하세요.
#        * 3의 배수 인덱스에 해당하는 정수만 출력하세요.
#        * 3의 배수 인덱스에 해당하는 정수의 합계를 출력하세요.
# ---------------------------------------------------------
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
threeNums = nums[3::3]

print(f'3의 배수: {threeNums}')
print(f'3의 배수 합계: {threeNums[0]+threeNums[1]+threeNums[2]+threeNums[3]+threeNums[4]+threeNums[5]}')