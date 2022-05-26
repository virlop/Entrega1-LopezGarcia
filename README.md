# Primera entrega Proyecto Final

Este codigo contiene:
 - Vistas 
 - Formularios
 - Modelos
 - Templates

**importante: Este ejemplo fue probado con python 3.8.13 y Django 4.0.4, usando Bootstrap v5**

Primero correr el servidor con los siguientes comandos:
```
cd mi-primer-mvt
python3 manage.py migrate
```
```
python3 manage.py runserver
```
## Funcionalidades

Este código tiene 4 modelos: Persona, Mascota, Perro y Gato. Los últimos dos heredan de Mascota.
En el inicio se muestra la lista de Familiares (Persona) y de Mascotas (Gatos y Perros) cargados en la DB. Se puede eliminar cualquiera de ellos con el botón "Borrar". También se muestran los botones "Agregar Familiar", "Agregar mascota GATO" y "Agregar mascota PERRO" para cargar los correspondientes objetos en la DB. Para ello se debe completar el formulario correspondiente y hacer click en "Guardar".
El botón "Refrescar página" sirve para actualizar la página. Se encuentra en todos los templates.
El header y el footer tienen un link que lleva al inicio. También se encuentra en todos los templates.
