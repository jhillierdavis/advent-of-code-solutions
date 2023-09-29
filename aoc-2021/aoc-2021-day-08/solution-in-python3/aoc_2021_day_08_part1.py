import fileutils

def count_words_by_length(input_str:str, list_word_sizes:[int]) -> int:
    words = input_str.split(" ")

    #print(f"DEBUG: words={words}")

    count = 0
    for word in words:
        if len(word) in list_word_sizes:
            count += 1
    return count

def count_words_by_length_from_file(filename:str, list_word_sizes:[int]) -> int:
    lines = fileutils.get_file_lines(filename)

    count = 0
    for line in lines:
        parts = line.split("|")
        count += count_words_by_length(parts[1], list_word_sizes)

    return count