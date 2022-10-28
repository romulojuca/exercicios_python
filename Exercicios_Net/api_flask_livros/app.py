from flask import Flask, request, jsonify

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atômicos',
        'autor': 'James Clear'
    }
]

#consultar todos
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)#Retorna lista toda


#consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


#Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()# Obtem informação do usuario para nosso API
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)# faz o update desse livro para o que o usuario pediu
            return jsonify(livro[indice])


#criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
