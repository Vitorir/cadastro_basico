import json

usuarios = []

# Funções para cada funcionalidade
def cadastrar(usuarios):
    nome = input("Digite o nome: ")
    senha = input("Digite senha: ")
    email = input("Digite email: ")

    usuario = {
        "nome": nome,
        "senha": senha,
        "email": email
    }

    usuarios.append(usuario)
    print("Usuario cadastrado com sucesso!")

def visualizar(usuarios):
    for i, usuario in enumerate(usuarios):
        print(f"Usuario de numero {i + 1}")
        print(f"Nome: {usuario['nome']}")
        print(f"Senha: {usuario['senha']}")
        print(f"Email: {usuario['email']}")

def remover(usuarios, indice):
    if 0 <= indice < len(usuarios):
        usuario_removido = usuarios.pop(indice)
        print(f"O usuario {usuario_removido['nome']} foi removido")
    else:
        print("Indice invalido")

def atualizar(usuarios, indice):
    if 0 <= indice < len(usuarios):
        usuario_alterado = usuarios[indice]

        nome = input("Digite nome")
        senha = input("Digite senha")
        email = input("Digite email")
        
        usuario_alterado['nome'] = nome
        usuario_alterado['senha'] = senha
        usuario_alterado['email'] = email
    
    else:
        print("Indice invalido")

def salvar(usuarios):
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo)

while True:
    print("Opções")
    print("1 - Cadastrar")
    print("2 - Visualizar")
    print("3 - Remover")
    print("4 - Atualizar")
    print("5 - Salvar")
    print("6 - Sair")

    opcao = input("Digite  aopcao")

    match opcao:
        case '1':
            cadastrar(usuarios)