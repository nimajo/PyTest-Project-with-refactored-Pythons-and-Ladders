import turtle
import os 
os.chdir(os.path.dirname(__file__)) #Changes Working Directory to the file's directory

# global score variables used for scoreboard
score_1 = 0
score_2 = 0
    


def main(): #defining the main which contains all subprograms
    import turtle
    
 




# Turtle Graphics Setup
    turtle.setup(width=0.400, height=0.666,startx=1110, starty=0) # Sets up turtle graphics top right of screen
    turtle.title (" Snakes & Ladders Game" ) # Turtle Graphics Title
    turtle.bgcolor("#FFCC99") # changes background color to hex code color #FFCC99
    

# Grid Creation     
    def grid():  #defines 'grid' which contains components and subcomponents which make up the 5x5 board
        gridt1 = turtle.Turtle() #imports new turtle called gridt1
        gridt1.speed(0)
        gridt1.ht() # hides turtle to help with aesthetics
        gridt1.penup()
        gridt1.goto(-350,-350) # goes to (-350, -350) which is roughly bottom left of screen, it will begin drawing from there
        gridt1.pendown()
        gridt1.pensize(5)

        def box(size): #defines 'box' which contains the instructions that the gridt1 turtle will use to move in the shape of a box/square, ('size' is the the size of the box)
            for i in range(4):
                gridt1.speed(0)
                gridt1.forward(size)
                gridt1.left(90)                

        def row(nos, size): #defines 'row' which contains the instructions that gridt1 will use to begin drawing the first row of boxes,  ('nos' means the number of squares)
            for i in range(nos):
                gridt1.speed(0)
                box(size)
                gridt1.forward(size)
            gridt1.penup()
            gridt1.left(180)
            gridt1.forward(nos * size)
            gridt1.left(180)
            gridt1.pendown()

        def AmountOfRows(aor, nos, size): #defines 'AmountOfRows' which contains the instructions that will begin drawing the entire grid
            for i in range(aor):   #This code begins the drawing of the grid
                gridt1.speed(0)
                row(nos,size)
                gridt1.penup()
                gridt1.left(90)
                gridt1.forward(size)
                gridt1.right(90)
                gridt1.pendown()
            gridt1.speed(0)    
            gridt1.penup()
            gridt1.right(90)
            gridt1.forward(aor * size)
            gridt1.left(90)
            gridt1.pendown()

        AmountOfRows(5,5, 125)   # sets the boundaries of the grid

    grid()    # calls upon the grid function, draws the grid


#   Number Labelling    

    def labelling(): #defines 'labelling' which contains functions for the numbered boxes
        numbers = turtle.Turtle()
        numbers.speed(0)
        numbers.ht()
        numbers.penup()
        numbers.goto(-340,-255)
        numbers.pendown()
        numbers.write("1", font=("Calibri", 17, "normal")) #labels box 1
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("2", font=("Calibri", 17, "normal")) #labels box 2
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("3", font=("Calibri", 17, "normal")) #labels box 3
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("4", font=("Calibri", 17, "normal")) #labels box 4
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("5", font=("Calibri", 17, "normal")) #labels box 5
        numbers.left(90)
        numbers.penup()
        numbers.forward(125)
        numbers.left(90)
        numbers.pendown()
        numbers.write("6", font=("Calibri", 17, "normal")) #labels box 6
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("7", font=("Calibri", 17, "normal")) #labels box 7
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("8", font=("Calibri", 17, "normal")) #labels box 8
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("9", font=("Calibri", 17, "normal")) #labels box 9
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("10", font=("Calibri", 17, "normal")) #labels box 10
        numbers.penup()
        numbers.right(90)
        numbers.forward(125)
        numbers.right(90)
        numbers.pendown()
        numbers.write("11", font=("Calibri", 17, "normal")) #labels box 11
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("12", font=("Calibri", 17, "normal")) #labels box 12
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("13", font=("Calibri", 17, "normal")) #labels box 13
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("14", font=("Calibri", 17, "normal")) #labels box 14
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("15", font=("Calibri", 17, "normal")) #labels box 15
        numbers.penup()
        numbers.left(90)
        numbers.forward(125)
        numbers.left(90)
        numbers.pendown()
        numbers.write("16", font=("Calibri", 17, "normal")) #labels box 16
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("17", font=("Calibri", 17, "normal")) #labels box 17
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("18", font=("Calibri", 17, "normal")) #labels box 18
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("19", font=("Calibri", 17, "normal")) #labels box 19
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("20", font=("Calibri", 17, "normal")) #labels box 20
        numbers.penup()
        numbers.right(90)
        numbers.forward(125)
        numbers.right(90)
        numbers.pendown()
        numbers.write("21", font=("Calibri", 17, "normal")) #labels box 21
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("22", font=("Calibri", 17, "normal")) #labels box 22
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("23", font=("Calibri", 17, "normal")) #labels box 23
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("24", font=("Calibri", 17, "normal")) #labels box 24
        numbers.penup()
        numbers.forward(125)
        numbers.pendown()
        numbers.write("25", font=("Calibri", 17, "normal")) #labels box 25
        numbers.penup()
    
    labelling()



  # Turtle Shapes ( Ladders & Snakes )
     

    def ladder1(): #function for an image of the ladder1
        import turtle
        ladder = turtle.Turtle()
        ladderscr = turtle.Screen()
        ladderscr.addshape("ladder.gif") 
        ladder.shape("ladder.gif")
        ladder.penup()
        ladder.goto(-47, 150) #covers boxes 18 & 23
    ladder1()    

    
        
    def ladder2(): #function for an image of the ladder2
        import turtle
        ladder2 = turtle.Turtle()
        ladderscr2 = turtle.Screen()
        ladderscr2.addshape("ladder2.gif")
        ladder2.shape("ladder2.gif")
        ladder2.penup()
        ladder2.goto(-170, -120) #covers boxes 9 & 12
    ladder2()    

           
        
    def ladder3(): #function for an image of the ladder3
        import turtle
        ladder3 = turtle.Turtle()
        ladderscr3 = turtle.Screen()
        ladderscr3.addshape("ladder3.gif")
        ladder3.shape("ladder3.gif")
        ladder3.penup()
        ladder3.goto(220, -190) # covers boxes 5 & 15
    ladder3()

    def snake1(): #function for an image of the snake1
        import turtle
        snake = turtle.Turtle()
        snakescr = turtle.Screen()
        snakescr.addshape("snake.gif")
        snake.shape("snake.gif")
        snake.penup()
        snake.goto(70, 90) # covers boxes 24 & 14
    snake1()    

    def snake2(): #function for an image of the snake2
        import turtle
        snake2 = turtle.Turtle()
        snakescr2 = turtle.Screen()
        snakescr2.addshape("snake2.gif")
        snake2.shape("snake2.gif")
        snake2.penup()
        snake2.goto(-50, -190) # covers boxes 8 & 3
    snake2()        

    def snake3(): #function for an image of the snake3
        import turtle
        snake3 = turtle.Turtle()
        snakescr3 = turtle.Screen()
        snakescr3.addshape("snake3.gif")
        snake3.shape("snake3.gif")
        snake3.penup()
        snake3.goto(-280, -90) # covers boxes 20 & 1
    snake3()
