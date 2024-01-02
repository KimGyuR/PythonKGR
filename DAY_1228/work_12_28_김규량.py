#1
#1-1 'kim1234@naver.com' 데이터에서 @ 앞부분만 출력
sentence = 'kim1234@naver.com'
print(sentence[0:7]) # @ 앞부분 출력
print(sentence[7]) # @만 출력

#1-2 'http;//www.naver.com' 데이터에서 도메인 이름만 출력
sentence = 'http;//www.naver.com'
print(sentence[-9:])

#1-3 '홍길동'에서 이름만 출력
name = '홍길동'
print(name[1:])
print(name[1], name[2], sep='')

#1-4 AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr에서 대문자, 소문자 따로 출력
seq = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
print(seq[1::2])
print(seq[0::2])

#1-5 ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ에서 숫자만 출력
seq = 'ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ'
print(seq[3::4])

#1-6 주민등록번호는 881120-1068234입니다.
#     주민등록번호를 생년월일 부분과 숫자부분으로 나누어 출력하세요.
idnum = '881120-1068234'
print("생년월일:", idnum[:6], "숫자부분:", idnum[-7:-1])

#2
num = int(input("정수 입력 : "))

print(f'10진수 {num} \n16진수: {hex(num)} \n8진수: {oct(num)} \n2진수: {bin(num)}')

#3
word1 = input("단어 입력: ")
word2 = input("단어 입력: ")
word3 = input("단어 입력: ")

print(f'코드 값이 가장 큰 단어 : {max(word1, word2, word3)}')
print(f'코드 값이 가장 작은 단어 : {min(word1, word2, word3)}')

#4
sentence = "내년 갑진년 용띠해 날아오르라!"
print("내년 갑진년 용띠해 날아오르라!")

word = input("단어 입력: ")
print(f'{word}단어 메시지 존재 여부 : {word in sentence}')
print(f'{word}단어 메시지 존재 여부 : {word not in sentence}')

#5
word = input("단어 입력: ")
print(f'{word}코드값: {bin(ord(word[0]))}{bin(ord(word[1]))[2:]}{bin(ord(word[2]))[2:]}')
print(f'{word}코드값: {hex(ord(word[0]))}{hex(ord(word[1]))[2:]}{hex(ord(word[2]))[2:]}')