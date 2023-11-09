# Herança Múltipla

# Existem dois tipos de herança múltipla:

# Multi-derivação direta: A classe inferior herda diretamente atributos de duas classes superiores
# Multi-derivação indireta: As classes inferiores podem herdar atributos de classes em níveis ainda mais superiores


# Multi-derivação direta:
class Classe1:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome


class Classe2:
    def __init__(self, endereco):
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco


class Classe3(Classe1, Classe2):  # A ordem das classes importa, a primeira tem prioridade nos métodos herdados
    def __init__(self, nome, endereco, salario):
        super().__init__(nome)
        super().__init__(endereco)
        self.__salario = salario

    def get_salario(self):
        return self.__salario


# Multi-derivação indireta:
class Classe4:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome


class Classe5(Classe4):
    def __init__(self, nome, endereco):
        super().__init__(nome)
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco


class Classe6(Classe5):
    def __init__(self, nome, endereco, salario):
        super().__init__(nome, endereco)
        self.__salario = salario

    def get_salario(self):
        return self.__salario

