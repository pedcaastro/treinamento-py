from classes.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)   

    def __str__(self):
        return f'Restaurante: {self._nome}, Categoria: {self.categoria}, Ativo: {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'Restaurante: {restaurante._nome}, Categoria: {restaurante.categoria}, Ativo: {restaurante.ativo}, Média de Avaliação: {restaurante.media_avaliacao:.2f}')

    @property
    def ativo(self):
        return self._ativo

    def alternar_estado(self):
        self._ativo = not self._ativo
        estado = 'Ativo' if self._ativo else 'Inativo'
        print(f'O restaurante {self._nome} agora está {estado}.')

    def receber_avaliacao(self,cliente,nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)
        print(f'O restaurante {self._nome} recebeu uma avaliação de {nota} do cliente {cliente}.')

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        total = sum([avaliacao._nota for avaliacao in self._avaliacao])
        return total / len(self._avaliacao)

restaurante_praca = Restaurante('Praca', 'Comida Caseira')
restaurante_pizza = Restaurante('Pizza', 'Pizza')

Restaurante.listar_restaurantes()