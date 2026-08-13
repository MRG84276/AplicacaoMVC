from repositories.chamado_repository import ChamadoRepository

class ChamadoService:

    @staticmethod
    def consulta_chamados():
        chamados = ChamadoRepository.consulta_tudo()
        return [chamado.to_dict() for chamado in chamados]

    @staticmethod
    def buscar_por_id(chamado_id: int):
        chamado = ChamadoRepository.buscar_por_id(chamado_id)
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
    def atualiza_chamado(chamado_id: int, **kwargs):
        chamado_atualizado = ChamadoRepository.atualizar_chamado(chamado_id, kwargs)
        return chamado_atualizado.to_dict() if chamado_atualizado else None

    @staticmethod
    def exclui_chamado(chamado_id: int):
        return ChamadoRepository.excluir_chamado(chamado_id)

    @staticmethod
    def atribuir_tecnico(chamado_id: int, tecnico: str):
        chamado = ChamadoRepository.atribuir_tecnico(chamado_id, tecnico)
        return chamado.to_dict() if chamado else None

    @staticmethod
    def fechar_chamado(chamado_id: int):
        chamado = ChamadoRepository.fechar_chamado(chamado_id)
        return chamado.to_dict() if chamado else None