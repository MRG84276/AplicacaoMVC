from flask import Blueprint, jsonify, request
from helpdesk.database import db
from helpdesk.models.usuario import Usuario

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios]), 200

@usuario_bp.route('/', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    novo_usuario = Usuario(
        nome=dados.get('nome'),
        email=dados.get('email'),
        setor=dados.get('setor')
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify(novo_usuario.to_dict()), 201


@usuario_bp.route('/<int:id>', methods=['GET'])
def obter_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_dict()), 200

@usuario_bp.route('/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    dados = request.get_json()

    usuario.nome = dados.get('nome', usuario.nome)
    usuario.email = dados.get('email', usuario.email)
    usuario.setor = dados.get('setor', usuario.setor)
    if 'ativo' in dados:
        usuario.ativo = dados['ativo']

    db.session.commit()
    return jsonify(usuario.to_dict()), 200

@usuario_bp.route('/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    sucesso = UsuarioService.deletar_usuario(id)
    if not sucesso:
        return jsonify({'erro': 'Usuário não encontrado.'}), 404
        
    return jsonify({'mensagem': f'Usuário {id} removido com sucesso.'}), 200
    
