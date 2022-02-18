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
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\nSaldo: %10.2f\n" % self.saldo)

class ContaEspecial(Conta):
    def __init__(self, clientes, número, telefone, saldo = 0, limite=0):
        Conta.__init__(self, clientes, número, telefone, saldo)
        self.limite = limite
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
               self.saldo -= valor
               self.operações.append(["SAQUE", valor])
               return True
        else:
            print("Saldo insuficiente!")
            return False
    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\nSaldo: %10.2f\n" % self.saldo)
        print("\nTotal disponível para saque: %10.2f\n" %(self.saldo + self.limite))
        print("\nLimite: %10.2f\n" % self.limite)

conta1 = Conta('Francisca Joseane', '1.3445-3', '(83) 999517918', 500)
conta1.resumo()
conta1.saque(1000)
conta1.saque(100)
conta1.extrato()

conta2 = ContaEspecial('Klinsman Jorge', '1.8976-9', '(88) 999590275', 1200, 3000)
conta2.resumo()
conta2.saque(4300)
conta2.saque(100)
conta2.extrato()