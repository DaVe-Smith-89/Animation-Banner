import os
import time
import shutil
import sys
import glob

os.system("git pull")
os.system("clear")
myname = ["\n\n\n\n\t\t\033[94m\033[01m██████╗  █████╗ ██╗   ██╗███████╗\n",
        "\t\t\033[94m██╔══██╗██╔══██╗██║   ██║██╔════╝\n",
        "\t\t\033[94m██║  ██║███████║██║   ██║█████╗  \n",
        "\t\t\033[94m██║  ██║██╔══██║╚██╗ ██╔╝██╔══╝  \n",
        "\t\t\033[94m██████╔╝██║  ██║ ╚████╔╝ ███████╗\n",
        "\t\t\033[94m╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝\n\n",
        "\t\033[39m     ███████╗███╗   ███╗██╗████████╗██╗  ██╗\n",
        "\t\033[39m     ██╔════╝████╗ ████║██║╚══██╔══╝██║  ██║\n",
        "\t\033[39m     ███████╗██╔████╔██║██║   ██║   ███████║\n",
        "\t\033[39m     ╚════██║██║╚██╔╝██║██║   ██║   ██╔══██║\n",
        "\t\033[39m     ███████║██║ ╚═╝ ██║██║   ██║   ██║  ██║\n",
        "\t\033[39m     ╚══════╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝\n"]
for name in myname:
	print(name, end='')
	sys.stdout.flush()
	time.sleep(0.03)
time.sleep(2)
def logo():
	os.system("clear")
	print()
	print("\033[94m\033[01m   █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗")
	print("\033[94m  ██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝")
	print("\033[94m  ███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ")
	print("\033[94m  ██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ")
	print("\033[94m  ██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗")
	print("\033[94m  ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝")
	print()
	print("\033[39m      ██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ ")
	print("\033[39m      ██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗")
	print("\033[39m      ██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝")
	print("\033[39m      ██╔══██╗██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗")
	print("\033[39m      ██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║")
	print("\033[39m      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝")
	print()
	logdes = ["\t\033[01m\033[32m    [+] Coded By Dave Smith CYBER WARRIOR\n",
                  "\t\033[32m    [+] 👑 OWNER OF SL CYBER WARRIORSᵀᴹ \n\n"]
	for log in logdes:
		for lo in log:
			print(lo, end='')
			sys.stdout.flush()
			time.sleep(0.02)
choices = ["\n     \t\t\033[93m\033[40m[1] Add Banner\033[49m\n",
	   "     \t\t\033[93m\033[40m[2] Update Tool\033[49m\n",
	   "     \t\t\033[93m\033[40m[3] About Us\033[49m\n",
	   "     \t\t\033[93m\033[40m[4] Join Us\033[49m\n",
	   "     \t\t\033[93m\033[40m[5] Comment/Report errors\033[49m\n",
	   "     \t\t\033[93m\033[40m[6] exit\033[49m\n\n",
	   "\033[94mEnter Your Choice: "]
logo()
for choice in choices:
	for cho in choice:
		print(cho ,end='')
		sys.stdout.flush()
		time.sleep(0.02)
