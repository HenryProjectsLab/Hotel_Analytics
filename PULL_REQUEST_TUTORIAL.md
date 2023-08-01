# Tutorial para contribuir mediante Clones y Pull Requests

¡Hola equipo de Data Science! Gracias por unirse y contribuir al proyecto. En este tutorial, te guiaremos a través de los pasos para contribuir mediante clones directos y Pull Requests.
## Antes de todo acepta la invitación:
![Invitación](/Image/join.jpg)

## Los pasos del 1 al 4 solo se hacen una vez
imagen previa de los pasos 1 al 4
![](/Image/git.jpg)
## Paso 1: Inicia sesión en tu cuenta de GitHub

Si aún no inicias sesión en **Git Bash** usa el siguiente comando:

git config --global user.name "tu_nombre_de_usuario"

## Paso 2: Clona el repositorio

Clona el repositorio del proyecto en tu computadora local usando el siguiente comando:

git clone https://github.com/HenryProjectsLab/Hotel_Analytics.git


## Paso 3: Configura el repositorio remoto

Una vez clonado, ingresa al directorio del repositorio y configura el repositorio remoto para mantenerlo actualizado(solo se ejecuta al inicio):

cd Hotel_Analytics

git remote add origin https://github.com/HenryProjectsLab/Hotel_Analytics.git

## Paso 4 : Visualiza las ramas existentes

Antes de realizar cualquier cambio, es útil conocer las ramas existentes en el repositorio. Puedes usar el siguiente comando para visualizarlas:

git branch -a

Seguidamente cambia de rama con el siguiente comando. Para más detalles de cómo usar las rama ver: [CONTRIBUTING.md](CONTRIBUTING.md)

git checkout nombre-de-la-rama

## Los siguientes pasos son para cada Pull Request

Imagen previa de los pasos 5 y 6
![Elige la rama que usaste](/Image/git2.jpg)

## Paso 5: Hacer un commit

Una vez que hayas realizado los cambios en local, realiza un commit con un mensaje descriptivo:

git add .

git commit -m "Descripción de los cambios realizados"


## Paso 6: Empuja los cambios

Empuja los cambios de tu rama a la rama correspondiente en el repositorio remoto:

git push origin nombre-de-la-rama

## Paso 7: Crea el Pull Request

Ve a la página del repositorio en GitHub y selecciona la pestaña [Pull requests](https://github.com/HenryProjectsLab/Hotel_Analytics/pulls)

Luego, haz clic en el botón verde **[New Pull Request]**

Compara las ramas, entre "main" y la rama que usaste, guiate con la imagen:
![Elige la rama que usaste](/Image/pull.jpg)

* Ojo. En esta página podrás visualizar detalles de los cambios

Ahora presiona en el boton verde  
**[Create pull request]** Para detallar la solicitud de cambio

## Paso 8 : Describir el Pull Request (Último paso)

Proporciona una descripción clara y detallada de los cambios que has realizado en el Pull Request. Si es necesario, menciona problemas relacionados o etiquetas que ayuden a contextualizar los cambios, pero aún no crees el Pull Request
![](/Image/example.jpg)

Selecciona el **Reviewer**, si no lo haces, se generará un mensaje de error
![](/Image/rev.jpg)
**Listo, ahora presiona en el boton verde para crear el Pull Request**
## Paso 9: Esperar la revisión y aprobación

Una vez que hayas creado el Pull Request, otros miembros del equipo revisarán tus cambios y proporcionarán comentarios. Realiza las modificaciones necesarias si se requieren ajustes y, una vez que los revisores estén satisfechos, tu Pull Request será aprobado y fusionado en la rama correspondiente.

## ¿Qué pasa si se hicieron cambios en el repositorio remoto, pero tu repositorio local está desactualizado?
Imagen previa de los pasos
![](/Image/git3.jpg)
## Paso 1: Asegurarse de estar en la rama main
Antes de realizar cualquier actualización, asegúrate de estar en la rama main ejecutando el siguiente comando:

git checkout main

## Paso 2: Obtener los últimos cambios del repositorio remoto
Para asegurarte de tener los últimos cambios del repositorio remoto (GitHub) en tu repositorio local, simplemente ejecuta el siguiente comando:

git pull origin main

Esto traerá los cambios más recientes de la rama main del repositorio remoto y los fusionará automáticamente con tu repositorio local.

**¡Listo, tu repositorio local ya tendrá los cambios del repo remoto!**


