import random

class TrianglePathSolver:

    def __init__(self, file=None,seed=50,triangle_depth=50):

        if file:
            with open(file) as tri:
                self.tri = [e.strip('\n').split() for e in tri.readlines()]
                self.tri = [[int(i) for i in e] for e in self.tri]
        else:
            self.tri = self.generate_triangle(triangle_depth,seed)

    def generate_triangle(self,depth,s):
        random.seed(s)
        return [[random.randint(1,100) for _ in range(e)] for e in range(1,depth+1)]

    def solve_triangle(self):
        iterating_triangle = self.tri
        last = [(e,[e]) for e in iterating_triangle.pop()]
        iterating_triangle.append(last)
        all_paths = []
        while True:
            last_line = iterating_triangle.pop()
            if not iterating_triangle:
                return (((last_line[0][0],last_line[0][1],len(last_line[0][1]))),all_paths)
            second_last_line = iterating_triangle.pop()
            new_line = []
##            previous_line_paths = [e[1] for e in last_line]
##            this_line_paths = []
            for i,e in enumerate(second_last_line):
                two_prior = last_line[i:i+2]
                max_prev = max(two_prior,key=lambda x:x[0])
                new = (e + max_prev[0],max_prev[1]+[e])
##                this_line_paths.append(new[1])
                new_line.append(new)
            iterating_triangle.append(new_line)
            

if __name__ == '__main__':

    t = TrianglePathSolver(file='triangle.txt')
##    t = TrianglePathSolver(seed=234,triangle_depth=1200)
    solution_total = t.solve_triangle()
    solution = solution_total[0]
    paths = solution_total[1]
    print('The max sum is: ',solution[0])
    print('The path is: ',solution[1][::-1])
    print('The path length is: ',solution[2])
