import requests
import json
from requests.auth import HTTPDigestAuth
import cx_Oracle
from sshtunnel import SSHTunnelForwarder
import sshtunnel

'''

db_host = '10.3.192.52'
with SSHTunnelForwarder(
    ('130.35.155.106', 22),
    ssh_username="oaluser",
	ssh_password="oalpass",
	ssh_pkey="oalkey_ssh.key",
    remote_bind_address=(db_host, 1521)
) as tunnel:
	port = tunnel.local_bind_port
	DSN = "oalgeneric[oalfin]/FusionDev2#@GXPBT_OCI:%d/pgxpbt.dpdbfront1.oal.oraclevcn.com" % port
	conn = cx_Oracle.connect(DSN)
	cursor = conn.cursor()
	cursor.execute( select * from oalfsaas_repl.hr_organization_units_f_tl WHERE NAME='ORCL FR' )
	cursor = cursor.fetchall()
	print(cursor)'''

'''	

import paramiko
import sshtunnel

LOCAL_PORT = 38399

with sshtunnel.open_tunnel(
	('130.35.155.106', 22),
	ssh_username="oaluser",
    ssh_pkey="oalkey_ssh.key",
    ssh_password="oalpass",
    remote_bind_address=('10.3.192.52', 1521),
    local_bind_address=('0.0.0.0', 8002)
) as tunnel:
	client = paramiko.SSHClient()
	client.load_system_host_keys()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	DSN = "oalgeneric[oalfin]/FusionDev2#@localhost:%d/pgxpbt.dpdbfront1.oal.oraclevcn.com" % LOCAL_PORT
	client.connect(DSN)
	# do some operations with client session
	client.close()'''


'''
HOST = "130.35.155.106"
REMOTE_PORT = 1521
LOCAL_PORT = 38399
USER_NAME = "oaluser"
DSN = "oalgeneric[oalfin]/FusionDev2#@localhost:%d/pgxpbt.dpdbfront1.oal.oraclevcn.com" % LOCAL_PORT

with sshtunnel.SSHTunnelForwarder(HOST, ssh_username = USER_NAME,ssh_pkey="oalkey_ssh.key",
        remote_bind_address = ("10.3.192.52", REMOTE_PORT),
        local_bind_address = ("", LOCAL_PORT)) as server:



	conn = cx_Oracle.connect(DSN)
	cursor = conn.cursor()
	cursor.execute(select * from oalfsaas_repl.hr_organization_units_f_tl WHERE NAME='ORCL FR')
	cursor = cursor.fetchall()
	print(cursor)'''
	
	




a='ORCL FR'


con = cx_Oracle.Connection("oalgeneric[oalfin]/FusionDbGt#1@129.157.240.219:1522/pgxpgt.corpssotest.oraclecloud.internal")
cursor = con.cursor()
cursor.prepare('''select ORGANIZATION_ID from oalfsaas_repl.hr_organization_units_f_tl WHERE language = 'US' and NAME = :id ''')
cursor.execute(None, {'id': a})
executedCursor = cursor.fetchall()
executedCursor_OrgIds = executedCursor[0][0]
print(executedCursor_OrgIds)