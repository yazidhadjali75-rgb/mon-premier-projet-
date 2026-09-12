import random

def choix_ordinateur():
    return random.choice(["pierre", "feuille", "ciseaux"])

def determiner_gagnant(joueur, ordinateur):
    if joueur == ordinateur:
        return "égalité"
    
    combinaisons_gagnantes = {
        "pierre": "ciseaux",
        "feuille": "pierre",
        "ciseaux": "feuille"
    }
    
    if combinaisons_gagnantes[joueur] == ordinateur:
        return "joueur"
    else:
        return "ordinateur"

def jouer():
    choix_valides = ["pierre", "feuille", "ciseaux"]
    score_joueur = 0
    score_ordinateur = 0

    while True:
        print("\nChoisis : pierre, feuille ou ciseaux (ou 'quitter')")
        choix_joueur = input().lower()

        if choix_joueur == "quitter":
            break

        if choix_joueur not in choix_valides:
            print("Choix invalide, réessaie.")
            continue

        choix_pc = choix_ordinateur()
        print(f"L'ordinateur a choisi : {choix_pc}")

        resultat = determiner_gagnant(choix_joueur, choix_pc)

        if resultat == "égalité":
            print("Égalité !")
        elif resultat == "joueur":
            print("Tu as gagné !")
            score_joueur += 1
        else:
            print("L'ordinateur a gagné !")
            score_ordinateur += 1

        print(f"Score -> Toi : {score_joueur} | Ordinateur : {score_ordinateur}")

    print(f"\nScore final -> Toi : {score_joueur} | Ordinateur : {score_ordinateur}")

if __name__ == "__main__":
    jouer()