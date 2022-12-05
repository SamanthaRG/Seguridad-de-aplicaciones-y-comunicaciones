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
  - Maquina Debian:
  ![image](https://user-images.githubusercontent.com/83337658/204322522-bf5a05d0-dd12-4ffc-84a4-4c31111f3c73.png)
  ![image](https://user-images.githubusercontent.com/83337658/204323275-c535b69b-63f8-48ce-918a-b81cb6bd3de8.png)
  
  - Maquina Apache:
  ![image](https://user-images.githubusercontent.com/83337658/204325776-c9f4596d-5e7c-42f1-8e1a-ea82d6155da1.png)
  ![image](https://user-images.githubusercontent.com/83337658/204327470-eb1b6cb1-c106-463e-9688-ee295c8e4c75.png)
  
  - Maquina User:
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
  - Maquina Debian:
  ![image](https://user-images.githubusercontent.com/83337658/204330579-2d66b919-cc4a-410f-9b0e-4a553968fd4d.png)
  ![image](https://user-images.githubusercontent.com/83337658/205100894-cd98dd80-b116-421c-a516-dbffc7c0f09c.png)
  
  - Maquina Apache:
  ![image](https://user-images.githubusercontent.com/83337658/204339561-b4057913-b080-4e58-a554-9323d82c2e86.png)
  ![image](https://user-images.githubusercontent.com/83337658/205102285-af930448-567f-4431-a677-0374639d161f.png)
  
  - Maquina User:
  ![image](https://user-images.githubusercontent.com/83337658/204340927-ed438a68-4407-4d18-b49d-77780a9b6f22.png)
  ![image](https://user-images.githubusercontent.com/83337658/205103354-fb2322fe-d6fb-4e54-a63e-c7bddba1a884.png)


- Maquina Debian:
  Editamos el archivo ```/etc/sysctl.conf```:
  
   ![image](https://user-images.githubusercontent.com/83337658/205665313-7bab07f6-bd81-42fc-97f6-a58dc5c064d7.png)
  
  Descomentamos la línea con ```net.ipv4.ip_forward=1```:
  
   ![image](https://user-images.githubusercontent.com/83337658/205664728-8acf331f-a8e7-46ae-b4ba-e28c059e87c2.png)
  
  Y hacemos```sysctl -p /etc/sysctl.conf```:
  
    ![image](https://user-images.githubusercontent.com/83337658/205665949-f26aec4f-96d3-4e22-9be3-1a7102fc041c.png)


