# CS 177 - project3.py
# Salman Chughtai
# Jacob R Gifford
#
# This program is a video game designed to allow a user to guess a secret word
#  within a given number of tries. The program uses multiple interactive
#  graphics window with a control panel to control the game, and game windows
#  to play the game. The game involves multiple rounds and allows the user to
#  start a new game or quit at any time. Additionally, the game displays a list
#  of high scores, ability to save score, and a hint button. In addition to the
#  base game, there were 3 custom features described below.
#
# Custom Feature 1: Full Word Guess
#  This feature allows a user to guess the secret word rather than guess
#  individual letters. If the player guesses correctly, they get 5 extra points.
#  However, an incorrect guess results in an automatic loss. The guess
#  button is available while the game is played in the guess window. Once
#  pressed, it opens a new graphics window allowing users to enter a guess.
#  Afterwards, the window is closed and the game is updated accordingly
#
# Custom Feature 2: Add Words to the Game
#  This feature allows a user to add words to the game. This is done through
#  a button in the control panel that can be pressed before the game is started
#  only. The button opens a new graphics window that comes with instructions.
#  After an entry is made, the program checks that it is a string, it is
#  within 4-6 letters, and is not already in the list. If those requirements
#  are met, the word is added. Or else, an error message is displayed.

import random
import string
from time import sleep

# Import libraries
from graphics import *


# The ctrPan() function creates the control panel for the game. It accepts no
#  input arguments and has three output arguments. The window created, and two
#  rectangles
def ctrlPan():
    # Create a window for the Control Panel
    win = GraphWin("Welcome to: ", 300, 250)
    win.setBackground("gray")

    # Create a Rectangle for the Title and draw formatted text inside
    title_box = Rectangle(Point(0, 0), Point(300, 30))
    title_box.draw(win)
    title_box.setFill("black")
    title_center = title_box.getCenter()
    title_text = "GUESS MASTER 2.0"
    title_msg = Text(title_center, title_text)
    title_msg.draw(win)
    title_msg.setStyle("bold")
    title_msg.setTextColor("gold")

    # Create a box for the game description and draw formatted text inside
    descript_box = Rectangle(Point(20, 95), Point(280, 170))
    descript_box.draw(win)
    descript_box.setFill("white")
    descript_center = descript_box.getCenter()
    descript_txt = "This is a game where your score is \
    \n based on your number of 4-6 letter words \n you can guess within 10 tries."
    descript_msg = Text(descript_center, descript_txt)
    descript_msg.draw(win)
    descript_msg.setSize(10)
    descript_msg.setFace("helvetica")

    # Create a box and associated text for the New button
    New_box = Rectangle(Point(15, 45), Point(70, 75))
    New_box.draw(win)
    New_box.setFill("gold")
    New_center = New_box.getCenter()
    New_txt = "NEW"
    New_msg = Text(New_center, New_txt)
    New_msg.draw(win)
    New_msg.setStyle("bold")
    New_msg.setTextColor("black")

    # Hint box and text
    hintBox = Rectangle(Point(157.5, 45), Point(212.5, 75))
    hintBox.setFill('white')
    hintBox.draw(win)
    hintTxt = Text(Point(185, 60), 'HINT')
    hintTxt.setStyle('bold')
    hintTxt.setTextColor('red')
    hintTxt.draw(win)

    # Create a box and associated text for the Quit Button
    Quit_box = Rectangle(Point(230, 45), Point(285, 75))
    Quit_box.draw(win)
    Quit_box.setFill("black")
    Quit_center = Quit_box.getCenter()
    Quit_txt = "QUIT"
    Quit_msg = Text(Quit_center, Quit_txt)
    Quit_msg.draw(win)
    Quit_msg.setStyle("bold")
    Quit_msg.setTextColor("gold")

    # meteormode toggle button
    meteorBox = Rectangle(Point(87.5, 45), Point(142.5, 75))
    meteorBox.setFill('purple')
    meteorBox.draw(win)
    meteorTxt = Text(Point(116, 60), 'METEOR')
    meteorTxt.setStyle('bold')
    meteorTxt.setTextColor('cyan')
    meteorTxt.draw(win)
    meteorTxt.setSize(10)

    # Create text for game instructions
    Instruct_txt = "Click NEW to start a game..."
    Instruct_msg = Text(Point(150, 225), Instruct_txt)
    Instruct_msg.draw(win)
    Instruct_msg.setSize(12)

    # Create high scores button and associated text
    highscores = Rectangle(Point(55, 175), Point(145, 205))
    highscores.draw(win)
    highscores.setFill('red')
    highsctxt = Text(Point(100, 190), 'HIGH SCORES')
    highsctxt.setStyle('bold')
    highsctxt.setSize(9)
    highsctxt.setTextColor('white')
    highsctxt.draw(win)

    AddBox = Rectangle(Point(165, 175), Point(255, 205))
    AddBox.draw(win)
    AddBox.setFill('blue')
    Addtxt = Text(Point(210, 190), 'ADD WORDS')
    Addtxt.setStyle('bold')
    Addtxt.setSize(9)
    Addtxt.setTextColor('white')
    Addtxt.draw(win)

    return (New_box, Quit_box, hintBox, win, highscores, meteorBox, AddBox)


# The ChooseWord() function chooses a secret word. It accepts no input arguments
#  and returns a secret word
def ChooseWord():
    # Open the words.txt file, read it, assign its contents to a list, and close
    filename = open("words.txt", "r")
    allwords = filename.read()
    filename.close()
    allwords = allwords.splitlines()

    # Use the random library to select a random word from the list
    secword = random.choice(allwords)
    return secword


