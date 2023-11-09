# Herança em python

# Herança em linguagem computacional tem basicamente o mesmo significado que na realidade, objetos ou classes "herdam"
# características de outros objetos ou classes

# É um princípio fundamental para o reaproveitamento de código!


class Mamifero:
    def __init__(self, pelos, mamas, idade):
        self.__pelos = pelos
        self.__mamas = mamas
        self.__idade = idade

    def comunicar(self):
        pass


class Cachorro(Mamifero):
    def __init__(self, pelos, mamas, idade, rabo):
        super().__init__(pelos, mamas, idade)  # Podemos herdar as características da classe superior, com o super()
        self.__rabo = rabo

    def latir(self):
        pass


class Gato(Mamifero):
    def __init__(self, pelos, mamas, idade, rabo):
        Mamifero.__init__(pelos, mamas, idade)  # Podemos usar o nome da classe superior também para herdar
        self.__rabo = rabo

    def miar(self):
        pass


