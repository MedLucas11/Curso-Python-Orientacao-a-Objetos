# Métodos mágicos (métodos especiais)

# Eles são métodos do tipo __(nome_do_método)__

# __repr__
# Mostra a representação do elemento
class Livro:
    def __init__(self, titulo, autor, editora, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__ano = ano


livro1 = Livro('Algoritmos e Programação de Computadores', 'Piva Jr, et al', 'Elsevier', 2019)
livro2 = Livro('Estrutura de Dados e Técnicas de Programação', 'Piva Jr, et al', 'Elsevier', 2014)

print(livro1)
print(livro2)
print('-----------------------------------------------------------')
# Sem sobreescrever nada na classe a impressão mostrará a representação original da classe


class Livro2:
    def __init__(self, titulo, autor, editora, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__ano = ano

    def __repr__(self):
        return f'{self.__titulo} - {self.__autor}'  # Definindo o método __repr__ mudamos o que será mostrado no print()


livro3 = Livro2('Algoritmos e Programação de Computadores', 'Piva Jr, et al', 'Elsevier', 2019)
livro4 = Livro2('Estrutura de Dados e Técnicas de Programação', 'Piva Jr, et al', 'Elsevier', 2014)

print(livro3)
print(livro4)
print('-----------------------------------------------------------')

# __str__
# Esse método tem prioridade em relação ao __repr__ e será mostrado no print() caso seja definido

class Livro3:
    def __init__(self, titulo, autor, editora, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__ano = ano

    def __repr__(self):
        return f'{self.__titulo} - {self.__autor}'

    def __str__(self):
        return f'{self.__ano} - {self.__titulo}'


livro5 = Livro3('Algoritmos e Programação de Computadores', 'Piva Jr, et al', 'Elsevier', 2019)
livro6 = Livro3('Estrutura de Dados e Técnicas de Programação', 'Piva Jr, et al', 'Elsevier', 2014)

print(livro5)
print(livro6)