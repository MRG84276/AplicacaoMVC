from flask import Blueprint, jsonify, request
from helpdesk.database import db
from helpdesk.models.chamado import Chamado
from helpdesk.models.usuario import Usuario

chamado_bp = Blueprint('chamado_bp', __name__)

@chamado_bp.route('/', methods=['GET'])
def listar_chamados():
    chamados = Chamado.get_all()
    return jsonify([c.to_dict() for c in chamados]), 200

@chamado_bp.route('/<int:id>', methods=['GET'])
def obter_chamado(id):
    chamado = Chamado.get(id)
    return jsonify(chamado.to_dict()), 200

@chamado_bp.route('/', methods=['POST'])
def criar_chamado():
    dados = request.get_json()
    if not dados or not dados.get('titulo') or not dados.get('descricao'):
        return jsonify({'erro': 'Título e descrição são obrigatórios.'}), 400
    novo_chamado = ChamadoRepository.cadastrar_chamado(dados)

    if not novo_chamado:
        return jsonify({'erro': 'Não foi possível criar o chamado. Verifique os dados informados.'}), 400
    return jsonify(novo_chamado.to_dict()), 201

@chamado_bp.route('/<int:id>', methods=['PUT'])
def atualizar_chamado(id):
    dados = request.get_json()
    
    chamado_atualizado = ChamadoRepository.atualizar_chamado(id, dados)

    if not chamado_atualizado:
        return jsonify({'erro': f'Chamado com ID {id} não encontrado.'}), 404

    return jsonify(chamado_atualizado.to_dict()), 200


@chamado_bp.route('/<int:id>', methods=['DELETE'])
def deletar_chamado(id):
    chamado = Chamado.get_or_404(id)
    removido = ChamadoRepository.excluir_chamado(id)

    if not removido:
        return jsonify({'erro': f'Chamado com ID {id} não encontrado para exclusão.'}), 404

    return jsonify({'mensagem': f'Chamado {id} removido com sucesso.'}), 200

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
    dados_estatisticas = ChamadoRepository.get_estatisticas_chamados()

    return jsonify(dados_estatisticas), 200
