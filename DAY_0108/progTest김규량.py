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

# 길격에 대한 함수: 길격이 나왔을 때 출력하는 문구
def lucky_man(nameCount):
    if nameCount =='1' or nameCount == '17' or nameCount == '21' or nameCount == '32' or nameCount == '52':
        print("길격 입니다!!  활동적인 기운을 지녔군요.\n")
    elif nameCount == '3' or nameCount == '13' or nameCount =='16' or nameCount == '18' or nameCount == '45' or nameCount == '63' or nameCount == '75':
        print("길격 입니다!!  두뇌회전이 빠르고 명석한 기운을 지녔군요.\n")
    elif nameCount == '5' or nameCount == '15' or nameCount == '47' or nameCount == '78':
        print("길격 입니다!!  돈을 넘어 명예와 권세를 이룰 기운이군요. \n")
    elif nameCount == '6' or nameCount == '38' or nameCount == '51' or nameCount == '57' or nameCount == '58' or nameCount == '65' or nameCount == '76':
        print("길격 입니다!!  책임감과 노력 그리고 인내의 기운을 지녔군요.\n")
    elif nameCount == '23' or nameCount == '31' or nameCount == '39' or nameCount == '41' or nameCount == '48':
        print("길격 입니다!!  리더십, 지도력이 뛰어난 기운을 지녔군요\n")
    elif nameCount == '7' or nameCount == '24' or nameCount == '25' or nameCount == '35':
        print("길격 입니다!!  마음이 넓고 포용력있는 기운이군요.\n")
    elif nameCount == '29' or nameCount == '73':
        print("길격 입니다!!  지혜가 깃든 기운이군요.\n")
    elif nameCount == '33' or nameCount == '37':
        print("길격 입니다!!  자신감과 지모가 깃든 기운이군요\n")
    elif nameCount == '11' or nameCount == '68' or nameCount == '71':
        print("길격 입니다!!  성실함이 깃든 기운이군요\n")
    elif nameCount == '8' or nameCount == '61' or nameCount == '67':
        print("길격 입니다!!  마인드 컨트롤이 뛰어난 기운이군요\n")
    elif nameCount == '81':
        print("길격 입니다!!  하고 싶은거 다해도 다 되는 기운이군요.\n")

# 흉격에 대한 함수: 흉격이 나왔을 때 출력하는 문구
def unLucky_man(nameCount):
    if nameCount == '2' or nameCount == '14' or nameCount == '19' or nameCount == '36':
        print("흉격 입니다 ㅠㅠ  매사 타이밍이 안 맞는 기운을 지녔군요.\n")
    elif nameCount == '4' or nameCount == '12' or nameCount == '46' or nameCount == '50' or nameCount == '55' or nameCount == '59':
        print("흉격 입니다 ㅠㅠ 당신의 이름엔 의지가 약하며 인내력이 없는 기운을 지녔군요.\n")
    elif nameCount == '26' or nameCount == '40':
        print("흉격 입니다 ㅠㅠ  일에 비해 대가가 별로 없는 기운을 지녔군요.\n")
    elif nameCount == '9' or nameCount == '80':
        print("흉격 입니다 ㅠㅠ  사람 복이 없는 기운을 지녔군요.\n")
    elif nameCount == '20' or nameCount == '22' or nameCount =='27' or nameCount == '28' or nameCount == '30' or nameCount == '34' or nameCount == '42' or nameCount == '54':
        print("흉격 입니다 ㅠㅠ  되는 일이 없거나 운이 안 좋은 기운을 지녔군요.\n")
    elif nameCount == '10' or nameCount == '49' or nameCount == '64' or nameCount == '66' or nameCount == '69' or nameCount == '72' or nameCount == '74':
        print("흉격 입니다 ㅠㅠ  가지고 있는 장점과 시작은 좋으나 운이 안 따라주는 기운을 지녔군요.\n")
    elif nameCount =='56' or nameCount == '70':
        print("흉격 입니다 ㅠㅠ  자신감이 결여된 기운을 지녔군요.\n")
    elif nameCount == '43' or nameCount == '53':
        print("흉격 입니다 ㅠㅠ  겉과 속이 너무 다른 기운을 지녔군요.\n")
    elif nameCount == '44' or nameCount == '60' or nameCount == '79':
        print("흉격 입니다 ㅠㅠ  정신이 불안정한 기운을 지녔군요.\n")
    elif nameCount == '62':
        print("흉격 입니다 ㅠㅠ  자기 꾀에 자기가 넘어가는 기운을 지녔군요.\n")
    elif nameCount == '77':
        print("흉격 입니다 ㅠㅠ  가진 것이 많으나 점점 운이 기우는 기운을 지녔군요.\n")

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

        lucky_man(nameCount)  # 함수를 불러와 조건에 맞는 값이 나오면 출력
        unLucky_man(nameCount)  # 함수를 불러와 조건에 맞는 값이 나오면 출력
    else:
        print('숫자가 아닌 글자가 들어왔습니다. 다시 입력해주세요.\n')