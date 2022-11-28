#### FIREWALLS AND SANDBOXING

# Configuración de red en máquinas virtuales

## Configuración Virtual Box
En Virtual Box, por cada maquina vamos a Configuración, Red y cambiamos los Adaptadores según nos convenga a continuación:
* En máquina FW, creamos 3 adaptadores de red, uno puente, otro red interna (nombre DMZ_lan), otro red interna (nombre user_lan):
  ![image](https://user-images.githubusercontent.com/83337658/204324389-03a87065-d927-4349-b16e-c081dc437d07.png)
* En máquina Apache, adaptador red interna (nombre DMZ_lan):
  ![image](https://user-images.githubusercontent.com/83337658/204324673-b0966e6e-3c68-45da-b0aa-3e2d04e3a485.png)
* En máquina user1, adaptador red interna (nombre user_lan):
  ![image](https://user-images.githubusercontent.com/83337658/204324973-34c81f48-92d6-42c5-8764-0ad257c9ee01.png)

## Cambiar nombre de host en clones y asignar IPs
### Hostname
En cada máquina, editamos el archivo ```/etc/hostname```, cambiamos el texto por el nombre de cada máquina:
  -Maquina Debian:
  ![image](https://user-images.githubusercontent.com/83337658/204322522-bf5a05d0-dd12-4ffc-84a4-4c31111f3c73.png)
  ![image](https://user-images.githubusercontent.com/83337658/204323275-c535b69b-63f8-48ce-918a-b81cb6bd3de8.png)
  -Maquina Apache:
  
  -Maquina User:
