import estudo
import estudo2


class Banco():

    def __init__(self , agencias: list[int] | None = None, clientes: list[estudo2.Pessoa] | None = None, contas: list[estudo.Conta] | None = None,):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []


    def _checa_agencia(self, conta):
        if conta in self.agencias:
            print('_checa_agencia' , True)
            return True 
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente' , True)
            return True 
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta' , True)
            return True 
        return False

    def autenticar(self, cliente: estudo2.Pessoa , conta: estudo.Conta):
        return self._checa_agencia(conta) and \
        self._checa_cliente(cliente) and \
        self._checa_conta(conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r} , {self.contas!r} , {self.clientes!r})'
        return f'{class_name} , {attrs}'
    
if __name__ == '__main__':

    c1 = estudo2.Cliente('CARLOS' , 22)
    cc1 = estudo.ContaCorrente(11, 222, 0 , 0) 
    c1.conta = cc1
    banco = Banco()
    banco.clientes.extend([c1]) 
    banco.contas.extend([cc1])
    banco.agencias.extend([222])
    print(banco)

    print(banco.autenticar(c1 , cc1))