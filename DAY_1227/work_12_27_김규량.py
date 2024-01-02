# 1 아래 데이터를 저장하는 코드 작성
# 자신 고향 도시, 혈액형, 좋아하는 계절, 키, 전화번호, 국적 저장
city = 'Daegu'
blood = 'O'
season = 'winter'
tall = 183
number = "010-8523-0783"
country = 'Korea'

# 블럭 선택 코드 => shift + alt + E
# 2 화면출력 되도록 코드 작성
# [신상 정보]
# MBTI : INFP   혈액형 : A     성별 : M
# 몸무게 : 95    키 : 183
# 2-1 여러데이터 출력 방식
mbti = 'ISFP'
blood = 'O'
gender = 'M'
height = 183.1
weight = 95
print("[ 신상 정보 ]")
print('MBTI :', mbti, '혈액형 :', blood, '성별 :', gender, sep='   ')
print('몸무게 :', weight, '키 :', height, sep='    ')

# 2-2 서식지정자 출력 방식
print("[ 신상 정보 ]")
print('MBTI : %s 혈액형 : %s 성별 : %s'%(mbti, blood, gender), sep='   ')
print('몸무게 : %d, 키 : %.2f'%(weight, height), sep='    ')

# 2-3 F-스트링 출력 방식 => Format 약자
print("[ 신상 정보 ]")
print(f'MBTI : {mbti} 혈액형 : {blood} 성별 :{gender}', sep='   ')
print(f'몸무게 : {weight} 키 : {height}',  sep='    ')


# 3
#3-1
n =50
f = 0.91
w = 'Winter'
b = False
print(f'데이터 {n}      =>  {type(n)} 타입')
print(f'데이터 {f}    =>  {type(f)} 타입')
print(f'데이터 {w}  =>  {type(w)} 타입')
print(f'데이터 {b}   =>  {type(b)} 타입')

#3-2
season = input("좋아하는 계절은? ")
print(f'당신은 {season}을 좋아하는 군요!')

seasonE = input("봄은 영어로? ")
print(f'봄은 {seasonE}입니다.')


# 4
print('(힙 영역) 데이터 즉 객체 저장  (스택 영역) 변수 저장')

# 5
print('정수 ==> (int), 실수 ==> (float), 글자 ==> (str), 논리 ==> (bool)')
print('0b1011: (2진수), 0o13: (8진수), 0xb: (16진수)')

# 6
length1 = int(input('직육면체 가로길이(cm) : '))
length2 = int(input('직육면체 세로길이(cm) : '))
height = int(input('직육면체 높이길이(cm) : '))
print(f'직사각형 넓이 : {length1*length2}')
print(f'직육면체 부피 : {length1*length2*height}')