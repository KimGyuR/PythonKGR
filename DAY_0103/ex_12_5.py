# ---------------------------------------------------------
# - 문자열 여러개의 실수 숫자 여러개를 두 줄로 입력 받기
# _ 첫번째 입력 받은 값은 Key
# - 두번째 입력 받은 값은 Value
# - 딕셔너리로 저장해 주세요.
# ---------------------------------------------------------
twoData = input("문자열 4~5개, 실수 숫자 4~5개 두 줄로 입력\n")

# key와 value로 데이터 분리
keys, values=twoData.split(',')         # 'aa bb cc dd, 1.1 2.2 3.3 4.4'
keys=keys.split()                       # 'aa bb cc dd'
values=values.split()                   # '1.1 2.2 3.3 4.4'

# 입력 데이터 존재 여부 체크
if (len(keys==4 and len(values)==4 or keys==5 and len(values)==5)):
    dataDict = {}
    if len(keys)==4:
        dataDict[0] = values[0]
        dataDict[1] = values[1]
        dataDict[2] = values[2]
        dataDict[3] = values[3]
    else:
        dataDict[0] = values[0]
        dataDict[1] = values[1]
        dataDict[2] = values[2]
        dataDict[3] = values[3]
        dataDict[4] = values[4]
else:
    print("입력된 데이터가 정확하지 않습니다.")