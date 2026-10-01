# 1
w = int(input("Width: "))
l = int(input("Length: "))
h = int(input("Height: "))

print(f"You need {w*l + 2*l*h + 2*w*h} square meters of paint.")

# 2
x = int(input("Enter X: "))
y = int(input("Enter Y: "))

print(f"{"X" if x > y else "Y"} is greater")

#3
x = int(input("Enter X: "))
y = int(input("Enter Y: "))

if x % y == 0:
    print(f"{x} divided by {y} is {x//y}")
else:
    print("indivisible")

# 4
x = int(input("Enter X: "))
y = int(input("Enter Y: "))
z = int(input("Enter Z: "))

print(f"The largest is {max(x, y, z)}")

# 5
s = ""
for i in range(1, 11):
    s += str(i*2)
    if i == 10:
        break
    s += "\n"
print(s)

# 6
n = int(input("Enter N: "))
s = 1
for i in range(2, n+1):
    s *= i
print(f"{n}! = {s}")

# 7
A = int(input("Enter A: "))
B = int(input("Enter B: "))
s = 1
for i in range(B):
    s *= A
print(f"A^B is {s}")

# 8
n = int(input("Enter N: "))
s = 0
for i in range(1, n+1):
    if n % i == 0:
        print(i)
        s += 1
print(f"There are {s} divisors")

# 9
p = int(input("Enter price: "))
k20 = p // 20
p -= 20 * k20
k10 = p // 10
p -= 10 * k10
k5 = p // 5
p -= 5 * k5

print("20 Kc: ", k20)
print("10 Kc: ", k10)
print("5 Kc: ", k5)
print("1 Kc: ", p) # 1 Kc is just what's left :)

# 10
n = int(input("Enter number: "))
# unknown functions to us yet, but runs in o(1)
if str(bin(n)).replace("0b", "").replace("0", "") == "1": # ideally rewrite this to not use bin
    print("pow")
else:
    print("no")

# 11
print("Think of a number from 1 to 1000.")
n = 0
low = 0
high = 1000
while True:
    g = (low + high) // 2
    inp = input(f"My guess: {g}.  Is this (h)igh, (l)ow, or (c)orrect? ")
    if inp == "c":
        print("Total guesses: ", n)
        break
    if inp == "h":
        high = g
    if inp == "l":
        low = g

# 12
y = int(input("Enter year: "))
if (y % 4 == 0 and not y % 100 == 0) or (y % 100 == 0 and y % 400 == 0):
    print("leap")
else:
    print("no leap")

# 13
# inefficient, but whatever at this point
n = int(input("Enter N: "))
s = 0
while (2 ** s) < n:
    s += 1
print(s)

# 14
n = int(input("Enter N: "))
s = 0
while (2 ** s) < n:
    if 2 ** (s+1) > n:
        break
    s += 1
print(s)

# 15
n = int(input("Enter N: "))
d = 0
while n != 0:
    n //= 10
    d += 1
print(d)

# Project Euler registration solution
k = 0
for i in range(1, 508001):
    s = i ** 2
    if s % 2 != 0:
        k += s
    print(i ** 2, k)

# 16
s = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        s += i
print(s) # 233168

# 17
prev = 0
prev2 = 1
s = 0
while prev + prev2 <= 4_000_000:
    n = prev + prev2
    if n % 2 == 0:
        s += n
    prev = prev2
    prev2 = n
    print(n)
print(s) # 4613732