from fltk import *
from math import *
import numpy as np


def vecteur_vitesse():
    
    for i in range:
        grille_x=[i]
    for n in range:
        grille_y=[n]
        
    grille=[i,n]
    
    vecteur = np.array([0,0])
    
    
def bas (vecteur, vitesse):
    vecteur = vecteur + (0,1*vitesse)
    
def haut (vecteur,vitesse):
    vecteur = vecteur + (1*vitesse,0)
    
def droite(vecteur,vitesse):
    vecteur = vecteur + (vitesse+1,0)

def gauche(vecteur,vitesse):
    vecteur = vecteur + (vitesse-1)
    
    
    
    
    
    

   
       
    
    

    


    
  
    
    





cree_fenetre(400, 300)
attend_ev()  
ferme_fenetre()