import math
import numpy as np
import pygame
import sys

#Constante du jeu
ROW = 6
COLUMN = 7
RAYON = 45

def initialisationGrille():
    grille = np.zeros((ROW,COLUMN))
    return grille

#Création de la grille en interface graphique correspondant à la matrice
def grille(board):
    for c in range(COLUMN):
        for r in range(ROW):
            pygame.draw.rect(screen,(33,66,124), (c*100, (r+1)*100, 100,100))
            pygame.draw.circle(screen, (0,0,0),(c*100+50,(r*100 + 150)),RAYON)
    
    for c in range(COLUMN):
        for r in range(ROW):
            if board[r][c] == 1:
                pygame.draw.circle(screen, (255,0,0),(c*100+50,height - (r*100 +50)),RAYON)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, (255,255,0),(c*100+50,height - (r*100 +50)),RAYON)
    pygame.display.update() 
      
#Verifie si on a 4 pions alignés
def victoire(grille,pion):
    #Alignement horizontale
    for c in range(COLUMN -3):
        for r in range(ROW):
            if grille[r][c] == pion and grille[r][c+1] == pion and grille[r][c+2] == pion and grille[r][c+3] == pion :
                return True

    #Alignement verticale
    for c in range(COLUMN):
        for r in range(ROW - 3):
            if grille[r][c] == pion and grille[r+1][c] == pion and grille[r+2][c] == pion and grille[r+3][c] == pion :
                return True

    #Alignement diagonales
    for c in range(COLUMN -3):
        for r in range(ROW - 3):
            if grille[r][c] == pion and grille[r+1][c+1] == pion and grille[r+2][c+2] == pion and grille[r+3][c+3] == pion :
                return True
    #Alignement anti-diagonales
    for c in range(COLUMN):
        for r in range(3,ROW):
            if grille[r][c] == pion and grille[r-1][c] == pion and grille[r-2][c] == pion and grille[r-3][c] == pion :
                return True

def grilleRemplie(board):
    isFull = True
    for c in range(COLUMN):
        for r in range(ROW):
            if board[r][c] == 0:
               isFull = False                 
               break
    return isFull

def next_open_row(grille, col):
    for r in range(ROW):
        if grille[r][col] == 0:
            return r
                        
isGameOver = False
grilleJeu = initialisationGrille()
pygame.init()
pygame.display.set_caption('Puissance 4')

width = COLUMN * 100
height = (ROW + 1) * 100
tour = 0

font = pygame.font.SysFont("Courier",50)
screen = pygame.display.set_mode((width,height)) 
grille(grilleJeu)
pygame.display.update()

while not isGameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()   
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,(0,0,0),(0,0,width,100))
            posx = event.pos[0]
            if tour == 0:
                pygame.draw.circle(screen,(255,0,0),(posx,50),RAYON)
            else:
                pygame.draw.circle(screen,(255,255,0),(posx,50),RAYON)
            pygame.display.update()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,(0,0,0),(0,0,width,100))
            if tour == 0:
               posx = event.pos[0]
               col =  int(math.floor(posx/100))
               
               if(grilleJeu[ROW -1][col] == 0):
                row = next_open_row(grilleJeu, col)
                grilleJeu[row][col] = 1         
                #print(f'({row},{col})')
                if victoire(grilleJeu,1):
                    label = font.render("victoire du joueur 1!!",1,(255,0,0))
                    screen.blit(label,(40,10))
                    isGameOver = True             
            
            else:
                posx = event.pos[0]
                col =  int(math.floor(posx/100))
                if(grilleJeu[ROW -1][col] == 0):
                    row = next_open_row(grilleJeu, col)
                    grilleJeu[row][col] = 2         
                    #print(f'({row},{col})')
                    if victoire(grilleJeu,2):
                        label = font.render("victoire du joueur 2!!",1,(255,255,0))
                        screen.blit(label,(40,10))
                        isGameOver = True
           
            if grilleRemplie(grilleJeu) and not victoire(grilleJeu,1) and not victoire(grilleJeu,1):
                label = font.render("Match nul,grille remplie",1,(0,255,0))
                screen.blit(label,(40,10))
                isGameOver = True
                
            tour += 1
            tour %= 2 
            grille(grilleJeu)                          
            
            if isGameOver:
                pygame.time.wait(3000)  