# The GamePan() function creates the Game Panel. It accepts no input arguments
#  and returns the graphics created as a list.
def GamePan(meteorRain):
    # Create the window for the Game Panel
    win = GraphWin("Save the Block P", 500, 500)
    if meteorRain == 0:
        win.setBackground("gold")
    if meteorRain == 1:
        win.setBackground("cyan")

    ## Create Circles for each letter of the alphabet
    # Intialize loop variables
    circle_rad = 500 / 26 - 0.5
    circle_X = [0]
    circle_Y = [0] * 26
    circle_center = [0] * 26
    circle = [Circle(Point(0, 0), 0)] * 36
    # Create a for loop iterating over the number of letters in the alphabet
    for i in range(26):
        # Define coordinates for the first circle
        if i == 0:
            circle_Y[i] = 435
            circle_X[i] = circle_rad + 7.5
        # Define coordinates of circles in the first row
        elif i <= 12:
            circle_Y[i] = 435
            circle_X.append(circle_X[-1] + 2 * circle_rad)
        # Define coordinates of the first circle in the second row
        elif i == 13:
            circle_Y[i] = 477
            circle_X.append(circle_X[0])
        # Define coordinates of the circles in the second row
        elif i > 13:
            circle_Y[i] = 477
            circle_X.append(circle_X[-1] + 2 * circle_rad)
        # Create circles using the defined coordinates, and radii, and draw
        circle_center[i] = Point(circle_X[i], circle_Y[i])
        circle[i] = Circle(circle_center[i], circle_rad)
        circle[i].draw(win)
        if meteorRain == 0:
            circle[i].setFill("black")
        if meteorRain == 1:
            circle[i].setFill("purple")

    ## Create Text objects for each letter of the alphabet in each circle
    # Get the list of letters using the string library
    letters = string.ascii_uppercase
    # Initialize loop variables
    circle_letters = [0] * 26
    # Create a for loop iterating over the number of letters in the alphabet
    for i in range(26):
        # Create text objects for each letter and draw them in the circles
        circle_letters[i] = Text(circle_center[i], letters[i])
        circle_letters[i].draw(win)
        circle_letters[i].setTextColor("white")

    ## Create block P (white)
    # Create a list containting all polygons and define their coordinates
    BlockP_back = [0] * 10
    BlockP_back[0] = Polygon(Point(200, 110), Point(250, 110), Point(240, 170), Point(190, 170))
    BlockP_back[1] = Polygon(Point(190, 170), Point(240, 170), Point(230, 230), Point(180, 230))
    BlockP_back[2] = Polygon(Point(180, 230), Point(230, 230), Point(220, 290), Point(170, 290))
    BlockP_back[3] = Polygon(Point(170, 290), Point(220, 290), Point(210, 350), Point(160, 350))
    BlockP_back[4] = Polygon(Point(150, 350), Point(220, 350), Point(215, 380), Point(145, 380))
    BlockP_back[5] = Polygon(Point(250, 110), Point(300, 110), Point(290, 170), Point(240, 170))
    BlockP_back[6] = Polygon(Point(300, 110), Point(350, 110), Point(340, 170), Point(290, 170))
    BlockP_back[7] = Polygon(Point(290, 170), Point(340, 170), Point(330, 230), Point(280, 230))
    BlockP_back[8] = Polygon(Point(280, 230), Point(330, 230), Point(320, 290), Point(270, 290))
    BlockP_back[9] = Polygon(Point(270, 290), Point(220, 290), Point(230, 230), Point(280, 230))
    # Draw all polygons in the list using a for loop
    if meteorRain == 0:
        for i in range(len(BlockP_back)):
            BlockP_back[i].draw(win)
            BlockP_back[i].setFill("white")
    if meteorRain == 1:
        for i in range(len(BlockP_back)):
            BlockP_back[i].draw(win)
            BlockP_back[i].setFill("white")
    ## Create Block P (black)
    BlockP_front = [0] * 10
    # Use a for loop iterating over length of back block P, and clone the
    #  polygons
    if meteorRain == 0:
        for i in range(len(BlockP_front)):
            BlockP_front[i] = BlockP_back[i].clone()
            BlockP_front[i].draw(win)
            BlockP_front[i].setFill("black")
    if meteorRain == 1:
        for i in range(len(BlockP_front)):
            BlockP_front[i] = BlockP_back[i].clone()
            BlockP_front[i].draw(win)
            BlockP_front[i].setFill("black")

    ## Choose a secret word by calling the ChooseWord() function
    secword = ChooseWord()

    ## Create a box for each letter in the secret word
    # Initialize loop variables
    secword_box = [0] * len(secword)
    # Determine secret word length and create starting rectangle accordingly
    if len(secword) == 4:
        secword_box[0] = Rectangle(Point(150, 50), Point(200, 100))
    elif len(secword) == 5:
        secword_box[0] = Rectangle(Point(125, 50), Point(175, 100))
    elif len(secword) == 6:
        secword_box[0] = Rectangle(Point(100, 50), Point(150, 100))
    # Use a for loop iterating over length of the secret word to create
    #  remaining polygons
    for i in range(1, len(secword_box)):
        # Clone previous rectangle and move the width of the rectangle over
        secword_box[i] = secword_box[i - 1].clone()
        secword_box[i].move(50, 0)
    # Draw all rectangles
    for i in range(len(secword_box)):
        secword_box[i].draw(win)

    ## Create Undrawn text for secret word in the boxes
    secword_text = [0] * len(secword)
    for i in range(len(secword)):
        secword_text[i] = Text(secword_box[i].getCenter(), secword[i])

    Guessbox = Rectangle(Point(435, 10), Point(490, 40))
    Guessbox.setFill('dark gray')
    Guessbox.draw(win)

    Guess = Text(Point(462.5, 25), 'GUESS')
    Guess.setStyle('bold')
    Guess.setTextColor('white')
    Guess.draw(win)
    Guess.setSize(10)

    ## Put all variables to be returned in a list
    graphics = [win, circle, circle_letters, BlockP_front, secword, secword_box, secword_text, Guessbox]
    return (graphics)


