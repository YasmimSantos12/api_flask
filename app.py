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

# CREATE
@app.route("/tarefas", methods=["POST"])
def criar():
    dados = ler_dados()
    nova = request.json

    nova["id"] = len(dados) + 1
    dados.append(nova)

    salvar_dados(dados)
    return jsonify(nova), 201

# READ
@app.route("/tarefas", methods=["GET"])
def listar():
    return jsonify(ler_dados())

# UPDATE
@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = ler_dados()

    for tarefa in dados:
        if tarefa["id"] == id:
            tarefa.update(request.json)
            salvar_dados(dados)
            return jsonify(tarefa)

    return {"erro": "Não encontrado"}, 404

# DELETE
@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar(id):
    dados = ler_dados()

    novos = [t for t in dados if t["id"] != id]

    salvar_dados(novos)
    return {"msg": "Deletado"}

app.run(debug=True)