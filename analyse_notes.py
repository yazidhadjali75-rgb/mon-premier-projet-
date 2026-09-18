import numpy as np

notes = np.array([12, 15, 8, 20, 9, 14, 17, 5, 11, 18, 
                   10, 13, 16, 7, 19, 6, 12, 15, 9, 14])

moyenne = np.mean(notes)
mediane = np.median(notes)
ecart_type = np.std(notes)
note_max = np.max(notes)
note_min = np.min(notes)
nb_admis = np.sum(notes >= 10)
notes_triees = np.sort(notes)

print("Notes des élèves :", notes)
print(f"Moyenne : {moyenne:.2f}")
print(f"Médiane : {mediane}")
print(f"Écart-type : {ecart_type:.2f}")
print(f"Note maximale : {note_max}")
print(f"Note minimale : {note_min}")
print(f"Nombre d'élèves ayant la moyenne : {nb_admis} sur {len(notes)}")
print("Notes triées :", notes_triees)