# 5) Utilizando a classe Televisão modificada no exercício anterior, crie duas instâncias (objetos), 
# especificando o valor de min e max por nome.

class Televisao:
    def __init__(self, canalInicial, min=2, max=14):  # parametros no construtor
        self.ligada = False
        self.canal = canalInicial
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if(self.canal-1 >= self.cmin):
            self.canal -= 1

    def muda_canal_para_cima(self):
        if(self.canal+1 <= self.cmax):
            self.canal += 1

tv1 = Televisao(3)
tv1.cmin = 2
tv1.cmax = 10

tv2 = Televisao(5)
tv2.cmin = 3
tv2.cmax = 7


