import utils

def get_most_common_bit(offset, entries, default_value='1'):
    occurances = dict()

    for entry in entries:
        #print(f"DEBUG: entry={entry} offset={offset}")
        value = entry[offset]
        if value in occurances:
            occurances[value] += 1
        else:
            occurances[value] = 1

    #print(f"DEBUG: {occurances}")

    max_value = ""
    max_count = 0
    for key in occurances.keys():
        if occurances[key] == max_count:
            max_value = default_value
        elif occurances[key] > max_count:
            max_value = key
            max_count = occurances[key]
            
    return max_value

def get_least_common_bit(offset, entries):
    most_common_bit = get_most_common_bit(offset, entries)
    if '1' == most_common_bit:
        return '0'
    return '1'

def get_gamma_rate(filename):

    lines = utils.get_file_lines(filename)
    #print(f"DEBUG: lines={lines}")

    bit_length = len(lines[0])

    gamma_value = ""
    for i in range(0, bit_length):
        gamma_value = gamma_value + (get_most_common_bit(i, lines))    

    #for line in lines:

    return gamma_value

def get_epsilon_rate_from_gamma_rate(gamma_rate):
    inverse = ""
    for i in range(len(gamma_rate)):
        if gamma_rate[i] == "1":
            inverse = inverse + "0"
        else:
            inverse = inverse + "1"
    return inverse

def get_power_consumption_from_file(filename):
    gamma_rate:int = get_gamma_rate(filename)
    gamma_rate_int_value = utils.decimal_value_of_binary_string(gamma_rate)

    epsilon_rate = get_epsilon_rate_from_gamma_rate(gamma_rate)
    epsilon_rate_int_value = utils.decimal_value_of_binary_string(epsilon_rate)

    power_consumption = gamma_rate_int_value * epsilon_rate_int_value
    return power_consumption

# gamma_rate = get_gamma_rate('data-sample.txt')
# assert "10110" == gamma_rate, f"Not as expected: gamma_rate={gamma_rate}"
# gamma_rate_int_value = utils.decimal_value_of_binary_string(gamma_rate)
# assert  gamma_rate_int_value == 22

# epsilon_rate = get_epsilon_rate_from_gamma_rate(gamma_rate)
# assert "01001" == epsilon_rate, f"Not as expected: epsilon_rate={epsilon_rate}"
# epsilon_rate_int_value = utils.decimal_value_of_binary_string(epsilon_rate)
# assert epsilon_rate_int_value == 9

# power_consumption = gamma_rate_int_value * epsilon_rate_int_value
# assert power_consumption == 198

def calculate_oxygen_generator_rating(offset, entries):
    if len(entries) < 1:
        return ""
    
    if len(entries) == 1:
        return entries[0]
    
    most_common = get_most_common_bit(offset, entries, '1')

    subset = []
    for entry in entries:
        if entry[offset] == most_common:
            subset.append(entry)

    return calculate_oxygen_generator_rating(1 + offset, subset)


def calculate_co2_scrubber_rating(offset, entries):
    if len(entries) < 1:
        return ""
    
    if len(entries) == 1:
        return entries[0]
    
    least_common = get_least_common_bit(offset, entries)

    subset = []
    for entry in entries:
        if entry[offset] == least_common:
            subset.append(entry)

    return calculate_co2_scrubber_rating(1 + offset, subset)

def get_oxygen_generator_rating(entries):
    oxygen_generator_rating =  calculate_oxygen_generator_rating(0, entries)
    oxygen_generator_rating_int_value = utils.decimal_value_of_binary_string(oxygen_generator_rating)
    return oxygen_generator_rating_int_value

def get_co2_scrubber_rating(entries):
    co2_scrbber_rating =  calculate_co2_scrubber_rating(0, entries)
    co2_scrbber_rating_int_value = utils.decimal_value_of_binary_string(co2_scrbber_rating)
    return co2_scrbber_rating_int_value


def get_life_support_rating(filename):
    lines = utils.get_file_lines(filename)
    return get_oxygen_generator_rating(lines) * get_co2_scrubber_rating(lines)

