# Projet Script de sécurité : Outil qui permet de générer des mdp sécurisée par Othman BELAIDI.

import secrets
import string

def generer_mot_de_passe(longueur):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(secrets.choice(alphabet) for i in range(longueur))
    return mot_de_passe

longueur_mot_de_passe = 12 
mot_de_passe_securise = generer_mot_de_passe(longueur_mot_de_passe)
print(mot_de_passe_securise)
