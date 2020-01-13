n, result = int(input('Enter the number: ')),  0.0
for i in range(1, n):
    result += 1 / 2 ** i

print(round(result))
