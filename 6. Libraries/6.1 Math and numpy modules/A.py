from math import log, cos, sin, pi, e

x = float(input())
a = log(pow(x, 3 / 16), 32)
b = pow(x, cos((pi * x) / (2 * e)))
c = pow(sin(x / pi), 2)

f = a + b - c
print(f)