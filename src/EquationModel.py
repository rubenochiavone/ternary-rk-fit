from abc import ABCMeta, abstractmethod

class EquationModel:
    __metaclass__ = ABCMeta

    @abstractmethod
    def model(self, params, data, verbose = False) : res

    @abstractmethod
    def residual(self, params, data, y, verbose = False) : res
