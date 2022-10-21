import math

input_str = input()

values=input_str.split()
count=len(values)

if count == 1:
    a = int(input_str)
    if a <= 0:
        print('There can\'t be a circle with 0 radius')
    else:
        perimeter = 2*a*3.14
        area = 3.14*a**2
        print(f'circle: radius = {a}; perimeter = {perimeter}; area = {area}')
elif count == 2:
    a1, b1 = values
    a = int(a1)
    b = int(b1)
    if a <= 0 or b <= 0:
        print('There can\'t be a square or a rectangle with 0 side')
    else:
        if a == b:
            perimeter = a*4
            area = a**2
            print(f'square: side = {a}; perimeter = {perimeter}; area = {area}')
        else:
            perimeter = (a+b)*2
            area = a*b
            print(f'rectangle: side a = {a}; side b = {b}; perimeter = {perimeter}; area = {area}')
elif count == 3:
    a1, b1, c1 = values
    a = int(a1)
    b = int(b1)
    c = int(c1)
    if a <= 0 or b <= 0 or c <= 0:
        print('There can\'t be a triangle with 0 side')
    elif a + b <= c or a + c <= b or b + c <= a:
        print('There can\'t be a triangle where sum of 2 sides is less or equal to the 3-rd one')
    else:
        perimeter = a+b+c
        area = math.sqrt(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))
        print(f'triangle: side a = {a}; side b = {b}; side c = {c}; perimeter = {perimeter}; area = {area}')