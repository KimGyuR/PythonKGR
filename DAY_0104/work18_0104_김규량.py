# while에서 break로 반복문 끝내기
i = 0
while True:      # 무한 루프
    print(i)
    i += 1       # i를 1씩 증가시킴
    if i == 100: # i가 100일 때
        break    # 반복문을 끝냄. while의 제어 흐름을 벗어남

# for에서 break로 반복문 끝내기
for i in range(10000):  # 0부터 9999까지 반복
    print(i)
    if i == 100:        # i가 100일 때
        break           # 반복문을 끝냄. for 제어 흐름을 벗어남

# for에서 continue로 코드 실행 건너뛰기
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)

# while에서 continue로 코드 실행 건너뛰기
i = 0
while i < 100:
    i += 1
    if i%2 == 0:
        continue
    print(i)

# 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while True:     # 무한 루프
    print(i)
    i += 1
    if i == count:  # i가 입력받은 값과 같을 때
        break       # 반복문을 끝냄

# 입력한 숫자까지 홀수 출력하기
count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count+1):
    if i % 2 == 0:
        continue
    print(i)

# 연습문제
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1

# 심사문제
start, stop = map(int, input().split())

i = start

while True:
    if i % 10 == 3:
        i += 1
        continue
    if i > stop:
        break
    print(i, end=' ')
    i += 1