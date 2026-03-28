from flask import Flask, request, jsonify
import json

app = Flask(__name__)

ARQUIVO = "dados.json"

def ler_dados():
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

# CREATE - cadastrar questão
@app.route("/questoes", methods=["POST"])
def criar_questao():
    dados = ler_dados()
    nova = request.json

    nova["id"] = len(dados) + 1
    dados.append(nova)

    salvar_dados(dados)
    return jsonify(nova), 201

# READ - listar questões
@app.route("/questoes", methods=["GET"])
def listar_questoes():
    return jsonify(ler_dados())

# READ - buscar por ID
@app.route("/questoes/<int:id>", methods=["GET"])
def buscar_questao(id):
    dados = ler_dados()

    for q in dados:
        if q["id"] == id:
            return jsonify(q)

    return {"erro": "Questão não encontrada"}, 404

# UPDATE - atualizar questão
@app.route("/questoes/<int:id>", methods=["PUT"])
def atualizar_questao(id):
    dados = ler_dados()

    for q in dados:
        if q["id"] == id:
            q.update(request.json)
            salvar_dados(dados)
            return jsonify(q)

    return {"erro": "Questão não encontrada"}, 404

# DELETE - excluir questão
@app.route("/questoes/<int:id>", methods=["DELETE"])
def deletar_questao(id):
    dados = ler_dados()

    novos = [q for q in dados if q["id"] != id]

    salvar_dados(novos)
    return {"msg": "Questão deletada"}

app.run(debug=True)