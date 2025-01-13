class restaurante:
    nome =''
    categoria =''
    ativo = False

restaurante_praca = restaurante()
restaurante_praca.nome = 'praça do sushi'
restaurante_praca.categoria = 'japones'
restaurante_pizza = restaurante()

restaurantes = [restaurante_pizza,restaurante_praca]

print(restaurantes)