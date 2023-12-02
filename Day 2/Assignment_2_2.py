file_input = open("data2.txt", "r")
sum_of_games = 0
for row in file_input.readlines():
    r = 0
    b = 0
    g = 0
    game_id, draws = row.split(":")
    game, id_num = game_id.split()
    letter = 0
    print(row)
    while letter < len(draws):
        if draws[letter].isnumeric() and draws[letter+1].isnumeric():
            if draws[letter+3] == "r" and int(draws[letter]+draws[letter+1])>r:
                r = int(draws[letter]+draws[letter+1])
            elif draws[letter+3] == "g" and int(draws[letter]+draws[letter+1]) > g:
                g  = int(draws[letter]+draws[letter+1])
            elif draws[letter+3] == "b" and int(draws[letter]+draws[letter+1])> b:
                b = int(draws[letter]+draws[letter+1])
        elif draws[letter].isnumeric():
            if draws[letter+2] == "r" and int(draws[letter])>r:
                r = int(draws[letter])
            elif draws[letter+2] == "g" and int(draws[letter])>g:
                g = int(draws[letter])
            elif draws[letter+2] == "b" and int(draws[letter])>b:
                b = int(draws[letter])
        letter +=1
        if letter == len(draws)-1:
            sum_of_games += (r*g*b)
print(sum_of_games)

