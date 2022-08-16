#####IMPORT#####
import requests,random,sys,json,os,re,time
from time import sleep as slp
from os import system as cmd
####EMPTY####
totaldmp = 0
count = 0
reqs = requests.Session()
######COLOUR#####
BN = '\x1b[1;97m'
BR = '\x1b[1;91m'
BG = '\x1b[1;92m'
BY = '\x1b[1;93m'
BF = '\x1b[1;95m'
BB = '\x1b[1;96m'
ball = (BN,BR,BG,BY,BB)
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
## Color public
P = '\x1b[0;97m' # WHITE
M = '\x1b[0;91m' # MERAH
H = '\x1b[0;92m' # HIJAU.
K = '\x1b[0;93m' # KUNINg.
B = '\x1b[0;94m' # BIRU.
U = '\x1b[0;95m' # UNGU.
O = '\x1b[0;96m' # BIRU MUDA.
N = '\x1b[0m'    # WARNA MATI
I='\x1b[0;32m'
C='\x1b[0;36m'
M='\x1b[0;31m'
U='\x1b[0;35m'
K='\x1b[0;33m'
#P='\033[0;37m'
P='\x1b[00m'
H='\x1b[0;90m'
Q="\x1b[00m"
i='\x1b[0;32m'
c='\x1b[0;36m'
m='\x1b[0;31m'
u='\x1b[0;35m'
k='\x1b[0;33m'
b='\x1b[0;34m'
#P='\033[0;37m'
p='\x1b[00m'
h='\x1b[0;90m'
q="\x1b[00m"
version_xx=("2.0.3")
war = ("[+] ")
inp = ("[*] ")
bulat = ("[•] ")
garis = (war+"\033[1;92m═══════════════════════════════════════════════")
#####run text####
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
######STYLE#####
def logo():
    cmd('clear')
    print (
random.choice(ball) + """
\033[92;1m╭───────────────────────────────────────────────────────────╮
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m│        \033[91;1m██████╗  \033[92;1m███████╗ \033[93;1m███████╗  \033[94;1m█████╗  \033[96;1m████████╗      \033[92;1m│
\033[92;1m│        \033[91;1m██╔══██╗ \033[92;1m██╔════╝ \033[93;1m██╔════╝ \033[94;1m██╔══██╗ \033[96;1m╚══██╔══╝      \033[92;1m│
\033[92;1m│       \033[91;1m ██████╔╝ \033[92;1m█████╗   \033[93;1m█████╗   \033[94;1m███████║    \033[96;1m██║         \033[92;1m│
\033[92;1m│        \033[91;1m██╔══██╗ \033[92;1m██╔══╝   \033[93;1m██╔══╝   \033[94;1m██╔══██║    \033[96;1m██║         \033[92;1m│
\033[92;1m│       \033[91;1m ██║  ██║ \033[92;1m███████╗ \033[93;1m██║      \033[94;1m██║  ██║    \033[96;1m██║         \033[92;1m│
\033[92;1m│        \033[91;1m╚═╝  ╚═╝ \033[92;1m╚══════╝ \033[93;1m╚═╝      \033[94;1m╚═╝  ╚═╝    \033[96;1m╚═╝         \033[92;1m│
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m│           \x1b[1;33m╔══════════════════════════════════╗\033[1;91m            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m╔══════════════════════════════╗\033[1;33m ║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] TOOL NAME : FILE MAKING   \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] AUTHOR    : REFAT SHAHRIAR\033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] GITHUB    : REFAT-156     \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] FACEBOOK  : REFAT SHAHRIAR\033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] GROUP     : TERMUX LOVER  \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] WHATSAPP  : 01613732902   \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m╚══════════════════════════════╝\033[1;33m ║            \033[92;1m│
\033[92;1m│           \x1b[1;33m╚══════════════════════════════════╝\033[1;91m            \033[92;1m│
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m╰───────────────────────────────────────────────────────────╯
""") 
#####METHOD#####
cokbrut=[]
tokenku = []
pwpluss,pwnya=[],[]
#####LOGIN####
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_shahriar()
        except requests.exceptions.ConnectionError:
            print(' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN')
            exit()
    except IOError:
        login_shahriar()
