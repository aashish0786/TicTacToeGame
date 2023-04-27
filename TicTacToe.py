import time
import os
blank=[" "," "," "," "," "," "," "," "," "," "]
board=[1,2,3,4,5,6,7,8,9]
def boardval():
    global chances,final,a,b
    chances=[1,2,3,4,5,6,7,8,9]
    a=f"{(' '*10)+('-'*31)}"
    b=f"{' '*10}|{' ':^9}|{' ':^9}|{' ':^9}|"
    line1=f"{' '*10}|{chances[0]:^9}|{chances[1]:^9}|{chances[2]:^9}|"
    line2=f"{' '*10}|{chances[3]:^9}|{chances[4]:^9}|{chances[5]:^9}|"
    line3=f"{' '*10}|{chances[6]:^9}|{chances[7]:^9}|{chances[8]:^9}|"
    final=f"""{a}\n{b}\n{line1}\n{b}
{a}\n{b}\n{line2}\n{b}
{a}\n{b}\n{line3}\n{b}     
{a}"""
    print(final)

def boardblank(blank):
    a=f"{(' '*10)+('-'*31)}"
    b=f"{' '*10}|{' ':^9}|{' ':^9}|{' ':^9}|"
    line1=f"{' '*10}|{blank[0]:^9}|{blank[1]:^9}|{blank[2]:^9}|"
    line2=f"{' '*10}|{blank[3]:^9}|{blank[4]:^9}|{blank[5]:^9}|"
    line3=f"{' '*10}|{blank[6]:^9}|{blank[7]:^9}|{blank[8]:^9}|"
    final=f"""{a}\n{b}\n{line1}\n{b}
{a}\n{b}\n{line2}\n{b}
{a}\n{b}\n{line3}\n{b}     
{a}"""
    print(final)

def datax():
    if player1>0:
        board[player1-1]="X"
        blank[player1-1]="X"
    chances.remove(player1)

def datay():
    if player2>0:
        board[player2-1]="0"
        blank[player2-1]="0"
    chances.remove(player2)

def play1():
    global player1,player2
    i=1
    while i<=9:
        player1=int(input(f"{user1} turn:"))
        datax()
        os.system('cls')
        boardblank(blank)
        if board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8] or board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[2]==board[5]==board[8] or board[0]==board[4]==board[8] or board[2]==board[4]==board[6]:
            print(f"\nCongratulation {user1} you have won the game the game will exit in 5 second \n")
            time.sleep(5)
            break
        elif len(chances)==0:
            print("The game is draw thank you for playing\n\nThe game will exit in 5 second ")
            time.sleep(5)
            break
        print("Left chance\n")
        for j in chances:
            print(j,end="")
        print("\n")
        player2=int(input(f"{user2} turn:"))
        datay()
        os.system('cls')
        boardblank(blank)
        if board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8] or board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[2]==board[5]==board[8] or board[0]==board[4]==board[8] or board[2]==board[4]==board[6]:
            print(f"\nCongratulation {user2} you have won the game\nthe game will exit in 5 second")
            time.sleep(5)
            break
        print("Left chance\n")
        for j in chances:
            print(j,end="")
        print("\n")
        i+=1

def game():
    print("Initial Status of board\n\nYour current board is:\n\n")
    boardblank(blank)
    print("\n\n")
    print("left chances: ",end="")
    for i in chances:
        print(i,end="")
    print("\n")
    play1()

def menu():
    print("Initial Status of board\n\nYour current board is:\n\n")
    boardblank(blank)
    global user1,user2
    user1=input("Enter player one name: ").strip()
    print("\n")
    user2=input("Enter player two name: ").strip()
    os.system('cls')
    print("\n")
    o=["0","X"]
    print(f"""Symbols----> X and 0
\nChoosing the symbol of each player
\n{user1} symbol is {o[0]}
\n{user2} symbol is {o[1]}\n""")
    input("press enter key to start the game")
    os.system('cls')
    game()

def dashboard():
    print(f"\n{'Here are the key position to select your move':>60}\n\n")
    boardval()
    print("\n\nPress enter key to continue")
    input()
    os.system('cls')
    menu()
dashboard()