import math
    
# Defines ax^3 + bx^2 + cx + d by user input
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

# Checks for Evident Roots
if a + c == b + d:
    r = -1
elif a + b + c + d == 0:
    r = 1
elif d == 0:
    r = 0
else:
    print("This ecuation has no evident roots.")

# Applies the Ruffini method
e = a + 0
f = (e * r) + b
g = (f * r) + c

# Applies Bhaskara method
squareRoot = math.sqrt(f**2 - 4 * e * g)
r1 = (-f + squareRoot) / 2 * e
r2 = (-f - squareRoot) / 2 * e

# Outputs the roots
print(r, r1, r2)

factRoot = r * -1
factRoot1 = r1 * -1
factRoot2 = r2 * -1

if factRoot >= 0:
    sign = '+'
else:
    sign = '-'
    factRoot = factRoot * -1

if factRoot1 >= 0:
    sign1 = '+'
else:
    sign1 = '-'
    factRoot1 = factRoot1 * -1

if factRoot2 >= 0:
    sign2 = '+'
else:
    sign2 = '-'
    factRoot2 = factRoot2 * -1


print(str(a) + "(x", str(sign), str(factRoot) + ")(x", str(sign1), str(factRoot1) + ")(x", str(sign2), str(factRoot2) + ")")