def login_shahriar():
    try:
        os.system('clear')
        logo()
        print('\x1b[92m[•] PUT YOUR COOKIES') 
        asu = random.choice([m,k,h,b,u])
        cookie=input(f'\x1b[93m[•] NEED COOKIES :\x1b[92m')
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
        find_token = re.search("(EAAG\w+)", data.text)
        ken=open(".token.txt", "w").write(find_token.group(1))
        cok=open(".cok.txt", "w").write(cookie)
        print('\x1b[92m[✓] LOGIN SUCCESSFUL')
        os.system("python FILE-DUMP.py")
        exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        print("\x1b[1;91m[•] COOKIES EXPIRED ")
        exit()
######MENU#####
def menu(my_name,my_id):
    logo()
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        print('\x1b[1;91m[•] TOKEN EXPIRED')
        login_shahriar()
    print("\x1b[92m[•] YOUR ID :\x1b[97m "+my_name)
    print("\x1b[92m[•] YOUR UID :\x1b[97m "+my_id)
    print("\033[1;92m═══════════════════════════════════════════════")
    print("\n\x1b[91m[1] DUMP ID FROM PUBLIC")
    print("\x1b[92m[2] DUMP ID FROM FOLLOWERS")
    print("\x1b[93m[3] AUTO EXTREACT DUMP\033[1;97m[BEST]")
    print("\x1b[94m[4] DUMP FROM OLD ID\033[1;93m[OLD]")
    print("\x1b[95m[5] DUMP FROM NEW ID\033[1;92m[NEW]")
    print("\x1b[96m[0] LOGOUT COOKIES")
    choic=input('\n\x1b[37m[•] CHOOSE : \x1b[92m')
    if choic=="1":
        refatp()
    elif choic=="2":
         refatf()
    elif choic=="3":
        os.system('python MFILE.py')
    elif choic=="4":
        ___refatold___()
    elif choic=="5":
        ___refatnew___()
    elif choic=="0":
        os.system("rm -f .token.txt");os.system("rm -f .cok.txt");exit('\n\x1b[92m[✓] LOG OUT SUCCESSFULLY')
    else:
        print("\x1b[1;91m[•] CHOICE A VALID OPTION ")
        menu()
def refatp():
    global totaldmp,count
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except FileNotFoundError:
        print("\x1b[1;91m[•] TOKEN NOT FOUND")
        slp(1)
        cmd('rm -rf .tokn.txt')
        login()
    try:
        cmd('clear')
        logo()
        print('\x1b[93m[•] ENTER FILE SAVE PATH')
        print('\x1b[96m[•] EXAMPLE /sdcard/refat.txt')
        filepath = input("\x1b[94m[•] ENTER FILE NAME : \x1b[92m")
        apnd = open(filepath , 'a')
        for count in range(100000):
            count += 1
            fbuid = input(f"\n\x1b[0;94m[{count}] ENTER PUBLIC ID : \x1b[92m")
            if  fbuid=='stop':
                break
                apnd.close()
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":cok}).json()
                for idnm in dmp['friends']['data']:
                    totaldmp+=1
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')
            except KeyError:
                print("\n\x1b[1;91m[•] ID WAS NOT PUBLIC");pass
            print(f'\x1b[1;35m[•] TOTAL ID : {totaldmp}')
        apnd.close()
        print (f"\x1b[0;37mTOTAL DUMP {totaldmp} IDs ")
        print (f"\x1b[0;33mFILE LOCATION {filepath} ")
        input("\x1b[1;97mPRESS ENTER TO BACK ")
    except Exception as e:
        print("[•] ERROR : %s"%e)

