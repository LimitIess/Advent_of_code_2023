file_input = open("data2.txt", "r")
list_of_points = []
read_file = file_input.readlines()

list_of_cards = [1]*len(read_file)
for row in read_file:
    score_counter = 0
    card, numbers = row.split(":")
    _, card_id = card.split()
    winning_numbers, card_numbers  = numbers.split("|")
    card_numbers = card_numbers.split()
    winning_numbers = winning_numbers.split()
    tmp_counter = 0
    for number in range(len(winning_numbers)):
        if winning_numbers[number] in card_numbers:
            tmp_counter +=1
    for win_index in range(int(card_id), tmp_counter+int(card_id)):
        list_of_cards[win_index] += list_of_cards[int(card_id)-1]
print(sum(list_of_cards))        
