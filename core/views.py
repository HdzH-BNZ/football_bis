import json
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import fields, serializers, viewsets, status
from .serializers import (
    ClubsSerializer, JoueursSerializer
)
from .models import (Clubs, Joueurs)
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.db.models import Count, Max, Min
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)


@api_view(['GET', 'POST'])
def getClubs(request):
    if request.method == 'GET':
        clubs = Clubs.objects.all()
        serializer = ClubsSerializer(clubs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClubsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PATCH', 'PUT'])
def getOneClub(request, id_club):
    club = Clubs.objects.get(id = id_club)
    if request.method == 'GET':
        serializer = ClubsSerializer(club, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        data = request.data
        serializer = ClubsSerializer(club, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = request.data
        serializer = ClubsSerializer(club, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getJoueurs(request):
    joueurs = Joueurs.objects.all()
    serializer = JoueursSerializer(joueurs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getStats(request):
    #max = Joueurs.objects.annotate(Max(compteur=Count('club_pro')))
    #joueurs = Joueurs.objects.annotate(compteur=Count('club_pro'))
    joueurs = Joueurs.objects.filter(club_pro__pays='algerie').values('nom').distinct()
    #joueurs = Joueurs.objects.filter(club_pro='club_pro').annotate(compteur=Count('club_pro'))
    #print(max)
    vars(joueurs)
    #print(joueurs)
    for joueur in joueurs:
        print(joueur.compteur)
    serializer = JoueursSerializer(joueurs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    #return Response(joueurs)