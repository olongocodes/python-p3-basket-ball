def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


def num_points_per_game(player_name):
    #Accessing the game dictionary
    game_data = game_dict()

    #Searching for the player in the home team
    for player in game_data["home"]["players"]:
        if player["name"] == player_name:
            return player["points_per_game"]
        
    #searching for the player in away team  
    for player in game_data["away"]["players"]:
        if player["name"] == player_name:
            return player["points_per_game"]
    
    #return None if the player is not found
    return None

# Example usage:
# player_name = "Bradley Beal"
# points_per_game = num_points_per_game(player_name)

# if points_per_game is not None:
#     print(f"{player_name} has an average of {points_per_game} points per game.")
# else:
#     print(f"Player {player_name} not found.")


def player_age(player_name):
    #Accesiing the game dictionary
    game_data = game_dict()

    #Searching fo player in the home team
    for player in game_data["home"]["players"]:
        if player["name"] == player_name:
            return player["age"]
    
    #searching for player in the away team
    for player in game_data["away"]["players"]:
        if player["name"] == player_name:
            return player["age"]
        
    # Return None if the player is not found
    return None

# Example usage:
# player_name = "Bradley Beal"
# player_age_result = player_age(player_name)

# if player_age_result is not None:
#     print(f"{player_name}'s age is {player_age_result}.")
# else:
#     print(f"Player {player_name} not found.")  

def team_colors(team_name):
    #Accessing the game dictionary
    game_data = game_dict()

    #Checking if the team is in the home team
    if team_name == game_data["home"]["team_name"]:
        return game_data["home"]["colors"]
    
    #checking if the team is the away team
    elif team_name == game_data["away"]["team_name"]:
        return game_data["away"]["colors"]
    
    # Return None if the team is not found
    return None
    


# Example usage:
# team_name = "Washington Wizards"
# team_colors_result = team_colors(team_name)

# if team_colors_result is not None:
#     print(f"The colors of {team_name} are: {', '.join(team_colors_result)}.")
# else:
#     print(f"Team {team_name} not found.")

def team_names():
    game_data = game_dict()

    #Extract team names from the dictionary
    home_team_name = game_data["home"]["team_name"]
    away_team_name = game_data["away"]["team_name"]

    #Return a list of team names
    return [home_team_name, away_team_name] 

# Example usage:
# teams = team_names()
# print(f"The teams in the game are: {', '.join(teams)}.")

def player_numbers(team_name):
    game_data = game_dict()

    #checking if the team is the home team
    if team_name == game_data["home"]["team_name"]:
        return[player["number"] for player in game_data["home"]["players"]]
    
    #checking if the team is the away team
    elif team_name == game_data["away"]["team_name"]:
        return [player["number"] for player in game_data["away"]["players"]]
    
    return None

# Example usage:
# team_name = "Cleveland Cavaliers"
# player_numbers_result = player_numbers(team_name)

# if player_numbers_result is not None:
#     print(f"The jersey numbers for {team_name} are: {', '.join(map(str, player_numbers_result))}.")
# else:
#     print(f"Team {team_name} not found.")

def player_stats(player_name):
    game_data = game_dict()

    #searching for the player in the home team
    for player in game_data["home"]["players"]:
        if player["name"] == player_name:
            return player
        
    #searching for player in the away team
    for player in game_data["away"]["players"]:
        if player["name"] == player_name:
            return player
    
    return None

# Example usage:
# player_name = "Rui Hachimura"
# player_stats_result = player_stats(player_name)

# if player_stats_result is not None:
#     print(f"The stats for {player_name} are:\n{player_stats_result}")
# else:
#     print(f"Player {player_name} not found.")

def average_rebounds_by_shoe_brand():
    # Accessing the game dictionary
    game_data = game_dict()

    # Create a dictionary to store shoe brands and corresponding rebounds
    shoe_brand_rebounds = {}

    # Populate the shoe_brand_rebounds dictionary
    for team in game_data.values():
        for player in team["players"]:
            shoe_brand = player["shoe_brand"]
            rebounds = player["rebounds_per_game"]

            # Check if the shoe brand is already in the dictionary
            if shoe_brand in shoe_brand_rebounds:
                shoe_brand_rebounds[shoe_brand].append(rebounds)
            else:
                shoe_brand_rebounds[shoe_brand] = [rebounds]

    # Calculate and print the average rebounds for each shoe brand
    for brand, rebounds_list in shoe_brand_rebounds.items():
        average_rebounds = sum(rebounds_list) / len(rebounds_list)
        print(f"{brand}:  {average_rebounds:.2f} rebounds")

# Example usage:
# average_rebounds_by_shoe_brand()

def player_with_most_career_points():
    game_data = game_dict()

    all_players = game_data["home"]["players"] + game_data["away"]["players"]
    player_with_most_points = max(all_players, key=lambda player: player["career_points"])

    return player_with_most_points["name"]

#Example usage
# most_points_player = player_with_most_career_points()
# print(f"The player with the most career points is: {most_points_player}")

def common_jersy_numbers():
    game_data = game_dict()

    home_numbers = set(player["number"] for player in game_data["home"]["players"])
    away_numbers = set(player["number"] for player in game_data["away"]["players"])

    common_numbers = home_numbers.intersection(away_numbers)
    return list(common_numbers)

#Example usge
# common_numbers = common_jersy_numbers()
# if common_numbers:
#     print(f"The followig jersy numbers are won by players on both teams: {common_numbers}")
# else:
#     print("There sre no common jersy numbers between players on both teams.")
    

def player_with_longest_name():
    game_data = game_dict()

    all_players = game_data["home"]["players"] + game_data["away"]["players"]
    player_with_longest_name = max(all_players, key=lambda player: len(player["name"]))

    return player_with_longest_name["name"]

#example usage
longest_name_player = player_with_longest_name()
print(f"The player with the longest name is: {longest_name_player}")