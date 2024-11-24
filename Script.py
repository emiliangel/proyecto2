# Se improtan las librerías
import json
import requests
from pprint import pprint
import csv


##Orgdevices

####Definicion de funciones###

##GetOrganizations

def getorg():

    url = "https://api.meraki.com/api/v1/organizations"

    payload = None #cuerpo de datos en None por ser solicitud GET

    #Def de cabeceras
    headers = {
    "Authorization": "Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6", #Autenticacion de la solicitud con un token Bearer y la API KEY
    "Accept": "application/json" #Define respuesta a solicitud en formato Json
    }

    response = requests.request('GET', url, headers=headers, data = payload) #Se realiza solicitud GET
    return json.loads(response.text) #se obtiene la respuesta como cadena de texto, se convierte a un diccionario de python y retorna
       
    
#GetOrganizationsDevices

def getorgdevices (organization_id):

   
    url = "https://api.meraki.com/api/v1/organizations/{}/devices".format(organization_id) #se utiliza el método format () para pasar string de "id"

    payload = None

    headers = {
        "Authorization": "Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
        "Accept": "application/json"
    }

    
    response2 = requests.request('GET', url, headers=headers, data = payload)
    return json.loads(response2.text)
       

#Se busca entre la lista de devices el que contenga más elementos entre todas las listas, 
#se hace así porque hay unos devices que aunque son del mismo tipo, 
#tienen más atributos que otros

def largest_list (orgdev, tipo):
    x=[]
    for i in range (len(orgdev)):
        if (orgdev[i]["productType"]) == tipo:
            x.append(orgdev[i])
    x=max(x, key=len) 
    
    return x

## Escritura de filas en archivo .csv

def writerow (orgdev, tipo):
    for i in range (len(orgdev)):
        if (orgdev[i]["productType"]) == tipo:
            writer_csv.writerow(orgdev[i])


print('\n\n')

# Llamado de funciones

# Obtención de "id" de la organización correspondiente a la API key

b=getorg() # se almacena lista retornada de GetOrganization con "id" de la organizacion
#print(type(b))
d=dict(b[0]) # se transforma el tipo de dato
#se obtiene, finalmente el id, del diccionario obtenido de la lista de retornada por GetOrganization
org_id=d.get("id")

orgdev = getorgdevices(org_id) # se almacenan dispositivos retornados de GetOrganizationDevices con el "id" obtenido

##Se obtienen listas más grandes con appliance y wireless para ser usadas posteriormente en .csv

# lista más grande con appliance
a = list(largest_list (orgdev, "appliance"))
# lista más grande con wireless
b = list(largest_list (orgdev, "wireless"))

#se toma la lista que contenga más elementos para la cabecera de .csv

columns= a+b #se concatenan las listas
columns = list(set(columns)) #se eliminan elementos duplicados

devices = 'devices.csv' #se crea archivo .csv

with open(devices, mode='w', newline='') as archivo_csv: #se abre archivo .csv en modo escritura

## se crea el ojeto writer
    writer_csv = csv.DictWriter(archivo_csv, fieldnames=columns)
## asignar la fila del encabezado
    writer_csv.writeheader()
## se llaman funciones para llenar filas de .csv
    writerow(orgdev, "appliance") # para appliance
    writerow(orgdev, "wireless") # para wireless

