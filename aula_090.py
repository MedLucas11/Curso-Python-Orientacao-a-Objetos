# Criando classes

class Automovel:
    pass


meu_carro = Automovel()


class Automovel2:
    def __init__(self, placa):  # utilizamos o __init__ e passamos o parâmetro placa para o self
        self.placa = placa


meu_carro_2 = Automovel2('XYZ-0000')

print(meu_carro_2.placa)


class Automovel3:
    def __init__(self, placa):
        self.placa = placa

    def get_placa(self):   # Criamos o método get_placa, que retorna a placa informada
        return self.placa


meu_carro_3 = Automovel3('XXX-0000')
print(meu_carro_3.get_placa())


class Automovel4:
    def __init__(self, placa):
        self.placa = placa

    def get_placa(self):
        return self.placa

    def dirigir(self, velocidade):  # Criamos um método que mostra a velocidade
        print(f'Estou dirigindo a {velocidade} km/h')


meu_carro_4 = Automovel4('XZL-0111')

print(meu_carro_4.get_placa())
meu_carro_4.dirigir(120)
