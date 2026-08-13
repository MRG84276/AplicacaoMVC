from database import db
from models.usuario import Usuario

class UsuarioRepository:
    @staticmethod
    def consulta_tudo():
        """
        Retorna a lista de todos os usuários cadastrados no banco de dados.
        """
        return Usuario.query.all()

    @staticmethod
    def buscar_por_id(usuario_id: int):
        """
        Busca e retorna um único usuário pelo seu ID (Primary Key).
        """
        return Usuario.query.get(usuario_id)

    @staticmethod
    def pesquisa_email(email: str):
        """
        Busca e retorna um usuário pelo endereço de e-mail.
        """
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def cadastrar_usuario(dados: dict):
        """
        Cria um novo usuário na base de dados a partir de um dicionário.
        Exemplo de 'dados': {'nome': 'Carlos', 'email': 'carlos@empresa.com', 'setor': 'TI'}
        """
        novo_usuario = Usuario(
            nome=dados.get('nome'),
            email=dados.get('email'),
            setor=dados.get('setor')
        )
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario

    @staticmethod
    def atualizar_usuario(usuario_id: int, dados: dict):
        """
        Atualiza as informações de um usuário existente pelo seu ID.
        """
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
        """
        Remove um usuário do banco de dados pelo seu ID.
        """
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return True
        return False

    @staticmethod
    def ativar_usuario(usuario_id: int):
        """
        Altera o status do usuário para ativo (caso possua o campo 'ativo' no modelo).
        """
        usuario = Usuario.query.get(usuario_id)
        if usuario and hasattr(usuario, 'ativo'):
            usuario.ativo = True
            db.session.commit()
            return usuario
        return usuario

    @staticmethod
    def desativar_usuario(usuario_id: int):
        """
        Altera o status do usuário para inativo (caso possua o campo 'ativo' no modelo).
        """
        usuario = Usuario.query.get(usuario_id)
        if usuario and hasattr(usuario, 'ativo'):
            usuario.ativo = False
            db.session.commit()
            return usuario
        return usuario
        