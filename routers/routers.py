from flask import Blueprint

from controllers.usuario_controller import UsuarioController
from controllers.chamado_controller import ChamadoController

usuario_bp = Blueprint("usuario_bp", __name__)
chamado_bp = Blueprint("chamado_bp", __name__)

usuario_bp.add_url_rule('/', view_func=UsuarioController.index, methods=['GET'])
usuario_bp.add_url_rule('/usuarios', view_func=UsuarioController.listar, methods=['GET'])
usuario_bp.add_url_rule('/usuarios', view_func=UsuarioController.cadastrar, methods=['POST'])
usuario_bp.add_url_rule('/usuarios/<int:id>', view_func=UsuarioController.atualizar, methods=['PUT'])
usuario_bp.add_url_rule('/usuarios/<int:id>', view_func=UsuarioController.excluir, methods=['DELETE'])
usuario_bp.add_url_rule('/usuarios/<int:id>/ativar', view_func=UsuarioController.ativar, methods=['POST'])
usuario_bp.add_url_rule('/usuarios/<int:id>/desativar', view_func=UsuarioController.desativar, methods=['POST'])

chamado_bp.add_url_rule('/chamados', view_func=ChamadoController.listar, methods=['GET'])
chamado_bp.add_url_rule('/chamados/<int:id>', view_func=ChamadoController.buscar_por_id, methods=['GET'])
chamado_bp.add_url_rule('/chamados', view_func=ChamadoController.cadastrar, methods=['POST'])
chamado_bp.add_url_rule('/chamados/<int:id>', view_func=ChamadoController.atualizar, methods=['PUT'])
chamado_bp.add_url_rule('/chamados/<int:id>', view_func=ChamadoController.excluir, methods=['DELETE'])
chamado_bp.add_url_rule('/chamados/<int:id>/tecnico', view_func=ChamadoController.atribuir_tecnico, methods=['POST', 'PATCH'])
chamado_bp.add_url_rule('/chamados/<int:id>/fechar', view_func=ChamadoController.fechar, methods=['POST'])