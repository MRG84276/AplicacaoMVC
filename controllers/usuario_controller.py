from flask import Blueprint, jsonify, request
from services.usuario_service import UsuarioServices

usuario_bp = Blueprint("usuarios", __name__)


class UsuarioController:

    @staticmethod
    def valida_dados(dados):
        if not dados or not isinstance(dados, dict):
            return jsonify({"Erro": "JSON inválido ou ausente"}), 400

        nome = dados.get("nome", "")
        if not nome or len(nome) < 3:
            return jsonify({"Erro": "Nome inválido (mínimo 3 caracteres)"}), 400

        email = dados.get("email")
        if not email:
            return jsonify({"Erro": "Email obrigatório"}), 400
        if "@" not in email:
            return jsonify({"Erro": "Email inválido"}), 400

        setor = dados.get("setor")
        if not setor:
            return jsonify({"Erro": "Setor obrigatório"}), 400

        return True
     

    @staticmethod
    def index():
        """Retorna uma mensagem de boas-vindas ou a lista inicial."""
        return jsonify({
            "mensagem": "API de Chamados e Usuários ativa e rodando!",
            "status": "online"
        }), 200


    @staticmethod
    def listar():
        resultado = UsuarioServices.consulta_usuarios()
        return jsonify(resultado), 200

    @staticmethod
    def cadastrar():
        dados = request.get_json(silent=True)
        validacao = UsuarioController.valida_dados(dados)
        if validacao is not True:
            return validacao  # Retorna a resposta de erro diretamente (jsonify, 400)

        usuario = UsuarioServices.cadastra_usuario(
            nome=dados["nome"],
            email=dados["email"],
            setor=dados["setor"],
            ativo=dados.get("ativo", True)
        )

        if not usuario:
            return jsonify({"Erro": "Não foi possível cadastrar o usuário"}), 400

        usuario_id = usuario.get("id") if isinstance(usuario, dict) else usuario.id

        return jsonify({
            "mensagem": "Usuário cadastrado com sucesso",
            "id": usuario_id
        }), 201

    @staticmethod
    def atualizar(id):
        dados = request.get_json(silent=True)
        validacao = UsuarioController.valida_dados(dados)
        if validacao is not True:
            return validacao

        usuario = UsuarioServices.atualiza_usuario(
            id=id,
            nome=dados["nome"],
            email=dados["email"],
            setor=dados["setor"]
        )

        if not usuario:
            return jsonify({"Erro": "Usuário não encontrado"}), 404

        usuario_id = usuario.get("id") if isinstance(usuario, dict) else usuario.id

        return jsonify({
            "mensagem": "Usuário atualizado com sucesso",
            "id": usuario_id
        }), 200

    @staticmethod
    def excluir(id):
        sucesso = UsuarioServices.exclui_usuario(id)
        if not sucesso:
            return jsonify({"Erro": "Usuário não encontrado"}), 404

        return jsonify({
            "mensagem": "Usuário excluído com sucesso",
            "id": id
        }), 200

    @staticmethod
    def ativar(id):
        usuario = UsuarioServices.ativa_usuario(id)
        if not usuario:
            return jsonify({"Erro": "Usuário não encontrado"}), 404

        usuario_id = usuario.get("id") if isinstance(usuario, dict) else usuario.id

        return jsonify({
            "mensagem": "Usuário ativado com sucesso",
            "id": usuario_id
        }), 200

    @staticmethod
    def desativar(id):
        usuario = UsuarioServices.desativa_usuario(id)
        if not usuario:
            return jsonify({"Erro": "Usuário não encontrado"}), 404

        usuario_id = usuario.get("id") if isinstance(usuario, dict) else usuario.id

        return jsonify({
            "mensagem": "Usuário desativado com sucesso",
            "id": usuario_id
        }), 200

  @staticmethod
    def listar_chamados(id):
        """Busca e retorna todos os chamados abertos por um usuário específico."""
        chamados = ChamadoService.buscar_por_usuario(id)
        return jsonify(chamados), 200

