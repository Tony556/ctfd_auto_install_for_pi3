import sys, subprocess

#Clearing the CLI
subprocess.call('clear', shell=True)

def gunicornInstall():
    #Installing the Gunicorn server
    #Used as a more stable, longer lasting alternative to "serve.py's" Flask server
    subprocess.call(["sudo", "pip", "install", "gunicorn"])
    #Raw python file to be written to disk as a script
    gunicorn_file = '''import subprocess
rawinput = raw_input('What port would you like Gunicorn to run on? Default port: 8000 \\n')
if(rawinput==''):
    portToUse = str(8000)
else:
    portToUse = str(rawinput)
interface = subprocess.check_output('netstat -i | grep BMRU', shell=True).split()[0]
detectedIP = subprocess.check_output("ifconfig "+interface+" | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'", shell=True)
print 'Alright! Now, in your web browser, connect to http://'+detectedIP.rstrip()+':'+portToUse
print ''
print ''
subprocess.call('sudo gunicorn --bind 0.0.0.0:'+portToUse+' -w 1 "CTFd:create_app()"', shell=True)'''

    with open('CTFd-master/startGunicornCTFd.py', 'w+') as f:
        f.write(gunicorn_file)


#Warning the user about the possible risks.

try:
    raw_input('By installing and using this script, you are aware that any issues that may arise from running it, I am not accountable for.\nIf you wish to continue, just press ENTER. If not, press Ctrl+C to cancel this script.\n')
except KeyboardInterrupt:
    print('\nOk! See you next time!')
    sys.exit()


#Getting CTFd, unzipping it, and deleting the zip.
subprocess.call(["wget", "https://github.com/isislab/CTFd/archive/master.zip"])

subprocess.call(["unzip", "master.zip"])

subprocess.call(["rm", "master.zip"])


#Allowing certain files to be executable
subprocess.call(["chmod", "+x", "CTFd-master/prepare.sh"])
subprocess.call(["chmod", "+x", "CTFd-master/serve.py"])

#Executing CTFd's prepare script. "cwd" is ot make sure it can get the requirements from the .txt in the same directory.
#Getting the Current Working Directory and trimming trailing newline.
current = subprocess.check_output(['pwd']).rstrip()
subprocess.call(["sudo", "apt-get", "update"])
subprocess.call(["sudo", "./prepare.sh"], cwd=""+current+"/CTFd-master/")


gunicornInstall()

#Clearing the CLI
subprocess.call('clear', shell=True)

print 'Installed! Now you can launch the server by going into CTFd-master with "cd CTFd-master/" and running "python startGunicornCTFd.py"'
