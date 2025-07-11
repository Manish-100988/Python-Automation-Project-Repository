import paramiko
import time

ip_address = "192.168.122.72"
username = "david"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("Successful connection", ip_address)