import random
import time

print("In this round, we have CODING MINDS versus the Super Computer!")
time.sleep(2)
print()

# Generate opponent stats
opponent_health = random.randint(10, 200)
opponent_damage = random.randint(10, 50)
opponent_shield = random.randint(15, 50)
time.sleep(1)

print("Your opponent's monster has", opponent_health, "health.")
print("Your opponent's monster can do", opponent_damage, "damage.")
print("Your opponent's monster has", opponent_shield, "shield.")
time.sleep(2)
print()

# Define attribute types
attributes = ["Fire", "Water", "Grass"]
selected_attribute = random.choice(attributes)

# Define player deck
player_deck = {
    1: {"name": "Slime", "HP": 5, "ATK": 2, "DEF": 1},
    2: {"name": "Dragon", "HP": 100, "ATK": 50, "DEF": 30},
    3: {"name": "FlappyBird", "HP": 20, "ATK": 5, "DEF": 1},
    4: {"name": "BongoCat", "HP": 10, "ATK": 5, "DEF": 5},
    5: {"name": "Bahamut", "HP": 100, "ATK": 50, "DEF": 30},
    6: {"name": "Mario & Luigi", "HP": 100, "ATK": 20, "DEF": 30}
}

# Select a random monster card
player_card_num = random.randint(1, 6)
player_card = player_deck[player_card_num]

print(f"You will use monster {player_card_num} - {player_card['name']} from your deck.")
print(f"You will use attribute {selected_attribute} in this round!")
time.sleep(1.5)
print()

print("=== Your Monster Stats ===")
print(f"HP: {player_card['HP']}")
print(f"ATK: {player_card['ATK']}")
print(f"DEF: {player_card['DEF']}")
print()

# Battle simulation
player_hp = player_card['HP']
opponent_hp = opponent_health
round_num = 1

while player_hp > 0 and opponent_hp > 0:
    print(f"--- Round {round_num} ---")
    
    # Player attacks
    player_attack = max(0, player_card['ATK'] - opponent_shield)
    opponent_hp -= player_attack
    print(f"You deal {player_attack} damage to the opponent. Opponent HP is now {max(opponent_hp, 0)}.")
    
    # Opponent attacks
    opponent_attack = max(0, opponent_damage - player_card['DEF'])
    player_hp -= opponent_attack
    print(f"Opponent deals {opponent_attack} damage to you. Your HP is now {max(player_hp, 0)}.")
    
    print()
    time.sleep(1.5)
    round_num += 1

# Outcome
if player_hp <= 0 and opponent_hp <= 0:
    print("It's a draw! Both monsters fainted!")
elif player_hp <= 0:
    print("You lost! The Super Computer's monster wins!")
elif opponent_hp <= 0:
    print("You win! CODING MINDS defeats the Super Computer!")
