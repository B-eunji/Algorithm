A, B, V = map(int, input().split())

# 목표 높이 V에서 마지막 날은 미끄러지지 않으므로 A만큼만 더 올라가면 끝남
day = (V - A) / (A - B) + 1

# 결과가 정수이면 그대로 출력, 소수점이 있으면 하루를 더함
print(int(day) if day == int(day) else int(day) + 1)