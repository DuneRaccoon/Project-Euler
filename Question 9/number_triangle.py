def number_triangle(of_height):
    if of_height == 0: return False
    elif of_height == 1: return 1
    else:
        row = ' '*of_height-1 + '1' + ' '*of_height-1
        