# The drop() function moves a given polygon downwards. It accepts a polygon as
#  an input argument and retuns no outputs.
def drop(polygon):
    # Change the color of the polygon to Red
    polygon.setFill("red")

    step = 50
    # Initialize loop variables
    anchor = polygon.getPoints()
    anchory = anchor[0].getY()
    ypt = 600 - anchory
    dy = ypt / step

    # Create a for loop and move the polygon by the specified distance each
    #  iteration
    for i in range(step):
        polygon.move(0, dy)
    polygon.undraw()


# The insideRect() function determines whether a point is inside a rectangle.
#  It acceps a point and a rectangle as input arguments, and returns either True
#  or false, depending on whether the point is or isn't in the box.
def insideRect(Point, Rectangle):
    # Get the Left and Right Points of the rectangle
    RectangleP1 = Rectangle.getP1()
    RectangleP2 = Rectangle.getP2()

    # Set the minimum and maximum x values by getting the x values of the
    #  left and right points
    minx = RectangleP1.getX()
    maxx = RectangleP2.getX()

    # Set the minimum and maximum y values by getting the y values of the
    #  left and right points
    miny = RectangleP1.getY()
    maxy = RectangleP2.getY()

    # Determine if the x values and y values of the point are within the
    #  minimum and maximum allowable values. If they are, return True. Else,
    #  return False.
    if (Point.getX() <= maxx) and (Point.getX() >= minx):
        if (Point.getY() <= maxy) and (Point.getY() >= miny):
            return True
        else:
            return False
    else:
        return False


# The insideCirc() function determines whether a point is inside a circle.
#  It acceps a point and a circle as input arguments, and returns either True
#  or false, depending on whether the point is or isn't in the circle.
def insideCirc(Point, Circle):
    # Get the center and radius of the circle
    center = Circle.getCenter()
    radius = Circle.getRadius()

    # Get the x and y values of the center
    centerx = center.getX()
    centery = center.getY()

    # Get the x and y values of the point
    pointx = Point.getX()
    pointy = Point.getY()

    # Calculate the distance of the point away from the circle's center
    distance = ((pointx - centerx) ** 2 + (pointy - centery) ** 2) ** 0.5

    # If the distance is less than the circle's radius, return True. Else,
    #  return false.
    if distance <= radius:
        return True
    else:
        return False


# The CheckGuess() function determines whether a given guess is inside the
#  the secret word. If it is, it draws the text that is in the secret word box.
#  If not, it calls the drop function. It also edits the placeholder
#  list with the value of the guessed character. It returns the updated
#  placeholder and the score.
def CheckGuess(guess, secword, secword_text, score, BlockP, GameWin, placehold, usedLetters):
    # convert the secret word to a list
    secword = list(secword)

    ## Determine if the guessed character is in the secret word

    # If it is, determine where the secret word is and draw the text
    #  at those locations. Also update the placeholder string with the
    #  guess at the correct location
    usedLetters.append(guess)
    if guess in secword:

        for i in range(len(secword)):
            if secword[i] == guess:
                secword_text[i].draw(GameWin)
                placehold[i] = guess
    # If not, decrease the score by one, call the drop function on one element
    #  of the P, and remove that element from the list.
    else:
        score -= 1
        drop(BlockP[-1])
        del BlockP[-1]

    return score, placehold, usedLetters


# The scoreDraw() function draws the score message at the top of the
#  Game Window. It accepts the window and the score as an input and returns
#  the text object.
def scoreDraw(score, GameWin):
    scoremessage = "Score: " + str(score)
    scoreText = Text(Point(250, 25), scoremessage)
    scoreText.draw(GameWin)
    scoreText.setSize(18)
    return scoreText


# The startGame() function sets up all the conditions for starting a new game.
#  This includes calling the GamePan() function and initializing other variables
#  that are necessary to start a new game. It returns those variables
def startGame(meteorRain):
    # Call the GamePan() function and store its outputs. Then assign each of
    #  the elements in that list to individual variables
    Game_graphics = GamePan(meteorRain)
    GameWin = Game_graphics[0]
    GameCircles = Game_graphics[1]
    CirclesText = Game_graphics[2]
    BlockP = Game_graphics[3]
    secword = Game_graphics[4]
    secword_box = Game_graphics[5]
    secword_text = Game_graphics[6]
    GuessRect = Game_graphics[7]

    ## Initialize other variables for the loop
    # Set score
    score = 10
    # Initalize placeholder string
    placehold = [0] * len(secword)
    # State that no circle in the game panel has been clicked
    isClicked = [False] * len(GameCircles)
    # Call the scoreDraw() function to draw the score
    scoreText = scoreDraw(score, GameWin)
    # Indicates game is in progress
    Result = 'Playing'
    return score, GameWin, GameCircles, CirclesText, BlockP, \
           secword, secword_box, secword_text, \
           placehold, isClicked, scoreText, Result, GuessRect, meteorRain


# The play() function runs the game once the new button has been pressed.
#  The function terminates when the quit button has been pressed or the current
#  round has ended in a win or loss. It accepts necessary input arguments and
#  returns the Result of the round, the score, and the current Game Window.

