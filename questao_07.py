# 7) Modifique o método resumo da classe Conta para exibir o nome e o telefone de cada cliente.

class Conta:
    def __init__(self, clientes, número, telefone, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.telefone = telefone
        self.deposito(saldo)

    def resumo(self):
        print("N° da conta: %s \nSaldo:%10.2f \nCliente: %s \nTelefone: %s" %(self.número, self.saldo, self.clientes, self.telefone))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\nSaldo: %10.2f\n" % self.saldo)
        
conta1 = Conta('Francisca Joseane', '1.3445-3', '(83) 999517918', 50)
conta1.resumo()