"""
projekt_2A.py: druhý projekt do Engeto Online Python Akademie
BULLS & COWS
author: Tomáš Mokrý
email: tomas.mokry@gmail.com
discord: Tomas M#0922

"""
import time
from random import randint

def main():
    game_on = True
    game(game_on)
    

def game(game_on):
    
    welcome_text()
    number_comp = generate_number()
    rounds = 1
    start_time = time.time()
    
    while game_on:
        
        print(f'({number_comp})') 
        number_user = input('>>> ')
        warning = 'Wrong entry, try again.'
        
        if not number_user.isnumeric():
            print(warning)
            continue
        
        elif number_user.startswith('0'):
            print(warning)
            continue
        
        elif len(number_user) != 4:
            print(warning)
            continue
        
        elif find_duplicates(number_user) == False:
            print(warning)
            continue
        
        elif number_user == number_comp:
            game_on = False
        
        else: 
            show_game_result(find_bulls_cows(number_comp, number_user))
            rounds += 1
        
    else:
        evaluate_result(rounds)
        game_time = time.time() - start_time
        print(
            'Your game time:', 
            time.strftime("%H:%M:%S",time.gmtime(game_time))
            )
        name_pl = input('Please enter your name for statistics: ')
        s= f"Name: {name_pl}, gueses: {rounds}, time: {round(game_time,1)} s\n"
        with open("statistics.txt", mode='a') as stat_file:
            stat_file.write( s )
        print('Find your game staistics in file statistics.txt')
        
        
def find_bulls_cows(number_comp: str, number_user: str) -> list:
    """
    Description:
    Takes 2 numbers and checks same numbers positioned on same indexes
    and checks same numbers in each other.
    
    Example: 
    number_comp = '1234'
    number_user = '1432'

    Result:
    ---------
    [1,4]

    1 - one same number on same indexes
    4 - four same numbers in numbers
    ---------
    """
    bulls = 0
    cows = 0
    for i,j in enumerate(number_comp):
        if j == number_user[i]:
            bulls += 1
        if j in number_user:
            cows += 1
    return [bulls, cows]


def show_game_result(results: list) -> None:
    """
    Description:
    Takes result list [x,y]. 
    According to the number will asign name Bull,Cow for number == 1
    Bulls, Cows for number > 1 nad number 0
    Prints results 

    Example: 
    x = 3
    y = 1
    
    Result:
    ---------
    3 Bulls, 1 Cow
    ---------
    """ 
    separator = 48 * '-'
    name_1 = "Bulls"
    name_2 = "Cows"
    
    if results[0] == 1:
        name_1 = "Bull"
    if results[1] == 1:
        name_2 = "Cow"

    print(
        f'{results[0]} {name_1}, {results[1]} {name_2}', 
        separator, sep="\n"
        )


def welcome_text() -> None:
    """
    Description:
    Prints the welcome text

    """
    separator = 48 * '-'
    print(
        separator,
        "Hi there!",
        separator,
        "I've generated a random 4 digit number for you.",
        "Let's play a bulls and cows game.",
        separator, 
        "Enter a number: ",
        separator, sep = "\n"
        ) 


def generate_number() -> str:
    """
    Description:
    Generates 4 digit random number. Each digit is generated separately
    and added to the list. List is joined to string 4 digit number.
    
    Example: 
    number_generated = ["1", "5", "6", "9"]

    Result:
    ---------
    "1569"
    ---------
    """ 
    
    number_generated = []
    while len(number_generated) < 4:
    
        if (num := str(randint(1,9))) not in number_generated:
            number_generated.append(num)

    return ''.join(number_generated)
    
    
def evaluate_result(rounds: int) ->None:
    """
    Takes value of quesses and compare with limits.
    < 5; 5 < rounds < 10; rounds > 10
    Prints result

    Example: 
    rounds = 11

    Result:
    ---------
    evaluation = "That is not so good..." 
    ---------
    """ 
    separator = 48 * '-'
    
    if rounds < 5:
        evaluation = "That is amazing!"
    elif 5 < rounds < 10:
        evaluation = "That is average"
    else:
        evaluation = "That is not so good..." 
    
    print(
        f"Correct, you've guessed the right number \nin {rounds} guesses!",
    separator,evaluation,separator, sep = '\n'
    )

def find_duplicates(number_user:str) ->bool:
    """
    Takes one value, checking if there are duplicates in the value
    
    Example: 
    number_user = 1234
    number_user = 1222
    
    Result:
    ---------
    True
    False
    ---------
    """ 
    while int(number_user) > 0:
        rest = int(number_user) % 10
        number_user = int(number_user) // 10
        if str(rest) in str(number_user):
            return False
            break
    else:
        return True

if __name__ == "__main__":
    main()
