# Crud API Django Rest Framework

## Instalación
Para instalar el entorno virtual es necesario tener instalado, te recomiendo instalarlo desde python https://www.python.org/downloads/ y desactivado el modo restringido para la ejecución de scripts en windows para ello es necesario ejecutar la power shell de windows en modo administrador, te dejo los pasos en el siguiente artículo https://www.alexmedina.net/habilitar-la-ejecucion-de-scripts-para-powershell/#:~:text=Para%20cambiar%20esta%20configuraci%C3%B3n%20basta,ya%20aparece%20como%20%C2%ABUnrestricted%C2%BB.

### Windows (instalación entorno sobre el proyecto)

Comandos de instalación

    py -m virtualenv venv
    
Activar el entorno

	.\venv\Scripts\activate

### Otras alternativas (entorno global)

https://developer.mozilla.org/es/docs/Learn/Server-side/Django/development_environment

## Version Django
Django version **4.1.4**
Python version **3.11.1**

## Consultas a través de interfaz de DJANGO API REST

http://localhost:8000/api/projects/

## Lanzar consultas a través de cliente
En mi caso he utilizado la extensión de Thunder Client de VSCode https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client
	
|Consulta|URL|method|body| 
|--|--|--|--
|Obtener todos|http://localhost:8000/api/projects/|GET|*|
|Obtener uno|http://localhost:8000/api/projects/{id}|GET|*|
|Crear|http://localhost:8000/api/projects/|POST|Consulta crear|
|Eliminar|http://localhost:8000/api/projects/{id}|DELETE|*|
|Modificar todo|http://localhost:8000/api/projects/{id}|PUT|Consulta modificar|
|Modificar un valor|http://localhost:8000/api/projects/{id}|PATCH|Consulta modificar uno|

### Consultas

`**Consulta crear** 
{
  "title": "proyecto 1",
  "description": "Actualizado",
  "technology": "react js"
}
`
`**Consulta modificar**
{
  "title": "proyecto 1",
  "description": "Actualizado",
  "technology": "react js"
} `
`**Consulta modificar**
{
  "title": "proyecto 1"
} `

Mas información en https://www.django-rest-framework.org/
