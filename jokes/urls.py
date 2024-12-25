from django.urls import path

from .views import (
    JokeCreateView, JokeDetailView, JokeListView, JokeUpdateView, JokeDeleteView,
)

app_name = 'jokes'
urlpatterns = [
    path('joke/<slug>/update/', JokeUpdateView.as_view(), name='update'),
    path('', JokeListView.as_view(), name='list'),
    path('joke/<slug>', JokeDetailView.as_view(), name='detail'),
    path('joke/create/', JokeCreateView.as_view(), name='create'),
    path('joke/<slug>/delete/', JokeDeleteView.as_view(), name='delete'),
]