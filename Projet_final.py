from tkinter import *
from tkinter import font
import random
import os



Aléatoire = False
mots_possibles = []
mot_a_trouver = ""
score=0
NbreL=""
nb_max_essais = 11
nb_essais = 0
NmLi=11
ROUGE = "ROUGE"
txt_bnv="Bonjour ! \n Bienvenue dans MOTUS !\n\n Le but ? \n Trouver le plus de mots en 10 mins \n en ayant 11 essais par mot.\n\nVoici le CODE COULEUR : \n ROUGE = Bien placée \n JAUNE = Mal placée \n NOIR = Absente \n\nBon jeu !\n\n"

hauteur = 30 # hauteur d'une lettre
largeur = 20 # largeur d'une lettre

position_x = 330 #initalisation de la place des lettres proposées
position_y = 265

var_lettres = []
labels_lettres = []

mots = []
flags = []

fen=Tk() 
fen.title('MOTUS')  # titre de la fenetre
fen.iconbitmap("favicon.ico") # vignette motus 
Can = Canvas(fen,width=900, height=200, bg='white')
ImMotus = PhotoImage (file="Nm2.png") # rechercher pq il faut stoquer l'image dans une variable avant de las stoque dans item
item = Can.create_image(450,100,image=ImMotus)
Can.grid(row=0)

def commencer_mot ():
    global mot_a_trouver,mots,flags,NmLi #pour que les nouvelles valeurs soient accessibles ailleurs
    mot_a_trouver = random.choice(mots_possibles)
    position_indice = random.randint(0,NbreL-1)
    lettre_indice=mot_a_trouver[position_indice]
    print(mot_a_trouver) # a supprimer si on veux pas la solution en bas
    NmLi = 11
    svNbreE.set(str(NmLi))
    svNbrL.set("Le mot à trouver a "+str(NbreL)+" lettres.")
    svindice.set("INDICE : "+"_ "*(position_indice)+(lettre_indice)+" "+"_ "*(NbreL-position_indice-1)) #affichage indice
    
    mots = [" "*NbreL]*11
    flags = [["X"]*NbreL]*11

def initialiser(aleatoire, nombre):
    global Aléatoire , NbreL
    Aléatoire = aleatoire
    NbreL = nombre
    fen.geometry("901x600")
    svStatut.set(txt_bnv)
    fen.after(250,jouer_son) # latence en ms avant de jouer le son de motus pour que la fenettre est eu le temps de s'afficher
    fen.mainloop()

def commencer_partie():
    global score, NbreL, mots_possibles
    score=0
    Val["state"] = NORMAL
    boutondemarrer['state'] = DISABLED  # block le reset du mot + timer
    lbl["text"] = temps
    svStatut.set(txt_bnv)
    if Aléatoire :
        NbreL=random.randint(5,9)
    fichier_mot=open('dictionnaire'+str(NbreL)+'.txt','r')
    mots_possibles=fichier_mot.read().splitlines()
    fichier_mot.close()
    svNbreE.set(str(NmLi))
    lalargeur=400/NbreL

    for i in range(NbreL):
        Lettres[i].place(x=200+lalargeur*i, y=200, width=lalargeur, height=50)

    commencer_mot ()
    decompte()

def Afficher_les_differences(proposition_joueur,mot_a_trouver):
    liste_tags=['']*NbreL
    lettres_restantes = list(mot_a_trouver)
    
### on cherche les caracteres biens placés uniquement ###

    for i in range (NbreL):
       if proposition_joueur[i] == mot_a_trouver[i]:
        liste_tags[i]= 'B'
        lettres_restantes.remove(mot_a_trouver[i])

### on cherche ensuite les lettres mal placees ###
    
    for i in range (len(proposition_joueur)):
        if liste_tags[i] != 'B':
            if proposition_joueur[i] in lettres_restantes:
                liste_tags[i]= 'M'
                lettres_restantes.remove(proposition_joueur[i])
    return liste_tags # return pour stocker

def entree_mot() :
    global flags, score,NmLi
    le_mot = "" 
    for i in range (9):
        le_mot= le_mot+ Lettres[i].get()
        Mots[i].set("")
    le_mot = le_mot.upper() #passe le mot en maj en affichage, meme si deja en maj 

    NmLi=NmLi-1

    if len(le_mot) != NbreL:
        svStatut.set("⚠ ATTENTION ! ⚠ \n\n Il faut que le mot fasse "+str(NbreL)+" lettres. \n\n\n\n\n\n\n\n\n\n\n")
        NmLi=NmLi+1
        return

    if le_mot not in mots_possibles: # permet aussi de bloquer les chiffres dans les chaines de caracteres.
        svStatut.set("⚠ Le mot n'est pas dans le dictionnaire.\n\n""Merci de réessayer")
        NmLi=NmLi+1
        return

    mots.insert(0,le_mot)
    flags.insert(0, Afficher_les_differences(le_mot,mot_a_trouver))

    if le_mot == mot_a_trouver:
        score=score+1
        svStatut.set("Bien joué ton score est de "+str(score)+" point(s). Recommence directement !")
        commencer_mot()

    elif len(mots) == nb_max_essais*2: # pq multiplié par 2 ?
        svStatut.set("Tu as échoué à ce mot. \n\n Tu as dépassé le nombre d'essais maximum.\n\n Le mot était "+str(mot_a_trouver)+". \n\n Ton score est toujours de "+str(score)+" point(s).\n\n\n\n\n\n\n")
        commencer_mot()

