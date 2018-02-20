#####################
##    Final Game   ##
##  Jack Anderson  ##
##  Code Day PRJ   ##
##     2/18/18     ##
##   Version 1.0   ##
#####################

# ==========================================================
# Import Libraries
from cdGraphics import *
from CodeDay_Objects import *
import time

# ==========================================================
# Global Variables
CodeDayWindow = GraphWin("PyRacers Game", 1100, 650)
CodeDayWindow.setBackground("grey")
raceTrack = Image(Point(575, 325), "Track3.gif")

# ==========================================================
# Functions




# ==========================================================
# Main Function
def main():
    raceTrack = Image(Point(575, 325), "Track3.gif")
    # Create the Track
    raceTrack.draw(CodeDayWindow)

    #Create the cars
    car1 = Runner(525, 55, 10, CodeDayWindow, "red")
    car1.draw()



    direction = None

    while True:

        #print(car1.getX())
        #print(car1.getY())

        key = CodeDayWindow.checkKey()
        x = int(car1.getX())
        y = int(car1.getY())

        if key == "Up" or key == "Down" or key == "Left" or key ==  "Right":
            direction = key


        if direction == "Up":
            red, green, blue = raceTrack.getPixmap().getPixel(x, y - 10)
            if red != 0 and red != 255 and green != 0 and green != 255 and blue != 0 and blue != 255:
                direction = None
            else:
                car1.centerY = car1.getY() - car1.size



        elif direction == "Down":
            red, green, blue = raceTrack.getPixmap().getPixel(x, y + 10)
            if red != 0 and red != 255 and green != 0 and green != 255 and blue != 0 and blue != 255:
                direction = None
            else:
                car1.centerY = car1.getY() + car1.size

        

        elif direction == "Left":
            red, green, blue = raceTrack.getPixmap().getPixel(x - 10, y)
            if red != 0 and red != 255 and green != 0 and green != 255 and blue != 0 and blue != 255:
                direction = None
            elif red == 255 and green == 255 and blue == 255:
                CodeDayWindow.close()

                for i in range(1):
                    #===========================================
                    winnerWindow = GraphWin("You win!!!", 500, 500)
                    winnerWindow.setBackground("sky blue")
                    winMessage = Text(Point(250, 250), "Congratulations, You have won... here is your gold medal!!!")
                    winMessage.draw(winnerWindow)

                    medal = Circle(Point(250, 100), 50)
                    medal.setFill("yellow")
                    medal.setOutline("yellow")
                    medal.draw(winnerWindow)

                    medalMessage = Text(Point(250, 100), "#1")
                    medalMessage.draw(winnerWindow)



                    winnerWindow.getMouse()
                    winnerWindow.close()
            else:
                car1.centerX = car1.getX() - car1.size

        elif direction == "Right":
            red, green, blue = raceTrack.getPixmap().getPixel(x + 10, y)
            if red != 0 and red != 255 and green != 0 and green != 255 and blue != 0 and blue != 255:
                direction = None

                for i in range(1):
                    #===========================================
                    winnerWindow = GraphWin("You win!!!", 500, 500)
                    winnerWindow.setBackground("sky blue")
                    winMessage = Text(Point(250, 250), "Congratulations, You have won... here is your gold medal!!!")
                    winMessage.draw(winnerWindow)

                    medal = Circle(Point(250, 100), 50)
                    medal.setFill("yellow")
                    medal.setOutline("yellow")
                    medal.draw(winnerWindow)

                    medalMessage = Text(Point(250, 100), "#1")
                    medalMessage.draw(winnerWindow)



                    winnerWindow.getMouse()
                    winnerWindow.close()
            else:
                car1.centerX = car1.getX() + car1.size


        car1.move(direction)
        time.sleep(.075)


    # ============================================================



# ==========================================================
# Call main
main()