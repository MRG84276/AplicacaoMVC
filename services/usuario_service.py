from helpdesk.repositories.usuario_repository import UsuarioRepository
from repositories.chamado_repository import ChamadoReposotory

class UsuarioServices():
    @staticmethod
    def consulta_usuarios():
        usuarios = UsuarioRepository.consulta_tudo()
        
        resultado = []
        
        for usuario in usuarios:
            resultado.append({
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email,
                "setor": usuario.setor
            })
            
        return resultado

    @staticmethod
    def cadastra_usuario(**kwargs):
        usuario = UsuarioRepository.cadastrar_usuario(kwargs)
        return usuario

    @staticmethod
    def consultar_email(email):
        return UsuarioRepository.pesquisa_email(email)

    @staticmethod
    def atualiza_usuario(id, **kwargs):
        usuario = UsuarioRepository.atualizar_usuario(id, kwargs)
        return usuario

    @staticmethod
    def exclui_usuario(id):
        usuario = UsuarioRepository.excluir_usuario(id)
        return usuario

    @staticmethod
    def ativa_usuario(id):
        usuario = UsuarioRepository.ativar_usuario(id)
        return usuario

    @staticmethod
    def desativa_usuario(id):
        usuario = UsuarioRepository.desativar_usuario(id)
        return usuario