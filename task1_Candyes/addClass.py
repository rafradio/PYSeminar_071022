from operator import concat
import os
import random

class InitSets:
    def __init__(this):
        this.clear = lambda: os.system("CLS")
        
        this.InitGameSets()
        
    def InitGameSets(this):
        this.players = ["Первый", "Второй"]
        this.playersScore = [0, 0]
        this.playerTurn = random.randrange(0, 2)
        this.totalCand = 2021
        this.PlayMode()

    def PlayMode(this):
        while this.totalCand > 0:
            this.PrintField()
            
            this.takeCandies = this.InputPlayer()
            this.playersScore[this.playerTurn] += this.takeCandies
            this.totalCand -= this.takeCandies
            
            if this.totalCand == 0: break
            this.playerTurn = this.TogglePlayer(this.playerTurn)

        if this.playerTurn == 1: print("Второй выиграл")
        else: print("Первый выиграл")

    def PrintField(this):
        this.clear()
        print("На столе: ", this.totalCand, " конфет")
        print(f"У первого игрока: {this.playersScore[0]} конфет.\tУ второго игрока: {this.playersScore[1]} конфет")

    def TogglePlayer(this, player):
        if player == 0: return 1
        else: return 0

    def InputPlayer(this):
        while (True):
            try:
                a = int(input(f"{this.playerTurn + 1} ходит. Возьмите конфет: "))
            except:
                print("Попробуйте еще раз")
            else:
                if a > 0 and a <= this.totalCand and a <= 280: return a
                else: print("Цифры введены не верно!")