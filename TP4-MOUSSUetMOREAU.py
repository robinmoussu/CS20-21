#TP4 MOUSSU Guillemot & MOREAU Noé



#Une petite fonction

#1)Renvoie la factorielle d'un entier n positif (par deux méthodes).
def factorielle_recursif(n):
    if n==0:
        resultat=1
    else:
        resultat=n*factorielle_recursif(n-1)
    return resultat

def factorielle_iteratif(n):
    resultat=1
    for k in range(n,1,-1):
        resultat=resultat*k
    return resultat

#2)Le nombre 12! vaut 479 001 600.

#3)Pour 1! : 0 multiplication, pour 1! : 0 multiplication, pour 2!=2x1 : 1 multiplication.
#  Pour 3!=3x2x1 : 2 multiplucations. Donc pour n!=nx(n-1)x...x1 il y a n-1 multiplications.







#Manipulation de tableaux
#Soustraction et produit

#Créé une matrice de None, de dimensions de la matrice d'entrée
def creer_matrice_None(matrice):
    nbLignes=len(matrice)
    nbColonnes=len(matrice[0])
    matriceNone=[None]*nbLignes
    for indiceLigne in range(nbLignes):
        matriceNone[indiceLigne]=[None]*nbColonnes
    return matriceNone

#Soustrait 2 matrices de même dimensions
def soustraction_matrice(matrice1,matrice2):
    nbLignes=len(matrice1)
    nbColonnes=len(matrice1[0])
    matriceResultat=creer_matrice_None(matrice1)
    for indiceLigne in range(nbLignes):
        for indiceColonne in range(nbColonnes):
            matriceResultat[indiceLigne][indiceColonne]=matrice1[indiceLigne][indiceColonne]-matrice2[indiceLigne][indiceColonne]
    return matriceResultat


#Multiple une matrice par un coefficient réél
def multiplier_matrice(matrice,coefficient):
    nbLignes=len(matrice)
    nbColonnes=len(matrice[0])
    matriceResultat=creer_matrice_None(matrice)
    for indiceLigne in range(nbLignes):
        for indiceColonne in range(nbColonnes):
            matriceResultat[indiceLigne][indiceColonne]=matrice[indiceLigne][indiceColonne]*coefficient
    return matriceResultat








#Les ensembles

#Retourne l'intersection de 2 ensembles (listes) d'entiers
def intersection_ensembles(ensemble1,ensemble2):
    ensemble_resultat=[]
    if len(ensemble1)<=len(ensemble2):
        ensemble_petit=ensemble1
        ensemble_grand=ensemble2
    else:
        ensemble_petit=ensemble2
        ensemble_grand=ensemble1
    for element in ensemble_petit:
        if (element in ensemble_grand) and not(element in ensemble_resultat): #l'utilisation de in n'a pas été formellement interdite
            ensemble_resultat+=[element]
    return ensemble_resultat


#Retourne la réunion de 2 ensembles (listes) d'entiers
def reunion_ensembles(ensemble1,ensemble2):
    ensemble_resultat=[]
    for element in ensemble1:
        if not(element in ensemble_resultat):
            ensemble_resultat+=[element]
    for element in ensemble2:
        if not(element in ensemble_resultat):
            ensemble_resultat+=[element]
    return ensemble_resultat        
        

#Retourne la différence de 2 ensembles (listes) d'entiers (ensemble1 privé de ensemble2)
def difference_ensembles(ensemble1,ensemble2):
    ensemble_resultat=[]
    intersection=intersection_ensembles(ensemble1,ensemble2)
    for element in ensemble1:
        if not(element in ensemble_resultat) and not(element in intersection):
            ensemble_resultat+=[element]
    return ensemble_resultat


#Retourne un booléen True si ensemble1 est inclus dans ensemble2 (False sinon)
def inclusion(ensemble1,ensemble2):
    inclusion=True
    indice=0
    while inclusion==True and indice<len(ensemble1):
        inclusion=ensemble1[indice] in ensemble2
        indice+=1
    return inclusion






#Palidromes

#Renvoie True si le mot rentré est un palindrome (False sinon) ex: kayak
def mot_palindrome(mot):
    decoupage_mot=list(mot)
    mot_envers=[]
    for indice in range(len(decoupage_mot)-1,-1,-1):
        mot_envers+=decoupage_mot[indice]
    if decoupage_mot==mot_envers:
        resultat=True
    else:
        resultat=False
    return resultat
        


#Renvoie True si la phrase rentrée est un palindrome (False sinon). Peut contenir apostrophes et espaces.
def phrase_palindrome(phrase):
    decoupage_phrase=[]
    for element in phrase:
        if not(element in [" ","'"]):
            decoupage_phrase+=element
    phrase_envers=[]
    for indice in range(len(decoupage_phrase)-1,-1,-1):
        phrase_envers+=decoupage_phrase[indice]
    if decoupage_phrase==phrase_envers:
        resultat=True
    else:
        resultat=False
    return resultat