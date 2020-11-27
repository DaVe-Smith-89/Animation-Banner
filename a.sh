
#coded by Dave Smith
#owner of CYBER WORRIORS

#colour code

r='\e[1;31m'
g='\e[1;32m'
y='\e[1;33m'
b='\e[1;34m'
p='\e[1;35m'
lb='\e[1;36m'
gr='\e[1;30m'
wh='\e[1;37m'

#logo
clear
figlet By Dave | lolcat
sleep 0.5
figlet Smith | lolcat
sleep 2
clear
figlet Banner | lolcat -a
figlet Master | lolcat -a
echo -e $b"                                   By Dave Smith"
echo -e $lb"                         owner of CYBER WORRIORS"
echo
rm -rf /data/data/com.termux/files/usr/etc/motd
rm -rf /data/data/com.termux/files/usr/etc/zshrc
rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc
while true; do
    read -p "Are you wan´t to make your own banner( y /n )" yn
    case $yn in
        [Yy]* ) bash a4.sh ; break;;
        [Nn]* ) bash a1.sh ;;
        * ) echo "Please answer   yes    or    no.";;
    esac
done
