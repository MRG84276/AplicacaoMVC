from flask import Blueprint, jsonify, request
from services.chamado_service import ChamadoService

chamado_bp = Blueprint("chamados", __name__)

class ChamadoController:

    @staticmethod
    def listar():
        chamados = ChamadoService.consulta_chamados()
        return jsonify(chamados), 200

    @staticmethod
    def buscar_por_id(id):
        chamado = ChamadoService.buscar_por_id(id)
        if chamado:
            return jsonify(chamado), 200
        return jsonify({'erro': 'Chamado não encontrado'}), 404

    @staticmethod
    def buscar_por_usuario(usuario_id):
        chamados = ChamadoService.buscar_por_usuario(usuario_id)
        return jsonify(chamados), 200

    @staticmethod
    def cadastrar():
        dados = request.get_json(silent=True)
        
        if not dados or 'titulo' not in dados or 'descricao' not in dados:
            return jsonify({'erro': 'Título e descrição são obrigatórios'}), 400

        novo_chamado = ChamadoService.cadastra_chamado(**dados)
        return jsonify(novo_chamado), 201

    @staticmethod
    def atualizar(id):
        dados = request.get_json(silent=True)
        if not dados:
            return jsonify({'erro': 'Dados não fornecidos'}), 400

        chamado_atualizado = ChamadoService.atualiza_chamado(id, **dados)
        if chamado_atualizado:
            return jsonify(chamado_atualizado), 200
        return jsonify({'erro': 'Chamado não encontrado'}), 404

    @staticmethod
    def excluir(id):
        sucesso = ChamadoService.exclui_chamado(id)
        if sucesso:
            return jsonify({'mensagem': 'Chamado excluído com sucesso'}), 200
        return jsonify({'erro': 'Chamado não encontrado'}), 404

    @staticmethod
    def atribuir_tecnico(id):
        dados = request.get_json(silent=True) or {}
        tecnico = dados.get('tecnico')
        
        if not tecnico:
            return jsonify({'erro': 'Nome do técnico é obrigatório'}), 400

        chamado = ChamadoService.atribuir_tecnico(id, tecnico)
        if chamado:
            return jsonify(chamado), 200
        return jsonify({'erro': 'Chamado não encontrado'}), 404

    @staticmethod
    def iniciar(id):
        chamado = ChamadoService.iniciar_chamado(id)
        if chamado:
            return jsonify(chamado), 200
        return jsonify({'erro': 'Chamado não encontrado'}), 404

    @staticmethod
    def fechar(id):
        chamado = ChamadoService.fechar_chamado(id)
        if chamado:
            return jsonify(chamado), 200
        return jsonify({'erro': 'Chamado não encontrado'}), 404

    @staticmethod
    def obter_estatisticas():
        estatisticas = ChamadoService.obter_estatisticas()
        return jsonify(estatisticas), 200
