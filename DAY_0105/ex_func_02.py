# -------------------------------------------------------------------
# 다양한 함수의 형태 - (1) 기본
# -------------------------------------------------------------------
# 함수 기능 : 팩토리얼을 계산 후 계산 결과를 반환해주는 기능
# 함수 이름 : facT_Orial
# 매개 변수 : x
# 반 환 값 : 계산 결과
# -------------------------------------------------------------------
def facT_Orial(x):
    result = 1      # 결과 저장 변수
    if x:
        for i in range(x, 0, -1):
            result *= i
    return result

print(f'4! => {facT_Orial(4)}')

# 함수 기능 : 팩토리얼을 계산 후 계산 결과를 아래와 형태로 반환해주는 기능
#           예시 결과 3! : 3 * 2 * 1 = 6
# 함수 이름 : facT_Orial2
# 매개 변수 : x
# 반 환 값 : 계산 str
# -------------------------------------------------------------------
def facT_Orial2(x):
    strRet=f'{x}! : '
    result = 1      # 결과 저장 변수
    if x:
        for i in range(x, 0, -1):
            result *= i
            strRet = strRet + str(i)
            strRet = strRet +  (' * ' if i != 1 else ' = ')
            #print(strRet, result)

    return strRet + str(result)


print(facT_Orial2(3))
print(facT_Orial2(0))