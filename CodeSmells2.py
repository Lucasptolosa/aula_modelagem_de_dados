from dataclasses import dataclass


@dataclass
class Endereco:
    rua: str
    numero: int
    bairro: str
    cidade: str
    estado: str
    cep: str


@dataclass
class Contato:
    ddd: str
    telefone_numero: str


@dataclass
class Funcionario:
    nome: str
    cargo: str
    salario: float
    endereco: Endereco
    contato: Contato

    def exibir_dados(self):
        print(f"Funcionário: {self.nome} - {self.cargo}")
        print(
            f"Contato: ({self.contato.ddd}) "
            f"{self.contato.telefone_numero}"
        )
        print(
            f"Endereço: {self.endereco.rua}, "
            f"{self.endereco.numero} - "
            f"{self.endereco.bairro}, "
            f"{self.endereco.cidade}/{self.endereco.estado} "
            f"- CEP: {self.endereco.cep}"
        )