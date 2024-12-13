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


def get_turn_info_from(filename, prize_offset=0):
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
            prize = point.Point2D(prize_offset + x, prize_offset + y)
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
            print(f'DEBUG: Turn: button_a={button_a} button_b={button_b} prize={prize} cost={cost}')
            total_cost += cost
        elif size > 1: # Only appears to be one solution per turn!
            raise("Multiple solutions!")

    return total_cost

import math

def calculate_gradient(rise, run): 
    if run == 0: 
        return float('inf') # Return infinity if the run is zero (vertical line) gradient = rise / run return
    gradient = rise / run
    return gradient


def calculate_hypotenuse(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

def calculate_point_gradient(p):
    return calculate_gradient(p.get_y(), p.get_x())

def calculate_point_hypotenuse(p):
    return calculate_hypotenuse(p.get_y(), p.get_x())

def get_point_info(p):
    return calculate_hypotenuse(p.get_y(), p.get_x()), calculate_gradient(p.get_y(), p.get_x())


from itertools import combinations

def are_factors(numbers, target):
    factors = set()
    
    # Check each number individually
    for num in numbers:
        if target % num == 0:
            factors.add(num)

    
    
    # Check combinations of numbers
    for r in range(2, len(numbers) + 1):
        for combo in combinations(numbers, r):
            product = 1
            for num in combo:
                product *= num
            if product <= target and target % product == 0:
                factors.add(product)

    print(f"DEBUG: numbers={numbers} factors={factors} target={target}")            
    return factors


def has_factor(numbers, target):
    #print(f"DEBUG: numbers={numbers} target={target}")            
    for n in numbers:
        remainder = target % n
        #print(f"DEBUG: numbers={numbers} target={target} n={n} remainder={remainder}")   
        if remainder ==  0 or remainder in numbers:
            return True
        elif remainder > min(numbers):
            for x in numbers:                
                if x < remainder:
                    
                    r = remainder % x 
                    print(f"DEBUG: numbers={numbers} target={target} n={n} remainder={remainder} x={x} r={r}")  
                    if remainder % x == 0:                                    
                        print("Bingo!")
                        return True
    return False


from itertools import product

def find_combination_multiples_factors(x, y, z):
    multiples_factors = set()
    
    max_x = z // x
    max_y = z // y
    
    for i, j in product(range(1, max_x + 1), range(1, max_y + 1)):
        multiple = (x * i) + (y * j)
        if multiple <= z and z % multiple == 0:
            if z // multiple == 1:
                multiples_factors.add((i,j))
    
    return multiples_factors


def solve_part2(filename, prize_offset):
    turns = get_turn_info_from(filename, prize_offset)
    assert len(turns) > 0

    total_cost = 0
    for t in turns:        
        button_a, button_b, prize = t
        #print(f'DEBUG: Turn: button_a={button_a} button_b={button_b} prize={prize}')
        gradient_a = calculate_point_gradient(button_a)
        gradient_b = calculate_point_gradient(button_b)
        gradient_p = calculate_point_gradient(prize)
        #print(f'DEBUG: Gradients: gradient_a={gradient_a} gradient_b={gradient_b} gradient_p={gradient_p}')

        a_h, a_g = get_point_info(button_a)
        #print(f"DEBUG: a_g={a_g} a_h={a_h}")


        b_h, b_g = get_point_info(button_b)
        #print(f"DEBUG: b_g={b_g} b_h={b_h}")

        p_h, p_g = get_point_info(prize)
        #print(f"DEBUG: p_g={p_g} p_h={p_h}")

        """
        pfx = set()
        pfx.add(button_a.get_x())
        pfx.add(button_b.get_x())
        pfx.add(button_a.get_x() + button_b.get_x())
        pfx.add(button_a.get_x() + 2 * button_b.get_x())
        pfx.add(button_a.get_x() + 3 * button_b.get_x())

        
        pfy = set()
        pfy.add(button_a.get_y())
        pfy.add(button_b.get_y())
        pfy.add(button_a.get_y() + button_b.get_y())
        pfy.add(button_a.get_y() + 2 * button_b.get_y())
        pfy.add(button_a.get_y() + 3 * button_b.get_y())
        """

        fx = find_combination_multiples_factors(button_a.get_x(), button_b.get_x(), prize.get_x())
        fy = find_combination_multiples_factors(button_a.get_y(), button_b.get_y(), prize.get_y())
        intersection = fx & fy
        #print(f"DEBUG: fx={fx}")
        if intersection:
            print(f'DEBUG: Turn: button_a={button_a} button_b={button_b} prize={prize}')
            
            cost = min(calculate_cost(i[0], i[1]) for i in intersection)
            print(f"DEBUG: Bingo! intersection={intersection}  cost={cost} fx={fx} fy={fy}")
            total_cost += cost
        
        #break

    return total_cost