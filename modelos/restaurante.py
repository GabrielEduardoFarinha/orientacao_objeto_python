class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):   
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'nome do restaurante'.ljust(25)} | {'categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça do shushi', 'japones')
restaurante_praca.alterar_estado()
restaurante_pizza = Restaurante('Pizza do Jao', 'pizzaria')

Restaurante.listar_restaurantes()