def play(score, GameWin, GameCircles, CirclesText, BlockP,
         secword, secword_box, secword_text,
         placehold, isClicked, scoreText, Result, CtrlWin, New, Quit, Hint, High, GuessRect, meteorRain):
    # Initalize a while loop that terminates when the round is no longer in
    #  progress
    usedLetters = []

    # if meteorRain is on, start generating meteors
    if meteorRain == 1:
        i = 0
        r = random.randint(5, 50)
        c = Point(random.randint(200, 300), 0)
        meteor = Circle(c, r)
        meteor.setFill('red')
        meteor.draw(GameWin)
        dy = 1
        dx = random.randrange(-1, 1)

    while Result == 'Playing':
        mouse_pos = CtrlWin.checkMouse()
        game_mouse = GameWin.checkMouse()

        # only passes if meteor rain is on, otherwies game plays normally
        if meteorRain == 1:
            i += 1

            # used increments of i to regulate timing of meteor spawns
            if i > 2250:
                i = 0
                r = random.randint(5, 50)
                c = Point(random.randint(30, 470), 0)
                dx = random.randrange(-4, 4)
                meteor = Circle(c, r)
                meteor.setFill('red')
                meteor.draw(GameWin)

            if game_mouse != None:
                xVal = game_mouse.getX()
                yVal = game_mouse.getY()
                # Determine the radius of the inputted circle
                rad = meteor.getRadius()
                # Determine the center of the inputted circle
                center = meteor.getCenter()
                # Determine the x and y coordinates of the circle
                centerX = center.getX()
                centerY = center.getY()
                # Determine the distance between the center of the circle and the point
                disx = (centerX - xVal) ** 2
                disy = (centerY - yVal) ** 2
                distance = (disx + disy) ** .5

                if distance < rad:  # if a meteor is deflected then add 2 pts and despawn meteor
                    meteor.undraw()
                    score += 2
                    scoremessage = "Score: " + str(score)  # updates score
                    scoreText.setText(scoremessage)  # after hint used
                    break

                elif distance > rad:  # if player fails to click meteor of sufficient size, knock of blockp
                    if i == 550:
                        meteor.undraw()
                        if meteor.getRadius() >= 20:
                            if len(BlockP) > 0:
                                score = score - 1
                                scoremessage = "Score: " + str(score)  # updates score
                                scoreText.setText(scoremessage)  # after hint used
                                drop(BlockP[-1])
                                del BlockP[-1]
                                break
                            else:
                                Result = 'Lose'

            else:  # if player fails to click at all and meteor lands of sufficient size, knock off pblock
                if i == 550:
                    meteor.undraw()
                    if meteor.getRadius() >= 20:
                        if len(BlockP) > 0:
                            score = score - 1
                            scoremessage = "Score: " + str(score)  # updates score
                            scoreText.setText(scoremessage)  # after hint used
                            drop(BlockP[-1])
                            del BlockP[-1]
                            break
                        else:
                            Result = 'Lose'

            meteor.move(dx + (i / 999999999999),
                        dy + (i / 999999999999))  # moves meteor by dx and dy which are random values

        ## Define outcomes if click is in Ctrl Window
        if mouse_pos:

            ## Determine if click is in either the New box or Quit box
            ##  by calling the insideRect() function.
            NewClick = insideRect(mouse_pos, New)
            QuitClick = insideRect(mouse_pos, Quit)
            HintClick = insideRect(mouse_pos, Hint)
            HighClick = insideRect(mouse_pos, High)
            # If it is in the New box, close the current game window and
            #  start a new game by calling the startGame() function.

            if NewClick:
                GameWin.close()
                meteorRain = 0
                score, GameWin, GameCircles, CirclesText, BlockP, \
                secword, secword_box, secword_text, \
                placehold, isClicked, scoreText, Result, GuessRect, meteorRain = startGame(meteorRain)

            # if hint is clicked, drop 2 polygons, uncolor 3 incorrect circles
            #   handle exceptions by losing if list values are exceeded.
            if HintClick:
                for i in range(2):
                    if len(BlockP) > 0:
                        score -= 1
                        scoremessage = "Score: " + str(score)  # updates score
                        scoreText.setText(scoremessage)  # after hint used
                        drop(BlockP[-1])
                        del BlockP[-1]
                    else:
                        Result = 'Lose'

                hintlett, usedLetters = hint(secword, usedLetters)
                for i in range(3):
                    isClicked[hintlett[i]] = True
                    GameCircles[hintlett[i]].setFill("gold")
                    CirclesText[hintlett[i]].setTextColor("black")

            # If it is in the Quit box, close both the ctrl window and the
            #  game window. Return a result that the round has been quit
            if QuitClick:
                CtrlWin.close()
                GameWin.close()
                Result = 'Quit'
                return Result, score, GameWin, meteorRain
            if HighClick:
                highscore()

        ## Define outcomes for clicks in the game window
        if game_mouse:

            GameClick = insideRect(game_mouse, GuessRect)
            if GameClick:
                score, placehold = GuessWord(secword, score, BlockP, \
                                             secword_text, GameWin, placehold, scoreText)

            # Initalize variable for a click in one of the letter circles that
            #  resets each time a new click is registered
            Circle_click = [False] * len(GameCircles)

            # Create a for loop iterating over the number of circles
            for i in range(len(GameCircles)):

                # Determine if the mouse click is inside a circle by
                # calling the insideCirc() function
                Circle_click[i] = insideCirc(game_mouse, GameCircles[i])

                # If it is and the circle hasn't already been clicked,
                #  Indicate that the circle has been clicked, change the
                #  text color and circle color. Also, assign the text in
                #  the clicked circle to the variable guess and call the
                #  check Guess function. Update the score message with the
                #  new score

                if Circle_click[i] and isClicked[i] == False:
                    isClicked[i] = True
                    GameCircles[i].setFill("gold")
                    CirclesText[i].setTextColor("black")
                    guess = CirclesText[i].getText()
                    score, placehold, usedLetters = CheckGuess(guess, secword, secword_text, score, BlockP, GameWin,
                                                               placehold, usedLetters)
                    scoremessage = "Score: " + str(score)
                    scoreText.setText(scoremessage)

        # If each element of the placehold list is equal to the secret word
        #  indiate that the player has won the round/
        if placehold == list(secword):
            Result = 'Win'
        # If all the polygons in the P have been removed, indicate that the
        #  round has been lost.
        elif len(BlockP) <= 0:
            Result = 'Lose'

    return Result, score, GameWin, meteorRain


