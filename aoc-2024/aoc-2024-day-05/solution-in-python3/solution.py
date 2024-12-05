from helpers import fileutils
from collections import deque, defaultdict

from typing import Callable, Any, Iterable


def get_middle_value_from(array_of_integers:Iterable[int]) -> int:
    size =  len(array_of_integers)
    if size <= 0: # Guard
        return None
    
    middle_index = size//2
    if size % 2 == 0: # Even length
        middle_index -= 1
    return array_of_integers[middle_index]


def is_valid_page_number_ordering(list_of_page_numbers:list[int], preceding_page_map:dict[int:Iterable[int]]) -> bool:
    size = len(list_of_page_numbers)
    for i in range(size):
        current_page_number = list_of_page_numbers[i]

        for next in range((i+1), size):            
            subsequent_page_number = list_of_page_numbers[next]
            list_of_higher_priority_page_numbers = preceding_page_map.get(subsequent_page_number)
            
            if list_of_higher_priority_page_numbers == None:
                continue
            if current_page_number in list_of_higher_priority_page_numbers:
                return False
    return True


def get_preceding_page_map(lines:Iterable[str]) -> dict[int:Iterable[int]]:
    preceding_page_map = defaultdict(list)

    for l in lines:
        values = l.split('|')
        first:int = int(values[0])
        second:int = int(values[1])

        list_of_pages_before = preceding_page_map[first] # Avoid use of .get() as fails to initialise
        list_of_pages_before.append(second) 

        #preceding_page_map.update({first: list_of_pages_before})   # Unnecessary

    return preceding_page_map


def get_subssequent_page_map(lines:Iterable[str]) -> dict[int:Iterable[int]]:
    subsequent_page_map = defaultdict(list)

    for l in lines:
        values = l.split('|')
        first:int = int(values[0])
        second:int = int(values[1])    

        list_of_pages_after = subsequent_page_map[second] # Avoid use of .get() as fails to initialise
        list_of_pages_after.append(first)
        
        #subsequent_page_map.update({second: list_of_pages_after})  # Unnecessary

    return subsequent_page_map


def get_list_of_page_numbers_from(iterable_lines:Iterable[str]) -> Iterable[int]:
    list_of_page_numbers = []

    array_of_values = iterable_lines.split(',')
    for string_value in array_of_values:
        page_number = int(string_value)
        list_of_page_numbers.append(page_number)
    return list_of_page_numbers


def solve_part1(filename:str) -> int:
    # Process 1st section of page processing rules
    lines = fileutils.get_lines_before_empty_from_file(filename)  
    preceding_page_map = get_preceding_page_map(lines)

    answer:int = 0
    # Process 2nd section of page number updates
    for line in fileutils.get_lines_after_empty_from_file(filename): # Process each input line (string) of page numbers
        list_of_pages = get_list_of_page_numbers_from(line)

        if is_valid_page_number_ordering(list_of_pages, preceding_page_map):
            answer += get_middle_value_from(list_of_pages)

    return answer


def get_reprioritised_page_numbers(list_of_unprioritised_page_numbers:Iterable[int], page_orderings_after:dict[int:Iterable[int]]) -> Iterable[int]:
    queue_of_unprioritised_page_numbers = deque(list_of_unprioritised_page_numbers)
    list_of_prioritised_pages = []

    while len(queue_of_unprioritised_page_numbers) > 0:
        current_page_number = queue_of_unprioritised_page_numbers.popleft()
        is_priority_page_number = True

        for page_number in queue_of_unprioritised_page_numbers:
            list_of_priority_pages_after = page_orderings_after.get(page_number)
            if list_of_priority_pages_after is not None and current_page_number in list_of_priority_pages_after:
                is_priority_page_number = False
                break

        if is_priority_page_number: # Top-priority page amongst remaining page numbers
            list_of_prioritised_pages.append(current_page_number)
        else: # Return non-priority page number to queue for subsequent re-processing
            queue_of_unprioritised_page_numbers.append(current_page_number)

    return list_of_prioritised_pages
        

def solve_part2(filename:str) -> int:
    # Process 1st section of page processing rules
    lines = fileutils.get_lines_before_empty_from_file(filename)
    preceding_page_map = get_preceding_page_map(lines)
    subsequent_page_map = get_preceding_page_map(lines)

    answer:int = 0
    # Process 2nd section of page number updates
    for line in fileutils.get_lines_after_empty_from_file(filename): # Process each input line (string) of page numbers
        list_of_page_numbers = get_list_of_page_numbers_from(line)
        
        if not is_valid_page_number_ordering(list_of_page_numbers, preceding_page_map):
            list_of_reprioritised_page_numbers = get_reprioritised_page_numbers(list_of_page_numbers, subsequent_page_map)
            answer += get_middle_value_from(list_of_reprioritised_page_numbers)

    return answer