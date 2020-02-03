from Classes.Magasin import Magasin
import matplotlib.pyplot as plt
import pylab


def show_ca_mensuel():
    #plt.xlabel('Mois')
    #plt.ylabel('Chiffre d\'affaire')
    #for i in range(1,12):
    #    plt.plot(i, magasin.get_ca(i), '+--')
    #plt.show()

   
   fig = plt.figure()

   BarName = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']

   height = []
   width = 0.5
   for i in range(0,12):
        if Magasin.get_ca_mois(i+1) != None :
            plt.bar(BarName[i], Magasin.get_ca_mois(i+1))
   plt.xlabel('Mois')
   plt.ylabel('Chiffre d\'affaire')
   plt.grid()
   plt.show()

def show_moyenne_ticket_mensuel():
    fig = plt.figure()


    BarName = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']

    height = []
    width = 0.5
    for i in range(0,12):
        if Magasin.get_moyenne_ticket_mois(i+1) != None :
            plt.bar(BarName[i], float(str(Magasin.get_moyenne_ticket_mois(i+1))))
    plt.xlabel('Mois')
    plt.ylabel('Chiffre d\'affaire')
    plt.grid()
    plt.show()

def show_evo_mensual_categ() :
    fig = plt.figure()


    BarName = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']

    height = []
    width = 0.5
    for i in range(0,12):
        if Magasin.get_ca_mois_categ(i+1, 'Algues') != None :
            plt.bar(BarName[i], float(str(Magasin.get_ca_mois_categ(i+1, 'Algues'))))
        if Magasin.get_ca_mois_categ(i+1, 'Animaux') != None :
            plt.bar(BarName[i], float(str(Magasin.get_ca_mois_categ(i+1, 'Animaux'))))
    plt.xlabel('Mois')
    plt.ylabel('Chiffre d\'affaire')
    plt.grid()
    plt.show()