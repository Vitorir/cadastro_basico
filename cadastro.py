import json

# função para cadastro
def cadastrar_usuario(usuarios):
    nome = input("Digite seu nome: ")
    idade = input("Digite seu idade: ")
    email = input("Digite seu email: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)
    print("Usuario cadastrado com sucesso!\n")

# função para visualizar
def listar_usuarios(usuarios):
    for i, usuario in enumerate(usuarios):
        print(f"Usuario {i + 1}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Email: {usuario['email']}\n")


# função para remover
def remover_usuario(usuarios, indice):
    if 0 <= indice <= len(usuarios):
        usuario_removido = usuarios.pop(indice)
        print(f"\nO usuario {usuario_removido['nome']} foi removido! ")
    else:
        print("Indice inválido")

# Função para atualizar
def atualizar_usuario(usuarios, indice):
    if 0 <= indice < len(usuarios):
        usuario = usuarios[indice]
        print(f"Atualizando o usuário - {usuario['nome']}")
        nome = input("Digite o nome: ")
        idade = input("Idade")
        email = input("Email: ")

        usuario['nome'] = nome
        usuario['idade'] = idade
        usuario['email'] = email

        print(f"Usuario {usuario['nome']} atualizado com sucesso!")
    else:
        print("Indice invalido")

# Função para salvar
def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo)
    


# Lista de usuarios
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


    opcao = input("Escolha uma opcao\n")

    match opcao:
        case '1':
            cadastrar_usuario(usuarios)
        case '2':
            indice = int(input("\nDigite o numero do usuario que quer excluir"))
            remover_usuario(usuarios, indice - 1)
        case '3':
            listar_usuarios(usuarios)
        case '4':
            indice = int(input("Digite o numero do usuario: "))
            atualizar_usuario(usuarios, indice)
        case '5':
            salvar_usuarios(usuarios)
        case '6':
            print("Saindo do programa...")
            break
        case _:
            print("Opção invalida")