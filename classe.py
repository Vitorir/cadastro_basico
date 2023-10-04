import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
db = SQLAlchemy(app)

# Classe Usuario mapeada para a tabela do banco de dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.String(3), nullable=False)
    email = db.Column(db.String(255), nullable=False)

# Cria o banco de dados
with app.app_context():
    db.create_all()

# Função para salvar usuários no banco de dados
def salvar_usuarios(usuarios):
    for usuario in usuarios:
        novo_usuario = Usuario(nome=usuario['nome'], idade=usuario['idade'], email=usuario['email'])
        db.session.add(novo_usuario)
    db.session.commit()

# Função para listar usuários do banco de dados
def listar_usuarios():
    usuarios = Usuario.query.all()
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append({
            "nome": usuario.nome,
            "idade": usuario.idade,
            "email": usuario.email
        })
    return lista_usuarios

# Função para cadastrar usuário no banco de dados
def cadastrar_usuario(nome, idade, email):
    novo_usuario = Usuario(nome=nome, idade=idade, email=email)
    db.session.add(novo_usuario)
    db.session.commit()

# Função para remover usuário do banco de dados
def remover_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    return False

# Função para atualizar usuário no banco de dados
def atualizar_usuario(id, nome, idade, email):
    usuario = Usuario.query.get(id)
    if usuario:
        usuario.nome = nome
        usuario.idade = idade
        usuario.email = email
        db.session.commit()
        return True
    return False

# Rota para listar usuários
@app.route('/usuarios', methods=['GET'])
def listar():
    usuarios = listar_usuarios()
    return jsonify(usuarios)

# Rota para cadastrar usuário
@app.route('/usuarios', methods=['POST'])
def cadastrar():
    data = request.get_json()
    nome = data['nome']
    idade = data['idade']
    email = data['email']
    cadastrar_usuario(nome, idade, email)
    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"})

# Rota para remover usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def remover(id):
    if remover_usuario(id):
        return jsonify({"mensagem": "Usuário removido com sucesso!"})
    return jsonify({"erro": "Usuário não encontrado!"}), 404

# Rota para atualizar usuário
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.get_json()
    nome = data['nome']
    idade = data['idade']
    email = data['email']
    if atualizar_usuario(id, nome, idade, email):
        return jsonify({"mensagem": "Usuário atualizado com sucesso!"})
    return jsonify({"erro": "Usuário não encontrado!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
