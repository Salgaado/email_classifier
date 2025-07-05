Visão geral do projeto

# Como instalar dependências:
cd backend
pip install -r requirements.txt

# Como configurar:
cp backend/.env.example backend/.env
<!-- edite backend/.env com sua chave OPENAI_API_KEY -->

# Como rodar local:
<!-- # em uma aba -->
cd backend
python app.py
<!-- # em outra aba -->
cd public
py -3 -m http.server 5500

