# --------------------------------------------------------------
# [실습1] 2개의 정수를 입력 받은 후 4칙 연산 수행 결과를 반환하는 기능의
#        함수를 정의해 주세요.
#        함수이름 : fourCalc
#        매개변수 : n1, n2
#        반환결과 : 4칙 연산 결과
# --------------------------------------------------------------
def fourCalc(n1, n2):
    return n1+n2, n1-n2, n1*n2, n1/n2 if n2 else '다시 입력해주세요'

num1, num2 = map(int, input("두 개 정수 입력: ").split(" "))
print(fourCalc(num1, num2))
# --------------------------------------------------------------
# [실습2] 문자열을 16진수 코드값으로 변환 후 반환하는 함수를 정의해 주세요.
#        문자열 -------> 코드값 ------> 16진수
#        함수이름 : getCode
#        매개변수 : message
#        반환결과 : str
# --------------------------------------------------------------
def getCode(message):
    ret=''
    for msg in message:
        ret += hex(ord(msg))

    return ret
print(getCode('ks'))

# -------------------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember
# 매개 변수 : 이름, 전화번호, 아이디, 이메일, 취미. 주소, 생일, .......
#           가변 + 데이터 정보 함께
#           키워드 파라미터 **member
# 반 환 값 : '가입 완료 되었습니다.' str
# -------------------------------------------------------------------
def joinMember(**member):
    #print(type(member))
    print(member)
    # 멤버 저장소에 멤버 추가하기
    mList.append(member)
    #members[f'M{len(members)}']=member
    return "가입 완료 되었습니다."
# -------------------------------------------------------------------
# 함수 사용 즉 호출
# -------------------------------------------------------------------
# 가입된 회원들 저장 변수
members = {}
mList=[]

print(f'[BF] : {members}')

# 회원가입 기능 함수 호출
joinMember(name='Hong', age=17, birth='2001/01/01')
joinMember(id='Hong84', phone='010-0101-1111', job='doctor', blood='B')
joinMember(id='baby', birth='2024/01/01', blood='A')

print(f'[AF] : {members}')

# m={'name':'Hong', 'age':17}
# print(m.keys())
# print(m.values())
# print(m.items())

# -------------------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember2
# 매개 변수 : 필수 => id, pw
#           선택  => **option 이름, 전화번호, 아이디, 이메일, 취미. 주소, 생일, .......
#           가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료 되었습니다.' str
# -------------------------------------------------------------------
def joinMember2(id, pw, **option):
    # 멤버 저장소에 멤버 추가하기
    print('ok')

members={}
mList=[]

print(f'[BF] : {members}')

# 회원가입 기능 함수 호출
joinMember2('h', 'ph', age=17, birth='2001/01/01')
joinMember2('Hong84', '1234', phone='010-0101-1111', job='doctor', blood='B')

print(f'[AF] : {members}')

# -------------------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember3
# 매개 변수 : 필수 => id, pw, loc, gender
#           선택  => **option 이름, 전화번호, 아이디, 이메일, 취미. 주소, 생일, .......
#           가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료 되었습니다.' str
# -------------------------------------------------------------------
def joinMember3(id, pw, loc='내국인', gender='남자', **option):
    # 멤버 저장소에 멤버 추가하기
    print(id, pw, loc, gender, option)
    # 키 => id
    # 값 => pw, loc='내국인', gender='남자', **option0
    #       {'pw':123, 'loc':내국인, 'gender':'남자', 'etc':{option} }
    valueDict={}
    valueDict['pw']=pw
    valueDict['loc']=loc
    valueDict['gender']=gender
    valueDict['etc'] = option
    members[id] = valueDict

# -------------------------------------------------------------------
# 함수 사용 즉 호출
# -------------------------------------------------------------------
members={}
mList=[]

print(f'[BF] : {members}')

# 회원가입 기능 함수 호출
joinMember3('h1', 'ph')
joinMember3('h2', 'ph', gender='여자')
joinMember3('h3', 'ph', phone='010-2222-3310', blood='A')

print(f'[AF] : {members}')
for m in members.items():
    print(m)