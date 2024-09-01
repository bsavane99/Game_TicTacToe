import tkinter as tk

#Stockage des variables
boutons = [] 
joueur = 'X'
gagne = False

#Fonctions
def imprimer_gagnant():
    global gagne
    if gagne is False:
        gagne = True
        print('Le jeu est terminé! \nLe joueur ', joueur, ' a gagné le jeu!')

def changer_joueur():
    global joueur
    if joueur == 'X':
        joueur = '0'
    else:
        joueur = 'X'

def detecter_vict(colonne_clicke, ligne_clicke):
    #Victoir horizontale
    count=0
    for i in range(3):
        current_bouton = boutons[colonne_clicke][i]
        if current_bouton['text']==joueur:
            count += 1
    if count==3:
        imprimer_gagnant()

    #Victoir verticale
    count=0
    for i in range(3):
        current_bouton = boutons[i][ligne_clicke]
        if current_bouton['text']==joueur:
            count += 1
    if count==3:
        imprimer_gagnant()
    
    #Victoir diagonale
    count=0
    for i in range(3):
        current_bouton = boutons[i][i]
        if current_bouton['text']==joueur:
            count += 1
    if count==3:
        imprimer_gagnant()
        
    #Victoir diagonale inverse
    count=0
    for i in range(3):
        current_bouton = boutons[2-i][i]
        if current_bouton['text']==joueur:
            count += 1
    if count==3:
        imprimer_gagnant()
    #Detecter match nul
    if gagne is False:
        count=0
        for colonne in range(3):
            for ligne in range(3):
                current_bouton = boutons[colonne][ligne]
                if current_bouton['text']=='X' or current_bouton['text']=='0':
                    count += 1
        if count==9:
            print('Match nul!')  

#Placer les symboles sur la grille
def placer_symbol(colonne, ligne):
    bouton_clicke = boutons[colonne][ligne]
    if bouton_clicke['text']=='':
        if gagne is False:
            bouton_clicke.config(text=joueur)
            print(colonne, ligne)

            detecter_vict(colonne, ligne)
            changer_joueur()
    
#Dessiner des boutons dans la fenêtre d'espace
def draw_button():
    for colonne in range(3):
        boutons_col = []
        for ligne in range(3):
            bouton = tk.Button(
               espace, 
               font=('Arial', 20), 
               width=4, 
               height=2, 
               border=5,
               background='orange',
               command=lambda c=colonne, l=ligne:placer_symbol(c, l) 
               )
            bouton.grid(column=colonne, row=ligne)
            boutons_col.append(bouton)
        boutons.append(boutons_col)

#Création de femêtre de jeux
espace = tk.Tk()
espace.title("TicTacToe")
espace.minsize(width=500, height=300)
espace.config(background='grey', border=5)
#Affichage
draw_button()
espace.mainloop()

