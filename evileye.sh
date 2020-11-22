
#colour code

r='\e[1;31m'
g='\e[1;32m'
y='\e[1;33m'
b='\e[1;34m'
p='\e[1;35m'
lb='\e[1;36m'
gr='\e[1;30m'
wh='\e[1;37m'

#input
echo -e $g"          What is your banner name: "$wh
read a
echo -e $g"          What is your cowsay name: "$wh
read b

echo "clear" >remove.txt
echo "cowsay -f eyes "$b" | lolcat" >cowsay.txt
echo "figlet "$a" | lolcat" >bannername.txt
echo "PS1='\$ '" >mark.txt
rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc
touch bash.bashrc
cp bash.bashrc /data/data/com.termux/files/usr/etc/
cat "remove.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "cowsay.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "bannername.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
rm -rf remove.txt
rm -rf cowsay.txt
rm -rf bannername.txt

figlet Done!!! | lolcat
sleep 2
exit
