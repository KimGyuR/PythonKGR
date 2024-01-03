# 1~100 범위에서 2의 배수에 해당한 정수로 리스트 생성 ------------------------------
twoX = list(range(2,101,2))

# "246810.............100"
# twoX=str(twoX)
# print(twoX)
# print(twoX[0], twoX[-6], twoX[-2], twoX[-1])

# int ==> str 형변환

# -------------------------------------------------------------------
# 시퀀스 데이터 타입에서 원소/요소를 하나씩 빼서 반복코드 수행 => for in 반복문
# -------------------------------------------------------------------
# "24681012141618....100"
strNum=''
for num in twoX:
    strNum = strNum+ str(num)
print(f"strNum => {type(strNum)}\n{strNum}")

# 리스트 안에 모든 원소를 str 타입으로 변환해서 저장
# 데이터의 인덱스 범위 => 0 ~ len(data)-1
print(f'[Before] twoX => {twoX}')

for idx in range(len(twoX)):
    twoX[idx]=str(twoX[idx])
print(f'[After] twoX => {twoX}')