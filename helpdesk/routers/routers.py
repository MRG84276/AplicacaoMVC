from flask import Blueprint

from controllers.controllers import UsuarioController

usuario_bp = Blueprint("usuario_bp", __name__)

usuario_bp.add_url_rule('/', view_func=UsuarioController.index, methods=['GET'])
usuario_bp.add_url_rule('/usuarios', view_func=UsuarioController.listar, methods=['GET'])
usuario_bp.add_url_rule('/usuarios', view_func=UsuarioController.cadastrar, methods=['POST'])
usuario_bp.add_url_rule('/usuarios/<int:id>', view_func=UsuarioController.atualizar, methods=['PUT'])
usuario_bp.add_url_rule('/usuarios/<int:id>', view_func=UsuarioController.excluir, methods=['DELETE'])
usuario_bp.add_url_rule('/usuarios/<int:id>/ativar', view_func=UsuarioController.ativar, methods=['POST'])
usuario_bp.add_url_rule('/usuarios/<int:id>/desativar', view_func=UsuarioController.desativar, methods=['POST'])