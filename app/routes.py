from flask import render_template, request
from app import app
from app.game import get_action, get_verite, get_random_choice

votes = {'joueur1': 0, 'joueur2': 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/choisir', methods=['POST'])
def choisir():
    choix = request.form['choix']
    duel = False
    if choix == 'action':
        resultat = get_action()
        return render_template('index.html', resultat=resultat)
    elif choix == 'verite':
        resultat = get_verite()
        return render_template('index.html', resultat=resultat)
    elif choix == 'aleatoire':
        resultat = get_random_choice()
        return render_template('index.html', resultat=resultat)
    elif choix == 'duel':
        joueur1 = 'Joueur 1'
        joueur2 = 'Joueur 2'
        resultat1 = get_random_choice()
        resultat2 = get_random_choice()
        duel = True
        return render_template('index.html', duel=duel, joueur1=joueur1, joueur2=joueur2, resultat1=resultat1, resultat2=resultat2)

@app.route('/vote', methods=['POST'])
def vote():
    joueur = request.form['vote']
    votes[joueur] += 1
    return render_template('vote_result.html', votes=votes)

@app.route('/regles')
def regles():
    return render_template('regles.html')