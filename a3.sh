
#colour code

r='\e[1;31m'
g='\e[1;32m'
y='\e[1;33m'
b='\e[1;34m'
p='\e[1;35m'
lb='\e[1;36m'
gr='\e[1;30m'
wh='\e[1;37m'

#colour code

r='\e[1;31m'
g='\e[1;32m'
y='\e[1;33m'
b='\e[1;34m'
p='\e[1;35m'
lb='\e[1;36m'
gr='\e[1;30m'
wh='\e[1;37m'

echo -e $b"                                   By Dave Smith"
echo -e $lb"                         owner of CYBER WORRIORS"
echo
while true; do
    read -p "Are you wan´t to make banner with animation( y /n )" yn
    case $yn in
        [Yy]* ) bash animation.sh ; break;;
        [Nn]* ) bash evileye.sh ;;
        * ) echo "Please answer   yes    or    no.";;
    esac
done


