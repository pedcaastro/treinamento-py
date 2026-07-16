class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}'
    

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'Restaurante: {restaurante.nome}, Categoria: {restaurante.categoria}, Ativo: {restaurante.ativo}')

restaurante_praca = Restaurante('Praca', 'Comida Caseira')
restaurante_pizza = Restaurante('Pizza', 'Pizza')

Restaurante.listar_restaurantes()