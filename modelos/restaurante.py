class restaurante:
    def __init__(self, nome, categoria):   
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = restaurante('Praça do shushi', 'japones')
restaurante_pizza = restaurante('Pizza do Jao', 'pizzaria')

restaurantes = [restaurante_pizza,restaurante_praca]

print(restaurante_pizza)
print(restaurante_praca)