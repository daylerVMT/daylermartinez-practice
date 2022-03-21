class Calculator:
    def add(self, val1, val2):
        return val1 + val2

    def valid_age(self, value):
        return 0 < value < 100

    def max(self, num1, num2, num3):
        if num1 > num2 and num1 > num3:
            return num1
        if num2 > num1 and num2 > num3:
            return num2
        if num3 > num2 and num3 > num1:
            return num3
        return print("num invalido")

    def isVocal(self, value):
        list = ("a", "e", "i", "o", "u")
        try:
            if isinstance(int(value), int):
                return "es numero"
        except:
            pass
        if isinstance(value, str):
            i = 0
            while i < 5:
                if list[i] == value:
                    return "es vocal"
                else:
                    return "es consonante"

    def inversa(self, value):
        new = ""
        i = len(value)
        while i >= 1:
            new = new + value[i - 1]
            i = i - 1
        return new

    def palindromo(self, value):
        new = ""
        i = len(value)
        while i >= 1:
            new = new + value[i - 1]
            i = i - 1
        return new == value

    def array(self, value):
        max = 0
        min = 10
        sum = 0
        i = 0
        for element in value:
            if element >= max:
                max = element
            if element <= min:
                min = element
            sum += element
            i += 1
        average = sum // i
        newList = [max, min, average]
        return newList

    def paises(self, listas):
        i = 0
        while i < len(listas):
            may = len(listas[0])
            if len(listas[i]) > may:
                mayor = listas[i]
            i = i + 1
        return mayor

    def binario(self, value):
        if value < 10:
            listas = (0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010)
            i = 0
            while i < len(listas):
                if value == i:
                    return listas[i]
                i = i + 1
        else:
            return "rango no aceptado"

    def cantidadChar(self, string):
        return len(string)
