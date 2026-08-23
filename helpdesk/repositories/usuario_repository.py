from helpdesk.database import db
from helpdesk.models.usuario import Usuario

class UsuarioRepository:
     
    @staticmethod
    def consulta_tudo():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_id(usuario_id: int):
        return Usuario.query.get(usuario_id)

    @staticmethod
    def pesquisa_email(email: str):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def cadastrar_usuario(dados: dict):
        email = dados.get('email')
        if not email:
            return None, "O e-mail é obrigatório."

        if Usuario.query.filter_by(email=email).first():
            return None, "Já existe um usuário cadastrado com este e-mail."

        novo_usuario = Usuario(
            nome=dados.get('nome'),
            email=email,
            setor=dados.get('setor')
        )
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario, None

    @staticmethod
    def atualizar_usuario(usuario_id: int, dados: dict):
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            if 'nome' in dados:
                usuario.nome = dados['nome']
            if 'email' in dados:
                usuario.email = dados['email']
            if 'setor' in dados:
                usuario.setor = dados['setor']
            
            db.session.commit()
            return usuario
        return None

    @staticmethod
    def excluir_usuario(usuario_id: int):
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return False, "Usuário não encontrado"
        chamados_vinculados = Chamado.query.filter_by(usuario_id=usuario_id).first()
        if chamados_vinculados:
            return False, "Não é possível excluir um usuário que possui chamados vinculados."

        db.session.delete(usuario)
        db.session.commit()
        return True, None

    @staticmethod
    def ativar_usuario(usuario_id: int):
        usuario = Usuario.query.get(usuario_id)
        if usuario and hasattr(usuario, 'ativo'):
            usuario.ativo = True
            db.session.commit()
        return usuario

    @staticmethod
    def desativar_usuario(usuario_id: int):
        usuario = Usuario.query.get(usuario_id)
        if usuario and hasattr(usuario, 'ativo'):
            usuario.ativo = False
            db.session.commit()
        return usuario

    @staticmethod
    def deletar(usuario):
        db.session.delete(usuario)
        db.session.commit()
        
