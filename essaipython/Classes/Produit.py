import sqlite3

class Produit:
    # int       id_prod
    # str       nom_prod
    # int       id_fourni
    # int       id_categ
    # int       id_sous_categ
    # str       qte_par_unite
    # float     prix_unite
    # int       unite_stockees
    # int       unite_commandees
    # int       niveau_reap
    # boolean   indisponible

    # On devrait vérifier que chaque argument int est de bon format en utilisant des try except quand on cast le type
    # et assert la taille du tableau de split, et faire une vérif en cas de chaîne vide (Saut de ligne à la fin du fichier .txt par exemple)
    # @[in] data :  sttr envoyé par le programme, contenu :
    #   "Refprod";"Nomprod";"NoFour";"CodeCateg";"NoSousCateg";"QteParUnit";"PrixUnit";"UnitesStock";"UnitesCom";"NiveauReap";"Indisponible"
    def __init__(self, data):

        tab = data.split(";")    
    
        self.id_prod = int(tab[0].strip('\"'))
        self.nom_prod = tab[1].strip('\"')
        self.id_fourni = int(tab[2].strip('\"'))
        self.id_categ = int(tab[3].strip('\"'))
        self.id_sous_categ = int(tab[4].strip('\"'))
        self.qte_par_unite = tab[5].strip('\"')
        self.prix_unite = float(tab[6].strip('\"').strip(' ').strip('€').replace(',', '.'))
        self.unite_stockees = int(tab[7].strip('\"'))
        self.unite_commandees = int(tab[8].strip('\"'))
        self.niveau_reap = int(tab[9].strip('\"'))
        self.indisponible = bool(tab[10].strip('\"'))

        #print("Produit n° " + str(self.id_prod) + " enregistré avec succès")


    
    @staticmethod
    def set_new_produit (data) :
        try :
            connect = sqlite3.connect("datas.db")
            cursor = connect.cursor()
            tab = data.split(";")
            le_tuple = (tab[0].strip('\"').strip(), tab[1].strip('\"').strip(),
                        tab[2].strip('\"').strip(), tab[3].strip('\"').strip(),
                        tab[4].strip('\"').strip(), tab[5].strip('\"').strip(),
                        tab[6].strip('\"').strip(' ').strip('€').replace(',', '.'),
                        tab[7].strip('\"').strip(), tab[8].strip('\"').strip(), tab[9].strip('\"').strip(), tab[10].strip('\"').strip())
            cursor.execute('INSERT INTO Produit VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', le_tuple)
            connect.commit()
        except Exception as e :
        # On devra gérer les diffrentes erreures, si une ligne ne s'execute pas pcq'elle existe déjà, inutile de rollback
            print("Erreur ->", e)
            connect.rollback()
        finally :
            connect.close()
    
    def __str__(self):
        print(self.id_prod)
