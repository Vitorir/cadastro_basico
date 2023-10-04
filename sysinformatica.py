class SysInformatica:
    def __init__(self, nome_item, preco_unitario):
        self.nome_item = nome_item
        self.preco_unitario = preco_unitario
        self.quantidade = 0
        self.valor_total = 0.0

    def gerar_fatura(self):
        self.valor_total = self.preco_unitario * self.quantidade

    def adicionar_item(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade
            self.gerar_fatura()
        else:
            print("Quantidade inválida. A quantidade deve ser maior que zero.")

    def remover_item(self, quantidade):
        if quantidade > 0 and quantidade <= self.quantidade:
            self.quantidade -= quantidade
            self.gerar_fatura()
        else:
            print("Quantidade inválida. A quantidade deve ser maior que zero e menor ou igual à quantidade atual.")

    def mostrar_fatura(self):
        print(f"Fatura para o item: {self.nome_item}")
        print(f"Preço Unitário: R${self.preco_unitario:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor Total: R${self.valor_total:.2f}")


# Aplicativo de teste
if __name__ == "__main__":
    item_informatica = SysInformatica("Mouse", 20.0)
    item_informatica.adicionar_item(5)  # Adiciona 5 unidades
    item_informatica.mostrar_fatura()

    item_informatica.remover_item(2)  # Remove 2 unidades
    item_informatica.mostrar_fatura()
