import math
class Shape:
    name = ""
    color = ""
    line_type = ""
    thickness = 0

    def __init__(self, isim, renk, cizgi, kalinlik):
        self.name = isim
        self.color = renk
        self.line_type = cizgi
        self.thickness = kalinlik
    def __str__(self):
        return "Name="+self.get_name() + "\nColor="+self.get_color() + "\nLine type="+self.get_line_type() + "\nThickness=" + str(self.get_thickness())

    def get_name(self):
        return self.name

    def set_name(self, isim):
        self.name = isim

    def get_color(self):
        return self.color

    def set_color(self, renk):
        self.color = renk

    def get_line_type(self):
        return self.line_type

    def set_line_type(self, cizgi):
        self.line_type = cizgi

    def get_thickness(self):
        return self.thickness

    def set_thickness(self, kalinlik):
        self.thickness = kalinlik


class Rectangle(Shape):
    width = 0
    height = 0

    def __init__(self, genislik, yukseklik, isim, renk, cizgi, kalinlik):
        self.width = genislik
        self.height = yukseklik
        Shape.__init__(self, isim, renk, cizgi, kalinlik)

    def __str__(self):
        return Shape.__str__(self) +"\nWidth="+str(self.get_width())+"\nHeight="+str(self.get_height())+"\nArea=" + "{0:.2f}".format(self.get_area())+  "\nPerimeter="+"{0:.2f}".format(self.get_perimeter())

    def get_width(self):
        return self.width

    def set_width(self, w):
        self.width = w

    def get_height(self):
        return self.height

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width + 2 * self.height


class Circle(Shape):
    radius = 0

    def __init__(self, r, isim, renk, cizgi, kalinlik):
        self.radius = r
        Shape.__init__(self, isim, renk, cizgi, kalinlik)

    def __str__(self):
        return Shape.__str__(self) +"\nRadius="+str(self.get_radius())+"\nArea=" + "{0:.2f}".format(self.get_area())+  "\nPerimeter="+"{0:.2f}".format(self.get_perimeter())


    def get_radius(self):
        return self.radius

    def set_radius(self, r):
        self.radius = r

    def get_area(self):
        return math.pi * self.radius**2

    def get_perimeter(self):
        return 2*math.pi*self.radius


class Triangle(Shape):
    edge1 = 0
    edge2 = 0
    edge3 = 0

    def __init__(self, e1, e2, e3, isim, renk, cizgi, kalinlik):
        self.edge1 = e1
        self.edge2 = e2
        self.edge3 = e3
        Shape.__init__(self, isim, renk, cizgi, kalinlik)

    def get_edge1(self):
        return self.edge1

    def set_edge1(self, e):
        self.edge1 = e

    def get_edge2(self):
        return self.edge2

    def set_edge2(self, e):
        self.edge2 = e

    def get_edge3(self):
        return self.edge3

    def set_edge3(self, e):
        self.edge3 = e

    def get_area(self):
        u = (self.edge1+self.edge2+self.edge3)/2
        return math.sqrt(u*(u-self.edge1)*(u-self.edge2)*(u-self.edge3))

    def get_perimeter(self):
        return self.edge1+self.edge2+self.edge3

    def __str__(self):
        return Shape.__str__(self) +"\nEdge1="+str(self.get_edge1())+"\nEdge2="+str(self.get_edge2())+"\nEdge3="+str(self.get_edge3())+"\nArea=" + "{0:.2f}".format(self.get_area())+  "\nPerimeter="+"{0:.2f}".format(self.get_perimeter())



class Square(Shape):
    edge1 = 0

    def __init__(self, e1, isim, renk, cizgi, kalinlik):
        self.edge1 = e1
        Shape.__init__(self, isim, renk, cizgi, kalinlik)

    def __str__(self):
        return Shape.__str__(self) +"\nEdge="+str(self.get_edge())+"\nArea=" + "{0:.2f}".format(self.get_area())+  "\nPerimeter="+"{0:.2f}".format(self.get_perimeter())


    def get_edge(self):
        return self.edge1

    def set_edge(self, e):
        self.edge1 = e

    def get_area(self):
        return self.edge1**2

    def get_perimeter(self):
        return self.edge1*4