def refatf():
    global totaldmp,count
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except FileNotFoundError:
        print("\x1b[1;91m[•] TOKEN NOT FOUND")
        slp(1)
        cmd('rm -rf .tokn.txt')
        login()
    try:
        cmd('clear')
        logo()
        print('\x1b[93m[•] ENTER FILE SAVE PATH')
        print('\x1b[92m[•] EXAMPLE /sdcard/refat.txt')
        filepath = input("\x1b[94m[•] ENTER FILE NAME : \x1b[92m")
        apnd = open(filepath , 'a')
        for count in range(100000):
            count += 1
            fbuid = input(f"\n\x1b[0;96m[{count}] ENTER FOLLOWER ID : \x1b[92m")
            if  fbuid=='stop':
                break
                apnd.close()
            try:
                dmp = requests.get(f'https://graph.facebook.com/{fbuid}?fields=subscribers.limit(50000)&access_token={token}',cookies = {"cookie":cok}).json()
                for idnm in dmp["subscribers"]["data"]:
                    totaldmp+=1
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')
            except KeyError:
                print("\n\x1b[1;91m[•] ID DON'T HAVE FOLLOWERS ");pass
            print(f'\x1b[1;32m[•] TOTAL ID : {totaldmp}')
        apnd.close()
        print (f"\x1b[0;32mTOTAL DUMP {totaldmp} IDs ")
        print (f"\x1b[0;32mFILE LOCATION {filepath} ")
        
        input("\x1b[1;97mPRESS ENTER TO BACK ")
        
    except Exception as e:
        print(f"\x1b[91m[•] ERORR : {e}")
 
