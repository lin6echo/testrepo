# Modifying Global Scope

enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f'enemies inside function {enemies}')
    
# increase_enemies()
# print(f'enemies outside function {enemies}')

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f'enemies inside function {enemies}')
    
# increase_enemies()
# print(f'enemies outside function {enemies}')

def increase_enemies():
    print(f'enemies inside function {enemies}')
    return enemies + 2
    
enemies = increase_enemies()
print(f'enemies outside function {enemies}')















