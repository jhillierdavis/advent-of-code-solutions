from helpers import fileutils
from collections import deque

from typing import Callable, Any, Iterable


def get_middle_value_from(array_of_integers:Iterable[int]) -> int:
    size =  len(array_of_integers)
    if size <= 0: # Guard
        return None
    
    middle_index = size//2
    if size % 2 == 0: # Even length
        middle_index -= 1
    return array_of_integers[middle_index]


def is_valid_page_number_ordering(list_of_page_numbers:list[int], orderings:dict[int:int]) -> bool:
    size = len(list_of_page_numbers)
    for i in range(size):
        current_page_number = list_of_page_numbers[i]

        for next in range((i+1), size):            
            subsequent_page_number = list_of_page_numbers[next]
            list_of_higher_priority_page_numbers = orderings.get(subsequent_page_number)
            
            if list_of_higher_priority_page_numbers == None:
                continue
            if current_page_number in list_of_higher_priority_page_numbers:
                return False
    return True


def get_dictionary_of_page_orderings_before_from(lines:Iterable[str]) -> dict:
    lookup_priority_before = dict()

    for l in lines:
        values = l.split('|')
        first:int = int(values[0])
        second:int = int(values[1])

        list_of_pages_before = lookup_priority_before.get(first)
        if None == list_of_pages_before:
            list_of_pages_before = [] # Initalise
        list_of_pages_before.append(second)

        lookup_priority_before.update({first: list_of_pages_before})  

    return lookup_priority_before


def get_dictionary_of_page_orderings_after_from(lines:Iterable[str]) -> dict:
    lookup_priority_after = dict()

    for l in lines:
        values = l.split('|')
        first:int = int(values[0])
        second:int = int(values[1])        
        list_of_pages_after = lookup_priority_after.get(second)
        if None == list_of_pages_after:
            list_of_pages_after = [] # Initialise
        list_of_pages_after.append(first)
        lookup_priority_after.update({second: list_of_pages_after})  

    return lookup_priority_after


def get_list_of_page_numbers_from(iterable_lines:Iterable[str]) -> Iterable[int]:
    list_of_page_numbers = []

    array_of_values = iterable_lines.split(',')
    for string_value in array_of_values:
        page_number = int(string_value)
        list_of_page_numbers.append(page_number)
    return list_of_page_numbers


def solve_part1(filename:str) -> int:
    lines = fileutils.get_lines_before_empty_from_file(filename)

    orderings = get_dictionary_of_page_orderings_before_from(lines)

    lines = fileutils.get_lines_after_empty_from_file(filename)

    answer:int = 0
    for l in lines: # Process each input line of page numbers
        list_of_pages = get_list_of_page_numbers_from(l)

        if is_valid_page_number_ordering(list_of_pages, orderings):
            answer += get_middle_value_from(list_of_pages)

    return answer


def get_reprioritised_page_numbers(list_of_unprioritised_page_numbers:Iterable[int], page_orderings_after:dict[int:Iterable[int]]) -> Iterable[int]:
    queue_of_unprioritised_page_numbers = deque(list_of_unprioritised_page_numbers)
    list_of_prioritised_pages = []

    while len(queue_of_unprioritised_page_numbers) > 0:
        current_page_number = queue_of_unprioritised_page_numbers.popleft()
        is_priority_page_number = True

        for pn in queue_of_unprioritised_page_numbers:
            list_of_priority_pages_after = page_orderings_after.get(pn)
            if list_of_priority_pages_after is not None and current_page_number in list_of_priority_pages_after:
                is_priority_page_number = False
                break

        if is_priority_page_number: # Top-priority page amongst remaining page numbers
            list_of_prioritised_pages.append(current_page_number)
        else: # Return non-priority page number to queue for subsequent re-processing
            queue_of_unprioritised_page_numbers.append(current_page_number)

    return list_of_prioritised_pages
        

def solve_part2(filename:str) -> int:
    lines = fileutils.get_lines_before_empty_from_file(filename)

    orderings_before = get_dictionary_of_page_orderings_before_from(lines)
    orderings_after = get_dictionary_of_page_orderings_after_from(lines)

    lines = fileutils.get_lines_after_empty_from_file(filename)

    answer:int = 0
    for l in lines: # Process each input line of page numbers
        list_of_page_numbers = get_list_of_page_numbers_from(l)
        
        if not is_valid_page_number_ordering(list_of_page_numbers, orderings_before):
            list_of_reprioritised_page_numbers = get_reprioritised_page_numbers(list_of_page_numbers, orderings_after)
            answer += get_middle_value_from(list_of_reprioritised_page_numbers)

    return answer