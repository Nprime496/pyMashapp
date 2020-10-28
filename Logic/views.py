from django.shortcuts import render
import csv
import codecs
import pandas as pd
from .logic import pair
from django.core.mail import send_mail


# Create your views here.

def home(request):
	return render(request,'home.html')
    

def read_csv(request):
    if request.POST and request.FILES:
        csvfile_parrains = request.FILES['csv_file_parrains']
        csvfile_filleuls = request.FILES['csv_file_filleuls']

        csvref_parrains = request.FILES['csv_reference_parrains']
        csvref_filleuls = request.FILES['csv_reference_filleuls']
        
        resultat=pair(csvfile_parrains,csvref_parrains,csvfile_filleuls,csvref_filleuls)
        
        #data_par=pd.read_csv(csvfile_parrains)
        print("resultat\n",resultat)
    return render(request, "presentation.html", locals())



def mail_parrain(dest,name_par,num_par=None):
        send_mail(
        'COPA ENSPY GI 2023',
        'Salut à toi, le filleul qui t\'a été attribué est {}, nous comptons sur toi pour l\'aider au mieux dans son insertion au prestigieux département de Génie Informatique. tu peux le contacter au numéro http://wa.me/+237683577764'.format(name_par),
        'nnanejunior@gmail.com',
        [dest],
        fail_silently=False,)

def mail_filleul(dest,name_fil,num_fil=None):
        send_mail(
         'COPA ENSPY GI 2023',
        'Salut à toi, le parrain qui t\'a été attribué est {}, mais le Polytechnique est une famille et le génie informatique ne fait pas exception, chacun de test ainés académique pourra te prodiguer les conseils nécessaires. tu peux le contacter au numéro http://wa.me/+237683577764'.format(name_par),
       'nnanejunior@gmail.com',
        [dest],
        fail_silently=False,)
def send_a_mail(request):
    for parrain in resultat:
        name_par=parrain[0]
        for filleul in parrain[1]:
            name_fil=filleul[0]
            mail_filleul(name_par,name_par)
            mail_parrain(name_fil,name_fil)
    print("finished")
    return render(request, "home.html", locals())


#lire le .csv
#une fois qu'il est lu, il est techniquement possible d'avoir une liste de parrains et de filleuls dans des fichiers differents
# utiliser ces listes pour populer les Google forms, 