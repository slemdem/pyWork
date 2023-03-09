def get_radius():
    r=int(input('넓이를 구하고자 하는 원의 반지름은? '))
    return r

def get_circle_area(r):
    radius = r
    area = 3.14*radius*radius
    return area

radius = get_radius()
area = get_circle_area(radius)
print('반지름 ',radius,'인 원의 넓이 = 3.14 x ',radius,' x ',radius,' = ',area, sep = '')
