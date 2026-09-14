# 1. Positive or Negative
# ○ Problem: Given a number, check if it is positive, negative, or zero.
# ○ Example: Input: -5 → Output: Negative
n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#Even or Odd
# ○ Problem: Check if a number is even or odd using if-else.
# ○ Example: Input: 7 → Output: Odd

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Compare Two Numbers
# ○ Problem: Take two numbers as input and print which one is greater, or if they
# are equal.
# ○ Example: Input: 4, 4 → Output: Equal

m = int(input("Enter second number: "))
if m > n:
    print(m)
else:
    print(n)

# 1. Check Empty String
# ○ Problem: Given a string, check if it is empty or not.
# ○ Example: Input: "" → Output: Empty String

s = ""
if s == "":
    print("Empty String")
else:
    print("Not Empty String")

# 2. Check First Character
# ○ Problem: Given a string, check if its first character is a vowel or consonant.
# ○ Example: Input: "Apple" → Output: Vowel
s = input("Enter a string: ")
if s[0].lower() in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# 3. Check String Length
# ○ Problem: Given a string, check if its length is greater than 5.
# ○ Example: Input: "Hello" → Output: Length is greater than 5

if len(s) > 5:
    print("Length is greater than 5")
else:
    print("Length is not greater than 5")

# 1. Print 1 to N
# ○ Problem: Take an integer N and print numbers from 1 to N using a for loop.
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(i)

# 2. Sum of N Numbers
# ○ Problem: Find the sum of all numbers from 1 to N using a while loop.
total = 0
while n > 0:
    total += n
    n -= 1
print("Sum of numbers from 1 to N is:", total)

# 3. Factorial of a Number
# ○ Problem: Calculate factorial of a given number using a for loop.
n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print("Factorial of", n, "is:", fact)
# 4. Reverse a Number
# ○ Problem: Take an integer input and reverse its digits using a while loop.
n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n%10
    reverse = reverse*10+digit
    n = n //10

print(reverse)

# ○ Example: Input: 1234 → Output: 4321
# 5. Count Digits
# ○ Problem: Count the number of digits in a given number using a do-while
# loop.

n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n = n //10

print(reverse)