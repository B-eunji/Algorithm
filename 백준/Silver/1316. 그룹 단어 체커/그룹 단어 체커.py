num = int(input())
group = 0

for _ in range(num):
    words = input().strip()
    seen = set() #이미 나온 문자 저장
    prev = '' # 이전 문자 기억
    is_group = True # 그룹 단어 여부
    
    for ch in words:
        if ch != prev:
            if ch in seen:
                is_group = False
                break
            seen.add(ch)
        prev = ch
        
    if is_group:
        group += 1
            
print(group)