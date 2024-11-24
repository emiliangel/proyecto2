# practica_2
# Instrucciones de uso:
# - Acceda al enlace del repositorio

# - En un directorio local, clone el repositorio con el comando "git clone {enlace del repositorio} "

# - En el repositorio clonado #encontrará el script de python

# - En la función GetOrganizations, # en la variable header con el uso del  token Bearer copie la API KEY asignada para consultas a la API

# -  Guarde los cambios, ejecute el # código, desde la terminal, con el 
# siguiente comando: python Script.py

# - Esto le generará, en el directorio  donde clonó el repositorio, un  archivo que se llamará "devices.csv" con las características  para los equipos de tipo wireless y appliance


# DOCUMENTACIÓN:
El script cuenta con dos funciones principales: 
getorg():  se encarga de validar mediante la librería requests la API KEY proporcionada, y retorna en  formato JSON la respuesta proporcionada por meraki, la cual contiene una lista de diccionarios con la id de la organización.

getorgdevices(): una vez obtenido el id de la organización se le pasa como parámetro a esta función para que retorne en formato JSON todos los equipos pertenecientes a dicha organización.

Luego de ejecutar estas funciones, se prepara la estructura para el archivo .csv contentivo de los equipos appliance y wireless, en primer lugar se toman las listas más grandes para cada tipo de equipo, es decir las que contienen más características (ya que según la información propocionada por meraki, algunos dispositivos tienen más características que otros), luego se concatenan dichas listas y se obtiene la más grande entre todas (entre todos los de tipo wireless y appliance) para formar así el encabezado del archivo .csv. Este proceso se realiza para evitar que en el encabezado del archivo .csv falten características que puedan tener algunos de los dispositivos a registrar.

Posteriormente, mediante una función, se llenan las filas del archivo .csv, filtrando por el tipo de equipo.

Finalmente, al ejecutar el Script, se genera un archivo con el nombre device.csv contentivo de las características para los dos tipos de equipos solicitados
