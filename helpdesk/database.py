from models import db, Usuario 

class UsuarioRepository:

    @staticmethod
    def consulta_tudo():
        return Usuario.query.all()

    @staticmethod
    def cadastrar_usuario(dados):
        novo_usuario = Usuario(
            nome=dados.get('nome'),
            email=dados.get('email'),
            setor=dados.get('setor')
        )
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario

    @staticmethod
    def pesquisa_email(email):
     
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def buscar_por_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def atualizar_usuario(id, dados):
        usuario = Usuario.query.get(id)
        if usuario:
            if 'nome' in dados:
                usuario.nome = dados['nome']
            if 'email' in dados:
                usuario.email = dados['email']
            if 'setor' in dados:
                usuario.setor = dados['setor']
            
            db.session.commit()
        return usuario

    @staticmethod
    def excluir_usuario(id):
        usuario = Usuario.query.get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return True
        return False

    @staticmethod
    def ativar_usuario(id):
        """
        Caso adicione um campo booleano 'ativo' no modelo Usuario no futuro,
        pode alterar o estado aqui.
        """
        usuario = Usuario.query.get(id)
        if usuario:
        
            db.session.commit()
        return usuario

    @staticmethod
    def desativar_usuario(id):
        """
        Caso adicione um campo booleano 'ativo' no modelo Usuario no futuro,
        pode alterar o estado aqui.
        """
        usuario = Usuario.query.get(id)
        if usuario:
       
            db.session.commit()
        return usuario