class Pais:
    def __init__(self, nome):
        self.nome = nome

    def eh_brasil(self):
        return self.nome == "Brasil"


class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

    def eh_brasileiro(self):
        return self.pais.eh_brasil()


class Endereco:
    def __init__(self, rua, estado):
        self.rua = rua
        self.estado = estado

    def eh_internacional(self):
        return not self.estado.eh_brasileiro()


class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def possui_endereco_internacional(self):
        return self.endereco.eh_internacional()


class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def possui_frete_internacional(self):
        return self.cliente.possui_endereco_internacional()


def verificar_frete_internacional(pedido):
    if pedido.possui_frete_internacional():
        print("Sujeito à taxa de importação.")
    else:
        print("Frete nacional padrão.")