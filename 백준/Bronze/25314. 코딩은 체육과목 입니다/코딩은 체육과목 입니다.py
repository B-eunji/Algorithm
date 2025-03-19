N = int(input()) # 바이트 수(long 1개당 4바이트)

long_i = N//4

pr_long = long_i * "long "
print(pr_long + "int")
     