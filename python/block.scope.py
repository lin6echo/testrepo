# Global scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    
    drink_potion()
print(player_health)

# There is no block scope

game_level = 3
enemies = ['skeleton', 'zombie', 'alien']
if game_level < 5:
    new_enemy = enemies[0]
    
print(new_enemy)

game_level = 3
def create_enemy():
    enemies = ['skeleton', 'zombie', 'alien']
    if game_level < 5:
        new_enemy = enemies[0]
    
print(new_enemy)

