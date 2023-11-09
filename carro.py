class Carro:
    def __init__(self, modelo, ano):
        self.__modelo = modelo
        self.__ano = ano
        self.__odometro = 0

    def get_descricao(self):
        nome = self.__modelo + ' ' + str(self.__ano)
        return nome.title()

    def get_odometro(self):
        return f'Esse carro tem {self.__odometro} km'

    def set_odometro(self, km):
        self.__odometro += km
