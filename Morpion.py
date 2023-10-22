import numpy as np

def taille_plateau(n=3):
    plateau = np.zeros((n,n))
    return plateau



def coup_possible(plateau,i,j):
    if i > len(plateau) or j> len(plateau) or plateau[i][j]!=0:
        return False
    return True

def partie_finie_egalite(plateau):
    ligne,colonne = len(plateau)-1,len(plateau)-1
    for i in range (ligne):
        for j in range (colonne):
                if plateau[i][j]==0:
                    return False
    return True, plateau




def partie_finie_victoire(plateau):
    L=[]
    victoire1=[1,1,1]
    victoire2=[2,2,2]
    for i in range (len(plateau)):
        for j in plateau[i]:
            L.append(j)
            if L==victoire1 or L==victoire2:
                return True,i,"ligne"
        L=[]
    for i in range(len(plateau)):
        for j in range (len(plateau)):
            L.append(plateau[j][i])
            if L == victoire1 or L==victoire2:   return True,j-1 ,"colonne"
        L=[]
    for i in range (len(plateau)):
        L.append(plateau[i][i])
    if L==victoire1 or L==victoire2:
        return True,"diag"
    L=[]
    plateau=np.fliplr(plateau)
    for j in range (len(plateau)):
        L.append(plateau[j][j])
    if L==victoire1 or L==victoire2:
        return True,"diag"

    return False

def coup(plateau,i,j,joueur):
    plateau[i][j]=joueur
    return plateau



def partie(plateau,i,j,joueur):
    if coup_possible(plateau,i,j):
        print("coup possible")
        coup(plateau,i,j,joueur)
        if partie_finie_victoire(plateau):
            return plateau,"victoire"
        if partie_finie_egalite(plateau):
            return plateau,"exaequo"
    else:
        print("coup pas possible")
    return plateau

















