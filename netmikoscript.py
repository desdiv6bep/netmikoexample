from netmiko import ConnectHandler
from getpass import getpass
import time

uname = input('Username: ')
pword = getpass('Password: ')

device = {
    'ip' : '192.168.11.11',
    'username' : uname,
    'password' : pword,
    'device_type' : 'cisco_ios'
}

c = ConnectHandler(**device)

output = c.send_command('show run')
timestr =  'backup' + time.strftime('%Y-%m-%d') +'.conf'

backup = open(timestr, 'w')

backup.write(output)
backup.close()
