# Simple validation of supplied values

def is_valid_non_empty_string(value:str):
    if not value:
        return False
    return isinstance(value, str) and len(value.strip()) > 0

def is_valid_positve_non_zero_int_value(value:int):
    #if not value or type(value) is not int or value <= 0:
    if not value or not isinstance(value, int) or value <= 0:
        return False
    return True