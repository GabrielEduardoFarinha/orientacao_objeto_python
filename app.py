from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_0 = Restaurante('praça do sushi', 'japonesa')
bebida_1 = Bebida('guaravita', 2.00, '300ml')
prato_1 = Prato('lamen', 49.00, 'Lamen de tonkostu')


def main():
    print(prato_1)
    print(bebida_1)



if __name__ == '__main__':
    main()