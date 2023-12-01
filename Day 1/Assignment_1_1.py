summed_values = 0

file_input = open("data.txt", "r")
for row in file_input.readlines():
    list_words = [letter for letter in row if letter.isdigit()]
    if len(list_words) == 1:
        str_value = int(list_words[0]+list_words[0])
    else:
        str_value = int(list_words[0]+list_words[-1])
    summed_values += str_value
print(summed_values)
