from helpers import fileutils


def get_sorted_lists_from(filename):
    lines = fileutils.get_file_lines_from(filename)

    a1 = []
    a2 = []
    for l in lines:
        values = l.split('   ')
        #print(f'DEBUG: l={l} values={values}')
        a1.append(int(values[0]))
        a2.append(int(values[1]))

    a1.sort()
    a2.sort()
    #print(f'DEBUG: a1={a1}')
    #print(f'DEBUG: a2={a2}')
    return a1, a2


def get_sum_of_absolute_distance_between_array_lists(a1, a2):
    count_dist = 0
    for i in range(len(a1)):
        count_dist += abs(a1[i] - a2[i])

    return count_dist


def solve_part1(filename):
    a1, a2 = get_sorted_lists_from(filename) 
    return get_sum_of_absolute_distance_between_array_lists(a1, a2)


def get_sum_of_frequency_of_occurance_of_elements_of_first_list_in_second_list(a1, a2):
    count_freq = 0
    for i in range(len(a1)):
        value = a1[i]
        count_freq += value * a2.count(value) # Ref. https://www.w3schools.com/python/ref_list_count.asp

    return count_freq


def solve_part2(filename):
    a1, a2 = get_sorted_lists_from(filename) 
    return get_sum_of_frequency_of_occurance_of_elements_of_first_list_in_second_list(a1, a2)