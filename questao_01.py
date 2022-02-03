# 1) Adicione os atributos tamanho e marca à classe Televisão. Crie dois objetos Televisão e 
# atribua tamanhos e marcas diferentes. Depois, imprima o valor desses atributos de forma a 
# confirmar a independência dos valores de cada instância (objeto).

class Televisao:
    def __init__(self, tamanho, marca):
           self.ligada = False
           self.canal = 2
           self.tamanho = tamanho
           self.marca = marca
    
    def getTamanho(self):
        return self.tamanho
    def getMarca(self):
        return self.marca
    def muda_canal_para_baixo(self):
        self.canal -= 1
    def muda_canal_para_cima(self):
        self.canal += 1

tv1 = Televisao(50, 'LG')
tv2 = Televisao(32, 'SAMSUNG')

print("O tamanho da primeira televisão é: %d polegadas e a marca é: %s" %(tv1.getTamanho(), tv1.getMarca()))

print("O tamanho da segunda televisão é: %d polegadas e a marca é: %s" %(tv2.getTamanho(), tv2.getMarca()))



