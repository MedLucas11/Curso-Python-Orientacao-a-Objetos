# __del__
# Essa ação é executada quando deletamos um objeto da memória. O python faz o "garbage collection" automaticamente.

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
        return self.__paginas + other.__paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado')


livro1 = Livro('Algoritmos e Programação de Computadores', 'Piva Jr, et al', 'Elsevier', 2019, 508)
livro2 = Livro('Estrutura de Dados e Técnicas de Programação', 'Piva Jr, et al', 'Elsevier', 2014, 399)

print(livro1 + livro2)
