from random import choices
import sys
print("="*67)
print(""" 'WELCOME' to 
\t \t 'Rock'  
\t \t 'Paper' 
\t \t 'Sciscor' 
                                                       game by ***""")
print("="*67)
print("""Instructions:
              Enter: [ r ] for Rock
              Enter: [ p ] for Paper
              Enter: [ s ] for Sicor
              Enter: [ x ] to exit the game""")

print("-"*67)
#user moves to code
user= input("Enter your move: ").lower()
codes = {"r":-1,"p":0,"s":1}
if user not in ("r","p","s"):
    print("read the instructions clearly and then  play")
    sys.exit()
user_code=codes[user]
#computer codes for moves
computer_codes=list(codes.values())
cc1=choices(computer_codes)
cc=int(cc1[0])    
# reverse dictionary: code -> name, so we can print things nicely
names = {-1: "Rock", 0: "Paper", 1: "Scissors"}
# print what each side chose
print(f"You chose: {names[user_code]}")
print(f"Computer chose: {names[cc]}")



if (user=="x"):
    print("Thankyou,for playing our game!")  
    sys.exit()
if (user_code==cc):
        print("It's a Draw!")
elif (user_code==-1) and (cc==0):
        print("Computer win! ")
elif (user_code==0) and (cc==-1):
        print("you win! ")
elif (user_code==1) and (cc==0):
        print("you win! ")
elif (user_code==0) and (cc==1):
        print("computer win! ")
elif (user_code==-1) and (cc==1):
        print("you win! ")
elif (user_code==1) and (cc==-1):
        print("computer win! ")                                                                                                            