from helpers import fileutils


def solve_part1(filename):
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

    count_diff = 0
    for i in range(len(a1)):
        count_diff += abs(a1[i] - a2[i])

    return count_diff


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
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
 
    count_sim = 0
    for i in range(len(a1)):
        occurs = 0
        for j in range(len(a2)):
            if a1[i] == a2[j]:
                occurs += 1
        count_sim += a1[i] * occurs 

    return count_sim