from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'gabriel'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


# Lista de Jogos
Jogo1 = Jogo('God of War', 'Ação/RPG', 'PS5')
Jogo2 = Jogo('The sims', 'RPG', 'PC')
lista_jogos = [Jogo1, Jogo2]


@app.route('/')
def index():
    return render_template('lista.html',
                           titulo="Jogos",
                           jogos=lista_jogos)


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)

    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect('/')
    else:
        flash('Não logado, tente novamente!')
        return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
