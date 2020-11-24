
rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc
echo "clear" >b.txt
echo 'echo """""' >a.txt
nano banner.txt
echo ' """"" | lolcat ' >don.txt
echo "PS1='\$ '" >mark.txt
cat "b.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "a.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "banner.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "don.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
cat "mark.txt" >>/data/data/com.termux/files/usr/etc/bash.bashrc
rm -rf don.txt
rm -rf banner.txt
rm -rf a.txt
rm -rf b.txt
cd
cd ..
cd usr
cd etc
cat bash.bashrc >>/data/data/com.termux/files/usr/etc/zshrc
figlet Done !!! | lolcat

