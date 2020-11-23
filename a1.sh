
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

echo
while true; do
    read -p "Are you wan´t to change $ mark( y /n )" yn
    case $yn in
        [Yy]* ) bash a2.sh ; break;;
        [Nn]* ) bash a3.sh ;;
        * ) echo "Please answer   yes    or    no.";;
    esac
done
rm -rf /data/data/com.termux/files/usr/etc/motd
rm -rf /data/data/com.termux/files/usr/etc/zshrc


