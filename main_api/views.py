from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DeckSerializer
from .models import Deck


#Offers all Deck data
@api_view(['GET'])
def MainAPI(request):
    decks = Deck.objects.all()
    serializer = DeckSerializer(decks, many=True)
    return Response(serializer.data)

#Post a Deck
@api_view(['POST'])
def MainAPI(request):
    serializer = DeckSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#Updates Deck for Likes and Comments
@api_view(['POST'])
def MainAPI(request):
    deck = Deck.objects.get(id=pk)
    serializer = DeckSerializer(instance=deck, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#Deletes Deck
@api_view(['DELETE'])
def MainAPI(request):
    deck = Deck.objects.get(id=pk)
    deck.delete()

    return Response("Deck Deleted!!!")
