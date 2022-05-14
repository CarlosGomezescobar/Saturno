# Saturno
Admin Dashboard / Users
Saturno Web App:

	1. ) Origen y Creacion:
	Desarrollo web, proyectado en sus inicios para el procedimientos operativos en la creacion de un software orientados a objetos. El genesis es la vinculacion principal de una interfaz que visualiza la pagina de administracion (ADMIN DASHBORAD), servicio operativo del Backend, ademas cuenta con una arquitectura escalable dandole originalidad en las Bases De Datos y sus correlaciones de las diferentes modelos en la Base De Datos, el cual destaca gran importancia en la modalidades y etapas del desarrollo web, Codificacion de las distintas varibles,formatos y dependencias. de igual manera su configuracion con las url's, conectividad entre en frontend y backend.

	2.) Previsto para la Segunda Fase:
		Realizacion de UX/UI del Usuario: 
		  login,logout, register, profile, settings, products list, cart, payments.


Ubuntu: 20.04,
Backend: Python 3.8.10,
Frontend: HTML, CSS, Javascript
Django: 4.0,
BDD: sqlite3,
Control de vesiones: GIT

-Crear Entorno Virtual:

	1- Crear Entorno:
		* sudo apt-get install python3-venv
		* python3 -m venv myvenv 
		* ls
		* 
		-- Activar el entorno virtual: source myvenv/bin/activate
	
- Descargar los Requerimientos:
	* pip3 install -r requirements.txt


	- Crear Proyecto
		* django-admin startproject Saturno .
		
	- Crear App.
		 * python3 manage.py startapp core

--Hacer Migraciones
	python3 manage.py makemigrations
	python3 manage.py migrate

--Crear Super User
	python3 manage.py createsuperuser
		username: 
		password:
		email: 

--Runserver

	python3 manage.py runserver
	
	
