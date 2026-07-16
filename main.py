from classes.restaurante_construtor import Restaurante

restaurante_praca = Restaurante('Praca', 'Comida Caseira')
restaurante_pizza = Restaurante('Pizza', 'Pizza')
restaurante_tomi = Restaurante('Tomi', 'Comida Japonesa')
restaurante_burger = Restaurante('Burger', 'Hamburgueria')

restaurante_praca.receber_avaliacao('João', 5)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Leandro', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()