# proyecto_sustituto_IA
Proyecto sustituto. Curso introducción a la Inteligencia Artificial. Alumno: Cristian Mateo Florez Restrepo, CC 1040183014

## Competencia utilizada
https://www.kaggle.com/competitions/spaceship-titanic/overview

## Para correr el colab de la fase 1
- Ejecutar las celdas de código en orden
- Ingresar el usuario y la key indicadas en el segundo bloque de código cuando se le requiera

## Para correr scripts de la fase 2
### Desde la terminal
Descargar el proyecto, ubicarse desde la términal en la carpeta 'scripts' y ejecutar el comando:
  
- docker build -t spaceship-titanic .

Luego comprobar que la imagen se genero con el siguiente comando y tomar nota del id
  
- docker images

Para luego montar el contenedor con el siguiente comando
  
- docker run -it IDIMAGEN

### En una nueva terminal
Luego, en otra terminal, comprobar los contenedores montados con el siguiente comando y tomar nota del CONTAINERID
  
- docker ps

Usar el siguiente comando para comprobar los archivos que se encuentran en el container, los cuales deben coincidir con los contenidos en la carpeta 'scripts'
  
- docker exec CONTAINERID ls

Ejecutar el siguiente comando para correr el script de entrenamiento, y con el comando anterior se comprueba que se generó un nuevo archivo llamado 'spaceship_titanic_model.pkl'
  
- docker exec -it CONTAINERID python train.py

Finalmente, ejecutar el siguiente comando para correr el script de predicción y almacenar su resultado en el archivo llamado 'predictions.csv'
  
- docker exec -it CONTAINERID python predict.py

### A tener en cuenta
- El archivo con los datos de entrenamiento debe llamarse 'train.csv' y estar ubicado en la carpeta 'scripts'.

- El archivo para realizar la predicción debe llamarse 'input_data.csv' y estar ubicado en la carpeta 'scripts'.

- Ambos archivos ya se encuntran en la carpeta 'scripts' de este repositorio.
