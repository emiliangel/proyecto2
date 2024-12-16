# Dockerfile de ejemplo

# Usar la imagen base de Ubuntu
FROM ubuntu:latest

# Instalar las dependencias necesarias
RUN apt-get update && apt-get install -y python3 python3-pip python3-requests

# Crear un directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos y el código de la aplicación
COPY . /app

# Definir el comando para ejecutar la aplicación
CMD ["python3", "app.py"]

COPY requirements.txt requirements.txt 
COPY Script.py Script.py

#RUN pip3 install -r requirements.txt