# Bull and cow Turtles
    def bull_and_cow():
        
        import turtle
        bull = turtle.Turtle()
        bullscr = turtle.Screen()
        bullscr.addshape("bull.gif")
        bull.shape("bull.gif")
        bull.penup()
        bull.goto(-300, -260) # starts from box 1

        import turtle
        cow = turtle.Turtle()
        cowscr = turtle.Screen()
        cowscr.addshape("cow.gif")
        cow.shape("cow.gif")
        cow.penup()
        cow.goto(-300, -300) # starts from box 1
   
#Rolling Mechanism    
                              
        def rolling():
            import random
            import turtle
            global score_1
            global score_2 
            player1 = turtle.textinput("Player 1", "Name of the player: ") # Takes Player1's Name with popout box
            
            player2 = turtle.textinput("Player 2", "Name of the player: ") # Takes Player1's Name with popout box


# Scoreboard system - Has to be after player name variables to avoid error

            
            import turtle
            scorebo = turtle.Turtle()
            scorebo.ht()
            scorebo.speed(0)            
            scorebo.penup()
            scorebo.goto(-50,329)
            scorebo.pendown()
            scorebo.write((player1,"Score is",score_1), font=("Courier", 14, "normal")) #Labels current score for player 1

        
            import turtle
            scorebo1 = turtle.Turtle()
            scorebo1.ht()
            scorebo1.speed(0)
            scorebo1.penup()
            scorebo1.goto(-50,280)
            scorebo1.pendown()
            scorebo1.write((player2,"Score is",score_2), font=("Courier", 14, "normal")) #Labels current score for player 2



            


            position1 = 1 # Starting Position is 1
            position2 = 1 # Starting Position is 1


            BooLoop  = True          # Boolean Variable
            while BooLoop == True:   # While Loop, constantly rolls until position >= 25 and user chooses not to restart using popout box
                

                input("Bull, Please press enter to roll")          #  Asks user to begin rolling
                r = random.randint(1,6)                      # Rolls dice, picks random number between 1 and 6
                print(player1 , " goes forward by", r )      # Confirmation of Rolled Number
                




                

###############################################################################  Dice Rolls
                if r == 1:                              # Conditional Statement for Rolling a 1
                    import turtle                       # Imports turtle when 1 is rolled, turtle is hidden then setup to goto top right position,
                    dice = turtle.Turtle()              # - after gone to position it will show itself,,, visual for dice roll 1 
                    dice.ht()
                    dice.speed(0)
                    dicescr = turtle.Screen()
                    dicescr.addshape("dice1.gif") 
                    dice.shape("dice1.gif")
                    dice.penup()
                    dice.goto(325, 240)
                    dice.st()
                    
                    oldposition1 = position1            # Stores Previous Position
                    position1 += 1                      # Current Position Stored

#################################                    
                    
                elif r == 2:                            # Conditional Statement for Rolling a 2
                    import turtle                       #Imports turtle when 2 is rolled, turtle is hidden then setup to goto top right position,
                    dice2 = turtle.Turtle()             # - after gone to position it will show itself,,, visual for dice roll 2 
                    dice2.ht()
                    dice2.speed(0)
                    dice2scr = turtle.Screen()
                    dice2scr.addshape("dice2.gif") 
                    dice2.shape("dice2.gif")
                    dice2.penup()
                    dice2.goto(325, 240)
                    dice2.st()
                    oldposition1 = position1            # Stores Previous Position
                    position1 += 2                      # Current Position Stored

#################################                    
                elif r == 3:                            # Conditional Statement for Rolling a 3 
                    import turtle                       # Imports turtle when 3 is rolled, turtle is hidden then setup to goto top right position,
                    dice3 = turtle.Turtle()             # - after gone to position it will show itself,,, visual for dice roll 3
                    dice3.ht()
                    dice3.speed(0)
                    dice13scr = turtle.Screen()
                    dice13scr.addshape("dice3.gif") 
                    dice3.shape("dice3.gif")
                    dice3.penup()
                    dice3.goto(325, 240)
                    dice3.st()

                    oldposition1 = position1            # Stores Previous Position
                    position1 += 3                      # Current Position Stored
