from random import randint 
game_contents = ["Rock","Paper","Scissor"]
opponent = game_contents[randint(0,2)]
me = False

while me == False:
    me = input("Rock,Paper,Scissor?")
    if me == opponent:
        print("Tie!")
    elif me == "Rock":
        if opponent == "Paper":
            print("You lose!" , opponent ,"covers ", me)
        else:
            print("You win!", me ,"Smashed", opponent)
    elif me == "Scissor":
        if opponent == "Rock":
            print("You lose!", opponent ,"Smashed",me)
        else:
            print("You win!", me ,"Cutts",opponent)
    elif me =="Paper":
        if opponent == "Scissor":
            print("You lose!",opponent ,"Cutts", me)
        else:
            print("You win!", me ,"covers",opponent)     
    else:
        print("Check Spelling!")
        
    me = False
    opponent = game_contents[randint(0,2)]

    
