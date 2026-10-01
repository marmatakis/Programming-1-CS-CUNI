x = 10
print(bin(x))
x = x // 2
print(bin(x))

# convert int to binary
n = int(input("Enter n: "))
p = 0
# find the biggest 2^p < n
while 2 ** p < n:
    if 2 ** (p+1) > n:
        break
    p += 1
print(p)
s = ""
count = 0
while p != 0:
    if n - 2**p < 0:
        p -= 1
        s += "0"
        continue
    s += "1"
    count += 1
    n -= 2 ** p
    p -= 1
s += "0"
print("binary string", s)
print("yes" if s.replace("11", "") == s else "no")
print("total amount of 1s", count)

# 1 - how many 1s are in binary representation of given n
n = int(input("Enter n: "))
count = 0
while n != 0:
    count += n % 2
    n //= 2
print(count)

# 2 - output 'yes' if in binary representation there are no consecutive 1s
# output 'no' ohterwise
n = int(input("Enter n: "))
answ = 'yes'
last = n % 2
n //= 2
while n != 0:
    print(n, last, n%2)
    if last == n%2 and last == 1:
        answ = 'no'
        break
    last = n%2
    n //= 2
print(answ)

# 3 - write "super number" from given number
# super number:
# if n < 10 -> n
# if n > 10 -> super number of sum of digits in decimal representation
x = int(input("Enter n: "))
# # this uses recusrion, which is more complex than needed + we didn't learn that yet
def superNumber(n):
    if n < 10:
        return n
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return superNumber(s)
print(superNumber(x))

# 3 - correct solution with 2 nested while loops, could also use n = str(s) and for loop - less efficient
n = int(input("Enter n: "))
while n > 10:
    x = n
    s = 0
    while x != 0:
        s += x % 10
        x //= 10
    n = s
print(n)

# 4 - read 1 line as a str with letters 'a' - 'z', ' '.
# print frequencies of each letter in the string
# very inefficient solution with storing in list
s = str(input("Enter string: "))
l = []
for item in s:
    if item == " ":
        continue
    l.append(item)
l.sort() # sort for order of letters a-z
t = []
for item in s:
    if item in t:
        continue
    t.append(item)
    print(f"{item} - {l.count(item)}")

# solution with converting str to list
s = list((input("Enter string: ")))
s.sort() # sort for order of letters a-z
l = []
for item in s:
    if item == " ":
        continue
    if item in l:
        continue
    l.append(item)
    print(f"{item} - {s.count(item)}")

# solution using dict & list of letters instead of using sort
s = str(input("Enter string: ")).lower()
l = {}
for item in s:
    if item == " ":
        continue
    if l.get(item):
        l[item] += 1
        continue
    l[item] = 1
order = "abcdefghijklmnopqrstuvwxyz"
for item in order:
    if item not in l:
        continue
    print(f"{item} - {l[item]}")
