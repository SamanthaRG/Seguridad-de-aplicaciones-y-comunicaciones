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
  ![image](https://user-images.githubusercontent.com/83337658/204325776-c9f4596d-5e7c-42f1-8e1a-ea82d6155da1.png)
  ![image](https://user-images.githubusercontent.com/83337658/204327470-eb1b6cb1-c106-463e-9688-ee295c8e4c75.png)
  -Maquina User:
  ![image](https://user-images.githubusercontent.com/83337658/204326624-deca14b9-3e7b-4a5f-978a-24fed5664f25.png)
  ![image](https://user-images.githubusercontent.com/83337658/204327033-015175a8-2978-47c2-8b8b-53bf6322b0b4.png)
  
  
### IP
Editar el archivo ```/etc/network/interface```

Añadir por cada interfaz
```
auto <interface_name>
iface <interface_name> inet static
address <ip> # la ip que toque
netmask <mask> # la mascara que toque
gateway <ip> # el gateway que toque
```
  -Maquina Debian:
  ![image](https://user-images.githubusercontent.com/83337658/204330579-2d66b919-cc4a-410f-9b0e-4a553968fd4d.png)
  #TODO: editar fichero interfaces
  -Maquina Apache:
  
  -Maquina User:
