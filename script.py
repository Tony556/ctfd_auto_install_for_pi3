import os
import subprocess

def staticIPSetup():
    rawinput = raw_input("Please enter a network interface for the static IP? Detected interface is: "+subprocess.check_output('netstat -i | grep BMRU', shell=True).split()[0]+"\nEnter nothing to use it")

#print subprocess.check_output(["sudo", "vim", "/etc/hostname"])
'''
subprocess.call(["wget", "https://github.com/isislab/CTFd/archive/master.zip"])

subprocess.call(["unzip", "master.zip"])

subprocess.call(["rm", "master.zip"])
'''

#subprocess.call(["chmod", "+x", "CTFd-master/prepare.sh"])
#subprocess.call(["sudo", "./prepare.sh"], cwd="/home/pi/CTFd_Script/CTFd-master/")
subprocess.call(["vim", "CTFd-master/CTFd/config.py"])
subprocess.call(["chmod", "+x", "CTFd-master/serve.py"])
#subprocess.call(["sudo", "python", "serve.py"], cwd="/home/pi/CTFd_Script/CTFd-master")
#TODO: Gunicorn, etc
#WORKING ON: Static IP
rawinput = raw_input('If you wish to assign this device a Static IP Address, type "Y" or "Yes"\nType anything else to continue without it.\n').lower()
if(rawinput == 'y' or rawinput == 'yes'):
    staticIPSetup()
