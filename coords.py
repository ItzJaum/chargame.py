class Coord:
    def __init__(self, x, y=0):
        if type(x) == list or type(x) == tuple:
            if len(x) == 0:
                self.x = -2
                self.y = -2
            else:
                self.x = x[0]
                self.y = x[1]
        elif type(x) == int:
            self.x = x
            self.y = y
        elif type(x) == Coord:
            self.x = x.x
            self.y = x.y
        elif x is None:
            self.x = -2
            self.y = -2         
        
        self.directions = {
            'up': 'self.y -= 1',
            'right': 'self.x += 1',
            'down': 'self.y += 1',
            'left': 'self.x -= 1'
        }

    def mv(self, direction):
        exec(self.directions[direction])

    @property
    def out_list(self):
        return [self.x, self.y]

    def __repr__(self):
        return f'x:{self.x} y:{self.y}'
    
    def __str__(self):
        return f'{self.x} {self.y}'

    def __eq__(self, coord):
        if self.x == coord.x and self.y == coord.y:
            return True
        else:
            return False
    
    def __gt__(self, coord):
        return True if (self.x > coord.x or self.y > coord.y) else False

    def __ge__(self, coord):
        return True if (self.x >= coord.x or self.y >= coord.y) else False

    def __lt__(self, coord):
        return True if (self.x < coord.x or self.y < coord.y) else False
    
    def __le__(self, coord):
        return True if (self.x <= coord.x or self.y <= coord.y) else False
