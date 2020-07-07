from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DeckSerializer
from .models import Deck


#All API uses
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Explore':'/explore/',  #GET all decks for Explore Decks page
        'Download':'/download/<str:pk>',    #GET one deck for download onto local device
        'Upload':'/upload/',    #POST create deck into Django DB
        'Update':'/update/<str:pk>',    #POST update one deck in regards to downloads # and likes #
        'Delete':'/delete/<str:pk>',    #DELETE one decks from Django DB
    }
    return Response(api_urls)

#Retreives all decks for explore decks
@api_view(['GET'])
def explore_list(request):
    decks = Deck.objects.all()
    serializer = DeckSerializer(decks, many=True)
    return Response(serializer.data)

#Downlaods one deck from Django DB
@api_view(['GET'])
def download(request, pk):
    deck = Deck.objects.get(id=pk)
    serializer = DeckSerializer(deck, many=False)
    return Response(serializer.data)

#Creates one deck
@api_view(['POST'])
def upload(request):
    serializer = DeckSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#Updates Deck for likes and downloads
@api_view(['POST'])
def update(request, pk):
    deck = Deck.objects.get(id=pk)
    serializer = DeckSerializer(instance=deck, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#Deletes a Deck
@api_view(['DELETE'])
def delete_deck(request, pk):
    deck = Deck.objects.get(id=pk)
    deck.delete()

    return Response("Deck Deleted!!!")
