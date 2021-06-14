from django.db import models
from rest_framework import serializers
from .models import (Clubs, Joueurs)

class ClubsSerializer(serializers.ModelSerializer):

    nom_nom = serializers.CharField(source="nom")

    class Meta():
        model = Clubs
        fields = ('id','nom', 'nom_nom', 'pays')

class JoueursSerializer(serializers.ModelSerializer):

    nom_nom = serializers.CharField(source="nom")
    nom_du_club = serializers.PrimaryKeyRelatedField(source="club_pro", queryset=Clubs.objects.all())
    pays = serializers.CharField(source="club_pro.pays")

    compteur = serializers.IntegerField()

    class Meta():
        model = Joueurs
        fields = [
            'id', 'nom', 'club_pro',  
            'nom_nom', 'nom_du_club', 'pays',
            'compteur',
        ]
        depth = 1
    
class StatsSerializer(serializers.ModelSerializer):

    class Meta():
        fields = '__all__'
