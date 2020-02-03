from datetime import datetime
from Classes.DetailTicket import DetailTicket
import sqlite3

class Ticket:
    # int       id_ticket
    # str       id_carte
    # int       id_caissier
    # date      date_ticket
    # liste     liste_details

    # On devrait vérifier que chaque argument int est de bon format en utilisant des try except quand on cast le type
    # @[in] data :  sttr envoyé par le programme, contenu :
    #   "NoTicket";"CodeCli";"Caissier";"DateTicket"
    def __init__(self, data):

        tab = data.split(";")    
    
        self.id_ticket = int(tab[0].strip('\"'))
        self.id_carte = tab[1].strip('\"')
        self.id_caissier = int(tab[2].strip('\"'))
        self.date_ticket = self.createDate(tab[3].strip('\"'))

        self.liste_details = []

        #print("Ticket n° " + str(self.id_ticket) + " enregistré avec succès")
        
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



    def set_detail(self, detail_ticket):
        self.liste_details.append(detail_ticket)

    def get_total(self):
        ret = 0.
        for detail in self.liste_details:
            ret += detail.get_total()
        return ret

    def get_mois(self):
        ret = self.date_ticket.month
        return ret

    def get_id_ticket(self):
        return self.id_ticket

    @staticmethod
    def set_new_ticket (data) :
        try :
            connect = sqlite3.connect("datas.db")
            cursor = connect.cursor()
            tab = data.split(";")
            le_tuple = (tab[0].strip('\"').strip(), tab[1].strip('\"').strip(), tab[2].strip('\"').strip(),
            Ticket.createDate(tab[3].strip('\"').strip()))
            cursor.execute('INSERT INTO Ticket VALUES(?, ?, ?, ?)', le_tuple)
            connect.commit()
        except Exception as e :
        # On devra gérer les diffrentes erreures, si une ligne ne s'execute pas pcq'elle existe déjà, inutile de rollback
            print("Erreur ->", e)
            connect.rollback()
        finally :
            connect.close()
    

    def __str__(self):
        print("Ticket n° : " + str(self.id_ticket) + " :\nClient : " + str(self.id_carte) + "\nCaissier : " + str(self.id_caissier) + "\nCréé le : " + self.date_ticket.__str__())

