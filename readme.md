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


  # 🚀 Próximos Passos & Ideias de Evolução
  ### Integração com Provedores de E-mail
    Conectar via OAuth a Gmail, Outlook ou IMAP, para que o app sincronize sua caixa de entrada automaticamente.
  ### Filtragem Avançada e Priorizações
    Aprender com seu comportamento: destacar e-mails de remetentes frequentes ou contatos VIP.
    “Snooze” e lembretes para e-mails que você queira rever mais tarde.
  ### Resumos Automáticos de Thread
    Quando um e-mail fizer parte de uma conversa longa, gerar um breve resumo para você entender o contexto em um relance.
  ### Templates Personalizáveis
    Permitir que o usuário salve respostas padrão e treine a IA para usar seu tom de voz ou assinatura personalizada.
  ### Análise de Anexos
    Extrair texto de PDFs, imagens (OCR) ou planilhas, e incluir isso na classificação e na resposta.
  ### Dashboard de Métricas
    Exibir estatísticas de e-mails recebidos, tempos de resposta, porcentagem de produtivos vs. improdutivos e tendências ao longo do tempo.
  ### Mobile App ou PWA
    Transformar o frontend em uma Progressive Web App com notificações push para alertas de e-mails prioritários. 
  ### Suporte Multilíngue
    Detectar o idioma do e-mail e gerar respostas adequadas em Português, Inglês, Espanhol, etc.
  ### Chatbot para ChatOps
    Integre um chatbot (Slack, Teams) que, ao receber o link de um e-mail, retorne imediatamente sua classificação e uma resposta sugerida.
  ### Automação de Fluxos
    Conectar com Zapier, Make ou outras plataformas de automação para acionar workflows (por ex., mover e-mails improdutivos para pastas específicas ou criar tarefas no Trello).
  ### Controle de Privacidade & Compliance
    Adicionar camadas de criptografia end-to-end e configurações de retenção de dados para atender a políticas de privacidade e compliance de empresas.
  ### Modelos Customizados & Fine-Tuning
    Permitir que o usuário faça fine-tuning de um modelo leve com seu próprio histórico de e-mails, para personalizar ainda mais as classificações e respostas.





