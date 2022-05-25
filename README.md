# RESMenu
## Descripción:
Un proyecto de pedido de comidas en un restaurante.
## Cómo ponerlo en marcha:
Una vez clonado el repositorio, deberá crear un ambiente
virtual e instalar las dependencias 
especificadas en **paquetes.txt**. 
Esta acción se realizará por única vez.
(windows)
``` 
>cd RESMenu_des_app
>py -3 -m venv venv
>venv\Sripts\activate
>pip -r paquetes.txt
```
Una vez creado y configurado el ambiente virtual,
escriba lo siguiente para ejecutar la aplicación:
(windows)
```
>py -m flask run
```
Si desea salir del ambiente virtual escriba **deactivate**.

## SQL y DB's:
La aplicación viene con un usuario de prueba y dos tipos de conexiones,
elija una según si usa MySQL o MariaDB en el 
[archivo python](app.py). Si desea correr la aplicación en
un servidor público, asegúrese de cambiar el nombre, 
la contraseña 
y, si lo encuentra necesario, cambiar los permisos.
