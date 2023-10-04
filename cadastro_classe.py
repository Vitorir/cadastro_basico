class Cadastro:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item} foi adicionado ao cadastro.")

    def listar_itens(self):
        if not self.itens:
            print("O cadastro está vazio.")
        else:
            print("Itens cadastrados:")
            for item in self.itens:
                print(item)

    def salvar_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for item in self.itens:
                arquivo.write(item + '\n')

    def carregar_de_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                self.itens = [linha.strip() for linha in arquivo.readlines()]
        except FileNotFoundError:
            pass

def main():
    cadastro = Cadastro()
    nome_arquivo = "cadastro.txt"
    cadastro.carregar_de_arquivo(nome_arquivo)

    while True:
        print("\nMenu:")
        print("1. Adicionar Item")
        print("2. Listar Itens")
        print("3. Salvar e Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            item = input("Digite o item a ser cadastrado: ")
            cadastro.adicionar_item(item)
        elif escolha == "2":
            cadastro.listar_itens()
        elif escolha == "3":
            cadastro.salvar_em_arquivo(nome_arquivo)
            print("Dados salvos. Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