# The GuessWord() function is called when a game is in progress and the Guess
#  button is pressed. The function opens a separate window where the user can
#  type in a geuss for the secret word. If the user is correct, they get five
#  extra points. If not, they lose the game. They can also choose to cancel in
#  the case that they change their mind and no longer wish to guess
def GuessWord(secword, score, BlockP, secword_text, GameWin, placehold, scoreText):
    # Initialize graphics window and entry box
    win = GraphWin('Guess', 150, 100)
    entry = Entry(Point(50, 25), 10)
    entry.draw(win)

    # Initialize check button and associated text
    Check = Rectangle(Point(100, 14), Point(140, 35))
    Check.setFill('blue')
    Check.draw(win)
    Checktxt = Text(Point(120, 24.5), 'CHECK')
    Checktxt.setSize(8)
    Checktxt.setStyle('bold')
    Checktxt.setTextColor('white')
    Checktxt.draw(win)

    # Initialize cancel button and associated text
    Cancelbox = Rectangle(Point(50, 60), Point(100, 85))
    Cancelbox.draw(win)
    Cancelbox.setFill('red')
    Canceltext = Text(Point(75, 72.5), 'CANCEL')
    Canceltext.setStyle('bold')
    Canceltext.setTextColor('white')
    Canceltext.setSize(8)
    Canceltext.draw(win)

    # Initialize variables for loop
    CancelClick = False
    CheckClick = False

    # Set up while loop running until either the cancel or check button is
    #  clicked
    while (CancelClick == False) and (CheckClick == False):

        # Check for a mouseclick
        mousepos = win.checkMouse()
        if mousepos:
            CancelClick = insideRect(mousepos, Cancelbox)
            CheckClick = insideRect(mousepos, Check)

            # If check button is clicked, determine if guess is the same as the
            #  secret word
            if CheckClick:
                WordGuess = entry.getText()
                WordGuess = WordGuess.upper()

                # If it is, draw the secret word, update placeholder, increase
                #  score, and return updated score and placeholder
                if WordGuess == secword:
                    for i in range(len(secword_text)):
                        secword_text[i].undraw()
                        secword_text[i].draw(GameWin)
                    score += 5
                    scoremessage = "Score: " + str(score)
                    scoreText.setText(scoremessage)
                    placehold = list(secword)
                    win.close()
                    return score, placehold
                # If not, drop all remaining polygons in blockP, adjust score,
                #  and return score and placeholder
                else:
                    while len(BlockP) >= 1:
                        score = score - 1
                        scoremessage = "Score: " + str(score)
                        scoreText.setText(scoremessage)
                        drop(BlockP[-1])
                        del BlockP[-1]
                    win.close()
                    return score, placehold
            # If cancel button is clicked, close window and return to game
            elif CancelClick:
                win.close()
                return score, placehold


# The Win() function updates the game for a win condition. It displays, the
#  win messages, waits for a click, and starts a new game with the ending score.
def Win(GameWin, score, CtrlWin, New, Quit, roundNum, High, meteorRain, Meteor):
    # Create the first win message and associated text object.
    WinMessage1 = "YOU WIN - BOILER UP!"
    WinText1 = Text(Point(250, 250), WinMessage1)
    WinText1.setTextColor("gray")
    WinText1.setStyle("bold")
    WinText1.setSize(20)
    WinText1.draw(GameWin)

    # Create the second win message and associated text object.
    WinMessage2 = "Click to continue"
    WinText2 = Text(Point(250, 280), WinMessage2)
    WinText2.setStyle("italic")
    WinText2.setTextColor("gray")
    WinText2.setSize(10)
    WinText2.draw(GameWin)

    # Initalize loop variables
    gameMouse = None
    QuitClick = False
    NewClick = False
    HighClick = False

    # Create a while loop for the condition that no click has been made in
    #  the game window and the new or quit buttons have not been clicked
    while (QuitClick == False) and (NewClick == False) and (gameMouse == None):
        # Check for a mouse click
        mouse_pos = CtrlWin.checkMouse()
        gameMouse = GameWin.checkMouse()
        # If mouse click is in the control window
        if mouse_pos:

            # Determine if mouse click is in either New or Quit box
            NewClick = insideRect(mouse_pos, New)
            QuitClick = insideRect(mouse_pos, Quit)
            HighClick = insideRect(mouse_pos, High)
            MeteorClick = insideRect(mouse_pos, Meteor)
            # If in new box, start game. If in quit box, close and terminate
            #  program.

            if NewClick:
                GameWin.close()
                meteorRain = 0
                score, GameWin, GameCircles, CirclesText, BlockP, \
                secword, secword_box, secword_text, \
                placehold, isClicked, scoreText, Result, GuessRect, meteorRain = startGame(meteorRain)

                return score, GameWin, GameCircles, CirclesText, BlockP, \
                       secword, secword_box, secword_text, \
                       placehold, isClicked, scoreText, Result, roundNum, GuessRect, meteorRain

            if MeteorClick:
                GameWin.close()
                meteorRain = 1
                score, GameWin, GameCircles, CirclesText, BlockP, \
                secword, secword_box, secword_text, \
                placehold, isClicked, scoreText, Result, GuessRect, meteorRain = startGame(meteorRain)

                return score, GameWin, GameCircles, CirclesText, BlockP, \
                       secword, secword_box, secword_text, \
                       placehold, isClicked, scoreText, Result, roundNum, GuessRect, meteorRain

            if QuitClick:
                CtrlWin.close()
                GameWin.close()
                score = 0
                GameWin = 0
                GameCircles = 0
                CirclesText = 0
                BlockP = 0
                secword = 0
                secword_box = 0
                secword_text = 0
                placehold = 0
                isClicked = 0
                scoreText = 0
                GuessRect = 0
                Result = 'Quit'

                return score, GameWin, GameCircles, CirclesText, BlockP, \
                       secword, secword_box, secword_text, \
                       placehold, isClicked, scoreText, Result, roundNum, GuessRect, meteorRain

            elif HighClick:
                highscore()

        elif gameMouse:
            GameWin.close()
            # Restart the game by setting the same inital conditions as the
            # startGame() function, but increase the score by 10 rather than
            # set it equal to 0.
            Game_graphics = GamePan(meteorRain)
            GameWin = Game_graphics[0]
            roundNum += 1
            score += 10
            GameCircles = Game_graphics[1]
            CirclesText = Game_graphics[2]
            BlockP = Game_graphics[3]
            secword = Game_graphics[4]
            secword_box = Game_graphics[5]
            secword_text = Game_graphics[6]
            GuessRect = Game_graphics[7]
            placehold = [0] * len(secword)
            isClicked = [False] * len(GameCircles)
            scoreText = scoreDraw(score, GameWin)
            Result = 'Playing'

            return score, GameWin, GameCircles, CirclesText, BlockP, \
                   secword, secword_box, secword_text, \
                   placehold, isClicked, scoreText, Result, roundNum, GuessRect, meteorRain


