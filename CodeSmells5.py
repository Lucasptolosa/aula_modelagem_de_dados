from dataclasses import dataclass
from xml.etree.ElementTree import Element, SubElement, tostring


@dataclass
class Produto:
    id_produto: int
    nome: str
    preco: float


class CalculadoraDeImposto:
    TAXA_IMPOSTO = 0.15

    def calcular_preco_com_imposto(self, produto: Produto):
        return produto.preco * (1 + self.TAXA_IMPOSTO)


class RepositorioProduto:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar_no_banco_de_dados(self, produto: Produto):
        sql = """
            INSERT INTO produtos (id, nome, preco)
            VALUES (?, ?, ?)
        """

        parametros = (
            produto.id_produto,
            produto.nome,
            produto.preco
        )

        with self.conexao:
            self.conexao.execute(sql, parametros)


class ExportadorProdutoXML:
    def exportar_para_xml(self, produto: Produto):
        elemento = Element("produto")

        SubElement(elemento, "id").text = str(produto.id_produto)
        SubElement(elemento, "nome").text = produto.nome
        SubElement(elemento, "preco").text = str(produto.preco)

        return tostring(elemento, encoding="unicode")