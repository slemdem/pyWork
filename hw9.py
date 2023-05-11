class Point:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y

    def show(self):
        print(f'({self.__x},{self.__y})',end ='')

    def set(self,x=0,y=0):
        self.__x = x
        self.__y = y
        
    def get(self):
        getxy =(self.__x,self.__y)
        return getxy
    
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y

class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.__lt = Point(x1,y1)
        self.__rb = Point(x2,y2)

    def show(self):
        print('좌측상단 꼭지점이 ',end ='')
        self.__lt.show()
        print('이고 우측하단 꼭지점이 ',end = '')
        self.__rb.show()
        print('인 사각형입니다.',end = '')
    
    def getWidth(self):
        x1 = self.__lt.getx()
        x2 = self.__rb.getx()
        w = x1 - x2
        if w < 0:
            w *=-1
        return w
    
    def getHeight(self):
        y1 = self.__lt.gety()
        y2 = self.__rb.gety()
        h = y1 - y2
        if h <0:
            h *= -1
        return h

    def getArea(self):
        h = self.getHeight()
        w = self.getWidth()
        return h*w

    def getPerimeter(self):
        h = self.getHeight()
        w = self.getWidth()
        return (h+w)*2

r1 =Rectangle(5,5,20,10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
