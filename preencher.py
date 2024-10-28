def moverNave(pos_x: float, pos_y: float, velocidade_x: float,
              velocidade_y: float, local_aterrar_inicio: int,
              local_aterrar_fim: int, local_aterrar_altura: int,
              gravidade: float) -> tuple[float, float]:
    """
        A posições horizontais são relativas ao lado esquerdo da janela, a posições verticais são relativas ao teto da janela.
        A velocidade máxima com que a nave pode aterrar é de 0.99, qualquer valor acima disso é considerado aterragem falhada.
        

    Argumentos:
        pos_x (float): posição horizontal
        pos_y (float): altura da nave em relação ao teto
        velocidade_x (float): velicidade horizontal da nave (negativo para a esquerda e positivo para a direita)
        velocidade_y (float): velocidade vertical da nave (negativo para cima e positivo para baixo)
        local_aterrar_inicio (int): posição horizontal do início da área de aterragem
        local_aterrar_fim (int): posição horizontal do fim da área de aterragem
        local_aterrar_altura (int): posição vertical da área de aterragem
        gravidade (float): valor da gravidade aplicada à nave

    Returna:
        tuplo[float,float]: retorna um tuplo com os valores de quanto aumentar/diminuar a velocidade horizontal e vertical da nave
        velocidade horizontal: [-1,1]
        velocidade vertical: [0,1]
    """
    trust_x, trust_y = list(
        map(float,
            input("velocidade horizonal,vertical:").split(',')))

    return trust_x, trust_y

