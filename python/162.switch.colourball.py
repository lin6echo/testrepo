import random

green = 5
red = 5
blue = 5
yellow = 5
i = 0
balls=[]

numbers = random.sample(range(1, 21), 20)

def print_output():
    print(balls)
    print(numbers) 

for num in numbers:
    i += 1    
    match num:
        case num if 1 <= num <= 5:
            balls.append('green')
            green -= 1
            if green == 0:
                print("Found all green balls after {} picks".format(i))
                print_output()
                quit()
           
        case num if 6 <= num <= 10:
            balls.append('red')
            red -= 1
            if red == 0:
                print("Found all red balls after {} picks".format(i))
                print_output()
                quit()
            
        case num if 11 <= num <= 15:
            balls.append('blue')
            blue -= 1
            if blue == 0:
                print("Found all blue balls after {} picks".format(i))
                print_output()
                quit()
     
        case num if 15 <= num <= 20:
            balls.append('yellow')
            yellow -= 1
            if yellow == 0:
                print("Found all yellow balls after {} picks".format(i))
                print_output()
                quit()
            
        case _:
            print('bad number')
            quit()
       

