import cmath

print("Question: ax**2 + bx + c = 0 ")
a = int(input("A: "))
b = int(input("b: "))
c = int(input("c: "))

D = b**2 - 4 *a*c
print(f'D = {D}')
if D > 0 :
    ques_1 = (-b + cmath.sqrt(D))/(2*a)
    ques_2 = (-b - cmath.sqrt(D))/(2*a)
    print(ques_1,ques_2)
elif D == 0:
    ques = (-b/2*a)
    print(ques)
else:
    print("Roots Are Imaginary ")