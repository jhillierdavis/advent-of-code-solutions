from helpers import fileutils
from collections import deque


# Trying out: Variable naming prefix convention
#
# c_* = char
# s_* = string
# i_* = int
# a?_* = array (subsequent char states type of contained elements)
# l?_* = list (subsequent char states type of contained elements)
# s?_* = set (subsequent char states type of contained elements) NB: At Least 2 chars before _ , so distinct from string
# d??_* = dictionary (subsequent chars states types of key & value)
#


def get_middle_int_array_value(a_int):
    i_middle = len(a_int)//2
    return a_int[i_middle]

def is_valid_page_number_ordering(li_page_numbers, orderings):
    i_length = len(li_page_numbers)
    for i in range(i_length):
        i_current_page_number = li_page_numbers[i]

        for j in range((i+1), i_length):            
            i_subsequent_page_number = li_page_numbers[j]
            li_higher_priority_page_numbers = orderings.get(i_subsequent_page_number)
            
            if li_higher_priority_page_numbers == None:
                continue
            if i_current_page_number in li_higher_priority_page_numbers:
                return False
    return True

def get_dictionary_of_page_orderings_before_from(as_lines):
    dili_page_orderings_before = dict()

    for s_line in as_lines:
        as_values = s_line.split('|')
        i_key = int(as_values[0])
        i_value = int(as_values[1])
        ai_page_numbers_before = dili_page_orderings_before.get(i_key)
        if None == ai_page_numbers_before:
            ai_page_numbers_before = []
        ai_page_numbers_before.append(i_value)
        dili_page_orderings_before.update({i_key: ai_page_numbers_before})  

    return dili_page_orderings_before


def get_dictionary_of_page_orderings_after_from(as_lines):
    dili_page_orderings_afer = dict()

    for s_line in as_lines:
        as_values = s_line.split('|')
        i_value = int(as_values[0])
        i_key = int(as_values[1])
        ai_page_numbers_after = dili_page_orderings_afer.get(i_key)
        if None == ai_page_numbers_after:
            ai_page_numbers_after = []
        ai_page_numbers_after.append(i_value)
        dili_page_orderings_afer.update({i_key: ai_page_numbers_after})  

    return dili_page_orderings_afer


def get_list_of_page_numbers_from(s_line):
    as_values = s_line.split(',')
    li_pages = []
    for s_value in as_values:
        i_page_number = int(s_value)
        li_pages.append(i_page_number)
    return li_pages


def solve_part1(s_filename):
    as_lines = fileutils.get_lines_before_empty_from_file(s_filename)

    dili_orderings = get_dictionary_of_page_orderings_before_from(as_lines)

    as_lines = fileutils.get_lines_after_empty_from_file(s_filename)

    i_answer = 0
    for s_line in as_lines:
        li_pages = get_list_of_page_numbers_from(s_line)

        if is_valid_page_number_ordering(li_pages, dili_orderings):
            i_answer += get_middle_int_array_value(li_pages)

    return i_answer


def get_reprioritised_page_list(li_pages, dili_page_orderings_after):
    qi_page_numbers_to_sort = deque(li_pages) # Use a queue to hold yet to be sorted (by priority) page numbers
    li_prioritised_pages = []

    while len(qi_page_numbers_to_sort) > 0:
        i_current_page_number = qi_page_numbers_to_sort.popleft()
        b_is_priority_page_number = True

        for i_unsorted_page_number in qi_page_numbers_to_sort:
            li_priority_pages_after = dili_page_orderings_after.get(i_unsorted_page_number)
            if li_priority_pages_after is not None and i_current_page_number in li_priority_pages_after:
                b_is_priority_page_number = False
                break

        if b_is_priority_page_number: # Top-priority page amongst remaining page numbers
            li_prioritised_pages.append(i_current_page_number)
        else: # Return non-priority page number to queue for subsequent re-processing
            qi_page_numbers_to_sort.append(i_current_page_number)

    return li_prioritised_pages
        

def solve_part2(s_filename):
    as_lines = fileutils.get_lines_before_empty_from_file(s_filename)

    dili_page_orderings_before = get_dictionary_of_page_orderings_before_from(as_lines)
    dili_page_orderings_after = get_dictionary_of_page_orderings_after_from(as_lines)

    as_lines = fileutils.get_lines_after_empty_from_file(s_filename)

    i_answer = 0
    for s_line in as_lines:
        li_pages = get_list_of_page_numbers_from(s_line)
        
        if not is_valid_page_number_ordering(li_pages, dili_page_orderings_before):
            l_reprioritised_pages = get_reprioritised_page_list(li_pages, dili_page_orderings_after)
            i_answer += get_middle_int_array_value(l_reprioritised_pages)

    return i_answer