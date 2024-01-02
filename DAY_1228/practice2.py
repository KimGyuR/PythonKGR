korea = input("국어 점수 : ")
math = input("수학 점수 : ")
eng = input("영어 점수 : ")
science = input("과학 점수 : ")

korea = int(korea)
math = int(math)
eng = int(eng)
science = int(science)

print(f'국어: {korea}, 수학: {math}, 영어: {eng}, 과학: {science}')
print(f'korea>=90 and math>85 and eng>80 and science>=80 => {korea>=90 and math>85 and eng>80 and science>=80}')

s = "Python is a \"programming language\" \nthat lets you work quickly\nand\nintegrate systems more effectively."
print(s)

s = """Python is a "programming language" that lets you work quickly
and 
integrate systems more effectively."""
print(s)