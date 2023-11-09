class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def identificacao(self):
        return self.__cpf


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, codigo):
        super().__init__(nome, sobrenome, cpf)
        self.__codigo = codigo

    def identificacao(self):
        return self.__codigo


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def identificacao(self):
        return self.__matricula


pessoa = Pessoa('Lucas', 'Medeiros', '523.991.158-48')
cliente = Cliente('Yasmin', 'Salles', '123.456.789-10', '20')
funcionario = Funcionario('Vitor', 'Medeiros', '987.654.321-01', '7701/20')

print(pessoa.identificacao())
print(cliente.identificacao())
print(funcionario.identificacao())
