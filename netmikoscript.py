from netmiko import ConnectHandler
from getpass import getpass
import time
from netmiko.ssh_exception import AuthenticationException,SSHException,NetMikoTimeoutException
import sys
sys.tracebacklimit = 0
int = 'a'


uname = input('Username: ')
pword = getpass('Password: ')

device = {
    'ip' : '192.168.11.11',
    'username' : uname,
    'password' : pword,
    'device_type' : 'cisco_ios'
}

try:
    c = ConnectHandler(**device)
    output = c.send_command('show run')
    timestr =  'backup' + time.strftime('%Y-%m-%d') +'.conf'
    backup = open(timestr, 'w')
    backup.write(output)
    backup.close()
except(AuthenticationException):
    print("An authentication error has occured while connection to: " + device['ip'])
except(NetMikoTimeoutException):
    print("Connection timeout to device: " + device['ip'])
except(SSHException):
    print("an error occured while while connecting to device " + device['ip'] + ' via SSH, check SSH.')
