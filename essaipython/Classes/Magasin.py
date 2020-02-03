import os
from Classes.Ticket import Ticket
from Classes.Produit import Produit
from Classes.DetailTicket import DetailTicket
from Classes.Categorie import Categorie
from Classes.CarteFidelite import CarteFidelite
from datetime import datetime
import sqlite3


class Magasin:
    # liste<Ticket>             tickets
    # liste<DetailTicket>       details_tickets
    # liste<Produit>            produits
    # liste<Categorie>          categories
    # liste<CarteFidelite>      cartes_fidelitees

    tickets = []
    details_tickets = []
    produits = []
    categories = []
    cartes_fidelitees = []

    # On fera toute l'initialisation ici pour avoir un main propre
    # On peut faire beaucoup plus propre ici en allant mettre les fichiers texte
    # dans un dossier dédié, puis parcourir tout les fichiers, en extraire le nom
    # et appeler set_objet à la suite
    #   for fichier in dossier:
    #       tab = read().split('n')
    #       for ligne in tab:
    #           magasin.set_objet(fichier.name, ligne)
    def __init__(self):

        dossier = os.listdir("Z:/2A/PJS3/essaipython/Data")
        for nom_fic in dossier:
            fichier = open("Data/" + nom_fic, "r")
            tab = fichier.read().split('\n')
            for ligne in tab:
                #self.set_objet(nom_fic, ligne)
                Magasin.maj_db(nom_fic, ligne)

        #self.set_detail()
    
    @staticmethod
    def get_detail_ticket_mois(mois) :
        result = ''
        if mois < 10 and mois > 0 :
            mois_tmp = '0' + str(mois)
        if mois > 9 and mois < 13 :
            mois_tmp = str(mois)
        try :
            connect = sqlite3.connect("datas.db")
            cursor = connect.cursor()
            result =  cursor.execute("""
            SELECT * 
            FROM DetailTicket as DT 
            WHERE DT.id_ticket 
            IN (    SELECT id_ticket 
                    FROM Ticket 
                    WHERE(  SELECT strftime('%m', date_ticket)) = ?)""", (mois_tmp,)).fetchall()
            
        except Exception as e :
            print("Erreur ->", e)
            connect.rollback()
        finally :
            connect.close()
            return result

    @staticmethod
    def get_detail_ticket_mois_categ(mois, categorie) :
        result = ''
        if mois < 10 and mois > 0 :
            mois_tmp = '0' + str(mois)
        if mois > 9 and mois < 13 :
            mois_tmp = str(mois)
        try :
            connect = sqlite3.connect("datas.db")
            cursor = connect.cursor()

            result =  cursor.execute("""
            SELECT * 
            FROM DetailTicket as DT 
            WHERE id_ticket 
            IN (    SELECT id_ticket 
                    FROM Ticket 
                    WHERE(  SELECT strftime('%m', date_ticket)) = ?)
            AND id_prod
            IN (    SELECT id_prod
                    FROM Produit
                    WHERE id_categ IN ( SELECT id_categ
                                        FROM Categorie
                                        WHERE nom_categ = ?""", (mois_tmp, str(categorie))).fetchall()
            
        except Exception as e :
            print("Erreur ->", e)
            connect.rollback()
        finally :
            connect.close()
            return result

    @staticmethod
    def get_ca_mois(mois):
        results = Magasin.get_detail_ticket_mois(mois)
        ret = 0
        for detail_ticket in results :
            ret += (detail_ticket[2] * detail_ticket[3]) - ((detail_ticket[2] * detail_ticket[3]) / 100 * detail_ticket[4])
        return ret

    @staticmethod
    def get_ca_mois_categ(mois, categorie):
        results = Magasin.get_detail_ticket_mois_categ(mois, str(categorie))
        ret = 0
        for detail_ticket in results :
            ret += (detail_ticket[2] * detail_ticket[3]) - ((detail_ticket[2] * detail_ticket[3]) / 100 * detail_ticket[4])
        return ret

    @staticmethod
    def get_moyenne_ticket_mois(mois):
        results = Magasin.get_detail_ticket_mois(mois)
        ret = 0
        i = 0
        for detail_ticket in results :
            ret += (detail_ticket[2] * detail_ticket[3]) - ((detail_ticket[2] * detail_ticket[3]) / 100 * detail_ticket[4])
            i += 1
        if i != 0 :
            return ret / i
        return ret

    @staticmethod
    def maj_db(type_objet, data) :
        if type_objet == "Categorie.txt":
            Categorie.set_new_cat(data)
        if type_objet == "Ticket.txt":
            Ticket.set_new_ticket(data)
        if type_objet == "CarteFidelite.txt":
            CarteFidelite.set_new_carte(data)
        if type_objet == "Produit.txt":
            Produit.set_new_produit(data)
        if type_objet == "DetailTicket.txt":
            DetailTicket.set_new_detail_ticket(data)
        if type_objet == "DetailTicket2.txt":
            DetailTicket.set_new_detail_ticket(data)
        if type_objet == "Ticket2.txt":
            Ticket.set_new_ticket(data)
            
    def set_objet(self, type_objet, data):
        if type_objet == "Ticket.txt":
            self.tickets.append(Ticket(data))
        if type_objet == "DetailTicket.txt":
            self.details_tickets.append(DetailTicket(data))   
        if type_objet == "Produit.txt":
            self.produits.append(Produit(data))
        if type_objet == "Categorie.txt":
            self.categories.append(Categorie(data))
        if type_objet == "CarteFidelite.txt":
            self.cartes_fidelitees.append(CarteFidelite(data))

    def set_detail(self):
        for ticket in self.tickets:
            for detail in self.details_tickets:
                if detail.get_id_ticket() == ticket.get_id_ticket():
                    ticket.set_detail(detail)

    def get_moyenn_ticket(self, mois):
        nb_ticket = 0
        for ticket in self.tickets:
            if ticket.get_mois() == int(mois):
                nb_ticket += 1
        ca = self.get_ca_mois(mois)
        if nb_ticket != 0:
            return ca / nb_ticket
        return ca

    def _get_ca(self, mois):
        ret = 0
        for ticket in self.tickets:
            if ticket.get_mois() == int(mois):
                ret += ticket.get_total()
        return ret

    # On va utiliser un switcher ici pour determiner le numero de categorie
    def get_ca_cat(self, code_cat):
        return    

    def __str__(self):
        print("")
