from operator import concat
import os
import random

class InitSets:
    def __init__(this):
        this.clear = lambda: os.system("CLS")
        this.InitGameSets()
        this.PlayMode()
        
    def InitGameSets(this):
        this.players = ["Первый", "Второй"]
        this.playersScore = [0, 0]
        this.playerTurn = random.randrange(0, 2)
        this.totalCand = 2021
        this.botStarting = False
        

    def PlayMode(this):
        while this.totalCand > 0:
            this.PrintField()
            if this.playerTurn == 0: this.takeCandies = this.InputPlayer()
            else: 
                this.takeCandies = this.BotTakesCalc()
                this.botStarting = True

            this.playersScore[this.playerTurn] += this.takeCandies
            this.totalCand -= this.takeCandies

            if this.totalCand == 0: break
            this.playerTurn = this.TogglePlayer(this.playerTurn)

        this.PrintField()
        if this.playerTurn == 1: print("Бот выиграл")
        else: print("Человек выиграл")

    def BotTakesCalc(this):
        max = this.totalCand if this.totalCand <= 480 else 480
        this.botTakes = random.randrange(1, max) if max > 1 else 1
        return this.botTakes

    def PrintField(this):
        
        this.clear()
        print("На столе: ", this.totalCand, " конфет")
        print(f"У человека: {this.playersScore[0]} конфет.\tУ бота: {this.playersScore[1]} конфет")
        if this.botStarting: print(f"Бот взял: {this.botTakes} конфет")

    def TogglePlayer(this, player):
        return 1 if player == 0 else 0

    def InputPlayer(this):
        while (True):
            try:
                a = int(input("Человек ходит. Возьмите конфет: "))
            except:
                print("Попробуйте еще раз")
            else:
                if a > 0 and a <= this.totalCand and a <= 480: return a
                else: print("Цифры введены не верно!")