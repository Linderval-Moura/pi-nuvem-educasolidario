from flask import Flask
import psycopg2
import psycopg2.extras

app = Flask(__name__)

def get_instituicoes():
    connection = psycopg2.connect(
        host='db',
        port='5432',
        database='educasolidario',
        user='root',
        password='root'
    )
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute('SELECT * FROM instituicoes')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

@app.route('/')
def index():
    dados = get_instituicoes()
    html = '<h1>EducaSolidário - Instituições Cadastradas</h1><ul>'
    for inst in dados:
        html += f'<li><b>{inst["nome"]}</b> ({inst["tipo"]} - {inst["cidade"]}): {inst["necessidade"]}</li>'
    html += '</ul>'
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')