### affichage de ttes les lettres + couleurs ###

    for m in range(11):
        for l in range(NbreL):
            var_lettres[m][l].set(mots[m][l]) # a quoi sert de mettre d'indice "m" et "l" ?
            couleur = "black" # couleur inicialisation

            if flags[m][l] == "B":
                couleur = "#FF0004" # code en hexadecimal d'une couleur : ROUGE
            elif flags[m][l] == "M":
                couleur = "#FFC100" # code en hexadecimal d'une couleur : JAUNE

            labels_lettres[m][l].configure(fg=couleur)
    svNbreE.set(str(NmLi))

# demander a thomas de me reexpliquer cette double boucle. pq dans une boucle ?

for m in range(11): # m est le numéro de la ligne qu'on créé
    ligne_lettres = [] # va stocker tous les string var d'une seule ligne
    ligne_labels = []
    for l in range(9): # l est le numéro de la lettre qu'on créé
        sv = StringVar()
        sv.set(" ")
        lefont=font.Font(family='Consolas', size=20)
        label = Label(fen, textvariable=sv, font=lefont)
        label.place(x= position_x + l*largeur, y=position_y + m*hauteur) # place au bonne endroit sur l'écran
        ligne_lettres.append(sv)
        ligne_labels.append(label)
    # on ajoute la ligne au tableau global
    var_lettres.append(ligne_lettres)
    labels_lettres.append(ligne_labels)

def decompte(): # timer
    time = int(lbl["text"])
    if time > 0 :
        lbl["text"]="%03d" %(time-1) # trois chiffres affichés en parmanance, sinon %02 pour 2 chiffres
        fen.after(1000,decompte) # en mili-seconde d'où 1000 ms = 1s
    elif time == 0 :
        svStatut.set("Partie terminée.\nTu as dépassé le temps accordé, le mot était "+str(mot_a_trouver)+".\nTon score est donc de "+str(score)+" point(s).\n\nRecommence !\n\n\n\n\n\n↓")
        boutondemarrer['state']=NORMAL
        Val["state"]=DISABLED

def jouer_son():
    if os.name=="nt": # Si c'est sur windows, par ce que windows = nt sur python, ne marche pas sur Lunux ou MAC os,ect.
        import winsound
        winsound.PlaySound("motus.wav", winsound.SND_FILENAME | winsound.SND_ASYNC) # joue le son pendant que le code s'execute, et donc sans le stop de 1 seconde. (dis asynchrone) - FILENAME = fichier - | = melange les deux infos en une variable unique

Val=Button(fen, text='VALIDER', command = entree_mot, width=30, height=40,font=font.Font(family="Consolas",size=12)) #bouton valider
Val.place(x=600,y=200, width=120, height=50)
Quit=Button(fen,text = 'QUITTER', command = fen.destroy, font=font.Font(family="Consolas",size=12),relief="raised")
Quit.place(x=720,y=548, width=180, height=52)
Val["state"] = DISABLED
lblNbreE = Label(fen,text= "Nombre d'essais restants :\n\n\n\n\n\n\n\n\n",font=font.Font(family="Consolas",size=8),relief="solid")
lblNbreE.place(x=720,y=298, width=180, height=175)
svNbreE = StringVar()
NbreE = Label(fen,textvariable=svNbreE,font=font.Font(family="Consolas",size=50))
NbreE.place(x=770,y=350,width=75, height=75)
temps = 600
lbl = Label(fen, text = temps, fg = '#AA0000', width = 5, font = "Time 50 bold",relief="solid")
lbl.place(x=720,y=200,width=180,height=100)
svNbrL= StringVar()
LblNbrL = Label(fen, textvariable=svNbrL, relief="solid")
LblNbrL.place(x=0,y=248,width=200, height=50)
svStatut = StringVar()
Labelstatut = Label(fen, textvariable=svStatut, width=31,wraplength=220, relief="solid") # 31 caractère, 225 pixels ( dans la police de base environ = à 8 pixels; donc difficile d'augmenter la police générale)
Labelstatut.place(x=0, y=296, width=200,height=304) # text commentaires/statut
boutondemarrer = Button(fen, text='COMMENCER',command=commencer_partie, font=font.Font(family="Consolas",size =15),relief="raised") # bouton demarer
boutondemarrer.place(x=720, y=473, width=180, height=75)
svindice = StringVar()
svindice.set("INDICE : ")
Labelindice = Label(fen,textvariable=svindice, font=font.Font(family="Consolas",size=10),relief="solid")
Labelindice.place(x=0,y=200, width=200, height=50)

Mots = []
Lettres = []

for i in range(9):
    Mots.append(StringVar())
    Mots[i].set("")
    Lettres.append(Entry(fen,bg="white",textvariable=Mots[i],font=font.Font(family="Consolas",size=20)))