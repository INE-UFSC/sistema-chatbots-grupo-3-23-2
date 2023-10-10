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
        self.datasource = datasource

    @property
    def cache(self):
        return self.__cache


    def dump(self):
        pickle.dump(self.cache, open(self.datasource, 'wb'))

    def load(self):
        self.cache = pickle.load(open(self.datasource, 'rb'))

    def add(self, key, obj):
        self.cache[key] = obj
        self.dump()
        
    def get(self, key):
        try:
            return self.cache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.cache.pop(key)
            self.dump()
        except KeyError:
            pass

    def get_all(self):
        return self.cache.values()
    