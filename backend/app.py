import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
from PyPDF2 import PdfReader
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("Faltando OPENAI_API_KEY no .env")


app = Flask(__name__)
CORS(app)

@app.after_request
def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error=str(e)), 500

def classify_and_respond(text: str):

    classify_prompt = (
        "Classifique este email nas categorias 'Produtivo' ou 'Improdutivo', respondendo apenas com a categoria, sem explicações.\n\n"
        f"\"\"\"{text}\"\"\""
    )
    classify_resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": classify_prompt}],
        temperature=0
    )
    category = classify_resp.choices[0].message.content.strip().capitalize()
    if category not in ["Produtivo", "Improdutivo"]:
        category = "Produtivo"


    reply_prompt = (
        f"Você é um assistente de atendimento ao cliente. Este email foi classificado como {category}. "
        "Gere uma resposta curta, educada e objetiva baseada no conteúdo abaixo, sem repetir o texto original:\n\n"
        f"\"\"\"{text}\"\"\""
    )
    reply_resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": reply_prompt}],
        temperature=0.6,
        max_tokens=150
    )
    reply = reply_resp.choices[0].message.content.strip()
    return category, reply

@app.route('/processar', methods=['POST'])
def process_email():
    text = None

    if 'file' in request.files:
        file = request.files['file']
        name = file.filename.lower()
        if name.endswith('.txt'):
            text = file.stream.read().decode('utf-8', errors='ignore')
        elif name.endswith('.pdf'):
            reader = PdfReader(file)
            pages = [p.extract_text() for p in reader.pages if p.extract_text()]
            text = "\n".join(pages)
        else:
            return jsonify(error="Formato não suportado"), 400

    elif request.form.get('texto'):
        text = request.form.get('texto')

    if not text:
        return jsonify(error="Nenhum texto ou arquivo enviado"), 400

    category, reply = classify_and_respond(text)
    return jsonify(categoria=category, resposta=reply)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
