# Atributos Privados

class Automovel:
    def __init__(self, placa, velocidade_max):
        self.placa = placa
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def __str__(self):
        return f'A velocidade é {self.velocidade_atual} km/h'

    def get_placa(self):
        return self.placa

    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} km/h')

    def acelerar(self):
        if self.velocidade_atual < self.velocidade_max:
            self.velocidade_atual += 10

    def frear(self):
        if self.velocidade_atual > 0:
            self.velocidade_atual -= 10


meu_carro = Automovel('XYZ-1234', 180)

print(meu_carro)
print(meu_carro.velocidade_max)
print(meu_carro.get_placa())
print('--------------------------')

print('Sem encapsulamento adequado')
meu_carro.placa = 'XXX-0000'
meu_carro.velocidade_max = 200
meu_carro.velocidade_atual = 190

print(meu_carro)
print(meu_carro.velocidade_max)
print(meu_carro.get_placa())


# Para tornar os métodos e os atributos acessíveis apenas dentro da própria classe, utilizamos "__" antes dos seus nomes


class Automovel2:
    def __init__(self, placa, velocidade_max):
        self.__placa = placa
        self.__velocidade_max = velocidade_max
        self.__velocidade_atual = 0

    def __str__(self):
        return f'A velocidade é {self.__velocidade_atual} km/h'

    def get_placa(self):
        return self.__placa

    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} km/h')

    def acelerar(self):
        if self.__velocidade_atual < self.__velocidade_max:
            self.__velocidade_atual += 10

    def frear(self):
        if self.__velocidade_atual > 0:
            self.__velocidade_atual -= 10


meu_carro2 = Automovel2('XYZ-0000', 180)

print(meu_carro2)
print(meu_carro2.__velocidade_max)  # Não é mais acessível de fora, portanto não pode ser impresso nem alterado
print(meu_carro2.get_placa())
print('--------------------------')


meu_carro2.__placa = 'XXX-0000'
meu_carro2.__velocidade_max = 200
meu_carro2.__velocidade_atual = 190

print(meu_carro2)
print(meu_carro2.__velocidade_max)
print(meu_carro2.get_placa())