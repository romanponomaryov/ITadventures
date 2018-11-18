""""
1) Install docker and docker-compose

To install follow this:
https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository
+
$ sudo apt-get install -y docker-compose

2) Pull our images from docker hub to your local machine

$ docker pull pomacb/django-mysql:1.0
$ docker pull pomacb/django-web:0.1

3) Create directory "cursor-kyiv" wherever you want and copy there or create with the same content file -> "docker-compose.yml"
from this repository

$ mkdir cursor-kyiv
$ cd cursor-kyiv/
$ touch docker-compose.yml

4) Initializing database container. Run command:

$ docker-compose up db

And wait till db initializing will be finished. You will observe such message in the end:

[System] [MY-011323] [Server] X Plugin ready for connections. Socket: '/var/run/mysqld/mysqlx.sock' bind-address: '::' port: 33060)

Press CTRL+C to stop container

5) Creating database
Run command to start db container:
$ docker-compose start db

Connect to container into mysql (password for root is "password"):
$ docker exec -it cursorkyiv_db_1 mysql -uroot -p

And run:
mysql> CREATE DATABASE cult_data;

And allow root to connect from all ips, run:

mysql> UPDATE mysql.user SET host='%' WHERE user = 'root';
mysql> ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
mysql> exit;

6) Initializing Django container, run:

$ docker-compose up django

Wait till server up:
django_1  | Starting development server at http://0.0.0.0:8000/

Press CTRL+C to stop container

And run it in background:

$ docker-compose start django

Now you can use our site but there is no content

7) Add django superuser, run:

$ docker exec -it cursorkyiv_django_1 python manage.py createsuperuser

8) To add content, run:



"""
