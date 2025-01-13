from modelos.restaurante import Restaurante

restaurante_0 = Restaurante('praça do sushi', 'japonesa')
restaurante_1 = Restaurante('pizza do jao', 'pizzaria')
restaurante_2 = Restaurante('Quentinhas do PP', 'popular')

restaurante_1.alterar_estado()

def main():
    Restaurante.listar_restaurantes()



if __name__ == '__main__':
    main()