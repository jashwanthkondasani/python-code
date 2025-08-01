n = 10
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum:", total)
n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)
num = 1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed Number:", rev)
