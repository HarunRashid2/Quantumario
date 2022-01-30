#GAME_STARTS!!!
game_starts = input("Do you want to play QuantuMario? Answer 'YES' or 'NO' ")
global win
if (game_starts == "YES") or (game_starts == "yes") or (game_starts == "Yes"):
    on_start()
    #Second Exposition = instructions (GET CODE!)
    length = 5
    global life
    life = 3
    level_1(length) #takes care of trivia as well
    level_2(length)
    level_3(length)
    if win == True:
        print("CONGRATULATIONS BLAH BLAH BLAH")
    
    else:
        print("Sad to see another great hero lose. . .Bowser lives on. . .")

else:
    print("Sorry to hear that!")
    pass
    
