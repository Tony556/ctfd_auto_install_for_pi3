import os
import subprocess

#print subprocess.check_output(["sudo", "vim", "/etc/hostname"])
'''
subprocess.call(["wget", "https://github.com/isislab/CTFd/archive/master.zip"])

subprocess.call(["unzip", "master.zip"])

subprocess.call(["rm", "master.zip"])
'''

subprocess.call(["chmod", "+x", "CTFd-master/prepare.sh"])
subprocess.call(["sudo", "./prepare.sh"], cwd="/home/pi/CTFd_Script/CTFd-master/")
subprocess.call(["vim", "CTFd-master/CTFd/config.py"])
subprocess.call(["chmod", "+x", "CTFd-master/serve.py"])
subprocess.call(["sudo", "python", "serve.py"], cwd="/home/pi/CTFd_Script/CTFd-master")
#TODO: Static ip, gunicorn, etc
