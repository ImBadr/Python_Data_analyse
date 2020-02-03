from datetime import datetime
import sqlite3

class CarteFidelite:
    # str   id_carte
    # str   nom_client
    # str   prenom_client
    # date  date_naissance
    # str   adresse
    # str   ville
    # int   code_postale
    # str   pays
    # str   num_tel

    # On devrait vérifier que chaque argument int est de bon format en utilisant des try except quand on cast le type
    # @[in] data :  sttr envoyé par le programme, contenu :
    #   "CodeCli";"Nom";"Prenom";"DateNaiss";"Adresse";"Ville";"CodePostal";"Pays";"Tel"
    def __init__(self, data):

        tab = data.split(";")    
    
        self.id_carte = tab[0].strip('\"').strip()
        self.nom_client = tab[1].strip('\"').strip()
        self.prenom_client = tab[2].strip('\"').strip()
        self.date_naissance = self.createDate(tab[3].strip('\"').strip())
        self.adresse = tab[4].strip('\"').strip()
        self.ville = tab[5].strip('\"').strip()
        self.code_postale = int(tab[6].strip('\"').replace(' ', ''))
        self.pays = tab[7].strip('\"').strip()
        self.num_tel = tab[8].strip('\"').strip()

        #print("Carte de fidélitée n° " + self.code_client + " enregistrée avec succès")
        
    # Bon, je ne suis pas sûr que les try except soient nécéssaires ici, mais ça nous permettra de savoir si les profs se sont trompés
    # et assert la taille du tableau de split
    # @[in] str_date :  str envoyé par le constructeur, contenu :
    #   "DD/MM/YY HH/mm/ss"
    @staticmethod
    def createDate (str_date):
        try:
            tab = str_date.split(" ")
            assert tab.__len__() == 2
        except AssertionError:
            print("Erreur lors de la convertion de la date, format = \"DD/MM/YY HH/mm/ss\" ")

        date = tab[0]
        heure = tab[1]

        try:
            tab = date.split("/")
            assert tab.__len__() == 3
        except AssertionError:
            print("-- Vous avez mal entre : \"DD/MM/YY\" ")

        jour = int(tab[0])
        mois = int(tab[1])
        annee = int(tab[2])

        try:
            tab = heure.split(":")
            assert tab.__len__() == 3
        except AssertionError:
            print("-- Vous avez mal entre : \"HH/mm/ss\" ")

        heure = int(tab[0])
        minute = int(tab[1])
        seconde = int(tab[2])

        try:
            date_ticket = datetime(annee, mois, jour, heure, minute, seconde)
            assert date_ticket != None
        except AssertionError:
            print("Erreur lors de la convertion de la date, format = \"DD/MM/YY HH/mm/ss\" ")

        return date_ticket

    
    @staticmethod
    def set_new_carte (data) :
        try :
            connect = sqlite3.connect("datas.db")
            cursor = connect.cursor()
            tab = data.split(";")
            le_tuple = (tab[0].strip('\"').strip(), tab[1].strip('\"').strip(), tab[2].strip('\"').strip(),
                        CarteFidelite.createDate(tab[3].strip('\"').strip()), 
                        tab[4].strip('\"').strip(), tab[5].strip('\"').strip(),
                        tab[6].strip('\"').replace(' ', ''), tab[7].strip('\"').strip(), tab[8].strip('\"').strip())
            cursor.execute('INSERT INTO CarteFidelite VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', le_tuple)
            connect.commit()
        except Exception as e :
        # On devra gérer les diffrentes erreures, si une ligne ne s'execute pas pcq'elle existe déjà, inutile de rollback
            print("Erreur ->", e)
            connect.rollback()
        finally :
            connect.close()

    
    def __str__(self):
        print("Carte n° : " + str(self.id_carte) + " :\nClient : " + str(self.id_carte) + " " + str(self.prenom_client) + " " + str(self.nom_client))