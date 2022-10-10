from operator import concat
import os
import random

class InitSets:
    def __init__(this):
        this.clear = lambda: os.system("CLS")

        this.InitGameSets()
        this.clear()
        this.PrintField()
        if this.anyoneWon: print(f"\n{this.indicator} выиграли")
        else: print("\nНикто не выиграл")

    def InitGameSets(this):

        this.gameField = [(lambda : ["*" for i in range(3)])() for x in range(3)]

        this.player = "First"

        while (this.CheckEmptyField()):

            this.anyoneWon = False
        
            this.clear()
            this.PrintField()
            print("\nХод можно сделать")
            if this.player == "First": this.indicator = "X"
            else: this.indicator = "O"

            a, b = map(int, input(f"{this.indicator} ход: ").split())
            
            this.gameField[a-1][b-1] = this.indicator
            this.PrintField()
            
            if this.CheckGameWin(this.indicator): 
                this.anyoneWon = True
                print(f"{this.indicator} выиграли") 
                return
            else: print("Вы еще не выиграли")

            this.player = this.TogglePlayer(this.player)
            
    def TogglePlayer(this, player):
        if player == "First": return "Second"
        if player == "Second": return "First"
        
    def CheckEmptyField(this):
        for i in range(len(this.gameField)): 
            if "*" in this.gameField[i]: return True
        return False


    def PrintField(this):
        for i in range(len(this.gameField)): print(this.gameField[i])

    def CheckGameWin(this, indicator):

        # checking rows
        for i in range(3):
            winFlag = True
            for j in range(3):
                if this.gameField[i][j] != indicator:
                    winFlag = False
                    break
            if winFlag: return winFlag

        # checking columns
        for i in range(3):
            winFlag = True
            for j in range(3):
                if this.gameField[j][i] != indicator:
                    winFlag = False
                    break
            if winFlag: return winFlag

        # checking diagonals
        winFlag = True
        for i in range(3):
            if this.gameField[i][i] != indicator:
                winFlag = False
                break

        if winFlag: return winFlag
        
        winFlag = True
        for i in range(3):
            if this.gameField[i][2-i] != indicator:
                winFlag = False
                break

        if winFlag: return winFlag
        else: return False