# The Lose() function displays the messages that appear when the round ends in
#  a loss. It also prompts the user to enter a name to save the score. Once
#  the user saves the game, the game window closes.

def Lose(CtrlWin, New, Quit, High, GameWin, score, roundNum, Meteor, meteorRain):
    # Initialise loop variables
    NewClick = False
    QuitClick = False
    HighClick = False
    MeteorClick = False

    # if you lose you are told you lost
    loseT = Text(Point(250, 150), 'SORRY - BETTER LUCK NEXT TIME')
    loseT.setTextColor('grey')
    loseT.setSize(16)
    loseT.draw(GameWin)

    # entry objects and text
    entryt = Text(Point(250, 200), 'ENTER PLAYER NAME:')
    entryt.setSize(15)
    entryt.setStyle('bold')
    entryt.setTextColor('blue')
    entryt.draw(GameWin)
    entryb = Entry(Point(250, 250), 15)
    entryb.draw(GameWin)

    # save button objects + text
    saveB = Rectangle(Point(220, 280), Point(280, 310))
    saveB.setFill('green')
    saveB.draw(GameWin)
    saveT = Text(Point(250, 295), 'SAVE')
    saveT.setFill('white')
    saveT.draw(GameWin)

    # Create a while loop for the condition that no click has been made in
    #  the game window and the new or quit buttons have not been clicked
    while (QuitClick == False) and (NewClick == False) and (MeteorClick == False):
        # Check for a mouse click
        mouse_pos = CtrlWin.checkMouse()
        if GameWin.isOpen():
            gameMouse = GameWin.checkMouse()
        # If mouse click is in the control window
        if mouse_pos:
            # Determine if mouse click is in either New or Quit box
            NewClick = insideRect(mouse_pos, New)
            QuitClick = insideRect(mouse_pos, Quit)
            HighClick = insideRect(mouse_pos, High)
            MeteorClick = insideRect(mouse_pos, Meteor)
            # If in new box, start game. If in quit box, close and terminate
            #  program.
            if NewClick:
                GameWin.close()
                meteorRain = 0
                score, GameWin, GameCircles, CirclesText, BlockP, \
                secword, secword_box, secword_text, \
                placehold, isClicked, scoreText, Result, GuessRect, meteorRain = startGame(meteorRain)

                return score, GameWin, GameCircles, CirclesText, BlockP, \
                       secword, secword_box, secword_text, \
                       placehold, isClicked, scoreText, Result, GuessRect, meteorRain

            if MeteorClick:
                GameWin.close()
                meteorRain = 1
                score, GameWin, GameCircles, CirclesText, BlockP, \
                secword, secword_box, secword_text, \
                placehold, isClicked, scoreText, Result, GuessRect, meteorRain = startGame(meteorRain)

                return score, GameWin, GameCircles, CirclesText, BlockP, \
                       secword, secword_box, secword_text, \
                       placehold, isClicked, scoreText, Result, GuessRect, meteorRain

            elif QuitClick:
                CtrlWin.close()
                GameWin.close()
                score = 0
                GameWin = 0
                GameCircles = 0
                CirclesText = 0
                BlockP = 0
                secword = 0
                secword_box = 0
                secword_text = 0
                placehold = 0
                isClicked = 0
                scoreText = 0
                Result = 'Quit'
                GuessRect = 0

                return score, GameWin, GameCircles, CirclesText, BlockP, \
                       secword, secword_box, secword_text, \
                       placehold, isClicked, scoreText, Result, GuessRect, meteorRain

            elif HighClick:
                highscore()

        elif gameMouse != None:
            x = gameMouse.getX()
            y = gameMouse.getY()

            if 220 < x < 280:  # coordinates specifying save
                if 280 < y < 310:
                    nameEntry = entryb.getText()
                    if nameEntry == '':
                        nameEntry = 'None'
                    f = open('scores.txt', 'a')
                    f.write(nameEntry + ',' + str(roundNum) + ',' + str(score) + '\n')
                    f.close()
                    GameWin.close()


# The hint function costs 2 guesses and provides the player with 3 incorrect letters.
def hint(secword, usedLetters):
    j = []
    k = []
    unguessedincorrect = []
    hint = []
    hinti = []
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x",
                "y", "z"]  # alphabet is added to compare indices of letters and populate lists
    for i in range(len(secword)):
        if secword[i] not in usedLetters:
            j.append(secword[i])  # creates list of unused CORRECT letters
    for i in alphabet:
        if i.upper() not in j:
            k.append(i.upper())  # list of incorrect letters
    for i in range(len(k)):
        if k[i] not in usedLetters:
            unguessedincorrect.append(k[i])  # list of unguessed incorrect letters
    for i in range(3):
        r = random.choice(unguessedincorrect)
        unguessedincorrect.remove(r)
        hint.append(r.lower())  # makes list of letters to be returned by hint
        usedLetters.append(r.upper())
    for lett in range(len(alphabet)):
        if alphabet[lett] in hint:  # returns the index of hint for circle dropping
            hinti.append(lett)

    return hinti, usedLetters


