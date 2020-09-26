from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DeckSerializer, UserSerializer
from .models import Deck


#Function for search function
def names_list(just_names_list, deck_query):
    new_list = []
    deck_name = deck_query.replace("%20", " ")
    for i in just_names_list:
        print(i + " " + deck_name)
        if deck_name in i.lower():
            new_list.append(i)
    return new_list

#All API uses
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Explore':'/explore/',  #GET all decks for Explore Decks page
        'New Account':'/account/',  #POST create new account
        'Search':'/search/<str:deck_name>/',    #GET one deck for download onto local device
        'Download':'/download/<str:pk>/',    #GET one deck for download onto local device
        'Upload':'/upload/',    #POST create deck into Django DB
        'Update':'/update/<str:pk>/',    #POST update one deck in regards to downloads # and likes #
        'Delete':'/delete/<str:user>&<str:deck_name>/',    #DELETE one decks from Django DB
    }
    return Response(api_urls)

#Retreives all decks for explore decks
@api_view(['GET'])
def explore_list(request):
    decks = Deck.objects.all().order_by('-downloads') #returns list of all decks in correct order from most downloads to least downloads
    topdecks = decks[:20]
    serializer = DeckSerializer(topdecks, many=True)
    return Response(serializer.data)

#Retreives decks for search decks
@api_view(['GET'])
def search(request, deck_query):
    all_decks = Deck.objects.all()
    just_names = [i.deck_name for i in all_decks] #extracts only the names of each deck

    name_query = names_list(just_names, deck_query) #sorts the names matching the search query

    decks = Deck.objects.filter(deck_name__in=name_query).order_by('-downloads') #gets the decks matching the elements of name_query
    topdecks = decks[:20]
    serializer = DeckSerializer(topdecks, many=True)
    return Response(serializer.data)

#Downlaods one deck from Django DB
@api_view(['GET'])
def download(request, pk):
    deck = Deck.objects.filter(id=pk)
    serializer = DeckSerializer(deck, many=True)
    return Response(serializer.data)

#Creates one deck
@api_view(['POST'])
def upload(request):
    serializer = DeckSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#Inputs new users
@api_view(['POST'])
def new_account(request):
    serializer = UserSerializer(data=request.data)

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
def delete_deck(request, user, deck_name):
    deck = Deck.objects.get(user=user, deck_name=deck_name)
    deck.delete()

    return Response("Deck Deleted!!!")
