from helpdesk.repositories.chamado_repository import ChamadoRepository
from helpdesk.repositories.usuario_repository import UsuarioRepository


class ChamadoService:

    @staticmethod
    def consulta_chamados():
        chamados = ChamadoRepository.consulta_tudo()
        return [chamado.to_dict() for chamado in chamados]

    @staticmethod
    def buscar_por_id(id: int):
        chamado = ChamadoRepository.buscar_por_id(id)
        return chamado.to_dict() if chamado else None

    @staticmethod
    def buscar_por_usuario(usuario_id: int):
        chamados = ChamadoRepository.buscar_por_usuario(usuario_id)
        return [chamado.to_dict() for chamado in chamados]

    @staticmethod
    def cadastra_chamado(**kwargs):
        novo_chamado = ChamadoRepository.cadastrar_chamado(kwargs)
        return novo_chamado.to_dict() if novo_chamado else None

    @staticmethod
    def atualiza_chamado(id: int, **kwargs):
        chamado_atualizado = ChamadoRepository.atualizar_chamado(id, kwargs)
        return chamado_atualizado.to_dict() if chamado_atualizado else None

    @staticmethod
    def exclui_chamado(id: int):
        return ChamadoRepository.excluir_chamado(id)

    @staticmethod
    def atribuir_tecnico(id: int, tecnico: str):
        chamado = ChamadoRepository.atribuir_tecnico(id, tecnico)
        return chamado.to_dict() if chamado else None

    @staticmethod
    def inicia_chamado(id: int):
        chamado = ChamadoRepository.iniciar_chamado(id)
        return chamado.to_dict() if chamado else None

    @staticmethod
    def fechar_chamado(id: int):
        chamado = ChamadoRepository.fechar_chamado(id)
        return chamado.to_dict() if chamado else None

    @staticmethod
    def consulta_chamados_abertos():
        chamados = ChamadoRepository.consulta_tudo()
        return [c.to_dict() for c in chamados if c.status == "Aberto"]

    @staticmethod
    def consulta_prioridade_alta():
        chamados = ChamadoRepository.consulta_tudo()
        return [c.to_dict() for c in chamados if c.prioridade == "Alta"]

    @staticmethod
    def obter_estatisticas():
        todos_usuarios = UsuarioRepository.consulta_tudo()
        todos_chamados = ChamadoRepository.consulta_tudo()

        abertos = 0
        em_atendimento = 0
        encerrados = 0

        for c in todos_chamados:
         
            status = str(c.status).lower()

            if status == "aberto":
                abertos += 1
            elif status == "em atendimento":
                em_atendimento += 1
            elif status == "encerrado":
                encerrados += 1

        return {
            "usuarios": len(todos_usuarios),
            "chamados": len(todos_chamados),
            "abertos": abertos,
            "em_atendimento": em_atendimento,
            "encerrados": encerrados
        }
