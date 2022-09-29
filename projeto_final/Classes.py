

class C1:

    # Construtor classe 1
    def __init__(self, atr1, atr2, atr3):
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3

    # Getters atributos da classe 1
    @property
    def atr1(self):
        return self._atr1

    @property
    def atr2(self):
        return self._atr2

    @property
    def atr3(self):
        return self._atr3

    # Setters atributos da classe 2
    @atr1.setter
    def atr1(self, valor):
        self._atr1 = valor

    @atr2.setter
    def atr2(self, valor):
        self._atr2 = valor

    @atr3.setter
    def atr3(self, valor):
        self._atr3 = valor

    # Metodos classe 1
    def metodo1(self):
        return self.atr1 + self.atr2

    def metodo2(self):
        return self.atr3 * 3
