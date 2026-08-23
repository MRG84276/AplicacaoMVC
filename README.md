# API REST - Gustavo Yvo


### 1. Criar o ambiente virtual
``` python -m venv venv```

### 2. ativar o ambiente virtual
```venv\Scripts\activate```

### 3. Instalar as dependências
```pip install -r requirements.txt```

### Caso esteja consifigurado do zero instale os pacotes e gere o arquivo de dependências:
```pip install flask flask-sqlalchemy```
```pip freeze > requirements.txt```

### 4. Iniciar a aplicação
```python app.py```

### Rotas Principais API

## Usuários (/usuarios)

### GET /usuarios - Lista todos os usuários
### POST /usuarios - Cadastra um novo usuário
### PATCH /usuarios/<id>/ativar - Ativa um usuário
### PATCH /usuarios/<id>/desativar - Desativa um usuário

## Chamados (/chamados)

### GET /chamados - Lista todos os chamados
### POST /chamados - Cria um novo chamado
### PUT /chamados/<id> - Atualiza um chamado existente
### DELETE /chamados/<id> - Remove um chamado
### PATCH /chamados/<id>/iniciar - Altera status para "Em atendimento"
### PATCH /chamados/<id>/fechar - Altera status para "Encerrado"
### GET /chamados/estatisticas - Retorna contadores e métricas
