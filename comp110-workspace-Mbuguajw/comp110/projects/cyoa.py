"""Project number two, the beginnings of a video game creator."""
__author__ = "730329579"

import random
from typing import Tuple
from typing import List
print("Welcome to the game,\n \"Street-Fighter, CompEdition\".")
print("Where you can play the legendary game in a simpler interface than a 500 lb gaming console.")
print("Come! \nEnter a world of strategy, rivarly, and honor!")
player1: str = input("What is your name warrior?: ")
cpu_fighter: str = "CPU"
player1_health: int = 200
player2_health: int = 200
player1_moves: Tuple[int, int, int, int] = (0, 0, 0, 0)
player2_moves: Tuple[int, int, int, int] = (0, 0, 0, 0)
ATTACK1: int = 10
ATTACK2: int = 25 
ATTACK3: int = 40
SWORDS: str = "\U00002694"
KNIFE: str = "\U0001F52A"
CHIRST: str = "\U0000271D" 
ARROW: str = "\U000027A1"	


def greet() -> None:
    """This produces the introduction statement to this version of street fighter."""
    """Here, player1 will give their name a choose their character based on their stats."""
    global player1
    global player1_moves
    global ARROW
    print(f"{ARROW} CHUN LI: \nPunch~ 10 \nKick~ 25 \nJump~ 25 \nSpecial Move~ 40")
    print(f"{ARROW} RYU: \nPunch~ 10 \nKick~ 10 \nJump~ 40 \nSpecial Move~ 40")
    print(f"{ARROW} E-HONDA: \nPunch~ 10 \nKick~ 10 \nJump~ 25 \nSpecial Move~ 40")
    fighter: str = input(f"Choose your fighter, {player1}: ")
    if fighter == "Chun Li":
        print(f"Now, {player1} you shall be formally recognized as: Chun Li")
        player1 = "Chun Li"
        chunlimoves: Tuple[int, int, int, int] = (ATTACK1, ATTACK2, ATTACK2, ATTACK3)
        player1_moves = chunlimoves
    elif fighter == "Ryu":
        print(f"Now, {player1} you shall be formally recognized as: Ryu")
        player1 = "Ryu"
        ryumoves: Tuple[int, int, int, int] = (ATTACK1, ATTACK1, ATTACK3, ATTACK3)
        player1_moves = ryumoves
    else:
        print(f"Now, {player1} you shall be formally recognized as: E-Honda")
        player1 = "E-Honda"
        ehondamoves: Tuple[int, int, int, int] = (ATTACK1, ATTACK1, ATTACK2, ATTACK3)
        player1_moves = ehondamoves


def opponent_setup() -> None:
    """This function chooses player1's opponent."""
    """This is done by random based on a random number retrival, with a number 
    assigned to each opponent available."""
    sagat: int = 0 
    vega: int = 1
    violent_ken: int = 2
    stats: str = ""
    cpu: int = random.randint(0, 2)
    global player2_moves
    global cpu_fighter
    global ARROW
    if cpu == sagat:
        cpu_fighter = "Sagat"
        sagatmoves: Tuple[int, int, int, int] = (ATTACK1, ATTACK1, ATTACK3, ATTACK3)
        player2_moves = sagatmoves
        stats = f"{ARROW}SAGAT: \nPunch~ 10 \nKick~ 10 \nJump~ 40 \nSpecial Move~ 40"
        print(f"Now, your opponent shall be:{stats}!!")
    elif cpu == vega:
        cpu_fighter = "Vega"
        vegamoves: Tuple[int, int, int, int] = (ATTACK1, ATTACK2, ATTACK2, ATTACK3)
        player2_moves = vegamoves
        stats = f"{ARROW}VEGA: \nPunch~ 10 \nKick~ 25 \nJump~ 25 \nSpecial Move~ 40"
        print(f"Now, your opponent shall be:{stats}!!")
    elif cpu == violent_ken:
        cpu_fighter = "Violent Ken"
        violentkenmoves: Tuple[int, int, int, int] = (ATTACK1, ATTACK1, ATTACK2, ATTACK3)
        player2_moves = violentkenmoves
        stats = f"{ARROW}VIOLENT KEN: \nPunch~ 10 \nKick~ 10 \nJump~ 25 \nSpecial Move~ 40"
        print(f"Now, your opponent shall be:{stats}!!")


def fight() -> bool:
    """This is the final show down between two characters.""" 
    """This function builds off of the information given of the two opponents 
    from the previous functions and faces them off to each other to duel 
    with random attacks to the player1's content."""
    global cpu_fighter
    global player1_moves
    global player1_health
    global player2_moves
    global player2_health
    global SWORDS
    global KNIFE
    c1a: str = "Not bad. However, can your handle THIS??"
    c1b: str = "square the FRICK up bruh, you don't want this smoke"
    c1c: str = f"on god? more like en {SWORDS} garde {KNIFE} if you keep using the name of the Lord in vain"
    c1d: str = "Prepare to meet your end, you GOON!!""Prepare to meet your end, you GOON!!"
    c2a: str = "ARRRGGHHHH! You think you're so sweet, huh? EAT THIS!"
    c2b: str = "Step out son, you don't want a n y of this cheese"
    c2c: str = "YOU and all your desendants shall rue the day you decided to square up with me"
    c2d: str = "Today, you meet your DOOM!!"
    player1reac: List[str] = [c1a, c1b, c1c, c1d]
    player2reac: List[str] = [c2a, c2b, c2c, c2d]
    start: str = input("Type anything and hit enter to start: ")
    if start == 1:
        print("3... \n2... \n1...\n...FIGHTT!!!")
    else:
        print("3... \n2... \n1...\n...FIGHTT!!!")
    player1_health = 200
    player2_health = 200
    while player1_health > 0 or player2_health > 0:
        i: int = random.randint(0, 3)
        player2_health = player2_health - player1_moves[i]
        print("P1 Health Bar: " + str(player1_health))
        print("P2 Health Bar: " + str(player2_health))
        print(f"{cpu_fighter}: {player2reac[i]}")
        p: int = random.randint(0, 3)
        player1_health = player1_health - player2_moves[p]
        print("P1 Health Bar: " + str(player1_health))
        print("P2 Health Bar: " + str(player2_health))
        print(f"{player1}: {player1reac[p]}")
    if player1_health <= 0 and player2_health > player1_health:
        print(f"{cpu_fighter}... WINS")
    elif player2_health <= 0 and player1_health > player2_health:
        print(f"{player1}... WINS")
    play: str = input("Care for a REMATCH??? Type 1 for yes, 2 for no. ")
    play_again: bool = False
    if int(play) == 1:
        play_again = True
    else:
        play_again = False
    return play_again
        

def main() -> None:
    """This function pulls all the other functions into one condensed piece of code."""
    greet()
    opponent_setup()
    while fight() == True:
        fight()
    print("GAME OVER")
    

if __name__ == "__main__":
    main()