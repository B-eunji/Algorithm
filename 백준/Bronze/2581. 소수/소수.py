M = int(input())
N = int(input())
prime_add = 0
prime_list = []

for i in range(M,N+1):
    if i > 1:
        is_prime = True
        for j in range(2,int(i**0.5)+1):
            if i % j ==0:
                is_prime = False
                break
        if is_prime:
            prime_add += i
            prime_list.append(i)

if not prime_list:
    print(-1)
else:
    print(prime_add)
    print(prime_list[0])