mcho = int(input())
def banner():
	logo()
	menu = ["\n\t\t\033[93m\033[40m[01] EvilEye Banner  (Normal)\033[49m\n",
		"\t\t\033[93m\033[40m[02] EvilEye Banner  (Animation)\033[49m\n",
		"\t\t\033[93m\033[40m[03] Custom Banner   (Normal)\033[49m\n",
		"\t\t\033[93m\033[40m[04] Custom Banner   (Animation)\033[49m\n",
		"\t\t\033[93m\033[40m[05] Neofetch Banner (Normal)\033[49m\n",
		"\t\t\033[93m\033[40m[06] Neofetch Banner (Animation)\033[49m\n",
		"\t\t\033[93m\033[40m[07] Neofetch Custom (Normal)\033[49m\n",
		"\t\t\033[93m\033[40m[08] Neofetch Custom (Animation)\033[49m\n",
		"\t\t\033[93m\033[40m[09] Help            (banners information)\033[49m\n",
		"\t\t\033[93m\033[40m[10] Main Menu\033[49m\n\n",
		"\033[94mEnter Your Choice: "]
	for men in menu:
		for me in men:
			print(me, end='')
			sys.stdout.flush()
			time.sleep(0.01)
	bc = int(input())

	if glob.glob("/data/data/com.termux/files/usr/etc/zshrc"):
		os.remove("/data/data/com.termux/files/usr/etc/zshrc")
	if glob.glob("/data/data/com.termux/files/usr/etc/bash.bashrc"):
		os.remove("/data/data/com.termux/files/usr/etc/bash.bashrc")
	if glob.glob("/data/data/com.termux/files/usr/etc/motd"):
		os.remove("/data/data/com.termux/files/usr/etc/motd")
	if glob.glob("/data/data/com.termux/files/usr/etc/dvsbanner"):
		os.remove("/data/data/com.termux/files/usr/etc/dvsbanner")
	if glob.glob("/data/data/com.termux/files/usr/etc/banner"):
		os.remove("/data/data/com.termux/files/usr/etc/banner")

	if bc == 1:
		font = ["\n\t\t\033[93m\033[40m[1] Figlet\033[49m",
			"\n\t\t\033[93m\033[40m[2] Toilet\033[49m",
			"\n\n\033[94mEnter Your Choice: "]
		for fon in font:
			for fo in fon:
				print(fo, end='')
				sys.stdout.flush()
				time.sleep(0.02)
		fonch = int(input())
		if fonch == 1:
			open("bash.bashrc" ,"w")
			open("zshrc" ,"w")
			ban = [ "\n\033[93m\033[40mEnter Your Banner Name: \033[49m" ]
			for ba in ban:
				for b in ba:
					print(b, end='')
					sys.stdout.flush()
					time.sleep(0.02)
			banin = str(input())
			cow = [ "\n\033[93m\033[40mEnter Your Cowsay Name: \033[49m" ]
			for co in cow:
				for c in co:
					print(c, end='')
					sys.stdout.flush()
					time.sleep(0.02)
			cowin = str(input())
			with open("bash.bashrc" ,"w") as bash:
				bash.write("cowthink -f eyes "+cowin+" | lolcat && ")
				bash.write("figlet "+banin+" | lolcat && ")
				bash.write("PS1=\"$ \"")
			with open("zshrc" ,"w") as zsh:
				zsh.write("cowthink -f eyes "+cowin+" | lolcat && ")
				zsh.write("figlet "+banin+" | lolcat && ")
				zsh.write("PS1=\"$ \"")
			shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
			shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
			os.system("figlet Done..! | lolcat")
		elif fonch == 2:
			open("bash.bashrc" ,"w")
			open("zshrc" ,"w")
			ban = [ "\n\033[93m\033[40mEnter Your Banner Name: \033[49m" ]
			for ba in ban:
				for b in ba:
					print(b, end='')
					sys.stdout.flush()
					time.sleep(0.02)
			banin = str(input())
			cow = [ "\n\033[93m\033[40mEnter Your Cowsay Name: \033[49m" ]
			for co in cow:
				for c in co:
					print(c, end='')
					sys.stdout.flush()
					time.sleep(0.02)
			cowin = str(input())
			with open("bash.bashrc" ,"w") as bash:
				bash.write("cowthink -f eyes "+cowin+" | lolcat && ")
				bash.write("toilet "+banin+" | lolcat && ")
				bash.write("PS1=\"$ \"")
			with open("zshrc" ,"w") as zsh:
				zsh.write("cowthink -f eyes "+cowin+" | lolcat && ")
				zsh.write("toilet "+banin+" | lolcat && ")
				zsh.write("PS1=\"$ \"")
			shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
			shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
			print()
			os.system("toilet Done..! | lolcat")
	elif bc == 2:
		font = ["\n\t\t\033[93m\033[40m[1] Figlet\033[49m",
			"\n\t\t\033[93m\033[40m[2] Toilet\033[49m",
			"\n\n\033[94mEnter Your Choice: "]
		for fon in font:
			for fo in fon:
				print(fo, end='')
				sys.stdout.flush()
				time.sleep(0.02)
		fonch = int(input())
		if fonch == 1:
			open("bash.bashrc" ,"w")
			open("zshrc" ,"w")
			ban = [ "\n\033[93m\033[40mEnter Your Banner Name: \033[49m" ]
			for ba in ban:
				for b in ba:
					print(b, end='')
					sys.stdout.flush()
					time.sleep(0.02)
			banin = str(input())
			cow = [ "\n\033[93m\033[40mEnter Your Cowsay Name: \033[49m" ]
			for co in cow:
				for c in co:
					print(c, end='')
					sys.stdout.flush()
					time.sleep(0.02)
			cowin = str(input())
			with open("bash.bashrc" ,"w") as bash:
				bash.write("cowthink -f eyes "+cowin+" | lolcat -a --speed=75 && ")
				bash.write("figlet "+banin+" | lolcat -a --speed=75 && ")
				bash.write("PS1=\"$ \"")
			with open("zshrc" ,"w") as zsh:
				zsh.write("cowthink -f eyes "+cowin+" | lolcat -a --speed=75 && ")
				zsh.write("figlet "+banin+" | lolcat -a --speed=75 && ")
				zsh.write("PS1=\"$ \"")
			shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
			shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
			os.system("figlet Done..! | lolcat -a")
		elif fonch == 2:
			open("bash.bashrc" ,"w")
			open("zshrc" ,"w")
			ban = [ "\n\033[93m\033[40mEnter Your Banner Name: \033[49m" ]
			for ba in ban:
				for b in ba:
					print(b, end='')
					sys.stdout.flush()
					time.sleep(0.02)
			banin = str(input())
			cow = [ "\n\033[93m\033[40mEnter Your Cowsay Name: \033[49m" ]
			for co in cow:
				for c in co:
					print(c, end='')
					sys.stdout.flush()
					time.sleep(0.02)
			cowin = str(input())
			with open("bash.bashrc" ,"w") as bash:
				bash.write("cowthink -f eyes "+cowin+" | lolcat -a --speed=75 && ")
				bash.write("toilet "+banin+" | lolcat -a --speed=75 && ")
				bash.write("PS1=\"$ \"")
			with open("zshrc" ,"w") as zsh:
				zsh.write("cowthink -f eyes "+cowin+" | lolcat -a --speed=75 && ")
				zsh.write("toilet "+banin+" | lolcat -a --speed=75 && ")
				zsh.write("PS1=\"$ \"")
			shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
			shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
			print()
			os.system("toilet Done..! | lolcat -a")
	elif bc == 3:
		open("bash.bashrc" ,"w")
		open("zshrc" ,"w")
		anim = [ "\n\033[93m\033[40mInsert your banner here..!\033[49m" ]
		for ani in anim:
			for an in ani:
				print(an, end='')
				sys.stdout.flush()
				time.sleep(0.04)
		time.sleep(2)
		os.system("nano dvsbanner")
		with open("bash.bashrc" ,"w") as bash:
			bash.write("lolcat --spread=1 --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && PS1=\"$ \"")
		with open("zshrc" ,"w") as zsh:
			zsh.write("lolcat --spread=1 --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && PS1=\"$ \"")
		shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("dvsbanner" ,"/data/data/com.termux/files/usr/etc")
		print()
		os.system("figlet Done..! | lolcat")
	elif bc == 4:
		open("bash.bashrc" ,"w")
		open("zshrc" ,"w")
		anim = [ "\n\033[93m\033[40mInsert your banner here..!\033[49m" ]
		for ani in anim:
			for an in ani:
				print(an, end='')
				sys.stdout.flush()
				time.sleep(0.04)
		time.sleep(2)
		os.system("nano dvsbanner")
		with open("bash.bashrc" ,"w") as bash:
			bash.write("lolcat -a --spread=1 --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && PS1=\"$ \"")
		with open("zshrc" ,"w") as zsh:
			zsh.write("lolcat -a --spread=1 --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && PS1=\"$ \"")
		shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("dvsbanner" ,"/data/data/com.termux/files/usr/etc")
		print()
		os.system("figlet Done..! | lolcat -a")
	elif bc == 5:
		open("bash.bashrc" ,"w")
		open("zshrc" ,"w")
		anim = [ "\n\033[93m\033[40mInsert your banner here..!\033[49m" ]
		for ani in anim:
			for an in ani:
				print(an, end='')
				sys.stdout.flush()
				time.sleep(0.04)
		time.sleep(2)
		os.system("nano dvsbanner")
		with open("bash.bashrc" ,"w") as bash:
			bash.write("echo && lolcat --spread=1 --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && echo && neofetch && PS1=\"$ \"")
		with open("zshrc" ,"w") as zsh:
			zsh.write("echo && lolcat --spread=1 --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && echo && neofetch && PS1=\"$ \"")
		shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("dvsbanner" ,"/data/data/com.termux/files/usr/etc")
		print()
		os.system("figlet Done..! | lolcat")
	elif bc == 6:
		open("bash.bashrc" ,"w")
		open("zshrc" ,"w")
		anim = [ "\n\033[93m\033[40mInsert your banner here..!\033[49m" ]
		for ani in anim:
			for an in ani:
				print(an, end='')
				sys.stdout.flush()
				time.sleep(0.04)
		time.sleep(2)
		os.system("nano dvsbanner")
		with open("bash.bashrc" ,"w") as bash:
			bash.write("echo && lolcat -a --spread=1 -a --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && echo && neofetch && PS1=\"$ \"")
		with open("zshrc" ,"w") as zsh:
			zsh.write("echo && lolcat -a --spread=1 --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && echo && neofetch && PS1=\"$ \"")
		shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("dvsbanner" ,"/data/data/com.termux/files/usr/etc")
		print()
		os.system("figlet Done..! | lolcat -a")
	elif bc == 7:
		open("bash.bashrc" ,"w")
		open("zshrc" ,"w")
		anim = [ "\n\033[93m\033[40mInsert your banner here..!\033[49m\n" ]
		for ani in anim:
			for an in ani:
				print(an, end='')
				sys.stdout.flush()
				time.sleep(0.04)
		time.sleep(2)
		os.system("nano dvsbanner")
		logod = [ "\n\033[93m\033[40mInsert your logo here..!\033[49m\n" ]
		for logod1 in logod:
			for logd in logod1:
				print(logd, end='')
				sys.stdout.flush()
				time.sleep(0.04)
		time.sleep(2)
		os.system("nano banner")
		with open("bash.bashrc" ,"w") as bash:
			bash.write("echo && lolcat --spread=1 -a --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && echo && neofetch --source /data/data/com.termux/files/usr/etc/banner | lolcat && PS1=\"$ \"")
		with open("zshrc" ,"w") as zsh:
			zsh.write("echo && lolcat --spread=1 --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && echo && neofetch --source /data/data/com.termux/files/usr/etc/banner | lolcat && PS1=\"$ \"")
		shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("dvsbanner" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("banner" ,"/data/data/com.termux/files/usr/etc")
		print()
		os.system("figlet Done..! | lolcat")

	elif bc == 8:
		open("bash.bashrc" ,"w")
		open("zshrc" ,"w")
		anim = [ "\n\033[93m\033[40mInsert your banner here..!\033[49m\n" ]
		for ani in anim:
			for an in ani:
				print(an, end='')
				sys.stdout.flush()
				time.sleep(0.04)
		time.sleep(2)
		os.system("nano dvsbanner")
		logod = [ "\n\033[93m\033[40mInsert your logo here..!\033[49m\n" ]
		for logo1 in logod:
			for logd in logo1:
				print(logd ,end='')
				sys.stdout.flush()
				time.sleep(0.04)
		time.sleep(2)
		os.system("nano banner")
		with open("bash.bashrc" ,"w") as bash:
			bash.write("echo && lolcat -a --spread=1 -a --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && echo && neofetch --source /data/data/com.termux/files/usr/etc/banner | lolcat -a --spread=1 --speed=100 && PS1=\"$ \"")
		with open("zshrc" ,"w") as zsh:
			zsh.write("echo && lolcat -a --spread=1 --speed=100 /data/data/com.termux/files/usr/etc/dvsbanner && echo && neofetch --source /data/data/com.termux/files/usr/etc/banner | lolcat -a --spread=1 --speed=100 && PS1=\"$ \"")
		shutil.move("bash.bashrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("dvsbanner" ,"/data/data/com.termux/files/usr/etc")
		shutil.move("banner" ,"/data/data/com.termux/files/usr/etc")
		print()
		os.system("figlet Done..! | lolcat -a")

	elif bc == 9:
		os.system("xdg-open https://github.com/DaVe-Smith-89/Animation-Banner-Help")
		time.sleep(5)
		banner()
	elif bc == 10:
		os.system("python Adv-Banner.py")
	else:
		print()
		print("\033[31mYour choice is wrong..!")
		print()
		time.sleep(2)
		banner()

if mcho == 1:
	banner()

elif mcho == 2:
	os.system("git pull")
	os.system("python Adv-Banner.py")

elif mcho == 3:
	logo()
	about = ["\n\033[44m\033[39mDave Smith Dave Smith Dave Smith Dave Smith Dave Smith Dave Smith\033[49m\n\n",
              "\n\033[93m\t     \033[40mCoded By Dave Smith ᶜʸᴮᴱᴿ ᵂᴬᴿᴿᴵᴼᴿ\033[49m\n",
              "\n\033[93m\t     \033[40mBy Cyber Warriors (A Technical channell )\033[49m\n",
              "\n\033[93m\t     \033[40mBy:\033[49m\n",
              "\033[93m\t\t     \033[40mDave Smith ft. John kener\033[49m\n",
              "\n\033[93m\t     \033[40mJoin us:\033[49m\n",
              "\033[93m\t\t     \033[40mTelegram: http://t.me/By_sstp\033[49m\n\n\n",
              "\033[44m\033[39mDave Smith Dave Smith Dave Smith Dave Smith Dave Smith Dave Smith\033[49m\n\n" ]

	inp = [ "\033[94mDo you wan\'t to go main menu (y/n):" ]
	for abo in about:
		print(abo, end='')
		sys.stdout.flush()
		time.sleep(0.04)
	for inpu in inp:
		for ip in inpu:
			print(ip, end='')
			sys.stdout.flush()
			time.sleep(0.02)
	b = input('')
	if b == 'Y' or b == 'y':
		os.system("python Adv-Banner.py")

	elif b == 'N' or b == 'n':
		print()
		os.system("echo '\e[1;32mThanks for using the tool'")
		print()
	else:
		print()
		print("\033[31mYour choice is wrong..!")
		time.sleep(2)
		os.system("python Adv-Banner.py")

elif mcho == 4:
	logo()
	join = [ "\n\t\t\033[40m\033[93m[1] Facebook Group\033[49m\n",
                 "\t\t\033[40m\033[93m[2] Telegram Group\033[49m\n",
                 "\t\t\033[40m\033[93m[3] Main Menu\033[49m\n\n",
                 "\033[94mEnter your choice:" ]
	for jo in join:
		for j in jo:
			print(j, end='')
			sys.stdout.flush()
			time.sleep(0.02)
	c = input()
	if c == '2':
		os.system("xdg-open http://t.me/By_sstp")
		time.sleep(5)
		os.system("python Adv-Banner.py")
	elif c == '3':
		os.system("python Adv-Banner.py")

	elif c == '1':
		os.system("xdg-open https://www.facebook.com/groups/424580708746052/?ref=share")
		time.sleep(5)
		os.system("python Adv-Banner.py")
	else:
		print()
		print("\033[31mYour choice is wrong..!")
		time.sleep(2)
		os.system("python Bomb-Master.py")
elif mcho == 5:
	os.system("xdg-open http://t.me/DaVe_Smith_89")
	time.sleep(5)
	os.system("python Adv-Banner.py")

elif mcho == 6:
	print()
	print("\033[32mThanks for using the tool")
	print()
else:
	print()
	print("\033[31mYour choice is wrong..!")
	time.sleep(2)
	os.system("python Adv-Banner.py")
