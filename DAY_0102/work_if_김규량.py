# 13 if 심사문제
price = int(input())
cash = int(input("Cash"))

if price > 0:
    if price>=cash:
        print(price-cash)

# ----------------------------------------------------------
# 14 심사문제
kor = int(input())
eng = int(input())
math = int(input())
sci = int(input())

subject1 = (kor+eng+math+sci)/4
subject2 = kor+eng+math+sci

if ((kor >= 0 and kor <= 100) and (eng >= 0 and eng <= 100) and
        (math >= 0 and math <= 100) and (sci >= 0 and sci <= 100)):
    if subject1 >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수입니다.")

# -----------------------------------------------------------
# 15 심사문제
age = int(input())
balance = 9000

elemstu = 650
child = 1050
adult = 1250

if age >= 7 and age <= 12:
    balance -= elemstu
elif age >= 13 and age <= 18:
    balance -= child
elif age >= 19:
    balance -= adult

print(balance)