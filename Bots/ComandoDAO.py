import DAO
import Comando

class ComandoDAO(DAO):

    def __init__(self, url):
        super().__init__(url)

    def add(self, codigo: int, comando: Comando):
            self.cache[codigo] = comando

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
