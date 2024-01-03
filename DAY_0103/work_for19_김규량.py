# for와 if로 계단식 별 출력
for i in range(1,6):
    print('*'*i)

# 중첩 루프
for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')

    print('i:', i, '\\n', sep='')

# 사격형으로 별 출력
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

for i in range(3):
    for j in range(7):
        print('*', end='')
    print()

# 계단식 별 출력
for i in range(5):
    for j in range(5):
        if j<=i:
            print('*', end='')
    print()

# 대각선 별 출력
for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ',end='')
    print()

# 연습문제
for i in range(5):
    for j in range(5):
        if j<i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
# 심사문제
h = int(input())

for i in range(h):
    for j in range(h):
        print(' ', end='')
    for j in range(h):
        if j<=i:
            print('*', end='')
    print()
