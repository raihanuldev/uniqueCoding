import cmath

a = int(input("A: "))
b = int(input("b: "))
c = int(input("c: "))

D = b**2 - 4 *a*c
print(f'D = {D}')
if D > 0 :
    x_1 = (-b + cmath.sqrt(D))/(2*a)
    x_2 = (-b - cmath.sqrt(D))/(2*a)
    print(x_1,x_2)
elif D == 0:
    x = (-b/2*a)
    print(x)
else:
    print("Roots Are no Imaginary ")