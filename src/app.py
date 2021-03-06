from flask import app, Flask, render_template

minha_app = Flask(__name__)

@minha_app.route('/')
def home():
    return render_template('tela-home.html')

@minha_app.route('/projetos')
def projetos():
    usu = 'Priscila'
    return render_template('projetos.html', usuario=usu)

@minha_app.route('/sobre_mim')
def sobre_mim():
    usu = 'Priscila'
    return render_template('sobre_mim.html', usuario=usu)

if __name__ == '__main__':
    minha_app.run('0.0.0.0')