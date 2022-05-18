# class in pyhton


class cube:
    def __init__(self,edge):
        self.edge=edge

    def volume(self):
        return self.edge*self.edge*self.edge

    def surface_area(self):
        return 6*self.edge*self.edge

cube1=cube(3)
print(cube1.volume())
print(cube1.surface_area())
