from datetime import datetime
import os
from threading import Timer
import zipfile

#Fecha del backup
fecha = datetime.today().strftime('%Y_%n_%d_%H_%M')


#Nombre del archivo de respaldo
copia = "backup/" 

username = "---------"
password = "---------"
hostname = "---------"


database_list="mysql -u%s -p%s -h %s --silent -N -e 'show databases'" % (username, password, hostname)

for database in os.popen(database_list).readlines():

    filename = "%s/%s-%s.sql" % (copia, fecha, database)

    os.popen("mysqldump -u%s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (username, password, hostname, database, filename))


