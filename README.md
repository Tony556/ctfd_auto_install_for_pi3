
![](https://github.com/Tony556/ctfd_auto_install_for_pi3/blob/master/autologo.png)
An autoinstaller script made in Python 2.7 for CTFd (built with and for the Raspberry Pi 3 Model B)
====

#NOTE: SCRIPT IS IN A WORKING STATE, BUT NOT FINISHED.

CTFd is a CTF in a can. This script puts that can into yet another can that includes basic eating utensils.

NOTES:

 - This is built with and for the Raspberry Pi 3 Model B running default Raspbian. *You may encounter issues on other systems.*
 - This is built assuming you have DHCPCD installed and use it to obtain your IP Address.

I am not responsible for any possible risk that happens on your device(s).

Install:
 1. Download the script however you like. A command you can use is `wget https://raw.githubusercontent.com/Tony556/ctfd_auto_install_for_pi3/master/script.py`
    - Shortened URL `wget -O script.py https://goo.gl/R62881`
 2. Run the script with `sudo python script.py`
    - If you encounter issues with apt-get, here are some recommended repositories for your `/etc/apt/sources.list` file. [Tutorial on how to use](https://askubuntu.com/questions/197564/how-do-i-add-a-line-to-my-etc-apt-sources-list)

     `deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main`

     `deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main`

     `deb https://deb.nodesource.com/node_0.10 jessie main`

     `deb-src https://deb.nodesource.com/node_0.10 jessie main`


[CTFd Repo](https://github.com/isislab/CTFd)

#SCRUM:

ICEBOX:

    Automatic apt-get repository installer

EMERGENCY:

IN PROGRESS:

TESTING:

    Gunicorn

COMPLETE:

    add "Type OK to accept the possible risk to your system. I AM NOT HELD ACCOUNTABLE etc etc"
    ~~Static IP~~ Removed from main script until further notice. Still enabled in script.py.old
