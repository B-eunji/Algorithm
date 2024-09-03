A = int(input())
B = int(input())

Three = A * (B%10)

Four = A * (B%100//10)

Five = A * (B // 100)


Six = Three + Four*10 + Five*100

print(Three)
print(Four)
print(Five)
print(Six)