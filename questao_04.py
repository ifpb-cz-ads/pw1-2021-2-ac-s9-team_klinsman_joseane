class Televisão:
     def __init__(self, canalInicial, min = 2, max = 14): #parametros no construtor
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

tv=Televisão(5)
for x in range(0,120):
     tv.muda_canal_para_cima()
print(tv.canal)
for x in range(0,120):
     tv.muda_canal_para_baixo()
print(tv.canal)

