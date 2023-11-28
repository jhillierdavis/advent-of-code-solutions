
def calculate_sequence(speed_x, speed_y, max_steps):
    seq = []
    current_pos_x = 0
    current_pos_y = 0
    current_speed_x = speed_x
    current_speed_y = speed_y
    for i in range(max_steps):
        current_pos_x += current_speed_x
        current_pos_y += current_speed_y
        seq.append((current_pos_x, current_pos_y))    

        # Adjust speeds
        if current_speed_x > 0:    
            current_speed_x -= 1
        elif current_speed_x < 0:
            current_speed_x += 1
        current_speed_y -= 1
    return seq


def transits_target_rectangle(sequence, target_area):
    for i in range(len(sequence)):
        p = sequence[i]        
        if p[0] >= target_area[0] and p[0] <= target_area[1]:
            if p[1] >= target_area[2] and p[1] <= target_area[3]:
                #print(f"DEBUG: Point {p} within target at sequence index {i}")
                return True
    return False

def calculate_max_y_in_xy_sequence_list(xy_sequence_list):
    # Gather all y values from list of (x,y) entries & return the max y value
    return max(map(lambda entry: entry[1], xy_sequence_list))

def calculate_height(target_rectange, target_speeds):
    return 0

def calculate_max_height(target_rectange):
    return 0 # TODO