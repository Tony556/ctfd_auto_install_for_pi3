import subprocess

def staticIPSetup():
    detectedInt = subprocess.check_output('netstat -i | grep BMRU', shell=True).split()[0]
    rawinput = raw_input("Please enter a network interface for the static IP? Detected interface is: "+detectedInt+"\nEnter nothing to use it, otherwise, enter the interface you would like to use\n")
    if(rawinput==''):
        interface = detectedInt
    else:
        interface = rawinput
    detectedIP = subprocess.check_output("ifconfig "+interface+" | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'", shell=True)
    rawinput2 = raw_input("Please enter an IP Address for the static IP? Detected IP for set interface is: "+detectedIP+"\nEnter nothing to use it, otherwise, enter the IP you would like to use\n")

staticIPSetup()