# The highscore function creates a scrolling graphics window of all the top
#  seven scores of the game
def highscore():
    # Open and read contents of scores file
    file = open('scores.txt', 'r')
    scores = file.read()
    scores = scores.splitlines()

    # Determine all of the saved scores
    highscores = []
    for element in scores:
        sublist = element.split(',')
        highscores.append(int(sublist[2]))

    # Sort the scores, identify the top seven, and then make a list of the
    #  unique scores within the top seven
    highscores.sort(reverse=True)
    if len(highscores) > 7:
        highscores = highscores[:7]
    highscores = list(set(highscores))
    highscores.sort(reverse=True)

    # Create a for loop iterating over number of unique scores in top seven
    sortedlist = []
    for j in range(len(highscores)):

        # Create a for loop iterating over total number of scores in file
        for i in range(len(scores)):

            # Create a sublist consisting of name, round number, score
            sublist = scores[i].split(',')

            # Identify if current lines score is equal to current high score
            #  value and append it to list if it is
            if int(sublist[2]) == highscores[j]:
                sortedlist.append(sublist)

    # Ensure sorted list is only seven elements long
    sortedlist = sortedlist[:7]

    # Create formatted strings for all the data in the top seven scores
    highscoretext = []
    for element in sortedlist:
        currenttext = '{:<10} {:^10} {:>10}'.format(element[0], element[1], element[2])
        highscoretext.append(currenttext)

    # Create a graphics window
    win = GraphWin("High Scores", 300, 110)
    win.setBackground('white')

    # Create text and graphics for the column titles of the high scores window
    titletext = '{:<10} {:^10} {:>10}'.format('Player', 'Rounds', 'Score')
    titlegraphic = []
    titlegraphic.append(Text(Point(150, 10), titletext))

    # Create text and graphics of the divider line
    bordertext = '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
    bordergraphic = []
    bordergraphic.append(Text(Point(150, 25), bordertext))

    # Create graphics for each score
    scoregraphic = [0] * len(highscoretext)
    x = 150
    y = 40
    scoregraphic[0] = Text(Point(x, y), highscoretext[0])
    for i in range(1, len(highscoretext)):
        y += 20
        scoregraphic[i] = Text(Point(x, y), highscoretext[i])

    # Combine all graphics, draw and set properties
    graphics = titlegraphic + bordergraphic + scoregraphic
    for i in range(len(graphics)):
        graphics[i].setSize(11)
        graphics[i].setFace('courier')
        graphics[i].draw(win)

    # Create a while loop until a mouse click is recognized
    MousePos = None
    while MousePos == None:

        # Check for mouse click
        MousePos = win.checkMouse()

        # Create a for loop iterating over all graphics element
        for element in graphics:

            # Move each graphics element and sleep
            step = -5
            element.move(0, step)
            sleep(.025)
            anchor = element.getAnchor()
            anchory = anchor.getY()

            # If graphics element moved off screen, move back to the bottom
            if anchory <= -10:
                element.move(0, 185)

    # Close window after mouseclick
    win.close()


# The AddWords() function allows a user to add additional 4-6 letter words
#  to the list of words used by the game. The function is called when
#  a button is pressed on the control panel and opens a new graphics
#  window. The graphics window gives instructions and allows the user to enter
#  a new word and gives error messages for invalid options (word already present
#  or not 4-6 letters long). This function only works before a game is started
def AddWords():
    # Initialize graphics window
    win = GraphWin('Add Words', 350, 120)
    win.setBackground('dark grey')

    # Initialize instructions
    Instructtxt = Text(Point(175, 80), 'If you would like, enter a 4-6 letter word \n'
                                       'to add to the possible list of words for the game. \n'
                                       'Press enter to submit and close to close the window.')
    Instructtxt.draw(win)
    Instructtxt.setSize(11)
    Instructtxt.setFill('blue')

    # Create entry box
    enterb = Entry(Point(95, 20), 10)
    enterb.draw(win)
    enterb.setFill('white')

    # Create enter button and associated text
    Enter = Rectangle(Point(160, 10), Point(220, 30))
    Enter.draw(win)
    Enter.setFill('green')
    Entertxt = Text(Point(190, 20), 'ENTER')
    Entertxt.setTextColor('white')
    Entertxt.setStyle('bold')
    Entertxt.setSize(10)
    Entertxt.draw(win)

    # Create close button and associated text
    Close = Rectangle(Point(230, 10), Point(290, 30))
    Close.draw(win)
    Close.setFill('red')
    Closetxt = Text(Point(260, 20), 'CLOSE')
    Closetxt.setStyle('bold')
    Closetxt.setTextColor('white')
    Closetxt.setSize(10)
    Closetxt.draw(win)

    # Create first error message (undrawn)
    Errortxt = Text(Point(175, 40), 'Word must be 4-6 letters ONLY')
    Errortxt.setSize(10)
    Errortxt.setTextColor('red')
    Errortxt.setStyle('bold')

    # Create first success message (undrawn)
    success = Text(Point(175, 40), 'Success!')
    success.setSize(10)
    success.setTextColor('green')
    success.setStyle('bold')

    # Create second error message (undrawn)
    Error2txt = Text(Point(175, 40), 'Word already in list')
    Error2txt.setSize(10)
    Error2txt.setTextColor('red')
    Error2txt.setStyle('bold')

    CloseClick = False
    EnterClick = False

    # Create a string of all the letters in alphabet
    letters = string.ascii_uppercase

    # Initialize while loop that runs while the Close button has not been clicked
    while CloseClick == False:
        # Check for mouse clicks
        mousePos = win.checkMouse()
        if mousePos:
            # Check for clicks inside either button
            CloseClick = insideRect(mousePos, Close)
            EnterClick = insideRect(mousePos, Enter)

            # If close button is pressed, close the function and terminate
            if CloseClick:
                win.close()
                return
            if EnterClick:

                # If enter button is pressed undraw all messages
                Errortxt.undraw()
                success.undraw()
                Error2txt.undraw()

                # Retrieve the text entered into the entry box and convert it to upper case
                newWord = enterb.getText()
                newWord = newWord.upper()

                # Determine if entry is string
                if (isinstance(newWord, str)):

                    # Determine if all characters in the string are in the
                    #  alphabet (determine if string is a word)
                    notletters = False
                    for letter in newWord:
                        if letter not in letters:
                            notletters = True

                    # Determine if word is 4-6 letters
                    if (len(newWord) >= 4) and (len(newWord) <= 6) and (notletters == False):

                        # If it is, read the text file and check if the word is in the file
                        f = open('words.txt', 'r')
                        file = f.read()
                        file = file.splitlines()
                        f.close()
                        if (newWord not in file):

                            # If not, open the file again and add the new word. Then draw success message
                            f = open('words.txt', 'a')
                            f.write(newWord + '\n')
                            f.close()
                            success.draw(win)

                        # If in file draw appropriate error message
                        else:
                            Error2txt.draw(win)
                    # If not 4-6 letters draw error message
                    else:
                        Errortxt.draw(win)
                # If not string draw error message
                else:
                    Errortxt.draw(win)


