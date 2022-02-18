class Estado:
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades
        
    def getPopulacaoTotal(self):
        total = 0
        for cidade in self.cidades:
            total += cidade.getPopulacao()
        return total

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
    def getPopulacao(self):
        return self.populacao
    

cidadesCE = [Cidade('Icó', 58000), Cidade('Ipaumirim', 14000), Cidade('Fortaleza', 2703391)]
estado1 = Estado('Ceará', 'CE', cidadesCE)

cidadesPB = [Cidade('Cajazeiras', 62000), Cidade('João Pessoa', 817000), Cidade('Patos', 108000)]
estado2 = Estado('Paraíba', 'PB', cidadesPB)

cidadesSP = [Cidade('Taboão Da Serra', 293652), Cidade('São Paulo', 11253503), Cidade('São José Dos Campos', 729737)]
estado3 = Estado('São Paulo', 'SP', cidadesSP)

print('A população do estado %s é: %d pessoas' %(estado1.nome, estado1.getPopulacaoTotal()))
print('A população do estado %s é: %d pessoas' %(estado2.nome, estado2.getPopulacaoTotal()))
print('A população do estado %s é: %d pessoas' %(estado3.nome, estado3.getPopulacaoTotal()))