def ___refatmixt___():
        try:
            token = open('.token.txt','r').read();cok = open('.cok.txt','r').read();___file = input('[•] ENTER FILE NAME :')+'.txt';___user = input("\n%s[%s•%s]%s USER :%s "%(B,P,B,P,H))
            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:
                ___get = requests.get("https://graph.facebook.com/"+___user+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":cok}).json()
                print("%s[%s•%s]%s NAME :%s %s"%(B,P,B,P,H,___get))
                print("%s "%(P))
            else:
                exit("%s[%s•%s]%s ONLY NUMBER"%(M,P,M,P))
        except (KeyError):
            exit("%s[%s•%s]%s USER ERORR"%(M,P,M,P))
        try:
            ___files = open('/sdcard/'+___file,'a')
            for z in requests.get("https://graph.facebook.com/"+___user+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":cok}).json()['friends']['data']:
                ___files.write(z['id']+'|'+z['name']+' \n')
                print('\r'+z['id']+'|'+z['name'])
            ___files.close()
            os.system("clear")
            logo()
            print("\n%s[%s•%s]%s DUMP SUCCESSFUL"%(H,P,H,P))
            print("%s[%s•%s]%s TOTAL ID :%s %s"%(H,P,H,P,K,len(open('/sdcard/'+___file,'r').readlines())))
            print("%s[%s•%s]%s YOUR FILE NAME :%s %s\n"%(H,P,H,P,K,'/sdcard/'+___file))
            input("%s[•] %sBACK%s%s"%(H,P,H,P));login()
        except (KeyError):
            exit("%s[%s!%s]%s DUMP FAILED"%(M,P,M,P))
        except (ConnectionError):
            exit("%s[%s!%s]%s CONNECTION ERROR"%(K,P,K,P))
def ___refatold___():
        try:
            token = open('.token.txt','r').read();cok = open('.cok.txt','r').read();___file = input('[•] ENTER FILE NAME :')+'.txt';___user = input("\n%s[%s•%s]%s USER :%s "%(B,P,B,P,H))
            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:
                ___get = requests.get("https://graph.facebook.com/"+___user+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":cok}).json()
                print("%s[%s•%s]%s ID NAME :%s %s"%(B,P,B,P,H,___get))
                print("%s "%(P))
            else:
                exit("%s[%s•%s]%s ONLY NUMBER"%(M,P,M,P))
        except (KeyError):
            exit("%s[%s•%s]%s USER ERROR"%(M,P,M,P))
        try:
         #   ___file = ___get.replace(' ','_')+'.txt'
            ___files = open('/sdcard/'+___file,'a')
            for z in requests.get("https://graph.facebook.com/"+___user+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":cok}).json()['friends']['data']:
                if len(z['id'])==1 or len(z['id'])==2 or len(z['id'])==3 or len(z['id'])==4 or len(z['id'])==5 or len(z['id'])==6 or len(z['id'])==7 or len(z['id'])==8 or len(z['id'])==9 or len(z['id'])==10:
                    ___files.write(z['id']+'|'+z['name']+' \n')
                    print('\r'+z['id']+'|'+z['name'])
                elif z['id'][:10] in ['1000000000']:
                    ___files.write(z['id']+'|'+z['name']+' \n')
                    print('\r'+z['id']+'|'+z['name'])
                elif z['id'][:9] in ['100000000']:
                    ___files.write(z['id']+'|'+z['name']+' \n')
                    print('\r'+z['id']+'|'+z['name'])
                elif z['id'][:8] in ['10000000']:
                    ___files.write(z['id']+'|'+z['name']+' \n')
                    print('\r'+z['id']+'|'+z['name'])
                elif z['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                    ___files.write(z['id']+'|'+z['name']+' \n')
                    print('\r'+z['id']+'|'+z['name'])
            ___files.close()
            os.system("clear")
            logo()
            print("\n%s[%s•%s]%s DUMP SUCCESSFUL"%(H,P,H,P))
            print("%s[%s•%s]%s TOTAL ID :%s %s"%(H,P,H,P,K,len(open('/sdcard/'+___file,'r').readlines())))
            print("%s[%s•%s]%s YOUR FILE NAME :%s %s\n"%(H,P,H,P,K,'/sdcard/'+___file))
            input("%s[•] %sBACK%s%s"%(H,P,H,P));login()
        except (KeyError):
            exit("%s[%s•%s]%s DUMP FAILED"%(M,P,M,P))
        except (ConnectionError):
            exit("%s[%s!%s]%s CONNECTION ERROR"%(K,P,K,P))
def ___mahadinew___():
        try:
            token = open('.token.txt','r').read();cok = open('.cok.txt','r').read();___file = input('[•] ENTER FILE NAME :')+'.txt';___user = input("\n%s[%s•%s]%s USER :%s "%(B,P,B,P,H))
            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:
                ___get = requests.get("https://graph.facebook.com/"+___user+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":cok}).json()
                print("%s[%s•%s]%s ID NAME :%s %s"%(B,P,B,P,H,___get))
                print("%s "%(P))
            else:
                exit("%s[%s•%s]%s ONLY NUMBER"%(M,P,M,P))
        except (KeyError):
            exit("%s[%s•%s]%s USER ERROR"%(M,P,M,P))
        try:
   #         ___file = ___get.replace(' ','_')+'.txt'
            ___files = open('/sdcard/'+___file,'a')
            for z in requests.get("https://graph.facebook.com/"+___user+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":cok}).json()['friends']['data']:
                if z['id'][:6] in ['100076','100077','100078','100079','100080','100081','100082','100083','100084','100085']:
                    ___files.write(z['id']+'|'+z['name']+' \n')
                    print('\r'+z['id']+'|'+z['name'])
            ___files.close()
            os.system("clear")
            logo()
            print("\n%s[%s•%s]%s DUMP SUCCESSFUL"%(H,P,H,P))
            print("%s[%s•%s]%s TOTAL ID :%s %s"%(H,P,H,P,K,len(open('/sdcard/'+___file,'r').readlines())))
            print("%s[%s•%s]%s YOUR FILE NAME :%s %s\n"%(H,P,H,P,K,'/sdcard/'+___file))
            input("%s[•] %sBACK%s%s"%(H,P,H,P));login()
        except (KeyError):
            exit("%s[%s•%s]%s DUMP FAILED"%(M,P,M,P))
        except (ConnectionError):
            exit("%s[%s•%s]%s CONNECTION ERROR"%(K,P,K,P))
login()
