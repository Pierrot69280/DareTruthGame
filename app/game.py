import random

actions = [
    "Fais 10 pompes.",
    "Chante une chanson pendant 30 secondes.",
    "Fais une danse rigolote.",
    "Imite un animal pendant une minute.",
    "Fais un compliment à la personne à ta gauche."
]

verites = [
    "Quel est ton plus grand secret ?",
    "As-tu déjà menti pour te sortir d'une situation gênante ?",
    "Quel est ton plus grand regret ?",
    "Quel est ton rêve le plus fou ?",
    "As-tu déjà triché à un examen ?"
]

def get_action():
    return random.choice(actions)

def get_verite():
    return random.choice(verites)

def get_random_choice():
    return random.choice([get_action(), get_verite()])
