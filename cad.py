import json
# 1. Listar funções 1 - cadastrar | 2 - visualizar | 3 - remover
# 2. Criar Interface

usuarios = []

# funçao cadastro
def cadastrar(usuarios):
    nome = input("Digite nome: ")
    senha = input("Digite senha: ")
    email = input("Digite email: ")

    usuario = {
        "nome": nome,
        "senha": senha,
        "email": email
    }

    usuarios.append(usuario)
    print("\nUsuario cadastrado com sucesso!")

# função para visualizar
def visualizar(usuarios):
    for i, usuario in enumerate(usuarios):
        print(f"\nUsuario de numero {i}")
        print(f"Nome: {usuario['nome']}")
        print(f"Senha: {usuario['senha']}")
        print(f"Email: {usuario['email']}\n")

# função para remover
def remover(usuarios, indice):
    if 0 <= indice < len(usuarios):
        usuario_removido = usuarios.pop(indice)
        print(f"O usuario {usuario_removido['nome']} foi removido!\n")
    else:
        print("Indice invalido")

# função para atualizar
def atualizar(usuarios, indice):
    if 0 <= indice <= len(usuarios):
        usuario_removido = usuarios[indice]
        print(f"Atualizando o usuario {usuario_removido['nome']}")

        nome = input("Digite nome: ")
        senha = input("Digite senha: ")
        email = input("Digite email: ")

        usuario_removido['nome'] = nome
        usuario_removido['senha'] = senha
        usuario_removido['email'] = email

    else:
        print(f"Indice invalido")


# função para salvar
def salvar(usuarios):
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo)


# laço
while True:
    print("Opções")
    print("1 - Cadastrar usuario")
    print("2 - Remover usuario")
    print("3 - Visualizar usuarios")
    print("4 - Salvar")
    print("5 - Sair")

    opcao = input("Digite a opção: ")

    match opcao:
        case '1':
            cadastrar(usuarios)
        case '2':
            indice = int(input("Digite o numero do usuario: "))
            remover(usuarios, indice)
        case '3':
            visualizar(usuarios)
        case '4':
            salvar(usuarios)
        case '5':
            print("Saindo...")
            break
