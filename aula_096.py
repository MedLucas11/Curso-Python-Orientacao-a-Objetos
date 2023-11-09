# Polimorfismo

# Essa propriedade permite que o mesmo método seja sobreposto em classes inferiores, para ser executado da forma
# adequada


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def emite_som(self):
        pass


class Arara(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emite_som(self):
        print('Grasna')


class Cascavel(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emite_som(self):
        print('Chocalha')


cobra = Cascavel('Celeste')
arara = Arara('Rio')

print(cobra.emite_som())
print(arara.emite_som())
