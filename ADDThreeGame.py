# Author: Samuel Bennett
# Date: 5/26/2021
# Description: Game to 15 with private data members storing numbers chosen, game state & whose turn it is.

class AddThreeGame:

    def __init__(self):
        self.__p1 = 0
        self.__p2 = 0
        self.__played = []
        self.__curstat = "UNFINISHED"

    def get_current_state(self):
        return self.__curstat

    def make_move(self, pl, x):
        if x in self.__played:
            return False
        if x > 9 or x < 1:
            return False
        if pl == "first":
            self.__p1 = self.__p1 + x
            self.__played.append(x)
        elif pl == "second":
            self.__p2 = self.__p2 + x
            self.__played.append(x)
        if self.__p1 == 15 and self.__p2 == 15:
            self.__curstat = "DRAW"
        elif self.__p1 == 15:
            self.__curstat = "FIRST_WON"
        elif self.__p2 == 15:
            self.__curstat = "SECOND_WON"
        if len(self.__played) == 9:
            self.__curstat = "DRAW"
        if self.__p1 > 15 and self.__p2 > 15:
            self.__curstat = "DRAW"
        return True


game = AddThreeGame()

while True:

    x = int(input("Player 1 please enter a number: "))
    while True:
        if game.make_move("first", x) == True:
            break
        else:
            x = int(input("Invalid input! Player 1 please re-enter a number: "))

    x = int(input("Player 2 please enter a number:"))
    while True:
        if game.make_move("second", x) == True:
            break
        else:
            x = int(input("Invalid input! Player 2 please re-enter a number: "))

    playstatus = game.get_current_state()
    if playstatus == "UNFINISHED":
        print("No one reached 15. Get ready for next round.\n")

    elif playstatus == "FIRST_WON":
        print("First player won!!!\n")
        break

    elif playstatus == "SECOND_WON":
        print("Second player won!!!\n")
        break

    elif playstatus == "DRAW":
        print("Game ends in draw\n")
        break