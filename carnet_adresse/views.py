from django.shortcuts import render, redirect
from . models import Adresse
from . forms import AdresseFormulaire
from django.contrib import messages

def home(request):
	all_adresses = Adresse.objects.all
	return render(request, 'home.html', {'all_adresses':all_adresses})

def ajouter(request):
	if request.method == "POST":
		form = AdresseFormulaire(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Le contact a été ajouté!'))
			return redirect('home')
		else:
			messages.success(request, ('Il y a eu une erreur...'))
			return render(request, 'ajouter.html', {})
	else:
		return render(request, 'ajouter.html', {})

def editer(request,list_id):
	if request.method == "POST":
		current_adresse = Adresse.objects.get(pk=list_id)
		form = AdresseFormulaire(request.POST or None, instance=current_adresse)
		if form.is_valid():
			form.save()
			messages.success(request, ('Le contact a été modifié!'))
			return redirect('home')
		else:
			messages.success(request, ('Il y a eu une erreur...'))
			return render(request, 'editer.html', {})
	else:
		get_adresse = Adresse.objects.get(pk=list_id)
		return render(request, 'editer.html', {'get_adresse':get_adresse})

def effacer(request,list_id):
	if request.method == "POST":
		current_adresse = Adresse.objects.get(pk=list_id)
		current_adresse.delete()
		messages.success(request, ('Le contact a été supprimé!'))
		return redirect('home')
	else:
		messages.success(request, ('Pas de suppression possible...'))
		return redirect('home')

