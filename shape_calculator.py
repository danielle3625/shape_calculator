class Rectangle:
    """
    Create a rectangle and define functions for calculating area, perimeter, diag, and a picture representation
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # set_width
    def set_width(self, width):
        self.width = width

    # set_height
    def set_height(self, height):
        self.height = height

    #get_area: Returns area (width * height)
    def get_area(self):
        area = self.width * self.height
        return area

    #get_perimeter: Returns perimeter (2 * width + 2 * height)
    def get_perimeter(self):
        per = (2 * self.width) + (2 * self.height)
        return per

    #get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
    def get_diagonal(self):
        return((self.width ** 2 + self.height ** 2) ** .5)

    #get_picture: 
    def get_picture(self):
        """
        Returns a string that represents the shape using lines of "*". 
        The number of lines should be equal to the height and * the number of "*" 
        in each line should be equal to the width. There should be a new line (\n) at the end of each line. 
        If the width * or height is larger than 50, this should return the string: "Too big for picture.".
        """
        line = ''
        if self.width and self.height <= 50:
            per_width = '*' * self.width
            for n in range(0, self.height):
                line = per_width + '\n' + line
            return line.rstrip()
        else:
            return 'Too big for picture.'
                

    #get_amount_inside: 
    def get_amount_inside(self, shape):

        self.shape = shape
        
        num_times = self.get_area() / (self.width * self.width)
        return int(num_times)
        


    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.width = side
        Rectangle.height = side

    def set_side(self, value):
        Rectangle.set_width(self, value)
        Rectangle.set_height(self, value)
    
    def __str__(self):
        return f'Square(side={self.width})'