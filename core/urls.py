from django.urls import path
from .views import (
    getClubs, getJoueurs, getOneClub, getStats, example_view
    )

urlpatterns = [
    path("clubs/", getClubs, name="getClubs"),
    path("clubs/<int:id_club>", getOneClub, name="getOneClub"),
    path("joueurs/", getJoueurs, name="getJoueurs"),
    path("stats/", getStats, name="getStats"),
    path("login/", example_view, name="example_view"),
]