class PagamentoCartao:
    def processar(self, total):
        print(f"Cobrando R$ {total} no cartão de crédito...")


class PagamentoBoleto:
    def processar(self, total):
        print(f"Gerando boleto no valor de R$ {total}...")


class GerenciadorDeVendas:
    FATOR_DESCONTO_VIP = 0.90
    ARQUIVO_RELATORIO = "relatorio_vendas.txt"

    def __init__(self):
        self._metodos_pagamento = {
            "CARTAO": PagamentoCartao(),
            "BOLETO": PagamentoBoleto(),
        }

    def _calcular_total(self, itens):
        return sum(
            item["preco"] * item["quantidade"]
            for item in itens
        )

    def _aplicar_desconto(self, total, cliente):
        if cliente["tipo"] == "VIP":
            return total * self.FATOR_DESCONTO_VIP
        return total

    def _processar_pagamento(self, metodo_pagamento, total):
        metodo = self._metodos_pagamento.get(metodo_pagamento)

        if metodo is not None:
            metodo.processar(total)

    def _gerar_relatorio(self, cliente, total):
        return (
            f"--- Relatório de Venda ---\n"
            f"Cliente: {cliente['nome']}\n"
            f"Total: R$ {total}\n"
        )

    def _salvar_relatorio(self, relatorio):
        with open(
            self.ARQUIVO_RELATORIO, "a", encoding="utf-8"
        ) as arquivo:
            arquivo.write(relatorio)

    def processar_venda_e_gerar_relatorio(
        self, itens, cliente, metodo_pagamento
    ):
        total = self._calcular_total(itens)
        total = self._aplicar_desconto(total, cliente)

        self._processar_pagamento(metodo_pagamento, total)

        relatorio = self._gerar_relatorio(cliente, total)
        self._salvar_relatorio(relatorio)

        print("Venda processada com sucesso.")