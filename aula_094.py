# Atributos de Classe

class Automovel:
    contador = 0  # Os atributos de classe são definidos antes do construtor
    precisao = 0.95

    def __init__(self, placa, velocidade_max):
        self.__id = Automovel.contador + 1
        self.__placa = placa
        self.__velocidade_max = velocidade_max * Automovel.precisao
        self.__velocidade_atual = 0
        Automovel.contador = self.__id

    def __str__(self):
        return f'{self.__id} - {self.__velocidade_atual} km/h'

    def get_placa(self):
        return self.__placa

    def get_velocidade_max(self):
        return self.__velocidade_max

    def set_velocidade_max(self, nova):
        self.__velocidade_max = nova

    def acelerar(self):
        if self.__velocidade_atual < self.__velocidade_max:
            self.__velocidade_atual += 10

    def frear(self):
        if self.__velocidade_atual > 0:
            self.__velocidade_atual -= 10


meu_carro = Automovel('XZX-1234', 180)
seu_carro = Automovel('ZTE-9874', 200)

print(meu_carro)
print(meu_carro.get_placa())
print(meu_carro.get_velocidade_max())
print('------------------------')
print(seu_carro)
print(seu_carro.get_placa())
print(seu_carro.get_velocidade_max())
