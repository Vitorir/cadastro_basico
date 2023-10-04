import json

# função para cadastro
def cadastrar_usuario(usuarios):
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu email: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!\n")

# função para visualizar
def listar_usuarios(usuarios):
    for i, usuario in enumerate(usuarios):
        print(f"Usuário {i + 1}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Email: {usuario['email']}\n")

# função para remover
def remover_usuario(usuarios, indice):
    if 0 <= indice < len(usuarios):
        usuario_removido = usuarios.pop(indice)
        print(f"O usuário {usuario_removido['nome']} foi removido!")
    else:
        print("Índice inválido")

# Função para atualizar
def atualizar_usuario(usuarios, indice):
    if 0 <= indice < len(usuarios):
        usuario = usuarios[indice]
        print(f"Atualizando o usuário - {usuario['nome']}")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        email = input("Digite o email: ")

        usuario['nome'] = nome
        usuario['idade'] = idade
        usuario['email'] = email

        print(f"Usuário {usuario['nome']} atualizado com sucesso!")
    else:
        print("Índice inválido")

# Função para salvar
def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo)

# Lista de usuários
usuarios = []

# interface
while True:
    print("Opções")
    print("1 - Cadastrar usuário")
    print("2 - Remover usuário")
    print("3 - Listar usuários")
    print("4 - Atualizar")
    print("5 - Salvar")
    print("6 - Sair\n")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_usuario(usuarios)
    elif opcao == '2':
        indice = int(input("\nDigite o número do usuário que quer excluir: ")) - 1
        remover_usuario(usuarios, indice)
    elif opcao == '3':
        listar_usuarios(usuarios)
    elif opcao == '4':
        indice = int(input("Digite o número do usuário: "))
        atualizar_usuario(usuarios, indice - 1)
    elif opcao == '5':
        salvar_usuarios(usuarios)
    elif opcao == '6':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida")
