import DAO
import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, codigo: int, cliente: Cliente):
            self.cache[codigo] = cliente

    def get(self, codigo: int):
        try:
            return self.cache[codigo]
        except KeyError:
            pass

    def remove(self, codigo: int):
        try:
            self.cache.pop(codigo)
            self.dump()
        except KeyError:
            pass
