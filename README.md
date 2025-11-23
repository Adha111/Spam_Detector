## De qué trata la práctica?
Esta práctica es un detector de spam donde usa un archivo scv para detectar qué mensajes se consideran spam dentro de un correo.

## ¿Cómo?
1.- Creamos una carpeta nueva
2.- Creamos el entorno virtual
3.-Creamos una carpeta de resources(src) y otra llamada data. 
4.- Creamos el archivo screen.py y spam_detector.py dentro de la carpeta resources (src)
5.- Creamos el código dentro del archivo spam_detector donde se hará la ejecución de detección de spam.
6.- Creamos el código dentro del archivo screen.py para obtener la parte gráfica usando la librería tkinter
7.- Ejecutamos el programa en un entorno virtual, pero a mí no me funcionó dentro de este. Para que funcionara tuve que ejecutarlo directamente del CMD.

## Trabajo futuro (mejoras)
Tuve un error ejecutando el programa en VSC, pero se solucionó de alguna manera ejecutando el programa directamente en el CMD.
En la sección de trabajo en VSC, al ejecutar/correr el archivo de python me marcaba un error dentro de la terminal en VSC:
PS C:\Users\estre\Documents\spam_detector> & C:/Users/estre/Documents/spam_detector/venv/Scripts/Activate.ps1
& : No se puede cargar el archivo C:\Users\estre\Documents\spam_detector\venv\Scripts\Activate.ps1 porque la ejecución de 
scripts está deshabilitada en este sistema. Para obtener más información, consulta el tema about_Execution_Policies en 
https:/go.microsoft.com/fwlink/?LinkID=135170.
En línea: 1 Carácter: 3
+ & C:/Users/estre/Documents/spam_detector/venv/Scripts/Activate.ps1
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
PS C:\Users\estre\Documents\spam_detector> & C:/Users/estre/Documents/spam_detector/venv/Scripts/python.exe c:/Users/estre/Documents/spam_detector/src/spam_detector.py
did not find executable at 'C:\Users\Posgrado-05\AppData\Local\Programs\Python\Python313\python.exe': El sistema no puede encontrar la ruta especificada.

PS C:\Users\estre\Documents\spam_detector> & C:/Users/estre/Documents/spam_detector/venv/Scripts/python.exe c:/Users/estre/Documents/spam_detector/src/screen.py
did not find executable at 'C:\Users\Posgrado-05\AppData\Local\Programs\Python\Python313\python.exe': El sistema no puede encontrar la ruta especificada.


 Sin embargo, al momento de correr el archivo directamente en el CMD de mi computadora, sí se ejecutó bien el programa, incluso lo probamos y todo salió bien.