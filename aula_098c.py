# __add__
# Realiza a operação de adição/concatenação entre dois elementos, ao sobreescrever esse método definimos o que será
# feito

class Livro:
    def __init__(self, titulo, autor, editora, ano, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__ano = ano
        self.__paginas = paginas

    def __repr__(self):
        return f'{self.__titulo} - {self.__autor}'

    def __str__(self):
        return f'{self.__ano} - {self.__titulo}'

    def __len__(self):
        return self.__paginas

    def __add__(self, other):
        return self.__paginas + other.__paginas  # retorna a soma do número de páginas nesse caso


livro1 = Livro('Algoritmos e Programação de Computadores', 'Piva Jr, et al', 'Elsevier', 2019, 508)
livro2 = Livro('Estrutura de Dados e Técnicas de Programação', 'Piva Jr, et al', 'Elsevier', 2014, 399)

print(livro1 + livro2)
