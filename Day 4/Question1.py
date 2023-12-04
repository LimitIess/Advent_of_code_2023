file_input = open("data.txt", "r")
list_of_points = []
for row in file_input.readlines():
    score_counter = 0
    _, numbers = row.split(":")
    winning_numbers,card_numbers  = numbers.split("|")
    card_numbers = card_numbers.split()
    for number in winning_numbers.split():
        if number in card_numbers:
            score_counter += 1
    if score_counter >= 1: 
        list_of_points.append(2**(score_counter-1))
print(sum(list_of_points))        
