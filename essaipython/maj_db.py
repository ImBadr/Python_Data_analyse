import sys
from Classes.Magasin import Magasin

nom_fic = sys.argv[1]

fichier = open("Data/" + nom_fic, "r")
tab = fichier.read().split('\n')
for ligne in tab:
    Magasin.maj_db(nom_fic, ligne)