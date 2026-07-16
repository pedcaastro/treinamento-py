class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Restaurante da Praça'
restaurante_praca.categoria = 'Comida Caseira'
restaurante_praca.ativo = True

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Restaurante da Pizza'
restaurante_pizza.categoria = 'Pizza' 
restaurante_pizza.ativo = True

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))