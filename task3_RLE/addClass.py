from operator import concat
import os

class InitSets:
    def __init__(this):
        this.clear = lambda: os.system("CLS")
        this.clear()
        this.string = input("Введите строчку для кодирования: ")
        this.codedString = this.CodeMessage()
        this.decodedString = this.DecodeMessage()
        this.Print()
        
    def CodeMessage(this):
        coded_string = ""
        i = 0
        while (i <= len(this.string)-1):
            count = 1
            ch = this.string[i]
            j = i
            while (j < len(this.string)-1):
                if (ch == this.string[j + 1]): 
                    count = count + 1
                    j = j + 1
                else: break
            coded_string += str(count) + ch
            i = j + 1
        return coded_string

    def DecodeMessage(this):
        decoded_string = ""
        i = 0
        
        while (i <= len(this.codedString) - 1):
            numberCh = int(this.codedString[i])
            wordCh = this.codedString[i + 1]
            for _ in range(numberCh):
                decoded_string += wordCh

            i = i + 2
        return decoded_string

    def Print(this):
        print(f"Введенная строка: {this.string}")
        print(f"Закодированная строка: {this.codedString}")
        print(f"Раскодированная строка: {this.decodedString}")
