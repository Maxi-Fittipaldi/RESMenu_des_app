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
La aplicación viene con un usuario de prueba. Asegúrese de
cambiar el nombre, la contraseña (tanto en el archivo de creación
de usuario como en el [archivo python](app.py)) 
y, si lo encuentra necesario, cambiar los permisos.
