from flask import Blueprint, jsonify, request
from helpdesk.database import db
from helpdesk.models.chamado import Chamado
from helpdesk.models.usuario import Usuario

chamado_bp = Blueprint('chamado_bp', __name__)

@chamado_bp.route('/', methods=['GET'])
def listar_chamados():
    chamados = Chamado.query.all()
    return jsonify([c.to_dict() for c in chamados]), 200

@chamado_bp.route('/<int:id>', methods=['GET'])
def obter_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    return jsonify(chamado.to_dict()), 200

@chamado_bp.route('/', methods=['POST'])
def criar_chamado():
    dados = request.get_json()
    if not dados or not dados.get('titulo') or not dados.get('descricao'):
        return jsonify({'erro': 'Título e descrição são obrigatórios.'}), 400

    novo_chamado = Chamado(
        titulo=dados.get('titulo'),
        descricao=dados.get('descricao'),
        prioridade=dados.get('prioridade', 'Média'),
        tecnico=dados.get('tecnico'),
        usuario_id=dados.get('usuario_id')
    )
    db.session.add(novo_chamado)
    db.session.commit()
    return jsonify(novo_chamado.to_dict()), 201

@chamado_bp.route('/<int:id>', methods=['PUT'])
def atualizar_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    dados = request.get_json()

    chamado.titulo = dados.get('titulo', chamado.titulo)
    chamado.descricao = dados.get('descricao', chamado.descricao)
    chamado.prioridade = dados.get('prioridade', chamado.prioridade)
    chamado.status = dados.get('status', chamado.status)
    chamado.tecnico = dados.get('tecnico', chamado.tecnico)

    db.session.commit()
    return jsonify(chamado.to_dict()), 200


@chamado_bp.route('/<int:id>', methods=['DELETE'])
def deletar_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    db.session.delete(chamado)
    db.session.commit()
    return jsonify({'mensagem': f'Chamado {id} removido com sucesso.'}), 200

@chamado_bp.route('/estatisticas', methods=['GET'])
def obter_estatisticas():
    total_chamados = Chamado.query.count()
    abertos = Chamado.query.filter_by(status='Aberto').count()
    em_andamento = Chamado.query.filter_by(status='Em Andamento').count()
    fechados = Chamado.query.filter_by(status='Fechado').count()
    total_usuarios = Usuario.query.count()

    return jsonify({
        'total_chamados': total_chamados,
        'status': {
            'abertos': abertos,
            'em_andamento': em_andamento,
            'fechados': fechados
        },
        'total_usuarios': total_usuarios
    }), 200