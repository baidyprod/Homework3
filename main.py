import math

input_str = input()

values=input_str.split()
count=len(values)

if count == 1:
    a = int(''.join(values))
    if a == 0:
        print('There can\'t be a circle with 0 radius')
    else:
        print(f'circle: radius = {a}; perimeter = {2*a*3.14}; area = {3.14*a**2}')
elif count == 2:
    a1, b1 = values
    a = int(''.join(a1))
    b = int(''.join(b1))
    if a == 0 or b == 0:
        print('There can\'t be a square or a rectangle with 0 side')
    else:
        if a == b:
            print(f'square: side = {a}; perimeter = {a*4}; area = {a**2}')
        else:
            print(f'rectangle: side a = {a}; side b = {b}; perimeter = {(a+b)*2}; area = {a*b}')
elif count == 3:
    a1, b1, c1 = values
    a = int(''.join(a1))
    b = int(''.join(b1))
    c = int(''.join(c1))
    if a == 0 or b == 0 or c == 0:
        print('There can\'t be a triangle with 0 side')
    elif a + b < c or a + c < b or b + c < a:
        print('There can\'t be a triangle where sum of 2 sides is less than the 3-rd one')
    else:
        print(f'triangle: side a = {a}; side b = {b}; side c = {c}; perimeter = {a+b+c}; area = {math.sqrt(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))}')


