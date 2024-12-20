# Se improtan las librerías
import json
import requests
from pprint import pprint
import csv
import time


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

    try:
            
        response = requests.request('GET', url, headers=headers, data = payload) #Se realiza solicitud GET
        response.raise_for_status() #se verifica que se este recibiendo la respuesta adecuada
        
        print('Solicitud exitosa para GetOrganizations')

        return json.loads(response.text) #se obtiene la respuesta como cadena de texto, se convierte a un diccionario de python y retorna
       
    #En caso que no se valide la respuesta adecuada se consideran las siguientes excepciones 

    except requests.exceptions.HTTPError as e:
        print('Error en la solicitud')
    except requests.exceptions.ConnectionError as e: 
        print(f'Error HTTP: {e}')
    except requests.exceptions.Timeout as e: 
        print(f'Error de conexión: {e}')
    except requests.exceptions.RequestException as e:
        print(f'Otro error en la solicitud: {e}')


       
    
#GetOrganizationsDevices

def getorgdevices (organization_id):

   
    url = "https://api.meraki.com/api/v1/organizations/{}/devices".format(organization_id) #se utiliza el método format () para pasar string de "id"

    payload = None

    headers = {
        "Authorization": "Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
        "Accept": "application/json"
    }

    try:
            
        response2 = requests.request('GET', url, headers=headers, data = payload)
        response2.raise_for_status()
        print('Solicitud exitosa para GetOrganizationDevices')

        return json.loads(response2.text)
       
    except requests.exceptions.HTTPError as e:
        print('Error en la solicitud')
    except requests.exceptions.ConnectionError as e: 
        print(f'Error HTTP: {e}')
    except requests.exceptions.Timeout as e: 
        print(f'Error de conexión: {e}')
    except requests.exceptions.RequestException as e:
        print(f'Otro error en la solicitud: {e}')
   
       

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

##EJECUCIÓN DE CONSULTA Y LLAMADO DE FUNCIONES

i=1
while True: ## Bucle infinito, será detenido posteriormente por time.sleep (cada 5 minutos)
    # Obtención de "id" de la organización correspondiente a la API key

    b=getorg() # se almacena lista retornada de GetOrganization con "id" de la organizacion
    #print(type(b))
    d=dict(b[0]) # se transforma el tipo de dato
    #se obtiene, finalmente el id, del diccionario obtenido de la lista de retornada por GetOrganization
    org_id=d.get("id")

    orgdev = getorgdevices(org_id) # se almacenan dispositivos retornados de GetOrganizationDevices con el "id" obtenido
    
    ##Se obtienen listas más grandes con appliance y wireless para ser usadas posteriormente en .cs
    
    # lista más grande con appliance
    a = list(largest_list (orgdev, "appliance"))
    # lista más grande con wireless
    b = list(largest_list (orgdev, "wireless"))

    #se toma la lista que contenga más elementos para la cabecera de .cs
    columns= a+b #se concatenan las listas
    columns = list(set(columns)) #se eliminan elementos duplicado

    devices = 'devices.csv' #se crea archivo .csv

    #se abre archivo .csv en modo escritura
    with open(devices, mode='w', newline='') as archivo_csv: 
    ## se crea el ojeto writer
        writer_csv = csv.DictWriter(archivo_csv, fieldnames=columns)
    ### asignar la fila del encabezado
        writer_csv.writeheader() 
    ## se llaman funciones para llenar filas de .csv
        writerow(orgdev, "appliance") # para appliance
        writerow(orgdev, "wireless") # para wireless
    print("Consulta número %d realizada y archivo devices.csv actualizado" %(i))
    i=i+1
    print('\n\n')
    time.sleep(300) ##temporizador que permite la ejecución del ciclo, después de cada 300 segundos (5 minutos)
