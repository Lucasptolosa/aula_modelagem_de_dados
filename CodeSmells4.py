from abc import ABC, abstractmethod


class Transporte(ABC):
    @abstractmethod
    def calcular_frete(self, distancia):
        pass


class Moto(Transporte):
    def calcular_frete(self, distancia):
        return distancia * 2.0


class Carro(Transporte):
    def calcular_frete(self, distancia):
        return distancia * 3.5 + 10.0


class Caminhao(Transporte):
    def calcular_frete(self, distancia):
        return distancia * 8.0 + 50.0


class Bicicleta(Transporte):
    def calcular_frete(self, distancia):
        return distancia * 1.0


class CalculadoraDeFrete:
    def __init__(self):
        self._transportes = {
            "MOTO": Moto(),
            "CARRO": Carro(),
            "CAMINHAO": Caminhao(),
            "BICICLETA": Bicicleta()
        }

    def calcular_frete(self, tipo_transporte, distancia):
        transporte = self._transportes.get(tipo_transporte)

        if transporte is None:
            raise ValueError("Tipo de transporte desconhecido")

        return transporte.calcular_frete(distancia)