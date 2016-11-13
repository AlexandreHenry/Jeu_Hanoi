

class Tour:
    def __init__(self,taille_max):
        self.nb_disques = 0
        self.disques = taille_max * [0]
    

class Hanoi:
    
    def __init__ (self, hauteur_max):
        self.hauteur=hauteur_max
        self.tours = [Tour(hauteur_max) for t in range(3)]
        
        for etage in range(hauteur_max):
            self.tours[0].disques[etage] = hauteur_max - etage
            
        self.tours[0].nb_disques = hauteur_max
        
def Chaine_etage(taille, largeur):
    espace =" "*(largeur-taille)
    chaine = ""
    if (taille>0):
        disque = "="*taille
        chaine = espace + "<" + disque + "!" + disque + ">" + espace
    else:
        chaine = espace + " ! " + espace
    return chaine
    
def Afficher_jeu(jeu):
    for etage in range(jeu.hauteur):
        etage_correct = jeu.hauteur - etage - 1        
        for colonne in range(3):
            taille = jeu.tours[colonne].disques[etage_correct]
            print (Chaine_etage(taille, jeu.hauteur), end='')
        print()

def Demander_tour_depart(jeu):
    print("Tour de depart ?")
    tour_depart=int(input())
    return tour_depart - 1
    
def Demander_tour_arriver(jeu):
    print("Tour de arriver ?")
    tour_arriver=int(input())
    return tour_arriver - 1
    
def Est_fini(jeu):
    return jeu.tours[2].nb_disques == jeu.hauteur   
    
def Deplacer_Disque(jeu,depart, arriver):
    nb_disques_depart = jeu.tours[depart].nb_disques
    nb_disques_arriver = jeu.tours[arriver].nb_disques    
    disque_depart = jeu.tours[depart].disques[nb_disques_depart-1]    
    
    jeu.tours[depart].disques[nb_disques_depart-1]=0
    jeu.tours[depart].nb_disques -= 1
    
    jeu.tours[arriver].disques[nb_disques_arriver]=disque_depart
    jeu.tours[arriver].nb_disques +=1

def Tour_depart_valide(jeu,depart):
    if depart < 0:
        return False
    if depart > 2:
        return False
    
    return jeu.tours[depart].nb_disques > 0
    
def Tour_arriver_valide(jeu,depart,arriver):
    if arriver<0:
        return False
    if arriver>2:
        return False
    
    dernier_disque_depart = jeu.tours[depart].nb_disques
    dernier_disque_arriver = jeu.tours[arriver].nb_disques
    
    if dernier_disque_arriver ==0:
        return True
        
    disque_arriver = jeu.tours[arriver].disques[dernier_disque_arriver-1]
    disque_depart = jeu.tours[depart].disques[dernier_disque_depart-1]
    
    return disque_arriver > disque_depart

        
    


le_jeu = Hanoi(3)
nb_mouvement = 0
while (not Est_fini(le_jeu)):
    Afficher_jeu(le_jeu)
    tour_depart = Demander_tour_depart(le_jeu)
    if (Tour_depart_valide(le_jeu,tour_depart)):
        tour_arriver = Demander_tour_arriver(le_jeu)
        if (Tour_arriver_valide(le_jeu,tour_depart,tour_arriver)):
            Deplacer_Disque(le_jeu, tour_depart, tour_arriver)
            nb_mouvement +=1
        else:    
            print("Arrivee invalide !")
    else:
        print("Depart invalide !")
        
Afficher_jeu(le_jeu)
print("Felicitation !')
    
