from flask import Flask, render_template_string
import psycopg2
import os
import time

app = Flask(__name__)

def get_db_connection():
    # Tenta conectar com retry para evitar erro caso o DB demore a subir
    for i in range(5):
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'db'),
                database=os.getenv('DB_NAME', 'educadb'),
                user=os.getenv('DB_USER', 'postgres'),
                password=os.getenv('DB_PASSWORD', 'password123')
            )
            return conn
        except Exception as e:
            print(f"Tentativa {i+1} falhou, tentando novamente...")
            time.sleep(2)
    return None

@app.route('/')
def index():
    conn = get_db_connection()
    if not conn:
        return "<h1>Erro: Não foi possível conectar ao banco de dados.</h1>", 500
    
    cur = conn.cursor()

    cur.execute('SELECT * FROM view_pending_needs;')
    needs = cur.fetchall()
    cur.close()
    conn.close()

    # Template HTML
    html = """
    <html>
        <head><title>EducaSolidario - Cloud</title></head>
        <body style="font-family: sans-serif; padding: 20px;">
            <h1>🎒 EducaSolidario - Necessidades Pendentes</h1>
            <p>Métricas de Nuvem: Conectado com sucesso ao PostgreSQL 16 na AWS.</p>
            <table border="1" cellpadding="10" style="border-collapse: collapse; width: 100%;">
                <tr style="background-color: #f2f2f2;">
                    <th>Instituição</th><th>Material</th><th>Qtd Necessária</th><th>Prioridade</th><th>Projeto</th>
                </tr>
                {% for n in needs %}
                <tr>
                    <td>{{ n[0] }}</td><td>{{ n[1] }}</td><td>{{ n[2] }}</td>
                    <td style="color: {{ 'red' if n[3] == 'urgente' else 'black' }}">{{ n[3] }}</td>
                    <td>{{ n[4] if n[4] else 'Geral' }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>
    """
    return render_template_string(html, needs=needs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)