#################################                    
                            
                elif r == 4:                            # Conditional Statement for Rolling a 4
                    import turtle                       # Imports turtle when 4 is rolled, turtle is hidden then setup to goto top right position,
                    dice4 = turtle.Turtle()             # - after gone to position it will show itself,,, visual for dice roll 4
                    dice4.ht()
                    dice4.speed(0)
                    dice4scr = turtle.Screen()
                    dice4scr.addshape("dice4.gif") 
                    dice4.shape("dice4.gif")
                    dice4.penup()
                    dice4.goto(325, 240)
                    dice4.st()

                    oldposition1 = position1            # Stores Previous Position
                    position1 += 4                      # Current Position Stored
                    
#################################
                elif r == 5:                            # Conditional Statement for Rolling a 5
                    import turtle                       # Imports turtle when 5 is rolled, turtle is hidden then setup to goto top right position,
                    dice5 = turtle.Turtle()             # - after gone to position it will show itself,,, visual for dice roll 5
                    dice5.ht()
                    dice5.speed(0)
                    dice5scr = turtle.Screen()
                    dice5scr.addshape("dice5.gif") 
                    dice5.shape("dice5.gif")
                    dice5.penup()
                    dice5.goto(325, 240)
                    dice5.st()

                    oldposition1 = position1            # Stores Previous Position
                    position1 += 5                      # Current Position Stored
#################################                        
                    
                elif r == 6:                            # Conditional Statement for Rolling a 6
                    import turtle                       # Imports turtle when 6 is rolled, turtle is hidden then setup to goto top right position,
                    dice6 = turtle.Turtle()             # - after gone to position it will show itself,,, visual for dice roll 6
                    dice6.ht()
                    dice6.speed(0)
                    dice6scr = turtle.Screen()
                    dice6scr.addshape("dice6.gif") 
                    dice6.shape("dice6.gif")
                    dice6.penup()
                    dice6.goto(325, 240)
                    dice6.st()

                    oldposition1 = position1            # Stores Previous Position
                    position1 += 6                      # Current Position Stored
                    

