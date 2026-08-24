from flask import Blueprint, jsonify, request
from helpdesk.database import db
from helpdesk.models.chamado import Chamado
from helpdesk.models.usuario import Usuario

chamado_bp = Blueprint('chamado_bp', __name__)
    
    
class ChamadoController:

    @chamado_bp.route('/', methods=['GET'])
    def listar_chamados():
        chamados = ChamadoRepository.consulta_tudo()
        return jsonify([c.to_dict() for c in chamados]), 200
    
    @chamado_bp.route('/<int:id>', methods=['GET'])
    def obter_chamado(id):
        chamado = ChamadoRepository.buscar_por_id(id)
        if not chamado:
            return jsonify({'erro': f'Chamado com ID {id} não encontrado'}), 404
        return jsonify(chamado.to_dict()), 200
    
    @chamado_bp.route('/', methods=['POST'])
    def criar_chamado():
        dados = request.get_json() 
        if not dados.get('titulo') or not dados.get('descricao'):
            return jsonify({'erro': 'Título e descrição são obrigatórios'}), 400
    
        novo_chamado = ChamadoRepository.cadastrar_chamado(dados)
        return jsonify(novo_chamado.to_dict()), 201
    
    @chamado_bp.route('/<int:id>', methods=['PUT'])
    def atualizar_chamado(id):
        dados = request.get_json() 
        chamado_atualizado, erro = ChamadoRepository.atualizar_chamado(id, dados)
    
        if erro:
            status_code = 404 if erro == "Chamado não encontrado" else 400
            return jsonify({'erro': erro}), status_code
    
        return jsonify(chamado_atualizado.to_dict()), 200
    
    @chamado_bp.route('/<int:id>', methods=['DELETE'])
    def deletar_chamado(id):
        removido = ChamadoRepository.excluir_chamado(id)
        if not removido:
            return jsonify({'erro': f'Chamado com ID {id} não encontrado'}), 404
    
        return jsonify({'mensagem': f'Chamado {id} removido com sucesso'}), 200
    
    @chamado_bp.route('/prioridade-alta', methods=['GET'])
    def buscar_prioridade_alta():
        chamados = ChamadoRepository.consulta_prioridade_alta()
        return jsonify([c.to_dict() for c in chamados]), 200
    
    @chamado_bp.route('/abertos', methods=['GET'])
    def buscar_abertos():
        chamados = ChamadoRepository.consulta_chamados_abertos()
        return jsonify([c.to_dict() for c in chamados]), 200
    
    @chamado_bp.route('/estatisticas', methods=['GET'])
    def obter_estatisticas():
        dados_estatisticas = ChamadoRepository.estatisticas_chamados()
        return jsonify(dados_estatisticas), 200


    @staticmethod
    def iniciar_chamado(id):
        chamado = ChamadoRepository.iniciar_chamado(id)
        if not chamado:
            return jsonify({'erro': f'Chamado com ID {id} não encontrado'}), 404
        return jsonify(chamado.to_dict()), 200

    @staticmethod
    def fechar_chamado(id):
        chamado = ChamadoRepository.fechar_chamado(id)
        if not chamado:
            return jsonify({'erro': f'Chamado com ID {id} não encontrado'}), 404
        return jsonify(chamado.to_dict()), 200

    @staticmethod
    def iniciar_chamado(id):
        chamado = ChamadoRepository.iniciar_chamado(id)
        if not chamado:
            return jsonify({'erro': f'Chamado com ID {id} não encontrado'}), 404
        return jsonify(chamado.to_dict()), 200


    @staticmethod
    def consulta_chamados_abertos():
        chamados = ChamadoRepository.consulta_tudo()
        lista_abertos = [c.to_dict() for c in chamados if c.status == "Aberto"]
        return jsonify(lista_abertos), 200

    @staticmethod
    def consulta_prioridade_alta():
        chamados = ChamadoRepository.consulta_tudo()
        lista_alta = [c.to_dict() for c in chamados if c.prioridade == "Alta"]
        return jsonify(lista_alta), 200

