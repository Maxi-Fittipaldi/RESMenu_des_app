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
- [x] rutas derivadas de _manage_ terminadas (0.3)
- [x] ruta menu (pedidos de comidas) (0.5)
- [x] roles (0.3)
- [x] carrito de compras (0.5)
- [x] modificar usuario (0.3)
- [x] verificación por mail (0.2)
- [x] ruta _orders_ (pedidos pendientes y marcarlos como completados) (0.4)
- [ ] SCSS (diseños exportados de figma)

### Otras tags:
Para arreglos de errores importantes, se utilizarán tags intermedias
(ej: v1.0.1, v0.3.1, etc.).
## Cómo ponerlo en marcha:
Primero, se debe clonar (es decir, descargar) el repositorio:
``` 
git clone https://github.com/Maxi-Fittipaldi/RESMenu_des_app.git
``` 
### _Setup_ con scripts (sólo apto para desarrollo):
Simplemente, siga los siguientes comandos:
``` 
cd RESMenu_des_app
. setup/bash/venv_setup.sh #por única vez
. setup/bash/env_vars.sh "_mail_" "_contraseña_" "_tipoDB_"#por instancia de terminal
flask run #correr el proyecto
``` 
Para salir del ambiente virtual, escriba _deactivate_.
Si desea volver a entrar, simplemente ejecute:
```
. setup/bash/run_setup.sh "_mail_" "_contraseña_" "_tipoDB_"
```
### _Setup_ manual:
Una vez clonado el repositorio, deberá crear un ambiente
virtual e instalar las dependencias 
especificadas en _paquetes.txt_. 
Esta acción se realizará por única vez:
(windows, git bash)
``` 
cd RESMenu_des_app
python -m venv venv
. venv/Scripts/activate
pip install -r paquetes.txt
```
**nota**: Temporalmente, se deberá crear el _venv_ fuera del proyecto para,
luego, introducirlo en éste. De lo contrario, se producirá un error.

El siguiente paso consiste en declarar las variables temporales,
estas deberán ser declaradas **cada vez** que ejecutes una nueva
instancia de tu terminal:
```
export FLASK_APP=__init__
export APP_MAIL_USERNAME=tu_gmail_de_verificación
export APP_MAIL_PASSWORD=string_de_la_app
export FLASK_ENV=development #sólo para pruebas
```
**importante**: El gmail que se encarga de validar debe tener
habilitado el 2FA y deberás generar un string de 16 caracteres
en el apartado _seguridad_ de la cuenta de google.

Una vez hecho todo lo anterior,
escriba lo siguiente para ejecutar la aplicación:
```
flask run
```
Si desea salir del ambiente virtual escriba _deactivate_.
No obstante, para utilizar las funciones SQL deberá crear una DB y un usuario.

## SQL y DB's:
La aplicación viene con un script de creación usuario de 
prueba y otro script de creación de la DB en la carpeta [SQL/scripts](/SQL/scripts).
Hay dos tipos de conexiones,
elija una según si usa MySQL o MariaDB con la variable de entorno **APP_DB** .

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
