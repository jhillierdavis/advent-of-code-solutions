from helpers import fileutils


def int_lines_from(filename):
    lines = fileutils.get_file_lines_from(filename)    
    values = [int(numeric_string) for numeric_string in lines]
    return values


def find_two_terms_for_sum(filename, target_sum):
    values = int_lines_from(filename)
    #print(values)
git 
    size = len(values)
    for i in range(size):
        #print(values[i])

        if values[i] >= target_sum:
            continue

        for j in values[i:]:
            sum = values[i] + j
            #print(f"DEBUG: {values[i]} + {j} = {sum}")
            if sum == target_sum:
                return [values[i], j]

    return [0, 0] # Unmatched!


def find_three_terms_for_sum(filename, target_sum):
    values = int_lines_from(filename)
    #print(values)

    size = len(values)
    for i in range(size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                #print(f"{i} {j} {k}")
                sum = values[i] + values[j] + values[k]
                if sum == target_sum:
                    return [values[i], values[j], values[k]]                


    return [0, 0, 0] # Unmatched!
