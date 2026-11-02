from dataclasses import dataclass
from datetime import date


@dataclass
class Hospede:
    nome: str
    cpf: str
    email: str


@dataclass
class Quarto:
    numero: int
    tipo: str
    valor_diaria: float


@dataclass
class Reserva:
    hospede: Hospede
    quarto: Quarto
    data_checkin: date
    data_checkout: date
    possui_cafe_da_manha: bool

    def calcular_total(self):
        total_dias = (self.data_checkout - self.data_checkin).days
        total = total_dias * self.quarto.valor_diaria

        if self.possui_cafe_da_manha:
            total += 50 * total_dias

        return total


def criar_reserva(reserva: Reserva):
    print(
        f"Reserva criada para {reserva.hospede.nome} "
        f"(CPF: {reserva.hospede.cpf})"
    )

    print(
        f"Quarto {reserva.quarto.numero} "
        f"({reserva.quarto.tipo})"
    )

    print(
        f"De {reserva.data_checkin} "
        f"até {reserva.data_checkout}"
    )

    total = reserva.calcular_total()

    print(f"Total a pagar: R$ {total}")