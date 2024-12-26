from .forms import JokeForm
from django.views.generic import ( 
    CreateView, DetailView, ListView, UpdateView, DeleteView, )

from django.urls import reverse_lazy

from .models import Joke

class JokeCreateView(CreateView):
    model = Joke
    form_class = JokeForm


class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')


class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm

# Create your views here.
