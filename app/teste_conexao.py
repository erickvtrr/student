# teste_conexao.py
import os
import re
from dotenv import load_dotenv
import psycopg2

print("Iniciando teste de conexão...")

# 1. Carregar variáveis do arquivo .env
load_dotenv()

# 2. Ler a URL do banco de dados
db_url = os.getenv("DATABASE_URL")

if not db_url:
    print("\nERRO: A variável DATABASE_URL não foi encontrada no .env!")
else:
    # Para segurança, vamos mascarar a senha antes de imprimir
    masked_url = re.sub(r':(.*?)\@', r':********@', db_url)
    print(f"Tentando conectar com a URL: {masked_url}")

    try:
        # 3. Tentar conectar
        conn = psycopg2.connect(db_url)
        print("\n✅ SUCESSO! A conexão com o banco de dados foi estabelecida.")
        conn.close()
    except Exception as e:
        # 4. Se falhar, mostrar o erro exato
        print("\n❌ FALHA AO CONECTAR. O erro foi:")
        print(f"   Tipo do Erro: {type(e).__name__}")
        print(f"   Mensagem: {e}")

print("\nTeste finalizado.")
