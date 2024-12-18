import re, math
from itertools import combinations

from helpers import fileutils, point

def calculate_cost_from_button_presses(presses_a, presses_b):
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
                cost = calculate_cost_from_button_presses(a,b)
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
            cost = calculate_cost_from_button_presses(a,b)                
            print(f'DEBUG: Turn: button_a={button_a} button_b={button_b} prize={prize} cost={cost}')
            total_cost += cost
        elif size > 1: # Only appears to be one solution per turn!
            raise("Multiple solutions!")

    return total_cost



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


def old_solve_part2(filename, prize_offset):
    turns = get_turn_info_from(filename, prize_offset)
    assert len(turns) > 0

    total_cost = 0
    for t in turns:                
        button_a, button_b, prize = t
        print(f'DEBUG: Turn: button_a={button_a} button_b={button_b} prize={prize}')

        map = dict() # map of gradient to hypotenuse & cost

        a_h, a_g = get_point_info(button_a)        
        map[a_g] = (a_h, 3, button_a)
        b_h, b_g = get_point_info(button_b)
        map[b_g] = (b_h, 1, button_b)
        button_ab = point.Point2D(button_a.get_x() + button_b.get_x(), button_a.get_y() + button_b.get_y())         
        ab_h, ab_g = get_point_info(button_ab)   
        map[ab_g] = (ab_h, 4, button_ab)
        button_abb = point.Point2D(button_a.get_x() + 2 * button_b.get_x(), button_a.get_y() + 2 * button_b.get_y())         
        abb_h, abb_g = get_point_info(button_abb)   
        map[abb_g] = (abb_h, 5, button_abb)
        button_abbb = point.Point2D(button_a.get_x() + 3 * button_b.get_x(), button_a.get_y() + 3 * button_b.get_y())         
        abbb_h, abbb_g = get_point_info(button_abbb)   
        map[abbb_g] = (abbb_h, 6, button_abbb)
        p_h, p_g = get_point_info(prize)

        
        min_diff = None
        index = None
        for k in map.keys():
            d = abs(p_g - k)
            if min_diff == None or d < min_diff:
                min_diff = d
                index = k        
        print(f"DEBUG: match index={index}")


        #print(f"DEBUG: a_g={a_g} a_h={a_h}")
        #print(f"DEBUG: b_g={b_g} b_h={b_h}")
        #print(f"DEBUG: ab_g={ab_g} ab_h={ab_h}")
        #print(f"DEBUG: abb_g={abb_g} abb_h={abb_h}")
        #print(f"DEBUG: abbb_g={abbb_g} abb_h={abbb_h}")
        #print(f"DEBUG: p_g={p_g} p_h={p_h}")

        print(f'DEBUG: map={map}')
        h, c, p = map[index]
        

        rounds = int(prize_offset // h)
        cost_offset = rounds * c
        target = (prize.get_x() - rounds * p.get_x(), prize.get_y() - rounds * p.get_y())
        print(f'DEBUG: rounds={rounds} cost={cost_offset} target={target} prize={prize} p={p}')
        
        
        prize = p

        fx = find_combination_multiples_factors(button_a.get_x(), button_b.get_x(), prize.get_x())
        fy = find_combination_multiples_factors(button_a.get_y(), button_b.get_y(), prize.get_y())
        intersection = fx & fy
        #print(f"DEBUG: fx={fx}")
        if intersection:
            print(f'DEBUG: Turn: button_a={button_a} button_b={button_b} prize={prize}')
            
            cost = cost_offset + min(calculate_cost_from_button_presses(i[0], i[1]) for i in intersection)
            print(f"DEBUG: Bingo! intersection={intersection}  cost={cost} fx={fx} fy={fy}")
            total_cost += cost
        
        #break

    return total_cost
"""
def solve_spedulartively(ax, ay, bx, by, px, py) -> int:
    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx
        
    if ca % 1 == cb % 1 == 0:
        return calculate_cost_from_button_presses(ca, cb)
    return 0



def solve(ax, ay, bx, by, px, py) -> int:
    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx
        
    if ca % 1 == cb % 1 == 0:
        return calculate_cost_from_button_presses(ca, cb)
    return 0
"""


def determine_buttons_presses_speculatively(ax, ay, bx, by, px, py) -> (int,int):
    max_presses_per_button = 100

    x_start = 0
    y_start = 0


    d = px // 100
    if d > max_presses_per_button:
        px -= d
        py -= d
    else:
        d = 0

    print(f"DEBUG: d={d} px={px} py={py}")
        
    for a in range(1 + x_start, 1 + max_presses_per_button):
        x = a * ax
        y = a * ay

        for b in range(1 + y_start, 1 + max_presses_per_button):
            #print(f'DEBUG: a={a} b={b}')
            x += bx
            y += by

            if x == px and y == py:
                return (a,b)    
    return (None, None)



def determine_buttons_presses(ax, ay, bx, by, px, py) -> (int,int):
    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx
        
    if ca % 1 == cb % 1 == 0:
        return (int(ca), int(cb))
    return (None, None)


def solve_part2(filename, prize_offset):
    total = 0

    #a_presses = set()
    #b_presses = set()
    for block in open(filename).read().split("\n\n"):
        instr = map(int, re.findall(r"\d+", block))
        ax, ay, bx, by, px, py = instr
        px += prize_offset
        py += prize_offset

        (ca,cb) = determine_buttons_presses(ax, ay, bx, by, px, py)
        if ca and cb:
            total += calculate_cost_from_button_presses(ca, cb)        

    #return int(total)
    #print(f"DEBUG: min a_presses={min(a_presses)} b_presses={min(b_presses)}")
    return total
        
