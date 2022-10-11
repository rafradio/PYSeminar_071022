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
        this.indicator = "O"
        this.player = "First"

        while (this.CheckEmptyField()):

            this.anyoneWon = False
        
            this.clear()
            this.PrintField()
            print("\nХод можно сделать")

            this.indicator = this.TogglePlayer(this.indicator)

            a, b = this.InputPlayer()
            
            this.gameField[a-1][b-1] = this.indicator
            this.PrintField()
            
            if this.CheckGameWin(this.indicator): 
                this.anyoneWon = True
                print(f"{this.indicator} выиграли") 
                return
            else: print("Вы еще не выиграли")
            
    def InputPlayer(this):
        while (True):
            try:
                a, b = map(int, input(f"{this.indicator} ходят: ").split())
            except:
                print("Попробуйте еще раз")
            else:
                if a > 0 and a < 4:
                    if b > 0 and b < 4: 
                        if this.gameField[a-1][b-1] == "*": return a, b
                    
                print("Цифры введены не верно!")

    def TogglePlayer(this, player):
        if player == "O": return "X"
        if player == "X": return "O"
        
    def CheckEmptyField(this):
        for i in range(len(this.gameField)): 
            if "*" in this.gameField[i]: return True
        return False


    def PrintField(this):
        for i in range(len(this.gameField)): print(this.gameField[i])

    def CheckGameWin(this, indicator):

        # rows
        for i in range(3):
            winFlag = True
            for j in range(3):
                if this.gameField[i][j] != indicator:
                    winFlag = False
                    break
            if winFlag: return winFlag

        # columns
        for i in range(3):
            winFlag = True
            for j in range(3):
                if this.gameField[j][i] != indicator:
                    winFlag = False
                    break
            if winFlag: return winFlag

        # diagonal 1
        winFlag = True
        for i in range(3):
            if this.gameField[i][i] != indicator:
                winFlag = False
                break

        if winFlag: return winFlag
        
        # diagonal 2
        winFlag = True
        for i in range(3):
            if this.gameField[i][2-i] != indicator:
                winFlag = False
                break

        if winFlag: return winFlag
        else: return False
