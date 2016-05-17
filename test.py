import subprocess
gunicorn_file = '''import subprocess
rawinput = raw_input('What port would you like Gunicorn to run on? Default port: 8000')
if(rawinput==''):
    portToUse = 8000
else:
    portToUse = rawinput
subprocess.call('gunicorn --bind 0.0.0.0:'+portToUse+' -w 1 "CTFd:create_app()"', shell=True)
'''
def gunicornInstall():
    #subprocess.call(["sudo", "pip", "install", "gunicorn"])
    print gunicorn_file

gunicornInstall()
