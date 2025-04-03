from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def buscar_livros(tema):
    api_key = 'AIzaSyAePSWGFC12iL7VYzPfTcupSN-v2JlZMCc'
    url = f"https://www.googleapis.com/books/v1/volumes?q={tema}&key={api_key}"
    resposta = requests.get(url)
    dados = resposta.json()

    livros = []
    for item in dados.get("items", [])[:5]:
        info = item["volumeInfo"]
        livros.append({
            "titulo": info.get("title", "Titulo não disponível"),
            "autor": ", ".join(info.get("authors", ["Autor desconhecido"])),
            "sinopse": info.get("description", "Sem descrição disponível")
        })
    
    return livros

@app.route("/buscar_livros",methods=["POST"])
def api_buscar_livros():
    dados = request.json
    tema = dados.get("tema")
    if not tema:
        return jsonify({"erro": "É necessário informar um tema"}), 400
    
    resultado = buscar_livros(tema)
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)