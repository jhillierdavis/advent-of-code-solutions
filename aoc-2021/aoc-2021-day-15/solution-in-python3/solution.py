from helpers import grid, fileutils, point


def get_next_lowest_risk_point(citon_grid:grid.Grid2D, current_point):
    x = current_point.get_x()
    y = current_point.get_y()

    point_next_down = point.Point2D(x, y+1)
    point_next_across = point.Point2D(x+1, y)

    if x >= citon_grid.get_width() - 1:
        return point_next_down

    if y >= citon_grid.get_height() - 1:
        return point_next_across
    
    symbol_next_down = int(citon_grid.get_symbol(point_next_down))
    symbol_next_across = int(citon_grid.get_symbol(point_next_across))

    if symbol_next_down <= symbol_next_across:
        return point_next_down
    else:
        return point_next_across


def calculate_initial_path_score(citon_grid:grid.Grid2D):
    current_point = point.Point2D(0,0)

    score = 0
    while not (current_point.get_x() >= citon_grid.get_width() - 1 and current_point.get_y() >= citon_grid.get_height() -1):
        current_point = get_next_lowest_risk_point(citon_grid, current_point)
        score += int(citon_grid.get_symbol(current_point))

    return score

def calculate_initial_path_score_from_file(filename):
    lines = fileutils.get_file_lines(filename)
    citon_grid = grid.lines_to_grid(lines)
    return calculate_initial_path_score(citon_grid)

def add_score(scores, citon_grid:grid.Grid2D, current_point, current_score):
    x = current_point.get_x()
    y = current_point.get_y()
    
    new_score = current_score
    if not (x == 0 and y == 0):
        symbol = int(citon_grid.get_symbol(current_point))
        #print(f"DBEUG: At current_point={current_point} symbol={symbol}" )
        new_score += int(citon_grid.get_symbol(current_point))
        for s in scores:
            if new_score >= s:
                print(f"DEBUG: Abandoning path with running score={new_score} greater (or equals to) s={s}")
                return 

    if x >= citon_grid.get_width() - 1 and y >= citon_grid.get_height() -1:
        if new_score not in scores:
            print(f"DBEUG: Addd final score={new_score} at current_point={current_point} symbol={symbol}" )
        scores.add(new_score)
        return
    
    
    if False:
        x = current_point.get_x() 
        if x < citon_grid.get_width() - 1:
            x += 1

        y =  current_point.get_y()
        if current_point.get_y() < citon_grid.get_height() - 1:  
            y += 1          

        add_score(scores, citon_grid, point.Point2D(x, y), new_score)

    if x < citon_grid.get_width() - 1:
        add_score(scores, citon_grid, point.Point2D(x+1, y), new_score)

    if y < citon_grid.get_height() - 1:        
        add_score(scores, citon_grid, point.Point2D(x, y+1), new_score)


def calculate_lowest_risk_score_from_grid(citon_grid):
    start_point = point.Point2D(0,0)

    scores = set()
    scores.add(calculate_initial_path_score(citon_grid))

    add_score(scores, citon_grid, start_point, 0)
    print(f"DEBUG: scores={scores}")

    return min(scores)

def calcuate_lowest_risk_score(filename):
    lines = fileutils.get_file_lines(filename)
    citon_grid = grid.lines_to_grid(lines)
    return calculate_lowest_risk_score_from_grid(citon_grid)
    #return calculate_initial_path_score(citon_grid)