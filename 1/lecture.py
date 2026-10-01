x = 10
y = 20
x = x + 1
print(x)

x += 3 # x = x + 3 
y *= 2 # y = y * 2

n = input("Name: ")
print(n)

x = int(input("Enter x: "))
print(x * 2)

if x > 100:
    print("x is big")
    x *= 2
    print("now", x, "is even bigger")
elif x > 50:
    print("x is kinda big")
else:
    print("x is small")

s = 0
while x > 0:
    s += x
    x -= 1
while x % 10 == 0: # while last digit is 0
    x = x // 10
print(x)

x = int(input('Enter x: '))
s = 0

for i in range(0, x + 1):
    print("i =", i)
    s += i
print(s)

r = range(1, 100_00)
print(r[50])