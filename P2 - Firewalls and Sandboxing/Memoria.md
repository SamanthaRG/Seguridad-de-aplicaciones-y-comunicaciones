# FIREWALLS AND SANDBOXING

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
    ![image](https://user-images.githubusercontent.com/83337658/208461447-884e240b-ed0f-4d97-9b0c-8043b7f2b0b2.png)
  
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

### MAQUINA APACHE
- Entrar como user y para descargar:

  ```wget https://dlcdn.apache.org/httpd/httpd-2.4.54.tar.gz```

  ```wget https://dlcdn.apache.org//apr/apr-1.7.0.tar.gz```

  ```wget https://dlcdn.apache.org//apr/apr-util-1.6.1.tar.gz```

  ```wget https://github.com/PCRE2Project/pcre2/releases/download/pcre2-10.40/pcre2-10.40.tar.gz```
 
  ```tar xvf pcre2-10.40.tar.gz```

  ```tar xvf httpd-2.4.54.tar.gz```
  
  ```tar xvf apr-1.7.0.tar.gz```

  ```tar xvf apr-util-1.6.1.tar.gz```

  ```mv apr-1.7.0 httpd-2.4.54/srclib/apr```
  
  ```mv apr-util-1.6.1 httpd-2.4.54/srclib/apr-util```
  
 - Entrar como root y para compilar:
  ```su```
 
  ```apt install build-essential libexpat-dev```

 - Entrar como user y para compilar:
 
  ```cd pcre2-10.40```
  
  ```./configure --prefix=/usr/local/pcre```
  
  ```make```
  
  ```make install```

  ```cd ..```

  ```cd httpd-2.4.54```

  ```mkdir -p /opt/apache```
  ```./configure --prefix=/opt/apache --with-included-apr --with-pcre=/usr/local/pcre/bin/pcre2-config```
  ```make```
  ```make install```
  ```exit```
  
  ### Configurar usuario/grupo
  ```su -```
  ```groupadd apache```
  ```useradd -c "Apache Server" -d /dev/null -g apache -s /bin/false apache```
  ```nano /opt/apache/conf/httpd.conf```

  En las líneas donde pone
  ```
  User daemon
  Group daemon
  ```
  Cambiar por
  ```
  User apache
  Group apache
  ```

  ### Probar si funciona
  ```
  # /opt/apache/bin/httpd -k start
  # wget -O - localhost
  # /opt/apache/bin/httpd -k stop
  ```
# REALITZACIÓ DE LA PRÀCTICA

## 1pt The apache service runs automatically when booting the system.
  
  Crear un fichero en ```nano /lib/systemd/system/apache.service``` y pegar:
  ```
  [Unit]
  Description=Apache
  After=network.target remote-fs.target nss-lookup.target

  [Service]
  Type=forking
  ExecStart=/opt/apache/bin/httpd -k start
  ExecStop=/opt/apache/bin/httpd -k stop
  Restart=on-abort

  [Install]
  WantedBy=multi-user.target
  ```
  Reiniciar el sistema, registrar el servicio (para autoarranque en startup) y arrancarlo/pararlo
  ```
  # systemctl daemon-reload
  # systemctl enable apache.service
  # systemctl start apache.service
  # systemctl stop apache.service
  ```
## 1pt The apache service is constrained to run in the chroot jail.  
  
 - Crear carpeta:
  ```mkdir chroot_jail```
  
 - Añadir carpetas:
  
  ```mkdir -p chroot_jail/{bin,lib,lib64}```
  
  ```mkdir chroot_jail/lib/x86_64-linux-gnu/```
  
  - Test Copiando bash:
  ```cp /bin/bash chroot_jail/bin/```
  
  - Resolver dependencias
  
  ```
  $ cd bin
  $ ldd bash

  $ cp -v /lib/x86_64-linux-gnu/{libtinfo.so.6,libdl.so.2,libc.so.6} chroot_jail/lib/x86_64-linux-gnu/
  $ cp -v /lib64/ld-linux-x86-64.so.2 chroot_jail/lib64/
  ```
  
  ![image](https://user-images.githubusercontent.com/83337658/208455499-4112c527-f3df-4ffc-9ee9-c9a1dd10ba9c.png)
  
 -  gid apache: 1001
  
 ``` 
  su
mkdir -p /opt/apache
./configure --prefix=/opt/apache --with-included-apr --with-pcre2=/usr/local/pcre2/bin/pcre2-config
make
make install
```

## Dins de la màquina debian, realitzem


## Inicialitzem iptables
```
iptables --flush
iptables -t nat --flush
```
## La interfície loopback permet tràfic
```
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
```
## Ho deneguem tot per defecte
```
iptables --policy INPUT DROP
iptables --policy OUTPUT DROP
iptables --policy FORWARD DROP
```
## Les connexions establertes les deixem passar
```
iptables -A INPUT   -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT  -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
```
## Habilitem el ping  
```
iptables -A INPUT -p icmp -j ACCEPT
iptables -A OUTPUT -p icmp -j ACCEPT
```
## Habilitem connexions ssh des de la xarxa user
```
iptables -A INPUT -p tcp -s 192.168.20.0/24 -d 192.168.20.1 --dport 22 -j ACCEPT
```
## Habilitem l'acces a Internet des de la xarxa user
```
iptables -t nat -I POSTROUTING -o enp0s3 -j MASQUERADE
iptables -A FORWARD -s 192.168.20.0/24 -j ACCEPT
```

- Dins de maquina user, podem provar que ens dona connexió ok a internet fent ```ping google.es```o ping ```8.8.8.8```
## Accés al servidor Apache de 192.168.10.100
```
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 192.168.10.100:80
iptables -A FORWARD -p tcp -d 192.168.10.100 --dport 80 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
```
## Limitacions al ping i a les connexions tcp des de l'exterior
```
iptables -A INPUT -i enp0s3 -p icmp -m limit --limit 30/minute  --limit-burst 5 -j ACCEPT
iptables -A INPUT -i enp0s3 -p tcp  -m limit --limit 300/minute --limit-burst 5 -j ACCEPT
```

# SCRIPT

Per tal de que aquestes commandes, s'executin en cadena i obtinguem el funcionament ideal del complex de xarxa entre les màquines, hem plantejat un script que recull tots aquests comandos, i que es podria executar a la maquina debian fent:

```
sh firewall.sh
```
o bé:

```
chmod a+x firewall.sh
./firewall.sh


Link de descarga del script:

https://drive.google.com/file/d/10PrsyR-TG1OV1z_0EFC4nPK3_MjXEFJ6/view?usp=share_link

Igualment, tenim aquest script al directori home de la nostra maquina Debian

# Comandes utils

```
ip a
ip link
system ctl restart networking.service
nano /etc/interfaces
ping 
```
