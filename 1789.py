sum = int(input())
n = 1
while n * (n + 1) / 2 <= sum:
  n += 1
print(n - 1)
