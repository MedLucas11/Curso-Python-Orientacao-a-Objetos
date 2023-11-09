from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=1000, salt_size=10)
        Usuario.contador = self.__id

    def get_nome_completo(self):
        print(f'{self.__id} - {self.__nome} {self.__sobrenome}')

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        else:
            print('Senha Incorreta!')
            return False


while True:
    nome_usuario = input('Digite seu nome: ')
    sobrenome_usuario = input('Digite seu sobrenome: ')
    email_usuario = input('Digite seu email: ')
    senha_usuario = input('Crie uma senha: ')
    confirma_senha = input('Digite novamente a senha: ')
    if senha_usuario == confirma_senha:
        usuario = Usuario(nome_usuario, sobrenome_usuario, email_usuario, senha_usuario)
        break
    else:
        print("As senhas não conferem")

print('Usuário criado com sucesso!')

checagem = input("Digite a senha para acesso: ")

if usuario.checa_senha(checagem):
    print('Acesso Permitido!!')
    usuario.get_nome_completo()
else:
    print('Acesso Negado')
