from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm

# Create your views here.

def list_view(request):
	context = {
		"pets" : Pet.objects.filter(available=True)
	}
	return render(request, 'list_page.html', context)

def detail_view(request, pet_id):
	context = {
		"pet": Pet.objects.get(id = pet_id)
	}
	return render(request, 'detail_view.html', context)

def create_pet(request):
	form = PetForm()
	if request.method == "POST":
		form = PetForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('list-view')

	context = {
		"form": form
	}
	return render(request, 'create_page.html', context)

def update_pet(request, pet_id):
	pet = Pet.objects.get(id = pet_id)
	form = PetForm(instance=pet)
	if request.method == "POST":
		form = PetForm(request.POST, request.FILES, instance=pet)
		if form.is_valid():
			form.save()
			return redirect('list-view')
	context = {
	"pet" : pet, 
	"form" : form
	}
	return render(request, 'pet_update.html', context)

def delete_pet(request, pet_id):
	Pet.objects.get(id=pet_id).delete()
	return redirect('list-view')


