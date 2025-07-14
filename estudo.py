import abc

class Conta(abc.ABC):

    def __init__(self, agencia , conta , saldo= 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractclassmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor):
        self.saldo += valor 
        self.detalhe(f'DEPÓSITO {valor}')   
        

    def detalhe(self, msg= ' '):
        print(f"O seu saldo {self.saldo}  {msg}")
        print("--"*10)    

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r} , {self.conta!r} , {self.saldo!r})'
        return f'{class_name} , {attrs}'


class ContaPoupanca(Conta):
    print("-=-" * 10)
    def sacar(self, valor):
        pos_saque = self.saldo - valor 
    

        if pos_saque >= 0:
            self.saldo -= valor
            self.detalhe(('Saque feito\n'))   
            return self.saldo
        
        print("Saque negado, saldo insuficeinte")

class ContaCorrente(Conta):

    def __init__(self, agencia , conta , saldo= 0, limite= 0):
        super().__init__(agencia, conta , saldo)
        self.limite = limite 

    def sacar(self, valor):
        pos_saque = self.saldo - valor 
        limite_max = -self.limite

        if pos_saque >= limite_max:
            self.saldo -= valor
            self.detalhe(('Saque feito'))   
            return self.saldo
        
        print(f"Saque negado, saldo insuficeinte seu limite{self.limite}")

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r} , {self.conta!r} , {self.saldo!r} , {self.limite!r})'
        return f'{class_name} , {attrs}'
        

if __name__ == '__main__':
    cp1 = ContaPoupanca(123,333, 100 )
    cp1.sacar(1)
    cp1.depositar(9)
    cp1.sacar(18)
    print("##")
    cc1 = ContaCorrente(100,333, 0 , 10 )
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(10)
    cc1.sacar(1)