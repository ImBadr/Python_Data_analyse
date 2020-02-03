import sqlite3

class DetailTicket:
    # int       id_ticket
    # int       id_prod
    # float     prix_unite
    # int       qte
    # float     remise


    # On devrait vérifier que chaque argument int est de bon format en utilisant des try except quand on cast le type
    # @[in] data :  sttr envoyé par le programme, contenu :
    #   "NoTicket";"Refprod";"PrixUnit";"Qte";"Remise%"
    def __init__(self, data):

        tab = data.split(";")    
    
        self.id_ticket = int(tab[0].strip('\"'))
        self.id_prod = int(tab[1].strip('\"'))
        self.prix_unite = float(tab[2].strip('\"').strip(' ').strip('€').replace(',', '.'))
        self.qte = int(tab[3].strip('\"'))
        self.remise = float(tab[4].strip('\"').strip(' ').replace(',', '.'))

        #print("DetailTicket n° " + str(self.id_ticket) + " enregistré avec succès")
        
    
    def get_total(self):
        return (self.prix_unite - (self.prix_unite / 100 * self.remise)) * self.qte
    
    def get_id_ticket(self):
        return self.id_ticket

    def get_id_prod(self):
        return self.id_prod

    @staticmethod
    def set_new_detail_ticket (data) :
        try :
            connect = sqlite3.connect("datas.db")
            cursor = connect.cursor()
            tab = data.split(";")
            le_tuple = (tab[0].strip('\"'), tab[1].strip('\"'), tab[2].strip('\"').strip(' ').strip('€').replace(',', '.'),
                        tab[3].strip('\"'), tab[4].strip('\"').strip(' ').replace(',', '.'))
            cursor.execute('INSERT INTO DetailTicket VALUES(?, ?, ?, ?, ?)', le_tuple)
            connect.commit()
        except Exception as e :
        # On devra gérer les diffrentes erreures, si une ligne ne s'execute pas pcq'elle existe déjà, inutile de rollback
            print("Erreur ->", e)
            connect.rollback()
        finally :
            connect.close()

    def __str__(self):
        print(self.id_ticket + self.id_prod)
