# __len__
# Esse método define um tamanho para que o python considere caso seja necessário utilizar a função len()

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


livro1 = Livro('Algoritmos e Programação de Computadores', 'Piva Jr, et al', 'Elsevier', 2019, 508)
livro2 = Livro('Estrutura de Dados e Técnicas de Programação', 'Piva Jr, et al', 'Elsevier', 2014, 399)

print(livro1)
print(len(livro1))
print('-----------------')
print(livro2)
print(len(livro2))
