# Print Solid Rectangle
# *****
# *****
# *****
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
# Print Hollow Rectangle
# *****
# *   *
# *****
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1:
            print("*",end="")

    if i !=0 and i != n-1:
        print("*"," "*(n-2),"*",end="")
    print()
# Print Half Pyramid
# *
# **
# ***
# ****
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

# Print Inverted Half Pyramid
# ****
# ***
# **
# *
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()

# Print Numbers Pyramid
# 1
# 12
# 123
# 1234

for i in range(n):
    p = 1
    for j in range(i+1):
        print(p,end="")
        p += 1
    print()