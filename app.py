from modelos.restaurante import Restaurante

restaurante_0 = Restaurante('praça do sushi', 'japonesa')
restaurante_1 = Restaurante('pizza do jao', 'pizzaria')
restaurante_2 = Restaurante('Quentinhas do PP', 'popular')

restaurante_0.receber_avaliacao('Junin', 10)
restaurante_0.receber_avaliacao('', 9)
restaurante_0.receber_avaliacao('Christakis', 2)

def main():
    Restaurante.listar_restaurantes()



if __name__ == '__main__':
    main()