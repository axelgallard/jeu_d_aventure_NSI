"""
Programme réalisé par Gallard Axel 1G9
"""
import pygame

statut_porte=0
def glob_statut_porte():
    global statut_porte
    statut_porte=1

code_capsule=0
def glob_code_capsule():
    global code_capsule
    code_capsule=1

message=''
def statut_message(msg):
    global message
    message=msg

porte_prec=0
def sau_porte_prec(num_piece):
    global porte_prec
    porte_prec=num_piece
#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((720,480))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
image1=pygame.image.load("chambre.png")
image2=pygame.image.load("couloir_1.png")
image3=pygame.image.load("salle_des_machines.png")
image4=pygame.image.load("armurerie.png")
image5=pygame.image.load("hall.png")
image6=pygame.image.load("garde_manger.png")
image7=pygame.image.load("zone_de_stockage.png")
image8=pygame.image.load("couloir_2.png")
image9=pygame.image.load("cockpit.png")
image10=pygame.image.load("capsule_d_evacuation.png")
plan=pygame.image.load("plan_avec_fond.png")
tuto=pygame.image.load("tuto.png")
fin=pygame.image.load("ecran_fin.png")
text1 = font.render("Chambre:Je ne pense pas qu'il y'ait grand chose à faire ici", True, (0,0,0),(255,255,255))
text2 = font.render("Couloir:Il  me permet d'aller dans plusieurs pièces", True, (0,0,0),(255,255,255))
text3 = font.render("Réacteur:Il vaudrait mieux ne toucher à rien si vous tenez à la vie", True, (0,0,0),(255,255,255))
text4 = font.render("Armurerie:Ici vous trouverez le code pour accéder aux capsules", True, (0,0,0),(255,255,255))
text5 = font.render("Hall:cette vue m'impressionne toujours autant", True, (0,0,0),(255,255,255))
text6 = font.render("Garde manger:Vous n'auriez jamais tenu le coup sans lui", True, (0,0,0),(255,255,255))
text7 = font.render("Zone de stockage:C'est ici que vous rangez les minerais que vous récoltez", True, (0,0,0),(255,255,255))
text8 = font.render("Couloir:Il  me permet d'aller dans plusieurs pièces", True, (0,0,0),(255,255,255))
text9 = font.render("Cockpit:Vous appuyez sur un bouton pour ouvrir l'armurerie", True, (0,0,0),(255,255,255))
text10 = font.render("Vous êtes enfin arrivé à la capsule vous allez pouvoir avoir la vie sauve",True, (0,0,0),(255,255,255))
text_plan = font.render("appuyer sur r pour retourner dans le jeu", True, (0,0,0),(255,255,255))

dansQuellePierceEstLePersonnage=11

def decrireLaPiece(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))
        fenetre.blit(text1,(0,400))
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(0,400))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(0,400))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(0,400))
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(0,400))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(0,400))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(0,400))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(0,400))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(0,400))
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(0,400))
    elif piece==11:
        fenetre.blit(tuto,(0,0))
    elif piece==12:
        fenetre.blit(plan,(0,0))
        fenetre.blit(text_plan,(0,450))
    elif piece==13:
        fenetre.blit(fin,(0,0))
    fenetre.blit(font.render(message,True, (0,0,0),(255,255,255)),(0,440))


def decision(direction,piece):
    print("Vous avez appuyer sur ",direction)
    memorisePiece=piece
    statut_message("")
    #lancer le jeu et finir le jeu
    if direction=='e':
        if piece==11:
            piece=1
        elif piece==10:
            piece=13
    #ouvrir carte avant début du jeu
    if direction=='r':
        if piece !=12:
            sau_porte_prec(piece)
            piece=12
        elif piece==12:
            piece=porte_prec
    #appuyez sur "z" pour que le personnage aille au nord
    if direction=='z':
        if piece==2:
            piece=1
        elif piece==4:
            piece=2
        elif piece==5:
            piece=6
        elif piece==7:
            piece=5
        elif piece==10:
            piece=8
    #appuyez sur "s" pour que le personnage aille au sud
    elif direction=='s':
        if piece==1:
            piece=2
        elif piece==2:
            if statut_porte==0:
                statut_message("la porte est verouillée ! vous pourrez l'ouvrir depuis une pièce du vaisseau")
            else:
                glob_code_capsule()
                statut_message("vous avez trouvé le code de la capsule")
                piece=4
        elif piece==6:
            piece=5
        elif piece==5:
            piece=7
        elif piece==8:
            if code_capsule==0:
                statut_message("vous avez besoin d'un code qui se situe dans l'une des pièces du vaisseau pour ouvrir cette porte")
            else:
                piece=10
                statut_message("appuyer sur e pour finir la partie")
    #appuyez sur "d" pour que le personnage aille l'est
    elif direction=='d':
        if piece==3:
            piece=2
        elif piece==2:
            piece=5
        elif piece==5:
            piece=8
        elif piece==8:
            glob_statut_porte()
            statut_message("vous venez de déverouiller l'armurerie")
            piece=9
    #appuyez sur "q" pour que le personnage aille l'ouest
    elif direction=='q':
        if piece==2:
            piece=3
        elif piece==5:
            piece=2
        elif piece==8:
            piece=5
        if piece==9:
            piece=8
    if message==(""):
        if memorisePiece==piece:
                statut_message("Il n'y a pas de pièce dans cette direction")
    else:
        print("Je vais aller voir la pièce no ",piece)
    return piece



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'a': #touche a pour quitter
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    pygame.display.flip()
pygame.quit()

