# Exemplo de herança múltipla

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def cumprimentar(self):
        return f'Sou {self.__nome}'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{super().get_nome()} andando!'

    def cumprimentar(self):
        return f'Sou {super().get_nome()} da terra!'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{super().get_nome()} nadando!"

    def cumprimentar(self):
        return f'Sou {super().get_nome()} da água'


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


# Teste

jabuti = Terrestre('Ninja')
print(jabuti.andar())
print(jabuti.cumprimentar())
print('-------------------')

golfinho = Aquatico('Flipper')
print(golfinho.nadar())
print(golfinho.cumprimentar())
print('-------------------')

pinguim = Pinguim('Capitão')
print(pinguim.nadar())
print(pinguim.andar())
print(pinguim.cumprimentar())  # O cumprimentar() tem prioridade da primeira classe nos parênteses, o Terrestre()
