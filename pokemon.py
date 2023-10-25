import requests
import sys

def getPokemon(cantidad):
    #get pokemon names
    urlPokemon="https://pokeapi.co/api/v2/pokemon/"
    param={'limit':cantidad}

    responseP=requests.get(urlPokemon,params=param)
    dataP=responseP.json()
    urlMove="https://pokeapi.co/api/v2/move/"
    responseM=""
    dataM=""
    listaPowers=[]
    listaPow=[]
    idPokemon=0

    for itemP in dataP['results']:
        nameP=itemP['name']
        #print("Name: "+nameP)
        #get pokemon IDs
        urlPokemon="https://pokeapi.co/api/v2/pokemon/"+itemP['name']
        responseP = requests.get(urlPokemon)
        dataP = responseP.json()
        sentence=str(dataP['forms'])
        splitment=sentence.split('/')
        idPokemon=splitment[-2]
        #print("ID: "+idPokemon)
        #get moves names of each pokemon
        urlPokemon = "https://pokeapi.co/api/v2/pokemon/"
        #print("Moves:")
        urlPokemon=urlPokemon+itemP['name']
        responseP = requests.get(urlPokemon)
        dataP = responseP.json()
        powerTotal=0
        for itemP in dataP['moves']:
            #print("--"+itemP['move']['name'])
            #get moves IDs and power of each pokemon move
            urlMove="https://pokeapi.co/api/v2/move/"
            urlMove=urlMove+"/"+itemP['move']['name']
            responseM=requests.get(urlMove)
            dataM=responseM.json()
            #print("  move ID: "+str(dataM['id']))
            #print("  power: "+str(dataM['power']))
            if dataM['power'] != None:
                powerTotal=powerTotal+dataM['power']
        listaPowers.append("name: "+nameP+", ID: "+idPokemon+", total power: "+str(powerTotal))
        listaPow.append(powerTotal)
    tmp=max(listaPow)
    index=listaPow.index(tmp)
    print(listaPowers[index])
    return listaPowers[index]

getPokemon(sys.argv[1])