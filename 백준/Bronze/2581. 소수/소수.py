M = int(input())
N = int(input())
prime_sum = 0
prime_list = []

for i in range(M, N+1):
    if i > 1:
        is_prime = True
        for j in range(2,int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
            prime_sum += i
    
if prime_list:
    print(prime_sum)
    print(prime_list[0])
else:
    print(-1)