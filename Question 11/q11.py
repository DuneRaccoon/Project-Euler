import random

def multiply(numbers,val):
    if not numbers[1:]: return val*numbers[0]
    return multiply(numbers[1:],val*numbers[0])

class GridTraversal:

    def __init__(self, grid_file = None,dimensions=20,seed=50):
        if grid_file:
            with open('grid.txt') as grid:
                self.grid = [e.strip('\n').split() for e in grid.readlines()]
        else:
            self.grid = self.generate_grid(dimensions,seed)
        self.seed = seed
        self.grid_coords = [(i,j) for i in range(len(self.grid)) for j in range(len(self.grid))]
        self.directions = ['up','up right','right','down right',
                      'down','down left','left','up left']

    def generate_grid(self,dimensions,s):
        random.seed(s)
        return [[str(random.randint(0,100)) for _ in range(dimensions)] for _ in range(dimensions)]

    def get_numbers(self,x,y,path,direction,of_length):
    ##    print(path)
        if of_length >= len(self.grid) or of_length >= len(self.grid[0]):
            return False
        if direction == 'up' and path == [] and x >= of_length-1:
                return self.get_numbers(x-1,y,path+[self.grid[x][y]],direction,of_length)
        elif direction == 'up' and path:
            if len(path) == of_length:
                return path
            else:
                return self.get_numbers(x-1,y,path+[self.grid[x][y]],direction,of_length)
            
        if direction == 'up right' and path == [] and x >= of_length-1 and y <= len(self.grid[-1]) - of_length:
                return self.get_numbers(x-1,y+1,path+[self.grid[x][y]],direction,of_length)
        elif direction == 'up right' and path:
            if len(path) == of_length:
                return path
            else:
                return self.get_numbers(x-1,y+1,path+[self.grid[x][y]],direction,of_length)

        if direction == 'right' and path == [] and y <= len(self.grid[-1]) - of_length:
                return self.get_numbers(x,y+1,path+[self.grid[x][y]],direction,of_length)
        elif direction == 'right' and path:
            if len(path) == of_length:
                return path
            else:
                return self.get_numbers(x,y+1,path+[self.grid[x][y]],direction,of_length)

        if direction == 'down right' and path == [] and x <= len(self.grid[-1]) - of_length and y <= len(self.grid[-1]) - of_length:
                return self.get_numbers(x+1,y+1,path+[self.grid[x][y]],direction,of_length)
        elif direction == 'down right' and path:
            if len(path) == of_length:
                return path
            else:
                return self.get_numbers(x+1,y+1,path+[self.grid[x][y]],direction,of_length)

        if direction == 'down' and path == [] and x <= len(self.grid[-1]) - of_length:
            return self.get_numbers(x+1,y,path+[self.grid[x][y]],direction,of_length)
        elif direction == 'down' and path:
            if len(path) == of_length:
                return path
            else:
                return self.get_numbers(x+1,y,path+[self.grid[x][y]],direction,of_length)

        if direction == 'down left' and path == [] and x <= len(self.grid[-1]) - of_length and y >= of_length-1:
            return self.get_numbers(x+1,y-1,path+[self.grid[x][y]],direction,of_length)
        elif direction == 'down left' and path:
            if len(path) == of_length:
                return path
            else:
                return self.get_numbers(x+1,y-1,path+[self.grid[x][y]],direction,of_length)

        if direction == 'left' and path == [] and x >= of_length-1:
            return self.get_numbers(x,y-1,path+[self.grid[x][y]],direction,of_length)
        elif direction == 'left' and path:
            if len(path) == of_length:
                return path
            else:
                return self.get_numbers(x,y-1,path+[self.grid[x][y]],direction,of_length)

        if direction == 'up left' and path == [] and x >= of_length-1 and y >= of_length-1:
            return self.get_numbers(x-1,y-1,path+[self.grid[x][y]],direction,of_length)
        elif direction == 'up left' and path:
            if len(path) == of_length:
                return path
            else:
                return self.get_numbers(x-1,y-1,path+[self.grid[x][y]],direction,of_length)

    def get_all_possible_paths(self,length=4):
        paths_dict = {}
        for cell in self.grid_coords:
            x,y = cell
            directions_dict = {}
            for d in self.directions:
                path = self.get_numbers(x,y,[],d,length)
                directions_dict[d] = path
            paths_dict[(self.grid[cell[0]][cell[1]],cell)] = directions_dict
        return paths_dict

    def print_current_grid(self):
        with open('grid_'+str(self.seed)+'.txt','w') as grid:
            for line in self.grid:
                print(' '.join(line),file=grid)

traversal = GridTraversal(dimensions=250)
possible_paths = traversal.get_all_possible_paths(length=86)
max_product = max([(multiply([int(i) for i in e],1),e,k1[1],k2) for k1,v in possible_paths.items() for k2,e in v.items() if e],key=lambda x:x[0])

print('The max product is: ',max_product[0])
print('The path is: ',max_product[1])
print('The start position is: ',max_product[2])
print('In the direction: ',max_product[3])
