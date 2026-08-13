from flask import jsonify, request
from services.services import UsuarioServices

class UsuarioController():
     def valida_dados(dados):
          if not dados:
               return jsonify({"Erro": "JSON inválido"}), 400
          if len(dados.get("nome", "")) < 3:
               return jsonify({"Erro": "Nome inválido"}), 400
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
def listar():
    resultado = UsuarioServices.consulta_usuarios()
    return jsonify(resultado)

@staticmethod
def cadastrar():
    dados = request.json
    valida_dados = UsuarioController.valida_dados(dados)
    if not valida_dados:
        return jsonify({"Erro": "Não foi possível validar os dados"}), 400
    

    usuario = UsuarioServices.cadastra_usuario(
        nome=dados["nome"],
        email=dados["email"],
        setor=dados["setor"],
        ativo=dados.get("ativo", True)
    )
     
    return jsonify({
       "mensagem": "Usuario cadastrado",
       "id": usuario.id
    })

def atualizar(id):
    dados = request.json
    valida_dados = UsuarioController.valida_dados(dados)
    if not valida_dados:
        return jsonify({"Erro": "Não foi possível validar os dados"}), 400
    
    usuario = UsuarioServices.atualiza_usuario(
        id=id,
        nome=dados["nome"],
        email=dados["email"],
        setor=dados["setor"]
    )
    
    if not usuario:
        return jsonify({"Erro": "Usuario não encontrado"}), 404
    
    return jsonify({
        "mensagem": "Usuario aualizado",
        "id": usuario.id
    })

def excluir(id):
    usuario = UsuarioServices.exclui_usuario(id)
    if not usuario:
       return jsonify({"Erro": "Usuario não encontrado"}), 404
    return jsonify({
        "mensagem": "Usuario excluido",
        "id": usuario.id
    })

def ativar(id):
    usuario = UsuarioServices.ativa_usuario(id)
    if not usuario:
        return jsonify({"Erro": "Usuario não encontrado"}), 404
    return jsonify({
        "mensagem": "Usuario ativado",
        "id": usuario.id
    })

def desativar(id):
    usuario = UsuarioServices.desativa_usuario(id)
    if not usuario:
        return jsonify({"Erro": "Usuario não encntrado"}), 404
    return jsonify({
        "mensagem": "Usuario Desativado",
        "id": usuario.id
    })

