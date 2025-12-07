num_players = int(input("Enter the number of players: "))
players_data = {}
for i in range(num_players):
    player_name = input(f"Enter the name of player {i + 1}: ")
    ones = int(input(f"Enter the number of ones scored by {player_name}: "))
    twos = int(input(f"Enter the number of twos scored by {player_name}: "))
    fours = int(input(f"Enter the number of fours scored by {player_name}: "))
    sixes = int(input(f"Enter the number of sixes scored by {player_name}: "))
    total_score = ones + 2 * twos + 4 * fours + 6 * sixes
    players_data[player_name] = {"Ones": ones, "Twos": twos, "Fours": fours, "Sixes": sixes, "Total Score": total_score}
print("\nTotal Scores:")
for player_name, player_info in players_data.items():
    print(f"{player_name}: {player_info['Total Score']} points")
