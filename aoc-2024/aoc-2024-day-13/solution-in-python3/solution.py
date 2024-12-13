from helpers import fileutils, point

def calculate_cost(presses_a, presses_b):
    # Button A presses cost 3 tokens, Button B presses cost 1 token
    return 3 * presses_a + 1 * presses_b


def determine_tokens(button_a, button_b, price, max_presses_per_button):
    #print(f'DEBUG: button_a={button_a} button_b={button_b} price={price}')

    matches = set()
    for a in range(1, 1 + max_presses_per_button):
        x = a * button_a.get_x()
        y = a * button_a.get_y()

        for b in range(1, 1 + max_presses_per_button):
            #print(f'DEBUG: a={a} b={b}')
            x += button_b.get_x()
            y += button_b.get_y()

            if x == price.get_x() and y == price.get_y():
                cost = calculate_cost(a,b)
                print(f"DEBUG: Bingo! at a={a} b={b} for x={x} y={y} cost={cost}")
                matches.add((a, b))
            elif x > price.get_x():
                break
            elif y > price.get_y():
                break
            #print(f"DEBUG: a={a} b={b} x={x} y={y}")
    return matches


def get_turn_info_from(filename):
    lines = fileutils.get_file_lines_from(filename)

    button_a = None
    button_b = None
    prize = None
    turns = []

    for l in lines:
        if len(l) == 0:
            continue

        label, value = l.split(':')
        left, right = (value.strip()).split(', ')
        x = int(left[2:])
        y = int(right[2:])
        p = point.Point2D(x,y)
        
        if label == 'Prize':
            prize = p
            turns.append((button_a, button_b, prize))
        elif label == 'Button A':
            button_a = p
        elif label == 'Button B':
            button_b = p

    return turns


def solve_part1(filename):
    turns = get_turn_info_from(filename)
    assert len(turns) > 0

    total_cost = 0
    for t in turns:
        button_a, button_b, prize = t
        matches = determine_tokens(button_a, button_b, prize, 100)
        size = len(matches)
        if size == 1:
            a, b = matches.pop()
            cost = calculate_cost(a,b)                
            print(f'DEBUG: button_a={button_a} button_b={button_b} prize={prize} cost={cost}')
            total_cost += cost
        elif size > 1: # Only appears to be one solution per turn!
            raise("Multiple solutions!")

    return total_cost


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"