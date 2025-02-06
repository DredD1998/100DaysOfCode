game_level = 10

enemies = ["Supriya","Zara","Priyanka"]

def create_enemy():
    new_enemies = " "
    if game_level < 5:
        new_enemies = enemies[0]
    print(new_enemies)