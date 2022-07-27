# RESMenu
## Descripción:
Un proyecto de pedido de comidas en un restaurante.
## Roadmap:
* **v0.1**: La aplicación contiene un login/signup con
encriptado de contraseña, sesiones incluidas y una ruta (manage)
para gestionar los productos a publicar (de manera experimental).
* **v0.5**: La ruta "manage" y derivadas están terminadas, hay otra ruta
(menu) para poder elegir y ordenar comidas (sólo cliente)
mediante un carrito de compras.
* **v1.0**: Los cocineros pueden ver las órdenes y marcarlas como completadas.
* **v1.1**: La aplicación envía un email a cada usuario que se registra.
### Otras tags:
Para arreglos importantes de errores, se utilizarán tags intermedias
(ej: v1.01, v0.3, etc.) y para **la actualización de estilos** se utilizará
el sufijo "-cssUp" (ej: v0.6-cssUp)
## Cómo ponerlo en marcha:
Una vez clonado el repositorio, deberá crear un ambiente
virtual e instalar las dependencias 
especificadas en **paquetes.txt**. 
Esta acción se realizará por única vez.
(windows, git bash)
``` 
$cd RESMenu_des_app
$python -m venv venv
$. venv/Scripts/activate
$pip install -r paquetes.txt
```
Una vez creado y configurado el ambiente virtual,
escriba lo siguiente para ejecutar la aplicación:
(windows, git bash)
```
$flask run
```
Si desea salir del ambiente virtual escriba **deactivate**.

## SQL y DB's:
La aplicación viene con un usuario de prueba y dos tipos de conexiones,
elija una según si usa MySQL o MariaDB en el 
[archivo python](app.py). Si desea correr la aplicación en
un servidor público, asegúrese de cambiar el nombre, 
la contraseña 
y, si lo encuentra necesario, cambiar los permisos.

## SASS (archivos .scss)
Para reinterpretar el código SCSS a CSS, deberá
instalarse la herramienta SASS y escribir en la carpeta
principal:
```
sass --watch static/SASS/index.scss static/CSS/index.css
```
