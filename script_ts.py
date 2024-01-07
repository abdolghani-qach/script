try:
	import requests,os,sys,time
	os.system('clear')
except:
	os.system('pip install requests')
def hh(x) :
	for i in x+  '\n' :
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.10)
if sys.version[0] != '3' :
	exit('اصدار تطبيقك غير متوافق مع لاداة ')
hh(' > welcome to my tool by Abdelghani Qach / R33D🦅< ')
ip = requests.get("https://api.ipify.org").text.strip()
print(f'>> Your IP  : {ip}')
#os.system('clear')
print('='*35)
print('[1] INSTAAL PKG Termux')
print('[2] UPDATE')
print('[0] EXIT')
print('='*35)
chss = input('choos ~> ')
if chss == '1' :
	os.system('apt update; apt upgrade -y; apt install figlet -y ; figlet WAIT ; pkg install sl -y ; apt install cmatrix -y ; pkg install coreutils -y ; clear ; figlet DARK ; apt install fish -y ; clear ; figlet DARK ; apt install toilet -y ; apt install w3m -y ; pkg install curl -y ; clear ; figlet DARK ; pkg install python -y ; pkg install python2 -y ; pkg install php -y ; clear ; figlet DARK ; pkg install clang -y ;clear;figlet DARK apt install mechanize -y ; pkg install nano -y ; pkg install bash -y ; clear ; figlet sabrt habe ; pkg install ruby -y ; pip install --upgrade pip ; pip install requests ; pkg install python -y ; pkg install python2 -y ;clear;figlet dark; pip install bs4 ; pkg install bash -y ; pkg update ; pkg upgrade-y ; pkg install nmaq -y ; apt install golang -y ; apt install host -y ; clear ; apt install nano -y ; apt install havij -y ; apt install hydra -y ; apt install wireshark -y ; apt install cmatrix -y ; pkg install wget -y ; pkg install cowsay -y ; figlet DARK ; pkg install toilet -y ; pkg install help -y ; pkg install lolcat -y ; pkg install curl -y ; pkg install wgetrc -t ; pkg install uzip -y ; pkg install openssh -y ; clear ; pkg install net-tools -y ; pkg install tor -y ;clear;figlet DARK;pkg install unrar -y ; pkg install clang -y ; gem install lolcat ; pkg install w3m -y ; pip2 install wget ; pkg install git -y ;clear;figlet DARK ; pkg update ; pkg upgrade -y ; apt update ; apt upgrade -y ; clear ; figlet DARK pkg install python2 pkg install git;pkg install python2;pkg install git;clear;figlet Tawaw bo;figlet DARK')