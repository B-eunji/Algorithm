minute = 0

text = input().strip()

for ch in text:
    if ch in ['A' , 'B' , 'C']:
        minute += 3
    elif ch in ['D' , 'E' , 'F']:
        minute += 4
    elif ch in ['G' , 'H' , 'I']:
        minute += 5
    elif ch in ['J' , 'K' , 'L']:
        minute += 6
    elif ch in ['M' , 'N' , 'O']:
        minute += 7
    elif ch in ['P' , 'Q' , 'R' , 'S']:
        minute += 8
    elif ch in ['T' , 'U' , 'V']:
        minute += 9
    elif ch in ['W' , 'X' , 'Y' , 'Z']:
        minute += 10
        
print(minute)