#SCRUM:
'''
ICEBOX:
    Gunicorn
    add "Type OK to accept the possible risk to your system. I AM NOT HELD ACCOUNTABLE etc etc"

EMERGENCY:

IN PROGRESS:

TESTING:
    Static IP

COMPLETE:


'''
import os
import subprocess

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
subprocess.call(["vim", "CTFd-master/CTFd/config.py"])

#subprocess.call(["sudo", "python", "serve.py"], cwd="/home/pi/CTFd_Script/CTFd-master")


rawinput = raw_input('If you wish to assign this device a Static IP Address, type "Y" or "Yes"\nType anything else to continue without it.\n').lower()
if(rawinput == 'y' or rawinput == 'yes'):
    staticlist = staticIPSetup()
