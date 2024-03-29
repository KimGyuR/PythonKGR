# ---------------------------------------------------------------------
# str 데이터 타입 전용 함수 즉 메서드(Method) 살펴보기
# - 메서드(Method)
#   특정 데이터 타입에서만 사용 가능한 함수를 의미
# - 사용방법
#   변수명.메서드명() => msg='good'
#                     msg.메서드명()
#   데이터.메서드명() => 'good'.메서드명()
# ---------------------------------------------------------------------
# str을 대문자로 변환 ==> upper() 메서드
print("Kidding".upper())

# str을 소문자로 변환 ==> lower() 메서드
print("Kidding".lower())

# str이 모두 대문자인지 검사 후 결과 반환 => isupper() 메서드
print("Good".isupper())

# str이 모두 소문자인지 검사 후 결과 반환 => islower() 메서드
print("Good".islower())

# str이 0~9로 구성되어 있는지 검사 후 결과 반환 => isdecimal() 메서드
print("Good".isdecimal(), "012".isdecimal(), "-9".isdecimal())

# str이 문자로만 구성되어 있는지 검사 후 결과 반환 => isalpha() 메서드
print("Good".isalpha(), "Good2024".isalpha(), "韓契".isalpha())

# str이 문자, 숫자로만 구성되어 있는지 검사 후 결과 반환 => isalnum() 메서드
print("Good".isalnum(), "Good2024".isalnum(), "한글".isalnum())

# str이 문자에서 특정 문자/문자열로 시작하는지 검사 후 결과 반환
# 시작 => ??
print("??Happy New".startswith("??"))
print("??Happy New".startswith("!"))

# str이 문자에서 특정 문자/문자열로 끝나는지 검사 후 결과 반환
# 끝 => jpg
print("flower.jpg".endswith("jpg"))
print("flower.png".endswith("jpg"))
print("flower.txt".endswith(("jpg", "png", "txt")))

# str 특정 인덱스 문자를 변경해주는 메서드 => replace()메서드
name="HongGulDong"

# => u ===> i로 변경
print(name[5])

#name[5]='i' ==> 인덱싱으로는 미지원 기능 ==> 메서드 제공
print(name.replace('o', '*'))
print(name.replace('o', '*', 1))
name=name.replace('u','i')