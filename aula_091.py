# Criando e adicionando novas funcionalidades a classes

class Automovel:
    def __init__(self, placa, velocidade_max):  # Adicionamos mais um atributo no construtor da classe
        self.placa = placa
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def __str__(self):  # Ao utilizar o __str__ escolhemos oq será impresso ao chamar o objeto
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


meu_carro = Automovel('XYZ-1234', 180)  # Na criação do objeto, como não definimos um valor padrão, colocamos os dois

print(meu_carro.get_placa())
meu_carro.dirigir(100)
print(meu_carro)

for _ in range(20):
    meu_carro.acelerar()
    print(meu_carro)

for _ in range(20):
    meu_carro.frear()
    print(meu_carro)

