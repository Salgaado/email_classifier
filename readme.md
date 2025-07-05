# Email Classifier Web App

Uma aplicação web simples para classificar emails como **Produtivo** ou **Improdutivo** e gerar respostas automáticas usando a API da OpenAI.

"Temos Reuniões que poderiam ser Emails, e Emails que poderiam ser Reuniões. Bora classificar isso?"


##  Demo

- **Frontend** (Vercel): https://email-classifier-omega-umber.vercel.app/
- **Backend** (Render): https://email-classifier-2-9xp8.onrender.com


##  Estrutura do Projeto

email-classifier/
├── public/  # Frontend HTML + CSS + JS
│ ├── index.html
│ ├── styles.css
│ └── script.js
└── backend/ # API Flask + OpenAI
├── app.py
├── requirements.txt
└── .env

##  Pré-requisitos

- **Python 3.8+**  
- **pip**  
- Conta na [OpenAI](https://platform.openai.com/) e chave de API (`OPENAI_API_KEY`)  


##  Instalação e Execução Local

**Clone o repositório**

  git clone https://github.com/SEU_USUARIO/email-classifier.git
  cd email-classifier                 


## Configuração do Backend
  cd backend
  pip install -r requirements.txt
  cp .env.example .env
  python app.py

   'Lembre-se de editar o arquivo `.env` com sua chave `OPENAI_API_KEY` antes de rodar o backend!'

## Configuração do Frontend
  cd public
  python -m http.server 5500

   'O frontend será servido em http://localhost:5500'


# Como usar
  1. Acesse o frontend em http://localhost:5500
  2. Insira o texto do email no campo de entrada
  3. Clique em "Classificar" para ver se é Produtivo ou Improdutivo
  4. Clique em "Gerar Resposta" para obter uma resposta automática da OpenAI


# Funcionalidades
  1. Upload / Texto Livre: cole no textarea ou anexe um arquivo .txt ou .pdf.
  2. Classificação Zero-Shot: usa GPT-3.5-turbo para indicar Produtivo ou Improdutivo.
  3. Geração de Resposta: GPT-3.5-turbo gera uma mensagem curta, educada e objetiva.


# Deploy
  ### Frontend:
  Commit & Push no GitHub.
  Conecte o repositório no Vercel.
  Configure como Site Estático, apontando para a pasta public/.

  ### Backend:
  Commit & Push no GitHub.
  Conecte o repositório no Render como Web Service.
  Root Directory: backend/
  Build Command: pip install -r requirements.txt
  Start Command: gunicorn app:app --bind 0.0.0.0:5000 (ou python app.py)
  Variável de ambiente: OPENAI_API_KEY


# Testes
  Teste manualmente no frontend.
  Use ferramentas como Postman ou cURL para testar a API diretamente.



