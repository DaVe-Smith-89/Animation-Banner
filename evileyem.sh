
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

#input
echo -e $g"          What is your banner name: "$wh
read a
echo -e $g"          What is your cowsay name: "$wh
read b
echo -e $g"          Enter your mark(Instead $):"$wh
read c
echo -e $g"          Enter your mark colour code:"$wh
read d
echo

echo "clear" >remove.txt
echo "cowsay -f eyes "$b" | lolcat " >cowsay.txt
echo "figlet "$a" | lolcat " >bannername.txt
echo PS1=$d$c >mark.txt >mark.txt
rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc
touch bash.bashrc
cp bash.bashrc /data/data/com.termux/files/usr/etc/
cat "remove.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "cowsay.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "bannername.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "mark.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
rm -rf remove.txt
rm -rf cowsay.txt
rm -rf bannername.txt
rm -rf bash.bashrc
rm -rf mark.txt
echo -e $g"copy this command now:"$r
echo "            '\e[1;37m'"
echo -e $lb

while true; do
    read -p "Are you Copied the Command?(y/n)" yn
    case $yn in
        [Yy]* ) cd && cd .. && cd usr && cd etc && nano bash.bashrc ; break;;
        [Nn]* ) echo "Please copy the command" && sleep 3 && bash animationm.sh ;;
        * ) echo "Please answer   yes    or    no.";;
    esac
done
cd && cd .. && cd usr && cd etc && rm -rf zshrc && touch zshrc && cat bash.bashrc >>zshrc
figlet Done!!! | lolcat
sleep 2
exit

