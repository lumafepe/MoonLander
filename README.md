## Enunciado
A NASA precisa da tua ajuda para programar o sistema de aterragem da nova nave espacial.

A nave tem um motor que permite controlar a sua velocidade de descida. O motor tem uma potência que pode ser ajustada para um valor entre 0 e 1.

Para aterrar a nave com sucesso, quando tocar no chão, a sua velocidade deve ser inferior a 1.

Na lua existe uma gravidade muito pequena, que faz com que a nave ganhe 0,05 de velocidade vertical a cada movimento feito.

A nave tem um motor lateral que permite controlar a sua velocidade horizontal, a sua potência pode ser ajustada para um valor entre -1 e 1, acelerando a nave para a esquerda e para a direita respetivamente.

A nave deve aterrar na área de plana para que a missão seja um sucesso!

Deves editar a função `moverNave` no ficheiro `preencher.py` de forma a automatizar a função sem ser necessário interagires com o terminal.

## Input

- pos_x (float): posição horizontal atual da nave
- pos_y (float): posição vertical atual da nave
- velocidade_x (float): velicidade horizontal atual da nave (negativo para a esquerda e positivo para a direita)
- velocidade_y (float): velocidade vertical atual da nave (negativo para cima e positivo para baixo)
- local_aterrar_inicio (int): posição horizontal do início da área de aterragem
- local_aterrar_fim (int): posição horizontal do fim da área de aterragem
- local_aterrar_altura (int): posição vertical da área de aterragem
- gravidade (float): valor da gravidade aplicada à nave em cada movimento

## Output

- (potencia_motor_horizontal,potencia_motor_vertical) (tuplo[float,float]): potência a aplicar ao motor horizontal e vertical respetivamente
- -1 ≤ potencia_motor_horizontal ≤ 1
- 0 ≤ potencia_motor_vertical ≤ 1
