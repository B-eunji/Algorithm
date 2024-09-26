N = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for c in cro:
    N = N.replace(c, '*')
    
print(len(N))