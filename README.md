# API de Questões para Vestibular

## 📌 Descrição
API desenvolvida em Python com Flask para gerenciamento de questões de vestibular.  
Permite realizar operações de CRUD (Create, Read, Update, Delete) utilizando um arquivo JSON como base de dados.

## 🚀 Tecnologias
- Python
- Flask

## ⚙️ Como executar o projeto

1. Clone o repositório:
git clone https://github.com/YasmimSantos12/api_flask.git

2. Acesse a pasta:
cd seu-repositorio

3. Crie um ambiente virtual:
python -m venv venv

4. Ative o ambiente:
Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

5. Instale as dependências:
pip install flask

6. Execute o projeto:
python app.py

7. Acesse no navegador:
http://127.0.0.1:5000

---

## 📌 Rotas da API

### ➤ Criar questão
POST /questoes

Exemplo:
{
  "pergunta": "Qual é a capital do Brasil?",
  "alternativas": ["A) SP", "B) RJ", "C) Brasília", "D) BH"],
  "resposta": "C",
  "disciplina": "Geografia"
}

---

### ➤ Listar questões
GET /questoes

---

### ➤ Buscar questão por ID
GET /questoes/{id}

---

### ➤ Atualizar questão
PUT /questoes/{id}

---

### ➤ Deletar questão
DELETE /questoes/{id}

---

## 📂 Estrutura do projeto

- app.py → código principal da API
- dados.json → base de dados
- README.md → documentação

---

## 👩‍💻 Autora
Yasmim Santos  
Polo: Xambioá