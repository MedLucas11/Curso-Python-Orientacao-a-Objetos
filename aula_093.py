# Métodos getters e setters

class Automovel:
    def __init__(self, placa, velocidade_max):
        self.__placa = placa
        self.__velocidade_max = velocidade_max
        self.__velocidade_atual = 0

    def __str__(self):
        return f'A velocidade é {self.__velocidade_atual} km/h'

    def get_placa(self):
        return self.__placa

    def get_velocidade_max(self):  # Criamos métodos que permitem 'pegar' as informações que queremos
        return self.__velocidade_max

    def set_velocidade_max(self, nova):  # Criamos métodos que permitem 'settar" novas informações
        self.__velocidade_max = nova

    def acelerar(self):
        if self.__velocidade_atual < self.__velocidade_max:
            self.__velocidade_atual += 10

    def frear(self):
        if self.__velocidade_atual > 0:
            self.__velocidade_atual -= 10


meu_carro = Automovel('XYZ-0000', 180)

print(meu_carro)
print(meu_carro.get_placa())
print(meu_carro.get_velocidade_max())
print('---------------------------')

print('Com encapsulamento adequado')
meu_carro.set_velocidade_max(200)

print(meu_carro)
print(meu_carro.get_placa())
print(meu_carro.get_velocidade_max())
