from repositories.usuario_repository import UsuarioRepository
from repositories.chamado_repository import ChamadoRepository


class UsuarioServices:

    @staticmethod
    def usuario_para_dict(usuario):
        if usuario is None:
            return None
            
        return {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "setor": usuario.setor,
            "ativo": usuario.ativo
        }

    @staticmethod
    def consulta_usuarios():
        usuarios = UsuarioRepository.consulta_tudo()
        
        resultado = []
        for usuario in usuarios:
            resultado.append(UsuarioServices.usuario_para_dict(usuario))
            
        return resultado

    @staticmethod
    def buscar_por_id(id):
        usuario = UsuarioRepository.buscar_por_id(id)
        return UsuarioServices.usuario_para_dict(usuario)

    @staticmethod
    def cadastra_usuario(**kwargs):
        email = kwargs.get("email")
        if email and UsuarioRepository.pesquisa_email(email):
            raise ValueError("Já existe um usuário cadastrado com este e-mail.")

        novo_usuario = UsuarioRepository.cadastrar_usuario(kwargs)
        return UsuarioServices.usuario_para_dict(novo_usuario)

    @staticmethod
    def consultar_email(email):
        usuario = UsuarioRepository.pesquisa_email(email)
        return UsuarioServices.usuario_para_dict(usuario)

    @staticmethod
    def atualiza_usuario(id, **kwargs):
        usuario_atualizado = UsuarioRepository.atualizar_usuario(id, kwargs)
        return UsuarioServices.usuario_para_dict(usuario_atualizado)

    @staticmethod
    def exclui_usuario(id):
        chamados_do_usuario = ChamadoRepository.buscar_por_usuario(id)
        if len(chamados_do_usuario) > 0:
            raise ValueError("Não é possível excluir um usuário que possui chamados vinculados.")

        return UsuarioRepository.excluir_usuario(id)

    @staticmethod
    def ativa_usuario(id):
        usuario = UsuarioRepository.ativar_usuario(id)
        return UsuarioServices.usuario_para_dict(usuario)

    @staticmethod
    def desativa_usuario(id):
        usuario = UsuarioRepository.desativar_usuario(id)
        return UsuarioServices.usuario_para_dict(usuario)

    @staticmethod
    def consulta_chamados_usuario(usuario_id):
        chamados = ChamadoRepository.buscar_por_usuario(usuario_id)
        
        resultado = []
        for chamado in chamados:
            resultado.append({
                "id": chamado.id,
                "titulo": chamado.titulo,
                "descricao": chamado.descricao,
                "prioridade": chamado.prioridade,
                "status": chamado.status,
                "usuario_id": chamado.usuario_id
            })
            
        return resultado
