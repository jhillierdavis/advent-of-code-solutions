# Initial simplistic solution approach (to solve part1) - does NOT scale (for large number of elapsed days)!

def daily_growth(fish_ages:[int]):
    new_fish_ages = []
    offspring:int = 0
    for entry in fish_ages:
        if 0 == entry:
            offspring = 1 + offspring
            new_fish_ages.append(6)
        else:
            new_fish_ages.append(entry - 1)
    
    for i in range(offspring):
        new_fish_ages.append(8)

    return new_fish_ages
        
def get_number_of_fish_after_elapsed_days(initial_fish_ages:[int], days:int) -> int:
    fish_ages = initial_fish_ages   
    for i in range(days):
        fish_ages = daily_growth(fish_ages)
        #print(f"DEBUG: {fish_ages}")

    return len(fish_ages)