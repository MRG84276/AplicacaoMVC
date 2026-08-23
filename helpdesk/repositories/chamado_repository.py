from helpdesk.database import db
from helpdesk.models.chamado import Chamado


class ChamadoRepository:

    @staticmethod
    def consulta_tudo():
        return Chamado.query.all()

    @staticmethod
    def buscar_por_id(chamado_id: int):
        return Chamado.query.get(chamado_id)

    @staticmethod
    def buscar_por_usuario(usuario_id: int):
        return Chamado.query.filter_by(usuario_id=usuario_id).all()

    @staticmethod
    def cadastrar_chamado(dados: dict):
        novo_chamado = Chamado(
            titulo=dados.get('titulo'),
            descricao=dados.get('descricao'),
            prioridade=dados.get('prioridade', 'Média'),
            status=dados.get('status', 'Aberto'),
            tecnico=dados.get('tecnico'),
            usuario_id=dados.get('usuario_id')
        )
        db.session.add(novo_chamado)
        db.session.commit()
        return novo_chamado

    @staticmethod
    def atualizar_chamado(chamado_id: int, dados: dict):
        chamado = Chamado.query.get(chamado_id)
        if not chamado:
            return None, "Chamado não encontrado."

        if 'usuario_id' in dados:
            if not Usuario.query.get(dados['usuario_id']):
                return None, f"Usuário com ID {dados['usuario_id']} não encontrado."
            chamado.usuario_id = dados['usuario_id']
            if 'titulo' in dados:
                chamado.titulo = dados['titulo']
            if 'descricao' in dados:
                chamado.descricao = dados['descricao']
            if 'prioridade' in dados:
                chamado.prioridade = dados['prioridade']
            if 'status' in dados:
                chamado.status = dados['status']
            if 'tecnico' in dados:
                chamado.tecnico = dados['tecnico']
           

        db.session.commit()
        return chamado, None
        
    @staticmethod
    def excluir_chamado(chamado_id: int) -> bool:
        chamado = Chamado.query.get(chamado_id)
        if chamado:
            db.session.delete(chamado)
            db.session.commit()
            return True
        return False

    @staticmethod
    def atribuir_tecnico(chamado_id: int, nome_tecnico: str):
        chamado = Chamado.query.get(chamado_id)
        if chamado:
            chamado.tecnico = nome_tecnico
            db.session.commit()
        return chamado

    @staticmethod
    def iniciar_chamado(chamado_id: int):
        chamado = Chamado.query.get(chamado_id)
        if chamado:
            chamado.status = 'Em atendimento'
            db.session.commit()
        return chamado

    @staticmethod
    def fechar_chamado(chamado_id: int):
        chamado = Chamado.query.get(chamado_id)
        if chamado:
            chamado.status = 'Encerrado'
            db.session.commit()
        return chamado

    @staticmethod
    def consulta_prioridade_alta():
        return Chamado.query.filter_by(prioridade='Alta').all()

    @staticmethod
    def consulta_chamados_abertos():
        return Chamado.query.filter_by(status='Aberto').all()


    @staticmethod
    def estatisticas_chamados():
        return Chamado.query.all()

        total = len(chamados)
        abertos = sum(1 for c in chamados if c.status == 'Aberto')
        em_atendimento = sum(1 for c in chamados if c.status == 'Em atendimento')
        encerrados = sum(1 for c in chamados if c.status == 'Encerrado')
        alta_prioridade = sum(1 for c in chamados if c.prioridade == 'Alta')

        return {
            'total_geral': total,
            'abertos': abertos,
            'em_atendimento': em_atendimento,
            'encerrados': encerrados,
            'alta_prioridade': alta_prioridade
        }
