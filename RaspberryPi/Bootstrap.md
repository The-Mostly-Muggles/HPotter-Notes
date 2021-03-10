# Requirements

## Hardware

* Raspberry Pi, anything would really work, for pi0 networking would need to be added and wifi isn't ideal on the pi0w but should work.
* microSD card, 16-32gb very reasonably more than enough
* Decent power cord, Raspberries are tough boards but not when it comes to inconsistent power supplies
* Internet conection, ether hardwired preffered but wifi's also easy

## Software

* Image of the OS to flash on the SD card for the pi. Recommend the light weight headless (withouth desktop enviornment) Raspberry Pi OS Lite
> https://www.raspberrypi.org/software/operating-systems/
> 
https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-01-12/2021-01-11-raspios-buster-armhf-lite.zip

> linux or mac os ``` curl -O https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-01-12/2021-01-11-raspios-buster-armhf-lite.zip```

* check your hashsums
> linux ```sha256sum 2021-01-11-raspios-buster-armhf-lite.zip``` 

> MacOS ```shasum -a 256 2021-01-11-raspios-buster-armhf-lite.zip```

insure ouput matches the websites (lite is currently 'd49d6fab1b8e533f7efc40416e98ec16019b9c034bc89c59b83d0921c2aefeef')


* Program to flash the SD card, etcher works great
> debian based distros ```sudo apt update && sudo apt install balena-etcher-electron```

> MacOS ```brew install balenaetcher```

> Download for any OS here: https://www.balena.io/etcher/

### Bootstrapping

* Run etcher, select OS image, select sdcard, flash sdcard
* After flashing remount the card if needed and create file of name 'ssh' with zero content in /boot directory

> linux ```touch /media/$USER/boot/ssh```

> MacOS ```touch /Volumes/boot/ssh```

> Windows create and save a file with name 'ssh' no extention in the /boot directory of the card

* Unmount the card and plug everything in to go -unless you need wifi *

> linux ```vim [or nano or whatever] /media/$USER/boot/wpa_supplicant.conf```

> MacOS ```vim [or nano or whatever] /Volumes/boot/wpa_supplicant.conf```

> Windows create and save a file with name 'wpa_supplicant.conf' no extention in the /boot directory of the card

For each OS the contents of the 'wpa_supplicant.conf' file should be:

		country=US		#change country if needed
		ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
		update_config=1

		network={
    		ssid="NETWORK-NAME"
    		psk="NETWORK-PASSWORD"
		}

### Login add key

* Find the IP address of your pi, either logging into the network router or scanning the network will work fine
* If you don't have nmap install it; the flags are -v verbose, -A aggressive (enables OS detection), -T4 the speed of the scan, 192.168.???.???, 10.?.?.? CIDR notation for your local network

> nmap -v -A -T4 192.168.0.0/24

* If accessible to you it's probably faster to just login to your router in a browser at the gatway address

> http://192.168.0.1

* SSH into the pi
> ssh pi@192.168.0.???
		password: raspberry

* change the password from default
> passwd
> leave session open

* Generate SSH keys on host machine if you don't have them (currently two of  the strongest key options)
> ssh-keygen -t ed25519 -a 100  -f ~/.ssh/id_ed25519 -C "comments to distinguish this key"
> ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -C "comments to distinguish this key"

* if you like you can add the ssh-keys to your ssh-agent (on both mac and linux)
> ssh-add 

* check keys were added
> ssh-add -l

* Pass the your ssh-key to the raspberry
> ssh-copy-id pi@192.168.0.???

* return to previous session to ensure ssh-key.pub is within ~/.ssh/authorized_keys
> cat ~/.ssh/authorized_keys

#### Config & Hardening

* There are a ton of ways to continue to harden the pi's operating system, just going to go over some of the most significant*

* After changing password make changes needed within raspi-config
> sudo raspi-config
		+ change gpu memory to 16
        + set local to en_US rather than en_GB (use space bar to deselect) Be sure to select UTF-8
        + Expand file system
        + finish -> reboot

* Change ssh configurations, relogin through ssh
> sudo nano /etc/ssh/sshd_config
		change lines

> PermitRootLogin No

> PasswordAuthentication No

* Lots more could be done but those most important

> sudo reboot 


**optional** for ease of use for shortcuts
```
vim choice
----
#! /bin/bash -e

filename=".choices"

# see if there's a '-f filename'
if [[ "$1" == "-f" ]]
then
    # use it for the commands
    filename="$2"
    shift
    shift
elif [[ ! -r $filename ]]
then
    # otherwise, look in the current directory for a '.choices' file and
    # use that. if there isn't one here, look in parent directories until
    # there are no more parent directories.
    prefix=.
    while true
    do
        absolute=$(cd $prefix; pwd)

        if [[ -r "$absolute/$filename" ]]
        then
            filename=$absolute/$filename
            break
        fi

        if [[ "$absolute" = "/" ]]
        then
            echo "No $filename file found, exiting"
            exit 1
        fi

        prefix=$prefix/..
    done
fi

# if the user pre-supplied a number, use that.
if [[ "$1" != "" ]]
then
    a=$1
    shift
    echo `sed -ne "$a,$a p" "$filename"` "$*"
    eval `sed -ne "$a,$a p" "$filename"` "$*"
    exit
fi

IFS=$'\n'

# otherwise, give them a choice and remember it in their history.
select CHOICE in `cat $filename`
do
    echo "$CHOICE" >> ~/.bash_history
    eval $CHOICE $*
    break
done
----

chmod +x choice
sudo mv choice /usr/local/bin/

**optional** for ease of use for shortcuts


git clone https://github.com/The-Mostly-Muggles/HPotter.git
git checkout integration
git pull

> cd docker_files

> cd sshd
> docker build -t debian:sshd .
