# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 12:13:53 2020

@author: _Nprime496_
"""

"""
MASHAPP V1.0

Hey toi qui lit ceci, alors voilà le topo, ce programme se base sur l'algorithme de Gade,Chadley pour créer des "match" entre deux groupes.

voici les liens utiles à parcourir dans l'ordre susmentionné ;)


Okay après avoir parcouru ces liens, tu devrais avoir une meilleure idée de ce qui se trame ici, bon... l'algorithme de GeeksForGeeks a été modifié légèrement :) 
pour être plus adapté à nos besoins...les problèmes de la version originale sont:
    
- Nombre d'hommes et de femmes égal ce qui n'est pas très réaliste en vrai :( 
- Nombre de choix pour une personne restreint à un seul

Le code a de nombreux commentaires (on n'allait pas retraduire les commentaires de GFG quand même, et ça fait plus pro :) ), n'hésite pas à les lire si tu veux comprendre le pourquoi du comment.

avec la methode que j'ai faite, il y a un premier passage dans les choix où les meilleures associations sont retenues, et ensuite, on enleve ceux qui ont déjà été pris
du côté many et et on relance la boucle

"""
import pandas as pd
import numpy as np

SUFFIX_LEVEL="_pref"
IDENTIFIER="nom"
DELIMITER="\t"
CHOOSER="pref"
PHOTO="photo"
#NB: AJOUTER DES ASSERT POUR S'ASSURER QUE TOUT EST OK AVANT L'EXECUTION DU PROGRAMME
# Python3 program for stable marriage problem 
  
# Number of Men or Women 
  
# This function returns true if  
# woman 'w' prefers man 'm1' over man 'm' 
def wPrefersM1OverM(prefer, w, m, m1):
    N=len(prefer[0])#number of men
    # Check if w prefers m over her  
    # current engagment m1 
    for i in range(N): 
          
        # If m1 comes before m in lisr of w,  
        # then w prefers her current engagement, 
        # don't do anything 
        if (prefer[w][i] == m1): 
            return True
  
        # If m cmes before m1 in w's list,  
        # then free her current engagement  
        # and engage her with m 
        if (prefer[w][i] == m): 
            return False
  

# Prints stable matching for N boys and N girls.  
# Boys are numbered as 0 to N-1.  
# Girls are numbereed as N to 2N-1. 
def stableMarriage(mprefer,wprefer,alreadyTaken=[]):
    Nm=len(mprefer)
    Nw=len(wprefer)
    result={i:[] for i in range(Nw)}
    # Stores partner of women. This is our output  
    # array that stores paing information.  
    # The value of wPartner[i] indicates the partner  
    # assigned to woman N+i. Note that the woman numbers  
    # between N and 2*N-1. The value -1 indicates  
    # that (N+i)'th woman is free 
    
  
    # An array to store availability of men.  
    # If mFree[i] is false, then man 'i' is free, 
    # otherwise engaged. 


    print(alreadyTaken)
    tmpwPartner=[]
    
    while len(alreadyTaken)<Nm:
    
        mFree = [i in alreadyTaken for i in range(Nm)] 
        wPartner = [-1 for i in range(Nw)] 
      
        freeCount = Nm-len(alreadyTaken)
        
        c=0
        # While there are free men 
        while (freeCount > 0):
            if tmpwPartner==wPartner:
                c+=1
            else:
                c=0
            if c>=Nm:
                break
                
            tmpwPartner=wPartner.copy()
            # Pick the first free man (we could pick any) 
            m = 0
            while (m < Nm): 
                if (mFree[m] == False): 
                    break
                m += 1
      
            # One by one go to all women according to  
            # m's preferences. Here m is the picked free man 
            i = 0
            while i < Nw and mFree[m] == False: 
                w = mprefer[m][i] 
      
                # The woman of preference is free,  
                # w and m become partners (Note that  
                # the partnership maybe changed later).  
                # So we can say they are engaged not married 
                #print("w",w)
                #print("Nw",Nw)
                if (wPartner[w] == -1):
                    
                    wPartner[w] = m 
                    mFree[m] = True
                    freeCount -= 1
      
                else:  
                      
                    # If w is not free 
                    # Find current engagement of w 
                    m1 = wPartner[w] 
      
                    # If w prefers m over her current engagement m1, 
                    # then break the engagement between w and m1 and 
                    # engage m with w. 
                    if (wPrefersM1OverM(wprefer, w, m, m1) == False): 
                        wPartner[w] = m 
                        mFree[m] = True
                        mFree[m1] = False
                i += 1
                #a=input()
                #input()
                # End of Else 
            # End of the for loop that goes  
            # to all women in m's list 
        # End of main while loop 
        # Prthe solution 
        
        for i in range(Nw):
            if(wPartner[i]!=-1):
                result[i].append(wPartner[i])
        tmpalreadytaken=wPartner.copy()
        wprefer=removeAlreadyTaken(wprefer,tmpalreadytaken)
        alreadyTaken+=tmpalreadytaken
    print("result ",result)
    return result

    
def clean(datframe,dataframe_reference,columns):
    
    datframe = datframe.drop_duplicates(subset=['nom'], keep='last')
    datframe= pd.concat([datframe,dataframe_reference],sort=False)
    print("merged\n",datframe)
    datframe = datframe.reset_index(drop=True)
    datframe = datframe.drop_duplicates(subset = ['nom'], keep='first')
    for column in columns:
        datframe[column]=datframe[column].fillna("aucun")
        if (column+SUFFIX_LEVEL in datframe.columns):
            datframe[column+SUFFIX_LEVEL]=datframe[column+SUFFIX_LEVEL].fillna(0)
    print("cleaned\n",datframe)
    return datframe

  
def removeAlreadyTaken(prefer,alreadyTaken):
    #change order in preference list to make already taken elements less important than those wich need to be chosen
    for preference in prefer:
        i=0
        for j in range(len(preference)):
            if preference[j] not in alreadyTaken:
                tmp=preference[j]
                preference[j]=preference[i]
                preference[i]=tmp
                i+=1
    return prefer
    
#une limitation est qu'il est possible d'avoir des parrains sans filleuls
#un moyen d'y remedier est d'empêcher qu'un parrain ait deux filleuls quand un autre n'en a pas

# Driver Code 
def produce_scores_from_Dataframes(dataframe_reference,dataframe_candidate,consider_columns=None):
    #not efficient we must maybe change the order of the loop
    if consider_columns is None:
        consider_columns=dataframe_reference.columns
    assert all(column in dataframe_candidate.columns for column in consider_columns),"MashApp: Columns to consider when matching should have the same name in reference and candidate dataframes {}".format(consider_columns)
    scores_all=np.array([],dtype=int).reshape((len(dataframe_candidate),0))#les colonnes sont les annotateurs et les lignes sont les annotés
    
    for index,row in dataframe_reference.iterrows():
        scores_c=np.zeros(shape=(len(dataframe_candidate),1))
        for column in row.index:
            if column in consider_columns:
                foo = lambda x: pd.Series([i.strip() for i in x.split(",")])#to create multiple columns according to the different values in cell
                choices_references=pd.Series(row[column])#get row column as a series
                choices_candidates=dataframe_candidate[column]
                col_choices_c=choices_candidates.apply(foo)
                
                col_dummies_c=pd.get_dummies(col_choices_c, prefix='class')#obtain all values on different columns
                col_dummies_c=col_dummies_c.groupby(lambda x:x,axis=1).sum()#a weird problem forces us to use it to ensure that the columns are distinct
                
                col_choices_r=choices_references.apply(foo)
                col_dummies_r=pd.get_dummies(col_choices_r, prefix='class')
                coef=row[column+SUFFIX_LEVEL] if column+SUFFIX_LEVEL in row.index else 5

                allowed=[col for col in col_dummies_r.columns if col in col_dummies_c.columns]#columns which are only present in reference can't be used so must be removed
                number_items_common=col_dummies_r[allowed].dot(col_dummies_c[allowed].T).T
                score_for_column=number_items_common*coef-(len(allowed)-number_items_common)*0.125
                scores_c=scores_c+np.array(score_for_column)
        scores_all=np.hstack((scores_all,scores_c))
    return pd.DataFrame(scores_all)
 
def get_pref_from_scores(dataframe_scores):
    l=[]
    for column in dataframe_scores:
        l.append(list(dataframe_scores[column].sort_values(ascending=False).index))
    return l
    

def get_pref_with_choice(id_one,pref_list,ones,others,column):
    try:
        a=others[others[IDENTIFIER]==ones.iloc[id_one][column]]
        idx=a.index[0]
        pref_list.remove(idx)
        return [idx]+pref_list
    except Exception as e:
        print(e)
        return pref_list#s'il y a une erreur, on considère qu'il n'y a pas de parrain préféré

def get_final_pref(pref_lists,ones,others,column=CHOOSER):
    r=[]
    for i,el in enumerate(pref_lists):
        r.append(get_pref_with_choice(i,el,ones,others,column))
    return r
        


def create_pair(parrains,filleuls,colonnes,pref_column=None):
    scores_of_filleuls_on_parrains=produce_scores_from_Dataframes(parrains,filleuls,colonnes)
    pref_filleuls=get_pref_from_scores(scores_of_filleuls_on_parrains)
    pref_filleuls=get_final_pref(pref_filleuls,parrains,filleuls)
    scores_of_parrains_on_filleuls=produce_scores_from_Dataframes(filleuls,parrains,colonnes)
    print(scores_of_filleuls_on_parrains)
    pref_parrains=get_pref_from_scores(scores_of_parrains_on_filleuls)
    pref_parrains=get_final_pref(pref_parrains,filleuls,parrains)
    r=stableMarriage(pref_filleuls,pref_parrains,alreadyTaken=[])
    return r

def get_relevant(dataframe,indice,columns):
    e=dataframe.iloc[indice][columns]
    return e

def preprocess_photo(string):
    return ""
    return string.replace("open","uc")


def print_understandable(resultat,parrains,filleuls):
    r={}
    for item in resultat.keys():
        t=(parrains.iloc[item][IDENTIFIER],preprocess_photo(parrains.iloc[item][PHOTO]))
        r[t]=[]
        for el in resultat[item]:
            dt=(filleuls.iloc[el][IDENTIFIER],preprocess_photo(filleuls.iloc[el][PHOTO]))
            r[t].append(dt)
    return r

def pair(csvfile_parrains,csvref_parrains,csvfile_filleuls,csvref_filleuls):
    parrains=pd.read_csv(csvfile_filleuls,encoding="utf8",delimiter=DELIMITER)#inversion!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    parrains_ref=pd.read_excel(csvref_parrains,encoding="utf8")
    print(parrains)
    filleuls=pd.read_csv(csvfile_parrains,encoding="utf8",delimiter=DELIMITER)#inversion@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    filleuls_ref=pd.read_excel(csvref_filleuls,encoding="utf8")
    columns=["langue","loisir"]
    filleuls = clean(filleuls,filleuls_ref,columns)
    parrains = clean(parrains,parrains_ref,columns)
    resultat = create_pair(parrains,filleuls,columns)
    return print_understandable(resultat,filleuls,parrains)
  


# This code is contributed by Mohit Kumar & N'nane (3GI)