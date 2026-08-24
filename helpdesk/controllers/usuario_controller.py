from flask import Blueprint, jsonify, request
from helpdesk.database import db
from helpdesk.models.usuario import Usuario
from helpdesk.repositories.usuario_repository import UsuarioRepository

usuario_bp = Blueprint('usuario_bp', __name__)

class UsuarioController:

    @usuario_bp.route('/', methods=['GET'])
    def listar_usuarios():
        usuarios = UsuarioRepository.consulta_tudo()
        return jsonify([u.to_dict() for u in usuarios]), 200
    
    @usuario_bp.route('/', methods=['POST'])
    def criar_usuario():
        dados = request.get_json()
        if not dados.get('nome') or not dados.get('email'):
            return jsonify({'erro': 'Nome e e-mail são obrigatórios.'}), 400
            
        usuario, erro = UsuarioRepository.cadastrar_usuario(dados)
        if not usuario:
            return jsonify({'erro': erro}), 400
    
        return jsonify(usuario.to_dict()), 201
    
    
    @usuario_bp.route('/<int:id>', methods=['GET'])
    def obter_usuario(id):
        usuario = UsuarioRepository.buscar_por_id(id)
        return jsonify(usuario.to_dict()), 200
    
    @usuario_bp.route('/<int:id>', methods=['PUT'])
    def atualizar_usuario(id):
        dados = request.get_json() 
        usuario = UsuarioRepository.atualizar_usuario(id, dados)
    
        if not usuario:
            return jsonify({'erro': f'Usuário com ID {id} não encontrado para atualização.'}), 404
    
        return jsonify(usuario.to_dict()), 200
    
    @usuario_bp.route('/<int:id>', methods=['DELETE'])
    def deletar_usuario(id):
        sucesso, erro = UsuarioRepository.excluir_usuario(id)
        status_code = 404 if erro == "Usuário não encontrado." else 400
        if not sucesso:
            return jsonify({'erro': erro}), status_code
    
        return jsonify({'mensagem': f'Usuário {id} removido com sucesso.'}), 200
        
    @usuario_bp.route('/<int:id>/ativar', methods=['PATCH'])
    def ativar_usuario(id):
        usuario = UsuarioRepository.ativar_usuario(id)
    
        if not usuario:
            return jsonify({'erro': f'Usuário com ID {id} não encontrado.'}), 404
    
        return jsonify(usuario.to_dict()), 200
    
    @usuario_bp.route('/<int:id>/desativar', methods=['PATCH'])
    def desativar_usuario(id):
        usuario = UsuarioRepository.desativar_usuario(id)
    
        if not usuario:
            return jsonify({'erro': f'Usuário com ID {id} não encontrado.'}), 404
    
        return jsonify(usuario.to_dict()), 200
