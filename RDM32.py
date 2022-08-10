import requests,random,sys,json,os,re
from time import sleep as slp
from os import system as cmd
import os
totaldmp = 0
count = 0
try:
	os.mkdir('Data')
except:
	pass
try:
	os.remove('temp.txt')
except:
	pass
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
def logo():
	cmd('clear')
	print("""\033[92;1m
 @@@@@@@    @@@@@@@@   @@@@@@@@    @@@@@@    @@@@@@@
 @@@@@@@@   @@@@@@@@   @@@@@@@@   @@@@@@@@   @@@@@@@
 @@!  @@@   @@!        @@!        @@!  @@@     @@!
 !@!  @!@   !@!        !@!        !@!  @!@     !@!
 @!@!!@!    @!!!:!     @!!!:!     @!@!@!@!     @!!
 !!@!@!     !!!!!:     !!!!!:     !!!@!!!!     !!!
 !!: :!!    !!:        !!:        !!:  !!!     !!:
 :!:  !:!   :!:        :!:        :!:  !:!     :!:
 ::   :::    :: ::::    ::        ::   :::      ::
  :   : :   : :: ::     :          :   : :      :
\033[92;1m╔══════════════════════════════════════════════════╗
\033[92;1m║\033[97;1m                \33[1;41m𝘼𝙐𝙏𝙊 𝙁𝙄𝙇𝙀 𝘿𝙐𝙈𝙋𝙄𝙉𝙂\33[0m    \033[92;1m             ║
\033[92;1m╚══════════════════════════════════════════════════╝
 ::   :::    :: ::::    ::        ::   :::      ::
  :   : :   : :: ::     :          :   : :      :
\033[92;1m╔═════════════════╗════════════════════════════════╗
\033[92;1m║[\033[91;1m●\033[92;1m] \033[97;1m𝘿𝙀𝙑𝙊𝙇𝙊𝙋𝙀𝙍    \033[92;1m║\033[96;1m 𝘙𝘌𝘍𝘈𝘛 𝘚𝘏𝘈𝘏𝘙𝘐𝘈𝘙\033[92;1m                 ║
\033[92;1m║═════════════════╗════════════════════════════════\033[92;1  ║
\033[92;1m║[\033[91;1m●\033[92;1m] \033[97;1m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆     \033[92;1m║\033[95;1m 𝘙𝘌𝘍𝘈𝘛 𝘚𝘏𝘈𝘏𝘙𝘐𝘈𝘙\033[92;1m                 ║
\033[92;1m║═════════════════╗════════════════════════════════\033[92;1  ║
\033[92;1m║[\033[91;1m●\033[92;1m] \033[97;1m𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋     \033[92;1m║\033[94;1m +8801613732902\033[92;1m                 ║
\033[92;1m║═════════════════╗════════════════════════════════\033[92;1  ║
\033[92;1m║[\033[91;1m●\033[92;1m] \033[97;1m𝙂𝙄𝙏𝙃𝙐𝘽       \033[92;1m║\033[93;1m 𝘙𝘌𝘍𝘈𝘛-156     \033[92;1m                 ║
\033[92;1m║═════════════════╗════════════════════════════════\033[92;1  ║
\033[92;1m║[\033[91;1m●\033[92;1m] \033[97;1m𝙏𝙊𝙊𝙇𝙎        \033[92;1m║\033[96;1m 𝘈𝘜𝘛𝘖 𝘍𝘐𝘓𝘌 𝘋𝘜𝘔𝘗𝘐𝘕𝘎\033[92;1m              ║
\033[92;1m║═════════════════╗════════════════════════════════\033[92;1  ║
\033[92;1m║[\033[91;1m●\033[92;1m] \033[97;1m𝙉𝙊𝙏𝙀         \033[92;1m║\033[91;1m 3G,4G,5G 𝘚𝘗𝘌𝘌𝘋\033[92;1m                 ║
\033[92;1m╚══════════════════════════════════════════════════╝
 ::   :::    :: ::::    ::        ::   :::      ::
  :   : :   : :: ::     :          :   : :      :""")
