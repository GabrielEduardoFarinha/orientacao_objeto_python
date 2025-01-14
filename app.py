from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_0 = Restaurante('praça do sushi', 'japonesa')
bebida_1 = Bebida('guaravita', 2.00, '300ml')
bebida_1.aplicar_desconto()
prato_1 = Prato('lamen', 49.00, 'Lamen de tonkostu')
prato_1.aplicar_desconto()

restaurante_0.adicionar_no_cardapio(bebida_1)
restaurante_0.adicionar_no_cardapio(prato_1)

def main():
    restaurante_0.exibir_cardapio



if __name__ == '__main__':
    main()