
def comma_separated_values_to_list(csvs:str) -> list:
    output_list = []
    input = csvs.strip()
    if input:
        output_list = [value.strip() for value in csvs.strip().split(',')]
    return output_list