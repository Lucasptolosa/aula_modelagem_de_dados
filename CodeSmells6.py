class ProcessadorFinanceiro:
    TAXA_CREDITO = 0.05
    TAXA_DEBITO = 0.02

    def _validar_valor(self, valor):
        return valor > 0

    def _calcular_valor_com_taxa(self, valor, taxa):
        return valor * (1 + taxa)

    def _processar_pagamento(self, valor, taxa, tipo):
        if not self._validar_valor(valor):
            print("Valor inválido")
            return

        valor_com_taxa = self._calcular_valor_com_taxa(valor, taxa)
        print(f"Processando {tipo}: R$ {valor_com_taxa}")

    def processar_pagamento_credito(self, valor):
        self._processar_pagamento(
            valor, self.TAXA_CREDITO, "crédito"
        )

    def processar_pagamento_debito(self, valor):
        self._processar_pagamento(
            valor, self.TAXA_DEBITO, "débito"
        )