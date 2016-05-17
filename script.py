#SCRUM:
'''
ICEBOX:

EMERGENCY:

IN PROGRESS:
    Gunicorn

TESTING:
    Static IP

COMPLETE:
    add "Type OK to accept the possible risk to your system. I AM NOT HELD ACCOUNTABLE etc etc"

'''
import sys, subprocess

def staticIPSetup():
    #Getting the current RUNNING network interface. Keyword is RUNNING, since it searches for the BMRU tag on the interface. Unknown how it deals with wlan and ethernet connected.
    detectedInt = subprocess.check_output('netstat -i | grep BMRU', shell=True).split()[0]

    rawinput = raw_input("Please enter a network interface for the static IP? Detected interface is: "+detectedInt+"\nEnter nothing to use it, otherwise, enter the interface you would like to use\n")

    if(rawinput==''):
        interface = detectedInt
    else:
        interface = rawinput
    #Used a nice command from cyberciti.biz to get the IP from the interface.
    # http://www.cyberciti.biz/faq/how-to-find-out-the-ip-address-assigned-to-eth0-and-display-ip-only/

    detectedIP = subprocess.check_output("ifconfig "+interface+" | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'", shell=True)\

    rawinput2 = raw_input("Please enter an IP Address for the static IP? Detected IP for set interface is: "+detectedIP+"\nEnter nothing to use it, otherwise, enter the IP you would like to use\n")

    if(rawinput2==''):
        ipToUse = detectedIP
    else:
        ipToUse = rawinput2

    #More nice commands from online, this time from a Stack Overflow answer, to get the default gateway (cut out of the answer to fit my needs)
    # https://stackoverflow.com/questions/1204629/how-do-i-get-the-default-gateway-in-linux-given-the-destination

    detectedGateway = subprocess.check_output("ip route | awk '/default/ { print $3 }'", shell=True)\

    rawinput3 = raw_input("Please enter a Default Gateway for the static IP? Detected Gateway for set interface is: "+detectedGateway+"\nEnter nothing to use it, otherwise, enter the IP you would like to use\n")

    if(rawinput3==''):
        gatewayToUse = detectedGateway
    else:
        gatewayToUse = rawinput3

    #Open resolv.conf to get DNS records
    with open('/etc/resolv.conf') as f:
        #Split each record into different lines
        lists = f.read().splitlines()

    #Initialize the list of DNS Servers
    dns_servers = []

    for item in lists:
        #Split the items by the spaces
        item = item.split()
        if item[0] == 'nameserver':
            #Append each record into the array
            dns_servers.append(item[1])

    #TODO: Redo this??
    #Use the first record found.
    dnsToUse = dns_servers[0]

    #Data to insert into /etc/dhcpcd.config
    #Command: echo "data" | sudo tee -a /etc/dhcpcd.conf
    '''
    interface wlan0
    static ip_address=192.168.3.131
    static routers=192.168.3.2
    static domain_name_servers=8.8.8.8
    '''
    #Obtaining default gateway: ip route | awk '/default/ { print $3 }'

    #Appending to dhcpcd.config
    subprocess.call('echo "#AutoCTFd set Static IP settings"                             | sudo tee -a /etc/dhcpcd.conf', shell=True)
    subprocess.call('echo "interface '                    + interface                +'" | sudo tee -a /etc/dhcpcd.conf', shell=True)
    subprocess.call('echo "static ip_address='            + ipToUse                  +'" | sudo tee -a /etc/dhcpcd.conf', shell=True)
    subprocess.call('echo "static routers='               + gatewayToUse             +'" | sudo tee -a /etc/dhcpcd.conf', shell=True)
    subprocess.call('echo "static domain_name_servers='   + dnsToUse                 +'" | sudo tee -a /etc/dhcpcd.conf', shell=True)

    rawinput = raw_input('Do you wish to restart your network interface?\nType "Y" or "Yes" to do so, anything else to not.\n').lower()

    #Restarting network interface
    if rawinput == 'y' or rawinput == 'yes':
        subprocess.call('sudo service networking restart', shell=True)

def gunicornInstall():
    subprocess.call(["sudo", "pip", "install", "gunicorn"])
    gunicorn_file = '''import subprocess
rawinput = raw_input('What port would you like Gunicorn to run on? Default port: 8000')
if(rawinput==''):
    portToUse = 8000
else:
    portToUse = rawinput
subprocess.call('gunicorn --bind 0.0.0.0:8000 -w 1 "CTFd:create_app()"', shell=True)
    '''
    with open('startGunicornCTFd.py', 'w+') as f:
        f.write(gunicorn_file)


#Warning the user about the possible risks.

try:
    raw_input('By installing and using this script, you are aware that any issues that may arise from running it, I am not accountable for, and am unable to be held accountable.\nThis script edits core system files in order to do certain functions (said functions will be labeled), and issues may arise if your system has a varying configuration.\nIf you accept the risk, just press ENTER. If not, press Ctrl+C to cancel this script.\n')
except KeyboardInterrupt:
    print('\nOk! See you next time!')
    sys.exit()

'''
#Getting CTFd, unzipping it, and deleting the zip.
subprocess.call(["wget", "https://github.com/isislab/CTFd/archive/master.zip"])

subprocess.call(["unzip", "master.zip"])

subprocess.call(["rm", "master.zip"])
'''

#Allowing certain files to be executable
#subprocess.call(["chmod", "+x", "CTFd-master/prepare.sh"])
subprocess.call(["chmod", "+x", "CTFd-master/serve.py"])

#Executing CTFd's prepare script. "cwd" is ot make sure it can get the requirements from the .txt in the same directory.
#subprocess.call(["sudo", "./prepare.sh"], cwd="/home/pi/CTFd_Script/CTFd-master/")

#Allowing user to edit config.py
raw_input('You are now going to edit config.py. Press CTRL+X, then Y, then ENTER to exit after editing.\n')
subprocess.call(["nano", "CTFd-master/CTFd/config.py"])

#subprocess.call(["sudo", "python", "serve.py"], cwd="/home/pi/CTFd_Script/CTFd-master")


rawinput = raw_input('If you wish to assign this device a Static IP Address, type "Y" or "Yes"\nType anything else to continue without it.\nWARNING: THIS EDITS SYSTEM FILES (/etc/dhcpcd.conf)\n').lower()
if(rawinput == 'y' or rawinput == 'yes'):
    staticlist = staticIPSetup()

rawinput = raw_input('If you wish to install Gunicorn onto this device, type "Y" or "Yes"\nType anything else to continue without it.\n').lower()
if(rawinput == 'y' or rawinput == 'yes'):
    gunicornInstall()
    print 'Installed! Now you can launch Gunicorn with "python startGunicornCTFd.py"'