# The main() function calls all appropriate functions to run the game.
def main():
    roundNum = 1  # initialize roundNum
    ## Call the ctrlPan() function to create the control panel
    New, Quit, Hint, CtrlWin, High, Meteor, Add = ctrlPan()

    # Initialize loop variables
    NewClick = False
    QuitClick = False
    HintClick = False
    HighClick = False
    MeteorClick = False
    AddClick = False

    ## Create while loop before a game is started
    while (QuitClick == False) and (NewClick == False) and (MeteorClick == False):
        # Check for a mouse click
        mouse_pos = CtrlWin.checkMouse()
        if mouse_pos:
            # Determine if mouse click is in either New, Quit, or highscore box
            NewClick = insideRect(mouse_pos, New)
            QuitClick = insideRect(mouse_pos, Quit)
            HighClick = insideRect(mouse_pos, High)
            MeteorClick = insideRect(mouse_pos, Meteor)
            AddClick = insideRect(mouse_pos, Add)
            # If in new box, start game. If in quit box, close and terminate
            #  program. If in highscores, call highscore function
            if NewClick:
                meteorRain = 0
                score, GameWin, GameCircles, CirclesText, BlockP, \
                secword, secword_box, secword_text, \
                placehold, isClicked, scoreText, Result, GuessRect, meteorRain = startGame(meteorRain)

            if MeteorClick:
                # Initiates hardmode where meteors rain from the heavens. Clicking a meteor can deflect it and give you
                #       bonus points. If a meteor of sufficient size strikes the ground though, lose a blockP

                # explain to player how this mode works
                explainwin = GraphWin('Meteor Mode (HARD)', 350, 100)
                explainwin.setBackground('cyan')
                explaintext = Text(Point(175, 40), 'Click falling meteors to gain 2 bonus points!\n'
                                                   ' If a meteor of sufficient size strikes the ground\n'
                                                   'be prepared to lose blocks! \n')
                explaintext.setTextColor('purple')
                explaintext.draw(explainwin)
                explaintext.setSize(12)

                clickanywheretext = Text(Point(175, 85), 'Click in this window to continue ...')
                clickanywheretext.setTextColor('red')
                clickanywheretext.draw(explainwin)

                # exit the explanation window and start the game
                mouseclick = explainwin.getMouse()
                if mouseclick:
                    explainwin.close()
                    meteorRain = 1
                    score, GameWin, GameCircles, CirclesText, BlockP, \
                    secword, secword_box, secword_text, \
                    placehold, isClicked, scoreText, Result, GuessRect, meteorRain = startGame(meteorRain)

            if AddClick:
                AddWords()

            if QuitClick:
                CtrlWin.close()
                return

            if HighClick:
                highscore()

    # Create a while loop after a game is started
    while QuitClick == False:
        # While a round is still in progress, call the play() function
        if Result == 'Playing':
            Result, score, GameWin, meteorRain = play(score, GameWin, GameCircles, CirclesText, BlockP,
                                                      secword, secword_box, secword_text,
                                                      placehold, isClicked, scoreText, Result, CtrlWin, New, Quit, Hint,
                                                      High,
                                                      GuessRect, meteorRain)
        # If the round has ended in a Win, call the Win() function
        elif Result == 'Win':
            score, GameWin, GameCircles, CirclesText, BlockP, \
            secword, secword_box, secword_text, placehold, \
            isClicked, scoreText, Result, roundNum, GuessRect, meteorRain = Win(GameWin, score, CtrlWin, New, Quit,
                                                                                roundNum, High, meteorRain, Meteor)
        # If the round has ended in a Loss, call the Lose() function
        elif Result == 'Lose':
            score, GameWin, GameCircles, CirclesText, BlockP, \
            secword, secword_box, secword_text, placehold, \
            isClicked, scoreText, Result, GuessRect, meteorRain = Lose(CtrlWin, New, Quit, High, GameWin, score,
                                                                       roundNum, Meteor, meteorRain)
        # If the player has quit the game, terminate the program
        elif Result == 'Quit':
            return


main()
