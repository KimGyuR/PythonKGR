# ---------------------------------------------------------------
# str 데이터 타입과 관련된 내장 함수
# ---------------------------------------------------------------
# 원소/요소의 갯수를 알려 주는 내장 함수 => length의 약자 len() ===============
msg="christmas2023!"

print(f'len(msg) => {len(msg)}개')

#print(f'len(2024) => {len(2024)}개')   # 숫자 데이터는 길이 즉 원소/요소 없음


# 문자의 코드값을 알려 주는 내장 함수 => ord(문자1개) ==========================
print(f"ord('a') => {ord('a')}")

# Hello의 코드값 출력하기
codeH=ord('H')
codeE=ord('e')
codeL=ord('l')
codeO=ord('o')

print(f"Hello의 코드값 => {codeH} {codeE} {codeL} {codeL} {codeO}")
print(f"Hello의 코드값 => {bin(codeH)} {bin(codeE)} {bin(codeL)} {bin(codeL)} {bin(codeO)}")
print(f"Hello의 코드값 => {bin(codeH)[2:]} {bin(codeE)[2:]} {bin(codeL)[2:]} {bin(codeL)[2:]} {bin(codeO)[2:]}")


# 코드값에 해당하는 문자를 코드값을 반환해주는 내장 함수 => character의 약자 chr(코드값)  ==========================
# 코드값 65에 해당하는 문자 반환
print(f'char(65) => {chr(65)}')