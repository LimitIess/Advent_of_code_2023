summed_values = 0

file_input = open("data.txt", "r")
dict_numbers = {"one": 1, "two": 2, "three":3, "four": 4, "five":5, "six":6,
                "seven": 7, "eight": 8, "nine":9}
for row in file_input.readlines():
    print(f"Row: {row}")
    reversed_row = row[::-1]
    print(f"Reversed_row: {reversed_row}")
    tmp_dict = {}
    for number in dict_numbers.keys():
        tmp_2_index = None
        tmp_1_index = None
        if number in row:
            tmp_1_index = row.index(number)
            tmp_2_index = reversed_row.index(number[::-1])
            
        if tmp_2_index and (len(row) - tmp_2_index) != tmp_1_index:
            tmp_dict[tmp_1_index] = str(dict_numbers[number])
            tmp_dict[len(row)- tmp_2_index] = str(dict_numbers[number])
        elif tmp_2_index:
            tmp_dict[tmp_1_index] = str(dict_numbers[number])
            
    for letter in range(len(row)):
        if row[letter].isdigit():
            tmp_dict[letter] = row[letter]    
    if len(tmp_dict.keys()) == 1:
        get_element = list(tmp_dict.keys())[0]
        str_value = int(tmp_dict[get_element]+tmp_dict[get_element])
    else:
        max_value = max(tmp_dict.keys())
        min_value = min(tmp_dict.keys())
        str_value = int(tmp_dict[min_value]+tmp_dict[max_value])
    print(f"Value: {str_value}")
    summed_values += str_value
    
print(summed_values)
