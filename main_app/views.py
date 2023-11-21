from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Mythology, God
from .forms import PrayerForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def mythologies_index(request):
  mythologies = Mythology.objects.all()
  return render(request, 'mythologies/index.html', {
    'mythologies': mythologies
  })

def mythologies_detail(request, mythology_id):
  mythology = Mythology.objects.get(id=mythology_id)
  id_list = mythology.gods.all().values_list('id')
  gods_mythology_doesnt_have = God.objects.exclude(id__in=id_list)
  return render(request, 'mythologies/detail.html', {
    'mythology': mythology,
    'gods': gods_mythology_doesnt_have
  })

class MythologyCreate(CreateView):
  model = Mythology
  fields = ['name', 'region']
  success_url = '/mythologies/'

class MythologyUpdate(UpdateView):
  model = Mythology
  fields = ['region']

class MythologyDelete(DeleteView):
  model = Mythology
  success_url = '/mythologies'

class GodList(ListView):
  model = God

class GodDetail(DetailView):
  model = God

class GodCreate(CreateView):
  model = God
  fields = '__all__'
  success_url = '/gods'

class GodUpdate(UpdateView):
  model = God
  fields = ['name', 'description']

class GodDelete(DeleteView):
  model = God
  success_url = '/gods'

def assoc_god(request, mythology_id, god_id):
  # Note that you can pass a god's id instead of the whole god object
  Mythology.objects.get(id=mythology_id).gods.add(god_id)
  return redirect('detail', mythology_id=mythology_id)

def remove_god(request, mythology_id, god_id):
  # Note that you can pass a god's id instead of the whole god object
  Mythology.objects.get(id=mythology_id).gods.remove(god_id)
  return redirect('detail', mythology_id=mythology_id)

def add_prayer(request, mythology_id):
  form = PrayerForm(request.POST)
  if form.is_valid():
    new_prayer = form.save(commit=False)
    new_prayer.mythology_id = mythology_id
    new_prayer.save()
  return redirect('detail', mythology_id=mythology_id)