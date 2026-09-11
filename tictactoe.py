def afficher_plateau(plateau):
    print(f"{plateau[0]} | {plateau[1]} | {plateau[2]}")
    print("--+---+--")
    print(f"{plateau[3]} | {plateau[4]} | {plateau[5]}")
    print("--+---+--")
    print(f"{plateau[6]} | {plateau[7]} | {plateau[8]}")

def verifier_victoire(plateau, joueur):
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    for combo in combinaisons_gagnantes:
        if all(plateau[i] == joueur for i in combo):
            return True
    return False

def plateau_plein(plateau):
    return " " not in plateau

def jouer():
    plateau = [" "] * 9
    joueur_actuel = "X"

    while True:
        afficher_plateau(plateau)
        print(f"\nJoueur {joueur_actuel}, choisis une case (1-9) :")

        try:
            case = int(input()) - 1
        except ValueError:
            print("Entre un nombre entre 1 et 9.")
            continue

        if case < 0 or case > 8 or plateau[case] != " ":
            print("Case invalide ou déjà prise, réessaie.")
            continue

        plateau[case] = joueur_actuel

        if verifier_victoire(plateau, joueur_actuel):
            afficher_plateau(plateau)
            print(f"\nLe joueur {joueur_actuel} a gagné !")
            break

        if plateau_plein(plateau):
            afficher_plateau(plateau)
            print("\nMatch nul !")
            break

        joueur_actuel = "O" if joueur_actuel == "X" else "X"

if __name__ == "__main__":
    jouer()