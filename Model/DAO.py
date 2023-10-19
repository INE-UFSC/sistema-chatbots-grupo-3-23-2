from abc import ABC
import pickle

class DAO(ABC):
    def __init__(self, datasource):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.dump()

    @property
    def datasource(self):
        return self.__datasource

    @datasource.setter
    def datasource(self, datasource):
        self.__datasource = datasource

    @property
    def cache(self):
        return self.__cache


    def dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.dump()
        
    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            print("Tentativa de acessar objeto inexistente realizada!")

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.dump()
        except KeyError:
            print("Tentativa de excluir objeto inexistente realizada!")

    def get_all(self):
        return self.__cache.values()
    