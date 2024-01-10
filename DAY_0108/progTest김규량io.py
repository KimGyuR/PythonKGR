# 큰 주제: 성명학(작명 운세)
# 세부 주제: 수리오행
"""
김규량 金:8획, 奎:9획, 樑:15획
    원격: 24획, 형격: 17획, 이격: 23획, 정격: 32획
"""
"""
길격: 1, 3, 5, 6,7,8,
    11,13,15,16,17,18
    21,23,24,25,29,31
    32,33,35,37,38,39
    41,45,47,48,51,52
    57,58,61,63,65,67
    68,71,73,75,76,78,81
    43개
흉격: 38개
"""
file='luck.txt'
sentence={}
key=''
# 본 구문
print('이름 획수로 운세를 확인해 보자!(1 ~ 81 안에 획수)')
while True:
    nameCount = input("이름 획수 입력(0 입력시 종료): ")

    if nameCount.isdecimal():
        if nameCount == '0':
            print('프로그램 종료합니다.') # '0'을 입력시 종료 출력과 동시에 break
            break
        elif nameCount > '81':
            print('획수 범위 밖에 있습니다. 다시 입력해주세요.\n')
        elif nameCount>'0' or nameCount<'82':
            with open(file, mode='r', encoding='utf-8') as f:
                data = f.readline(2)
                print(data.strip())
    else:
        print('숫자가 아닌 글자가 들어왔습니다. 다시 입력해주세요.\n')