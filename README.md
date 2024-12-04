# Brutus

<p align="center"> 
	<img src="images/logo.jpeg" 
		 alt="Brutus logo"
		 width="200"/>
</p>

Herramienta para realizar ataques de fuerza bruta sobre el protocolo HTTP o HTTPS.

Puedes sentirte libre de utilizar diccionarios o entradas manuales.

**IMPORTANTE** : Siendo esta la primera versión, se tomá en consideración valores por defecto como las **COOKIES** ('session' o PHPSESSID), como también los atributos del formulario de logueo ('username' y 'password').

<p align="center">
    <img src="images/image01.png"
         alt="Brutus inicio"
         width="800"/>
</p>

¿Cómo funciona?
======
La herramienta comienza  obteniéndo argumentos como son la URL, usernames y passwords siendo estos 2 últimos valores manuales o por uso de diccionarios.

<p align="center">
    <img src="images/image02.png"
         alt="Brutus atack"  
         width="800"/>
</p>

<p align="center">
    <img src="images/image03.png"
         alt="Brutus atack"  
         width="800"/>
</p>

Si se llegará a dar el caso donde estamos frente a una aplicación hecha en PHP deberás colocarar las FLAGS correspondientes -php o --php.

<p align="center">
    <img src="images/image04.png"
         alt="Brutus atack"  
         width="800"/>
</p>

Puedes utilizar la opción verbose (-v, --verbose) para tener a detalle el proceso de autenticación.

<p align="center">
    <img src="images/image05.png"
         alt="Brutus atack"  
         width="800"/>
</p>

Si debesea recibir ayuda puedes usar la opción help (-h o --help) para ver las FLAGS disponibles

<p align="center">
    <img src="images/image06.png"
         alt="Brutus atack"  
         width="700"/>
</p>

Requisitos
======
Para tener un correcto funcionamiénto de la herramienta asegurate que cuentes con el intérprete de Python en un versión posterior a 3.6.
Si deseas cancelar la ejecución de la herramienta solo presiona Ctrl + C y estarás fuera.
