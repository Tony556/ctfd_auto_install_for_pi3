import subprocess
rawinput = raw_input('What port would you like Gunicorn to run on? Default port: 8000 \n')
if(rawinput==''):
    portToUse = str(8000)
else:
    portToUse = str(rawinput)
interface = subprocess.check_output('netstat -i | grep BMRU', shell=True).split()[0]
detectedIP = subprocess.check_output("ifconfig "+interface+" | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'", shell=True)
print 'Alright! Now, in your web browser, connect to http://'+detectedIP.rstrip()+':'+portToUse
print ''
print ''
subprocess.call('sudo gunicorn --bind 0.0.0.0:'+portToUse+' -w 1 "CTFd:create_app()"', shell=True)