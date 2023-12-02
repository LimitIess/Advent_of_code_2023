
file_input = open("data2.txt", "r")

sum_of_games = 0
for row in file_input.readlines():
    game_id, draws = row.split(":")
    game, id_num = game_id.split()
    letter = 0
    print(row)
    while letter < len(draws):
        if draws[letter].isnumeric() and draws[letter+1].isnumeric():
            if draws[letter+3] == "r" and int(draws[letter]+draws[letter+1])>12:
                break
            elif draws[letter+3] == "g" and int(draws[letter]+draws[letter+1])>13:
                break
            elif draws[letter+3] == "b" and int(draws[letter]+draws[letter+1])>14:
                break
        letter +=1
        if letter == len(draws)-1:
            print(f"Game {id_num} is possible.")
            sum_of_games += int(id_num)
print(sum_of_games)
    #game, id = game_id.split()
    #list_of_draws = draws.split(";")
    #for draw in list_of_draws:
    #    cubes = draw.split(",")
    #    for cube in cubes:
            
