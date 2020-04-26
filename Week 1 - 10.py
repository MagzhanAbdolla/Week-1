n = int(input())

chas = n % (60 * 24) // 60
minuts = n % 60

print(chas, minuts)
