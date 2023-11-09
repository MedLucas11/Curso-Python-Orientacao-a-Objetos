def nome_completo():
    print(f'')


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_cpf(self):
        return self.__cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = float(renda)

    def get_renda(self):
        return self.__renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula


cliente1 = Cliente('Lucas', 'Medeiros', '523.991.158-48', '500.00')
funcionario1 = Funcionario('Vitor', 'Silva', '123.456.789-10', '7701-5')

print(cliente1.get_nome())
print(funcionario1.get_nome())
print(cliente1.nome_completo())
print(funcionario1.nome_completo())
print(cliente1.get_renda())
print(funcionario1.get_matricula())
