count = int(input())

for i in range(0, count):
  a, b = map(int, input().split(" "))
  print(f"Case #{i+1}: {a+b}")