import sqlite3

class Categorie:
    # int       id_categ
    # str       nom_categ
    # str       description


    # On devrait vérifier que chaque argument int est de bon format en utilisant des try except quand on cast le type
    # @[in] data :  sttr envoyé par le programme, contenu :
    #   "CodeCateg";"NomCateg";"Description"
    def __init__(self, data):

        tab = data.split(";")    
    
        self.id_categ = int(tab[0].strip('\"'))
        self.nom_categ = tab[1].strip('\"')
        self.description = tab[2].strip('\"')

        #print("Categorie n° " + str(self.id_categ) + " enregistré avec succès")
        
    
    @staticmethod
    def set_new_cat (data) :
        try :
            connect = sqlite3.connect("datas.db")
            cursor = connect.cursor()
            tab = data.split(";")
            le_tuple = (tab[0].strip('\"').strip(), tab[1].strip('\"').strip(), tab[2].strip('\"').strip())
            cursor.execute('INSERT INTO Categorie VALUES(?, ?, ?)', le_tuple)
            connect.commit()
        except Exception as e :
            print("Erreur ->", e)
            connect.rollback()
        finally :
            connect.close()
    
    def __str__(self):
        print(self.id_categ)
