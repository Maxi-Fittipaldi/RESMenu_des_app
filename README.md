# RESMenu
## Descripción:
Un proyecto de pedido de comidas en un restaurante.
## Task list:
- [x] login (0.1)
- [x] signup (0.1)
- [x] logout (0.1)
- [x] encriptado de contraseñas (0.1)
- [x] sesiones (0.1)
- [x] ruta _manage_ (gestión de productos, experimental) (0.1)
- [ ] rutas derivadas de _manage_ terminadas
- [ ] ruta menu (pedidos de comidas)
- [ ] roles
- [ ] carrito de compras
- [x] modificar usuario (0.3)
- [x] verificación por mail (0.2)
- [ ] ruta _orders_ (pedidos pendientes y marcarlos como completados)
- [ ] SCSS (diseños exportados de figma)

### Otras tags:
Para arreglos de errores importantes, se utilizarán tags intermedias
(ej: v1.01, v0.3, etc.).
## Cómo ponerlo en marcha:
Una vez clonado el repositorio, deberá crear un ambiente
virtual e instalar las dependencias 
especificadas en _paquetes.txt_. 
Esta acción se realizará por única vez:
(windows, git bash)
``` 
$cd RESMenu_des_app
$python -m venv venv
$. venv/Scripts/activate
$pip install -r paquetes.txt
```
El siguiente paso consiste en declarar las variables temporales,
estas deberán ser declaradas **cada vez** que ejecutes una nueva
instancia de tu terminal:
```
$export FLASK_APP=__init__
$export APP_MAIL_USERNAME=tu_gmail_de_verificación
$export APP_MAIL_PASSWORD=string_de_la_app
$export FLASK_ENV=development #sólo para pruebas
```
**importante**: El gmail que se encarga de validar debe tener
habilitado el 2FA y deberás generar un string de 16 caracteres
en el apartado _seguridad_ de la cuenta de google.

Una vez hecho todo lo anterior,
escriba lo siguiente para ejecutar la aplicación:
```
$flask run
```
Si desea salir del ambiente virtual escriba _deactivate_.
No obstante, para utilizar las funciones SQL deberá crear una DB y un usuario.

## SQL y DB's:
La aplicación viene con un script de creación usuario de 
prueba y otro script de creación de la DB en la carpeta [SQL/scripts](/SQL/scripts).
Hay dos tipos de conexiones,
elija una según si usa MySQL o MariaDB en la
[configuración](config.py).

## Ambiente de producción:
Si desea correr la aplicación en
un servidor público, asegúrese de cambiar el nombre, 
la contraseña 
y, si lo encuentra necesario, cambiar los permisos del usuario de la DB.

## SASS (archivos .scss)
Para reinterpretar el código SCSS a CSS, deberá
instalarse la herramienta SASS y escribir en la carpeta
principal:
```
sass --watch static/SASS/index.scss static/CSS/index.css
```
