import estudo


class Pessoa():
    def __init__(self, nome = str , idade = int):
        self.nome : str = nome 
        self.idade : int = idade 

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome 

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade 

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r} , {self.idade!r})'
        return f'{class_name} , {attrs}'
    
class Cliente(Pessoa):
    def __init__(self, nome=str, idade=int) -> None:
        super().__init__(nome, idade)   
        self.conta: estudo.Conta | None = None

if __name__ == '__main__':

    c1 = Cliente('CARLOS' , 22)
    c1.conta = estudo.ContaCorrente(111, 222, 0 , 0) 
    print(c1)
    print(c1.conta)