###############################################################################
###############################################################################  BULL MECHANISM                    
###############################################################################
                bull.speed(4)   
                if position1 == 1:

                    bull.goto(-300,-260)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 2:
                    
                    bull.goto(-175,-260)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 3:

                    bull.goto(-50,-260)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 4:
                    
                    bull.goto(75,-260)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 5:
                    if position1 ==5:
                        bull.speed(4)
                        bull.goto(200,-260)                    
                        bull.goto(200,-10)                            #Snake, Takes bull to square 14
                        print(" ################################ ")   #Confirmation Print
                        print("#### Ladder Taken From 5 to 15###")
                        print(" ################################ ")
                        position1 = 15                              # Increases Position to correct value
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 6: # Conditional For if variable 'position1' 
                    
                    bull.goto(200,-260)
                    bull.goto(200,-135)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 7 and oldposition1 >= 6:
                    bull.goto(75,-135)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 7 and oldposition1 < 6: # Conditional For if variable 'position1' 
                    
                    bull.goto(200,-260)
                    bull.goto(200,-135)
                    bull.goto(75,-135)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 8 and oldposition1 >= 6: # Conditional For if variable 'position1'
                    if position1 == 8:
                        bull.speed(4)      
                        bull.goto(-50,-135)

                        bull.goto(-50,-260)                           #Snake, Takes bull to square 3
                        bull.right(180)                               #Makes Bull face correct way
                        print(" ################################ ")   #Confirmation Print
                        print("#### Snake Taken From 8 to 3###")
                        print(" ################################ ")
                        position1 = 3
                        
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 8 and oldposition1 < 6: # Conditional For if variable 'position1'
                    if position1 == 8:
                        
                        bull.speed(4)
                        bull.goto(200,-260)
                        bull.goto(200,-135)
                        bull.goto(-50,-135)

                        bull.goto(-50,-260)                           #Snake, Takes bull to square 3
                        bull.right(180)                               #Makes Bull face correct way
                        print(" ################################ ")   #Confirmation Print
                        print("#### Snake Taken From 8 to 3###")
                        print(" ################################ ")
                        position1 = 3
                        
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 9 and oldposition1 >= 6: # Conditional For if variable 'position1' 
                    if position1 == 9:
                    
                        bull.speed(4)   
                        print(" ################################ ")   #Confirmation Print
                        print("#### Ladder Taken From 9 to 12###")
                        print(" ################################ ")                    
                                   
                            
                        
                        bull.goto(-175,-135)
                        bull.goto(-175,-10)#ladder, goes to square 14
                        bull.right(180)#Makes Bull face correct way
                        position1 = 12
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 9 and oldposition1 < 6: # Conditional For if variable 'position1' 
                    if position1 ==9:
                        bull.speed(4)
                        print(" ################################ ")   #Confirmation Print
                        print("#### Ladder Taken From 9 to 12###")
                        print(" ################################ ")
                        bull.goto(200,-260)
                        bull.goto(200,-135)
                        bull.goto(-175,-135)
                        bull.goto(-175,-10)
                        bull.right(180)
                        position1 = 12

                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position1 == 10 and oldposition1 >= 6: # Conditional For if variable 'position1' 
                    
                    
                    bull.goto(-300,-135)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 10 and oldposition1 < 6: # Conditional For if variable 'position1' 
                    bull.goto(200,-260)
                    bull.goto(200,-135)
                    bull.goto(-300,-135)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 11 and oldposition1 >= 6: # Conditional For if variable 'position1' 
                    bull.goto(-300,-135)
                    bull.goto(-300,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 11 and oldposition1 < 6 : # Conditional For if variable 'position1' 
                    bull.goto(200,-260) #test w/o dead code
                    bull.goto(-300,-135)
                    bull.goto(200,-135)
                    bull.goto(-300,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 11 and oldposition1 >= 7: # Conditional For if variable 'position1' 

                    bull.goto(-300,-135)
                    bull.goto(-300,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                    
                elif position1 == 12 and oldposition1 >= 11: # Conditional For if variable 'position1' 
                    
                    bull.goto(-175,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 12 and oldposition1 < 11: # Conditional For if variable 'position1' 
                    bull.goto(-300,-135)
                    bull.goto(-300,-10)                    
                    bull.goto(-175,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 13 and oldposition1 >= 11: # Conditional For if variable 'position1' 

                    bull.goto(-50,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 13 and oldposition1 < 11: # Conditional For if variable 'position1' 
                    bull.goto(-300,-135)
                    bull.goto(-300,-10)                    
                    bull.goto(-50,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")    
                    
                elif position1 == 14 and oldposition1 >= 11: # Conditional For if variable 'position1' 
                    
                    bull.goto(75,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 14 and oldposition1 < 11: # Conditional For if variable 'position1' 
                    bull.goto(-300,-135)
                    bull.goto(-300,-10)                    
                    bull.goto(75,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 15 and oldposition1 >= 11: # Conditional For if variable 'position1' 
                    
                    bull.goto(200,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 15 and oldposition1 < 11: # Conditional For if variable 'position1' 
                    bull.goto(-300,-135)
                    bull.goto(-300,-10)                    
                    bull.goto(200,-10)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 16 and oldposition1 <= 11: # Conditional For if variable 'position1' 
                    bull.goto(-300,-10)                    
                    bull.goto(200,-10)
                    bull.goto(200,115)                    
                    bull.goto(200,115)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 16 and oldposition1 >= 15: # Conditional For if variable 'position1' 
                    
                    bull.goto(200,115)
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 16 and oldposition1 < 15: # Conditional For if variable 'position1' 
                    
                    bull.goto(200,-10)
                    bull.goto(200,115)
                elif position1 == 17 and oldposition1 >= 16: # Conditional For if variable 'position1' 
                    
                    bull.goto(75,115)
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 17 and oldposition1 < 16: # Conditional For if variable 'position1' 
                    bull.goto(200,-10)
                    bull.goto(200,115)                    
                    bull.goto(75,115)
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 18 and oldposition1 >= 16: # Conditional For if variable 'position1' 
                    
                    bull.speed(4)
                    bull.goto(-50,115)
                    bull.goto(-50,240)                            #Snake, Takes bull to square 23
                    bull.left(180)                                #Makes Bull face correct way
                    print(" ################################ ")   #Confirmation Print
                    print("#### Ladder Taken From 18 to 23###")
                    print(" ################################ ")                    
                    
                    position1 = 23
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 18 and oldposition1 < 16: # Conditional For if variable 'position1' 
                    bull.speed(4)
                    bull.goto(200,-10)
                    bull.goto(200,115)                    
                    bull.goto(-50,115)
                    bull.goto(-50,240)                            #Snake, Takes bull to square 23
                    bull.left(180)
                    print(" ################################ ")   #Confirmation Print
                    print("#### Ladder Taken From 18 to 23###")
                    print(" ################################ ")                    
                    
                    position1 = 23                    
                    #Makes Bull face correct way                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                                
                elif position1 == 19 and oldposition1 >= 16: # Conditional For if variable 'position1' 
                    
                    bull.goto(-175,115)
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 19 and oldposition1 < 16: # Conditional For if variable 'position1' 
                    bull.goto(200,-10)
                    bull.goto(200,115)                    
                    bull.goto(-175,115)
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 20 and oldposition1 >= 16: # Conditional For if variable 'position1' 
                    bull.speed(4)
                    bull.goto(-300,115)

                    bull.goto(-300,-260)                          #Snake, Takes bull to square 1
                    bull.right(180)                               #Makes Bull face correct way
                    print(" ################################ ")   #Confirmation Print
                    print("#### Snake Taken From 20 to 1###")
                    print(" ################################ ")                    
                    position1 = 1
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 20 and oldposition1 < 16: # Conditional For if variable 'position1' 
                    bull.speed(4)
                    bull.goto(200,-10)
                    bull.goto(200,115)                    
                    bull.goto(-300,115)


                    bull.goto(-300,-260)                          #Snake, Takes bull to square 1
                    bull.right(180)                               #Makes Bull face correct way
                    print(" ################################ ")   #Confirmation Print
                    print("#### Snake Taken From 20 to 1###")
                    print(" ################################ ")                    
                    position1 = 1
                    

                    
                    print(player1,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )

                    
                elif position1 == 21 and oldposition1 >= 16 : # Conditional For if variable 'position1' 
                    bull.goto(-300,115)
                    bull.goto(-300,240)
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 21 and oldposition1 < 16 : # Conditional For if variable 'position1' 
                    bull.goto(200,115)
                    bull.goto(-300,115)
                    bull.goto(-300,240)
                   
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position1 == 22 and oldposition1 >= 21 : # Conditional For if variable 'position1' 
                    bull.goto(-175,240)
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")
                elif position1 == 22 and oldposition1 < 21 : # Conditional For if variable 'position1' 
                    bull.goto(-300,115)
                    bull.goto(-300,240)
                    bull.goto(-175,240)
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 23 and oldposition1 >= 21: # Conditional For if variable 'position1' 
                    
                    bull.goto(-50,240)
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 23 and oldposition1 < 21: # Conditional For if variable 'position1' 
                    bull.goto(-300,115)
                    bull.goto(-300,240)                    
                    bull.goto(-50,240)
                    print("-------------------------------------------------------------------------------------------")
                    print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                    print("-------------------------------------------------------------------------------------------")                    
                elif position1 == 24 and oldposition1 >= 21: # Conditional For if variable 'position1'
                    if position1 == 24:
                        bull.goto(75,240)
                        bull.speed(4)
                        bull.goto(75,-10)

                        print(" ################################ ")   #Confirmation Print
                        print("#### Snake Taken From 24 to 14###")
                        print(" ################################ ")
                        position1 = 14
                        

                    
                        print("-------------------------------------------------------------------------------------------")
                        print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                        print("-------------------------------------------------------------------------------------------")

                elif position1 == 24 and oldposition1 < 21: # Conditional For if variable 'position1'
                    if position1 == 24:
                        
                        bull.goto(-300,115)
                        bull.goto(-300,240) 
                        bull.goto(75,240)
                        bull.speed(4)
                        bull.goto(75,-10)
                        
                        print(" ################################ ")   #Confirmation Print
                        print("#### Snake Taken From 24 to 14###")
                        print(" ################################ ")
                        position1 = 14
                        
           
                        print("-------------------------------------------------------------------------------------------")
                        print(player1 ,"'s Current Position is :", position1 , " , Your Old Position was :", oldposition1 )
                        print("-------------------------------------------------------------------------------------------")

                    
                elif position1 >= 25 and oldposition1 >= 21: # Conditional For if variable 'position1' 
                    bull.goto(200,240)
                    print("######################################")
                    print("###  WINNER WINNER CHICKEN DINNER  ###")    #Winner Confirmation
                    print("######################################")
                    print(player1, " Wins!!! ")

                    import turtle
                    winner2 = turtle.Turtle()
                    winner2scr = turtle.Screen()
                    winner2scr.addshape("win.gif") 
                    winner2.shape("win.gif")
                    winner2.penup()
                    winner2.goto(-0, 0) #covers centre with win screen
                    
                elif position1 >= 25 and oldposition1 < 21:
                    bull.goto(-300,115)
                    bull.goto(-300,240)
                    bull.goto(200,240)
                    print("######################################")
                    print("###  WINNER WINNER CHICKEN DINNER  ###")    #Winner Confirmation
                    print("######################################")
                    print(player1, " Wins!!! ")

                    import turtle
                    winner2 = turtle.Turtle()
                    winner2scr = turtle.Screen()
                    winner2scr.addshape("win.gif") 
                    winner2.shape("win.gif")
                    winner2.penup()
                    winner2.goto(-0, 0) #covers centre with win screen
                    

#Score System
                score_a = 0 #declares score_a
                


                if position1 >= 25:
                    score_a += 1 # adds one onto score_a
#Reset System
                if score_a >=1:
                    
                    
                    restart = turtle.textinput("Game result", "Well done " + player1 + ", you won ! \nDo you want to restart ? (y/n)") # Asks user if they want to carry on playing or quit, uses a popup screen
                    if restart== "y":
                        print("##########################################")
                        print("###  Please Wait for up to 15 Seconds! ###")  #Reset Takes Roughly 8 Seconds, User is told to wait 
                        print("##########################################")
                        score_1 += 1
                        print(player1, "Has a Current score of", score_1) # score counter
                        turtle.reset() # Resets all turtles to their original locations
                        turtle.ht()
                        winner2.ht()   #hides win.gif after reset
                        scorebo.reset()#resets/updates scoreboard
                        scorebo1.reset()#resets/updates scoreboard
                        scorebo1.ht()
                        scorebo.ht()                         
                        turtle.ht()    # Hides turtle at(0,0) which resets
                        main()         #reset
                        

                        


                        
                    else:
                        turtle.bye() # Closes turtle graphics
                        break



                                            
                                 
###############################################################################
###############################################################################     COW MECHANISM BELOW
###############################################################################





                input("Cow, Please press enter to roll")  # Asks User to begin rolling
                r = random.randint(1,6)                   # Picks random number between 1 and 6
                print(player2 , " goes forward by", r )   # Prints confirmation of steps taken
                


#################################                
                if r == 1:                              # Conditional Statement for Rolling a 1
                    import turtle                       # Imports turtle when 3 is rolled, turtle is hidden then setup to goto top right position,
                    dice = turtle.Turtle()              # - after gone to position it will show itself,,, visual for dice roll 3 
                    dice.ht()
                    dice.speed(0)
                    dicescr = turtle.Screen()
                    dicescr.addshape("dice1.gif") 
                    dice.shape("dice1.gif")
                    dice.penup()
                    dice.goto(325, 240)
                    dice.st()
                    
                    oldposition2 = position2            # Stores Previous Position
                    position2 += 1                      # Current Position Stored
#################################                    
                    
                elif r == 2:                            # Conditional Statement for Rolling a 2
                    import turtle                       #Imports turtle when 3 is rolled, turtle is hidden then setup to goto top right position,
                    dice2 = turtle.Turtle()             # - after gone to position it will show itself,,, visual for dice roll 3 
                    dice2.ht()
                    dice2.speed(0)
                    dice2scr = turtle.Screen()
                    dice2scr.addshape("dice2.gif") 
                    dice2.shape("dice2.gif")
                    dice2.penup()
                    dice2.goto(325, 240)
                    dice2.st()
                    oldposition2 = position2            # Stores Previous Position
                    position2 += 2                      # Stores Previous Position
#################################                    
                elif r == 3:                            # Conditional Statement for Rolling a 3
                    import turtle                       # Imports turtle when 3 is rolled, turtle is hidden then setup to goto top right position,
                    dice3 = turtle.Turtle()             # - after gone to position it will show itself,,, visual for dice roll 3
                    dice3.ht()
                    dice3.speed(0)
                    dice13scr = turtle.Screen()
                    dice13scr.addshape("dice3.gif") 
                    dice3.shape("dice3.gif")
                    dice3.penup()
                    dice3.goto(325, 240)
                    dice3.st()

                    oldposition2 = position2            # Stores Previous Position
                    position2 += 3                      #Current Position Stored
#################################                    
                            
                elif r == 4:                            # Conditional Statement for Rolling a 4
                    import turtle                       # Imports turtle when 4 is rolled, turtle is hidden then setup to goto top right position,
                    dice4 = turtle.Turtle()             # - after gone to position it will show itself,,, visual for dice roll 4
                    dice4.ht()
                    dice4.speed(0)
                    dice4scr = turtle.Screen()
                    dice4scr.addshape("dice4.gif") 
                    dice4.shape("dice4.gif")
                    dice4.penup()
                    dice4.goto(325, 240)
                    dice4.st()

                    oldposition2 = position2            # Stores Previous Position
                    position2 += 4                      #Current Position Stored
                    
#################################
                elif r == 5:                            # Conditional Statement for Rolling a 5
                    import turtle                       # Imports turtle when 5 is rolled, turtle is hidden then setup to goto top right position,
                    dice5 = turtle.Turtle()             # - after gone to position it will show itself,,, visual for dice roll 5
                    dice5.ht()
                    dice5.speed(0)
                    dice5scr = turtle.Screen()
                    dice5scr.addshape("dice5.gif") 
                    dice5.shape("dice5.gif")
                    dice5.penup()
                    dice5.goto(325, 240)
                    dice5.st()

                    oldposition2 = position2            # Stores Previous Position
                    position2 += 5                      #Current Position Stored
#################################                        
                    
                elif r == 6:                            # Conditional Statement for Rolling a 6
                    import turtle                       # Imports turtle when 6 is rolled, turtle is hidden then setup to goto top right position,
                    dice6 = turtle.Turtle()             # - after gone to position it will show itself,,, visual for dice roll 6
                    dice6.ht()
                    dice6.speed(0)
                    dice6scr = turtle.Screen()
                    dice6scr.addshape("dice6.gif") 
                    dice6.shape("dice6.gif")
                    dice6.penup()
                    dice6.goto(325, 240)
                    dice6.st()

                    oldposition2 = position2            # Stores Previous Position
                    position2 += 6                      #Current Position Stored
                    

###############################################################################
###############################################################################                      
###############################################################################
                cow.speed(4)    
                if position2 == 1: # Conditional For if variable 'position1'

                    cow.goto(-300,-300)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 2: # Conditional For if variable 'position2'
                    
                    cow.goto(-175,-300)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 3: # Conditional For if variable 'position2'

                    cow.goto(-50,-300)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 4: # Conditional For if variable 'position2'
                    
                    cow.goto(75,-300)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 5: # Conditional For if variable 'position2'
                    if position2 ==5:
                        cow.goto(200,-260)                    
                        cow.goto(200,-10)                            #Snake, Takes bull to square 14
                        print(" ################################ ")   #Confirmation Print
                        print("#### Ladder Taken From 5 to 15###")
                        print(" ################################ ")
                        position2 = 15
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 6: # Conditional For if variable 'position2'
                    
                    cow.goto(200,-300)  #extra coordinates prevent crossing diagonally
                    cow.goto(200,-175)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 7 and oldposition2 >= 6: # Conditional For if variable 'position2'
                    cow.goto(75,-175)
                    
                elif position2 == 7 and oldposition2 < 6: # Conditional For if variable 'position2'
                    
                    cow.goto(200,-300)
                    cow.goto(200,-175)   #extra coordinates prevent crossing diagonally
                    cow.goto(75,-175)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 8 and oldposition2 >= 6: # Conditional For if variable 'position2'
                    if position2 ==8:
                            
                        cow.goto(-50,-175)  #extra coordinates prevent crossing diagonally

                        cow.goto(-50,-300)                             #Snake, Takes bull to square 3
                        cow.right(180)                               #Makes Bull face correct way
                        print(" ################################ ")   #Confirmation Print
                        print("#### Snake Taken From 8 to 3###")
                        print(" ################################ ")
                        position2 = 3
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 8 and oldposition2 < 6: # Conditional For if variable 'position2'
                    if position2 ==8:
                        
                        cow.goto(200,-300)
                        cow.goto(200,-175)  #extra coordinates prevent crossing diagonally
                        cow.goto(-50,-175)

                        cow.goto(-50,-300)                           #Snake, Takes bull to square 3
                        cow.right(180)                               #Makes Bull face correct way
                        print(" ################################ ")   #Confirmation Print
                        print("#### Snake Taken From 8 to 3###")
                        print(" ################################ ")
                        position2 = 3
                        
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 9 and oldposition2 >= 6: # Conditional For if variable 'position2'
                    if position2 == 9:
                    
                           
                        print(" ################################ ")   #Confirmation Print
                        print("#### Ladder Taken From 9 to 12###")
                        print(" ################################ ")                    
                                   
                            
                        
                        cow.goto(-175,-175)
                        cow.goto(-175,-50)#ladder, goes to square 14
                        cow.right(180)#Makes Bull face correct way
                        position2 = 12
                    
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 9 and oldposition2 < 6: # Conditional For if variable 'position2'
                    if position2 ==9:
                        
                        print(" ################################ ")   #Confirmation Print
                        print("#### Ladder Taken From 9 to 12###")
                        print(" ################################ ")
                        cow.goto(200,-300)
                        cow.goto(200,-175)
                        cow.goto(-175,-175)
                        cow.goto(-175,-50)   #extra coordinates prevent crossing diagonally
                        cow.right(180)
                        position2 = 12

                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                    
                elif position2 == 10 and oldposition2 >= 6: # Conditional For if variable 'position2'
                    
                    
                    cow.goto(-300,-175)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 10 and oldposition2 < 6: # Conditional For if variable 'position2'
                    cow.goto(200,-300)
                    cow.goto(200,-175) #extra coordinates prevent crossing diagonally
                    cow.goto(-300,-175)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 11 and oldposition2 >= 6: # Conditional For if variable 'position2'
                    cow.goto(-300,-175) #extra coordinates prevent crossing diagonally
                    cow.goto(-300,-50)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 11 and oldposition2 < 6 : # Conditional For if variable 'position2'
                    cow.goto(200,-3000) 
                    cow.goto(-300,-175)
                    cow.goto(200,-175) #extra coordinates prevent crossing diagonally
                    cow.goto(-300,-50)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 11 and oldposition2 >= 7: # Conditional For if variable 'position2'

                    cow.goto(-300,-175)
                    cow.goto(-300,-50) #extra coordinates prevent crossing diagonally
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                    
                elif position2 == 12 and oldposition2 >= 11: # Conditional For if variable 'position2'
                    
                    cow.goto(-175,-50)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 12 and oldposition2 < 11: # Conditional For if variable 'position2'
                    cow.goto(-300,-175)
                    cow.goto(-300,-50)       #extra coordinates prevent crossing diagonally              
                    cow.goto(-175,-50)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 13 and oldposition2 >= 11: # Conditional For if variable 'position2'

                    cow.goto(-50,-50)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 13 and oldposition2 < 11: # Conditional For if variable 'position2'
                    cow.goto(-300,-175)
                    cow.goto(-300,-50)      #extra coordinates prevent crossing diagonally              
                    cow.goto(-50,-50)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
    
                    
                elif position2 == 14 and oldposition2 >= 11: # Conditional For if variable 'position2'
                    
                    cow.goto(75,-50)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")


                elif position2 == 14 and oldposition2 < 11: # Conditional For if variable 'position2'
                    cow.goto(-300,-175)
                    cow.goto(-300,-50)        #extra coordinates prevent crossing diagonally            
                    cow.goto(75,-50)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 15 and oldposition2 >= 11: # Conditional For if variable 'position2'
                    
                    cow.goto(200,-50)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")


                elif position2 == 15 and oldposition2 < 11: # Conditional For if variable 'position2'
                    cow.goto(-300,-175)
                    cow.goto(-300,-50)         #extra coordinates prevent crossing diagonally           
                    cow.goto(200,-50)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 16 and oldposition2 <= 11: # Conditional For if variable 'position2'
                    cow.goto(-300,-50)                    
                    cow.goto(200,-50)      #extra coordinates prevent crossing diagonally
                    cow.goto(200,75)                    
                    cow.goto(200,75)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 16 and oldposition2 >= 15: # Conditional For if variable 'position2'
                    
                    cow.goto(200,75)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 16 and oldposition2 < 15: # Conditional For if variable 'position2'
                    
                    cow.goto(200,-50)    #extra coordinates prevent crossing diagonally
                    cow.goto(200,75)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 17 and oldposition2 >= 16: # Conditional For if variable 'position2'
                    
                    cow.goto(75,75)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 17 and oldposition2 < 16: # Conditional For if variable 'position2'
                    cow.goto(200,-50)
                    cow.goto(200,75)           #extra coordinates prevent crossing diagonally          
                    cow.goto(75,75)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 18 and oldposition2 >= 16: # Conditional For if variable 'position2'
                    
                   
                    cow.goto(-50,75)    #extra coordinates prevent crossing diagonally
                    cow.goto(-50,200)                            #Snake, Takes bull to square 23
                    cow.left(180)                                #Makes Bull face correct way
                    print(" ################################ ")   #Confirmation Print
                    print("#### Ladder Taken From 18 to 23###")
                    print(" ################################ ")                    
                    
                    position2 = 23
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 18 and oldposition2 < 16: # Conditional For if variable 'position2'
                    
                    cow.goto(200,-50) #extra coordinates prevent crossing diagonally
                    cow.goto(200,75)                    
                    cow.goto(-50,75)
                    cow.goto(-50,200)                            #Snake, Takes bull to square 23
                    cow.left(180)
                    print(" ################################ ")   #Confirmation Print
                    print("#### Ladder Taken From 18 to 23###")
                    print(" ################################ ")                    
                    
                    position2 = 23                    
                    #Makes Bull face correct way
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                                
                elif position2 == 19 and oldposition2 >= 16: # Conditional For if variable 'position2'
                    
                    cow.goto(-175,75)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 19 and oldposition2 < 16: # Conditional For if variable 'position2'
                    cow.goto(200,-50)
                    cow.goto(200,75)      #extra coordinates prevent crossing diagonally              
                    cow.goto(-175,75)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 20 and oldposition2 >= 16: # Conditional For if variable 'position2'
                    
                    cow.goto(-300,75)

                    cow.goto(-300,-300)                          #Snake, Takes bull to square 1
                    cow.right(180)                               #Makes Bull face correct way
                    print(" ################################ ")   #Confirmation Print
                    print("#### Snake Taken From 20 to 1###")
                    print(" ################################ ")                    
                    position2 = 1
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                elif position2 == 20 and oldposition2 < 16: # Conditional For if variable 'position2'
                    cow.goto(200,-50)
                    cow.goto(200,75)         #extra coordinates prevent crossing diagonally           
                    cow.goto(-300,75)


                    cow.goto(-300,-300)                          #Snake, Takes bull to square 1
                    cow.right(180)                               #Makes Bull face correct way
                    print(" ################################ ")   #Confirmation Print
                    print("#### Snake Taken From 20 to 1###")
                    print(" ################################ ")                    
                    position2 = 1
                    

                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 21 and oldposition2 >= 16 : # Conditional For if variable 'position2'
                    cow.goto(-300,75)
                    cow.goto(-300,200)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 21 and oldposition2 < 16 : # Conditional For if variable 'position2'
                    cow.goto(200,75)
                    cow.goto(-300,75)  #extra coordinates prevent crossing diagonally
                    cow.goto(-300,200)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 22 and oldposition2 >= 21 : # Conditional For if variable 'position2'
                    cow.goto(-175,200)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")

                elif position2 == 22 and oldposition2 < 21 : # Conditional For if variable 'position2'
                    cow.goto(-300,75)
                    cow.goto(-300,200) #extra coordinates prevent crossing diagonally
                    cow.goto(-175,200)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 23 and oldposition2 >= 21: # Conditional For if variable 'position2'
                    
                    cow.goto(-50,200)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 23 and oldposition2 < 21: # Conditional For if variable 'position2'
                    cow.goto(-300,75)
                    cow.goto(-300,200)        #extra coordinates prevent crossing diagonally            
                    cow.goto(-50,200)
                    print("-------------------------------------------------------------------------------------------")
                    print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                    print("-------------------------------------------------------------------------------------------")
                    
                elif position2 == 24 and oldposition2 >= 21: # Conditional For if variable 'position2'
                    if position2 == 24:
                        cow.goto(75,200)
                        cow.speed(4)
                        cow.goto(75,-50)
                        cow.speed(4)

                        print(" ################################ ")   #Confirmation Print
                        print("#### Snake Taken From 24 to 14###")
                        print(" ################################ ")                    
                        position2 = 14
                        
                    
                        print("-------------------------------------------------------------------------------------------")
                        print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                        print("-------------------------------------------------------------------------------------------")

                elif position2 == 24 and oldposition2 < 21: # Conditional For if variable 'position2'
                    if position2 == 24:               
                            
                        cow.goto(-300,75)
                        cow.goto(-300,200)  #extra coordinates prevent crossing diagonally
                        cow.goto(75,200)
                        cow.speed(4)
                        cow.goto(75,-50)
                        cow.speed(4)
                        

                        print(" ################################ ")   #Confirmation Print
                        print("#### Snake Taken From 20 to 1###")
                        print(" ################################ ")                    
                        position2 = 14










                        
                        print("-------------------------------------------------------------------------------------------")
                        print(player2 ,"'s Current Position is :", position2 , " , Your Old Position was :", oldposition2 )
                        print("-------------------------------------------------------------------------------------------")

                    
                elif position2 >= 25 and oldposition2 >= 21: # Conditional For if variable 'position2'
                    cow.goto(200,200)
                    print("######################################")
                    print("###  WINNER WINNER CHICKEN DINNER  ###")  #Winner Confirm
                    print("######################################")
                    print(player2, " Wins!!! ")

                    import turtle
                    winner2 = turtle.Turtle()
                    winner2scr = turtle.Screen()
                    winner2scr.addshape("win.gif") 
                    winner2.shape("win.gif")
                    winner2.penup()
                    winner2.goto(-0, 0) #covers centre with win screen
                    
                elif position2 >= 25 and oldposition2 < 21: # Conditional For if variable 'position2'
                    cow.goto(-300,75)
                    cow.goto(-300,200)
                    cow.goto(200,200)
                    print("######################################")
                    print("###  WINNER WINNER CHICKEN DINNER  ###")  #Winner Confirm
                    print("######################################")
                    print(player2, " Wins!!! ")

                        
                    import turtle                 # Turtle for win.gif
                    winner2 = turtle.Turtle()
                    winner2scr = turtle.Screen()
                    winner2scr.addshape("win.gif") 
                    winner2.shape("win.gif")
                    winner2.penup()
                    winner2.goto(-0, 0) #covers centre with win screen
                    
# score system b
                score_b = 0 #score_b variable declared
                          
                if position2 >= 25:

                   score_b += 1           #score variable added 1
                   
# reset system b
                if score_b >=1:

                       
                    restart = turtle.textinput("Game result", "Well done " + player2 + ", you won ! \nDo you want to restart ? (y/n)") # Asks user if they want to carry on playing or quit, uses a popup screen
                    if restart == "y":
                        
                        print("##########################################")
                        print("###  Please Wait for up to 15 Seconds! ###")  #Reset Takes Roughly 8 Seconds, User is told to wait 
                        print("##########################################")
                        score_2 += 1
                        print(player2, "Has a Current score of", score_2)    #Score Counter
                        turtle.reset()#resets turtles to original positions
                        turtle.ht()
                        winner2.ht() #hides win.gif after reset
                        scorebo.reset()#resets/updates scoreboard
                        scorebo1.reset()#resets/updates scoreboard
                        scorebo.ht() # hides scoreboard 
                        scorebo1.ht()  # hides second scoreboard                      
                        main()       #reset

                        
                    else:
                        turtle.bye()# Closes turtle graphics
                        break


                    
#### Called Functions       
        rolling()   #Calls Rolling Function which contains most game mechanism
    bull_and_cow()  # Calls the function which contains two playable characters
    
           
main() # Main called
       



        
        
            
   
