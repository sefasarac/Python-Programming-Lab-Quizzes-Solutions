import math
# https://github.com/sefasarac

class Rectangle:
    width = 0
    height = 0
    def __init__(self, genislik, yukseklik):
        self.width = genislik
        self.height = yukseklik
    

    def __str__(self):
        return "\nWidth=" + str(self.get_width()) + "\nHeight=" + str(self.get_height()) + "\nArea=" + "{0:.2f}".format(self.get_area_rect()) + "\nPerimeter=" + "{0:.2f}".format(self.get_perimeter_rect())

    def get_width(self):
        return self.widthhgh

    def set_width(self, genislik):
        return self.set_width(genislik)

    def get_height(self):
        return self.height

    def set_height(self, yukseklik):
        return self.set_height(yukseklik)

    def get_area_rect(self):
        return self.width * self.height

    def get_perimeter_rect(self):
        return 2 * self.width + 2 * self.height


class Triangle:
    edge = 0

    def __init__(self, kose):
        self.edge = kose

    def __str__(self):
        return "\nEdge=" + str(self.get_edge()) + "\nArea=" + "{0:.2f}".format(self.get_area_tri()) + "\nPerimeter=" + "{0:.2f}".format(self.get_perimeter_tri())

    def get_edge(self):
        return self.edge

    def set_edge(self, kose):
        return self.set_edge(kose)

    def get_area_tri(self):
        return self.edge **2 * (math.sqrt(3) / 4)

    def get_perimeter_tri(self):
        return 3 * self.edge


class Square(Triangle):
    def __init__(self,kose):
        Triangle.__init__(self,kose)

    def __str__(self):
        return "\nWidth="+ str(self.get_edge()) + "\nHeight="+ str(self.get_edge()) + "\nArea=" + "{0:.2f}".format(self.get_area_square()) + "\nPerimeter=" + "{0:.2f}".format(self.get_perimeter_square())
    
    def get_area_square(self):
        return self.edge **2
    def get_perimeter_square(self):
        return self.edge * 4

class TrianglePrism(Triangle,Rectangle):
    kose1 = 0
    yukseklik1 = 0
    
    def __init__(self,kose,yukseklik):
        self.kose1=kose
        self.yukseklik1=yukseklik
        Rectangle.__init__(self,None,yukseklik)
        Triangle.__init__(self,kose)


    def __str__(self):
        return "\nArea=" + "{0:.2f}".format(self.get_area())  + "\nVolume=" + "{0:.2f}".format(self.get_volume())

    def get_area(self):
        return 2*(self.edge **2 * (math.sqrt(3) / 4)) + 3 * (self.edge * self.height)

    def get_volume(self):
        return (self.edge **2 * (math.sqrt(3) / 4)) * self.height

    
class SquarePyramid(Triangle) :     
    
    def __init__(self,kose):
        Triangle.__init__(self,kose)

    def __str__(self):
        return "\nArea=" + "{0:.2f}".format(self.get_area())

    def get_area(self):
        return (self.edge**2) + 3*(self.edge **2 * (math.sqrt(3) / 4))
    
