from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DeckSerializer, UserSerializer
from .models import Deck


#Function for search function
def search_list(given_list, search):
    new_list = []
    for i in given_list:
        if i == None:
            pass
        elif search in i.lower():
            new_list.append(i)
    return new_list

#search the hashtags
def accurate_names(raw_names, raw_tags, raw_descriptions):
    ids_from_names = [i.id for i in raw_names] #extracts only the names of each deck
    ids_from_tags = [i.id for i in raw_tags] #extracts only the hashtags of each deck
    ids_from_descriptions = [i.id for i in raw_descriptions] #extracts only the descriptions of each deck

    combined_list = ids_from_names + ids_from_tags + ids_from_descriptions
    returned_list = list(dict.fromkeys(combined_list))

    return returned_list

#All API uses
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Top Decks':'/topdecks/', #GET for the top ten most downloaded decks
        'New Decks':'/newdecks/', #GET for the 20 newest decks
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

@api_view(['GET'])
def topdecks(request):
    decks = Deck.objects.all().order_by('-downloads') #returns list of all decks in correct order from most downloads to least downloads
    topdecks = decks[:10]
    serializer = DeckSerializer(topdecks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def newdecks(request):
    decks = Deck.objects.all().order_by('-id')
    newdecks = decks[:20]
    serializer = DeckSerializer(newdecks, many=True)
    return Response(serializer.data)

#Retreives decks for search decks
@api_view(['GET'])
def search(request, deck_query):
    all_decks = Deck.objects.all()
    query = deck_query.replace("%20", "").lower()

    all_names = [i.deck_name for i in all_decks]
    all_tags = [i.tags for i in all_decks]
    all_descriptions = [i.description for i in all_decks]

    names_ofdecks = search_list(all_names, query)
    tags_ofdecks = search_list(all_tags, query)
    description_ofdecks = search_list(all_descriptions, query)

    decknames = Deck.objects.filter(deck_name__in=names_ofdecks)
    decksby_tag= Deck.objects.filter(tags__in=tags_ofdecks)
    decksby_description = Deck.objects.filter(description__in=description_ofdecks)

    officialmodelquery = accurate_names(decknames, decksby_tag, decksby_description)

    decks = Deck.objects.filter(id__in=officialmodelquery).order_by('-downloads')

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

#@api_view(['POST'])
#def uploadwithhashtags(request):
#    serializer = DeckSerializer(data=request.data)

#    if serializer.is_valid():
#        serializer.save()

#    return Response(serializer.data)

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
