def calculate_polygon_area_from(coords:list) -> float:
    # Calculate the area of a polygon from the sequence coords (x,y) list provided
    # Uses the area from the x axis between sequential coords for polygon corners (node coords)

    if coords[0] != coords[-1]:
        # First and last item in the list are the same coordinates
        coords.append(coords[0]) 
    
    total_diff = 0
    length = len(coords)
    for i in range(length-1):        
        y_diff = coords[i+1][1] + coords[i][1]
        x_diff = coords[i+1][0] - coords[i][0]
        area_diff = y_diff * x_diff
        total_diff += area_diff
    return abs(total_diff / 2.0)