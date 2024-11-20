N = int(input())
count = 0

while N >= 0:
    if N % 5 == 0:  # N이 5로 나누어 떨어지는 경우
        count += N // 5  # 5로 나눈 몫을 추가
        print(count)
        break
    N -= 3  # 5로 나누어 떨어지지 않으면 3을 뺍니다.
    count += 1  # 3kg 봉지 하나 사용
else:
    print(-1)  # 정확히 나눌 수 없는 경우