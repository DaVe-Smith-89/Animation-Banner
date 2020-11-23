rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc
#colour code

r='\e[1;31m'
g='\e[1;32m'
y='\e[1;33m'
b='\e[1;34m'
p='\e[1;35m'
lb='\e[1;36m'
gr='\e[1;30m'
wh='\e[1;37m'
echo -e $y
echo "
#usercolour code

red         '\\\e[1;31m'
green       '\\\e[1;32m'
yellow      '\\\e[1;33m'
blue        '\\\e[1;34m'
purple      '\\\e[1;35m'
lightblue   '\\\e[1;36m'
gray        '\\\e[1;30m'
white       '\\\e[1;37m'"

echo
echo -e $g"          Enter your mark(Instead $):"$wh
read c
echo -e $g"          Enter your mark colour code :"$wh
read d
echo

echo "clear" >b.txt
echo 'echo """""' >a.txt
nano banner.txt
echo ' """"" | lolcat -a ' >don.txt
echo PS1=$d$c >mark.txt
cat "b.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "a.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "banner.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "don.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "mark.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
rm -rf a.txt
rm -rf b.txt
rm -rf banner.txt
rm -rf don.txt
rm -rf mark.txt
sleep 2
echo -e $g"copy this command now:"$r
echo "            '\e[1;37m'"
echo -e $lb
while true; do
    read -p "Are you Copied the Command?(y/n)" yn
    case $yn in
        [Yy]* ) cd && cd .. && cd usr && cd etc && nano bash.bashrc ; break;;
        [Nn]* ) echo "Please copy the command" && sleep 3 && bash customam.sh ;;
        * ) echo "Please answer   yes    or    no.";;
    esac
done

figlet Done!!! | lolcat -a
sleep 2
exit