def login():
	logo()
	try:
		fbcokis= input('\033[1;93m[•] PUR YOUR COOKIS : ')
		head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
		open("data/token.txt", "w").write(eaag.group(1))
		open("data/cookie.txt", "w").write(fbcokis)
		token = open('data/token.txt','r').read()
		info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":fbcokis}).json()
		menu()
	except Exception as e:
		os.system("rm -f /sdcard/data/token.txt")
		print(f"Error {e}")
		slp(2)
		login()
def grep(f):
	o = input('\033[0;97m[•] NEW FILE NAME : ')
	try:
		ask_link = int(input('\033[1;96m[•] ENTER DUMP LIMIT : '))
	except:
		ask_link = 1
		completed = 0
	for links in range(ask_link):
		li = input('\033[1;91m[•] EXAMPLE \033[1;97m[100083,100084\n\033[1;92m[•] PUT YOUR UID CODE : ')
		os.system('cat '+f+' | grep "'+li+'" >> '+o)
	print("")
	
	print("[•] SEPARATING SUCCESSFUL")
	print("[•] NEW FILE SAVE " + o)
	input("[•] BACK ")
	menu()
def menu():
	fbidz = []
	logo()
	try:
		fbcokis = open("/sdcard/data/cookie.txt", "r").read()
		token = open('/sdcard/data/token.txt','r').read()
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
	except:
		slp(1)
		login()
	global totaldmp,count
	try:
		token=open('/sdcard/data/token.txt','r').read()
		fbcokis = open("/sdcard/data/cookie.txt", "r").read()
	except FileNotFoundError:
		print("\x1b[1;91m[!] TOKEN NOT FOUND")
		slp(1)
		cmd('rm -rf /sdcard/data/token.txt')
		login()
	try:
		cmd('clear')
		logo()
		try:
			fbbuid = input("\033[1;94m[•] EXAMPLE\033[1;91m [100084066754739]\n\033[1;95m[•] ENTER PUBLIC ID : ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			for idnm in dmp['friends']['data']:
				totaldmp+=1
				fbidz.append(idnm['id'])
		except KeyError:
			print("\n\x1b[1;91m[!] ID WAS NOT PUBLIC")
			menu()
		filepath = input("\033[1;92m[•] ENTER FILE NAME : ")
		print("\033[1;92m═══════════════════════════════════════════════")
		apnd = open(filepath,'w')
		for fbuid in fbidz:
			count += 1
			try:
				dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				for idnm in dmp['friends']['data']:
					apnd.write(idnm['id']+"|"+idnm['name']+'\n')
				print("\x1b[1;93m[•] DUMP SUCCESSFUL UID FROM : " + fbuid)
			except KeyError:
				print('\x1b[1;93m[•] DUMP SUCCESSFUL UID FROM : ' + fbuid)
		apnd.close()
		ch_x1 = input("\x1b[1;95m[•] DO YOU WANT TO USE ID SEPARATIR [n/y] : ")
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			newfile = input("\x1b[1;96m[•] FILE WITHOUT DUPLICATE ID SAVE : ")
			os.system('sort -r '+filepath+' | uniq > '+newfile)
			ch_x2 = input("\x1b[1;92m[•] DO YOU WANT TO USE ID SEPARATIR [n/y] : ")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(newfile)
			else:
				print("\033[1;92m═══════════════════════════════════════════════")
				print (f"\x1b[0;37m YOUR DUMP FILE SAVE AS :\x1b[1;92m {newfile} \x1b[0;37m")
				print("\033[1;92m═══════════════════════════════════════════════")
				print('\n')
				input("\n[•] BACK ")
				menu()
		else:
			print('\n')
			ch_x2 = input("[•] DO YOU WANT TO USE ID SEPARATIR [n/y] : ")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(filepath)
			else:
				print("\033[1;92m═══════════════════════════════════════════════")
				print (f"\x1b[0;37m TOTAL DUMP ID :\x1b[1;92m {totaldmp}")
				print (f"\x1b[0;37m YOUR DUMP FILE :\x1b[1;92m {filepath} ")
				print("\033[1;92m═══════════════════════════════════════════════")
				input("\n[•] BACK")
				menu()
	except Exception as e:
		print("[•] ERORR : %s"%e)
		exit("")
if __name__ == '__main__':
	menu()