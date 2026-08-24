from helpdesk.controllers.chamado_controller import ChamadoController

usuario_bp = Blueprint("usuario_bp", __name__)
chamado_bp = Blueprint("chamado_bp", __name__)


usuario_bp.add_url_rule('/usuarios', view_func=UsuarioController.listar_usuarios, methods=['GET'])
usuario_bp.add_url_rule('/usuarios', view_func=UsuarioController.criar_usuario, methods=['POST'])
usuario_bp.add_url_rule('/usuarios/<int:id>', view_func=UsuarioController.obter_usuario, methods=['GET'])
usuario_bp.add_url_rule('/usuarios/<int:id>', view_func=UsuarioController.atualizar_usuario, methods=['PUT'])
usuario_bp.add_url_rule('/usuarios/<int:id>', view_func=UsuarioController.deletar_usuario, methods=['DELETE'])
usuario_bp.add_url_rule('/usuarios/<int:id>/ativar', view_func=UsuarioController.ativar_usuario, methods=['PATCH'])
usuario_bp.add_url_rule('/usuarios/<int:id>/desativar', view_func=UsuarioController.desativar_usuario, methods=['PATCH'])


chamado_bp.add_url_rule('/chamados', view_func=ChamadoController.listar_chamados, methods=['GET'])
chamado_bp.add_url_rule('/chamados/abertos', view_func=ChamadoController.buscar_abertos, methods=['GET'])
chamado_bp.add_url_rule('/chamados/prioridade/alta', view_func=ChamadoController.buscar_prioridade_alta, methods=['GET'])
chamado_bp.add_url_rule('/chamados/<int:id>', view_func=ChamadoController.obter_chamado, methods=['GET'])
chamado_bp.add_url_rule('/chamados', view_func=ChamadoController.criar_chamado, methods=['POST'])
chamado_bp.add_url_rule('/chamados/<int:id>', view_func=ChamadoController.atualizar_chamado, methods=['PUT'])
chamado_bp.add_url_rule('/chamados/<int:id>', view_func=ChamadoController.deletar_chamado, methods=['DELETE'])
chamado_bp.add_url_rule('/chamados/<int:id>/fechar', view_func=ChamadoController.fechar_chamado, methods=['PATCH'])
chamado_bp.add_url_rule('/chamados/<int:id>/iniciar', view_func=ChamadoController.iniciar_chamado, methods=['PATCH'])
chamado_bp.add_url_rule('/chamados/abertos', view_func=ChamadoController.consulta_chamados_abertos, methods=['GET'])
chamado_bp.add_url_rule('/chamados/prioridade/alta', view_func=ChamadoController.consulta_prioridade_alta, methods=['GET'])
chamado_bp.add_url_rule('/estatisticas', view_func=ChamadoController.obter_estatisticas, methods=['GET'])
