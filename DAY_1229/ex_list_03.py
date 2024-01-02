# --------------------------------------------------------------------
# list의 원소/요소 데이터 변경 및 삭제
# --------------------------------------------------------------------
# "Merry Christmas"의 문자 1개 1개를 원소로 가지는 리스트로 생성하기
chris = list("Merry Chrismas")

print(f'chris => {chris}')

# => ' ' 데이터를 '***' 변경하기
print(f'chris => {chris[5]}')

chris[5] = '***'
print(f'chris => {chris}')

# 삭제 ==> del 데이터 또는 del(데이터)
del chris[5]
print(f'chris => {chris}')

del(chris[5])
print(f'chris => {chris}')
