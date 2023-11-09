from carro import Carro

carro_novo = Carro('Corolla', 2022)
print(carro_novo.get_descricao())

carro_novo.set_odometro(1200)
print(carro_novo.get_odometro())
