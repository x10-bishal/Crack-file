# python3
# CHANNEL : @BD_GAME_CHANGER_TEAM
# Github: https://github.com/X10-BISHAL
# THIS TOOL CREATE BY BISHAL

import os, base64, sys, time
from pprint import pformat
alphabet = [
    "\U0001f600",
    "\U0001f603",
    "\U0001f604",
    "\U0001f601",
    "\U0001f605",
    "\U0001f923",
    "\U0001f602",
    "\U0001f609",
    "\U0001f60A",
    "\U0001f61b",
]
MAX_STR_LEN = 70
OFFSET = 10

black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

ask = green + '\n[' + white + '•' + green + '] '+ yellow
success = green + '\n[' + white + '✓' + green + '] '
error = red + '\n[' + white + '!' + red + '] '
info= yellow + '\n[' + white + '•' + yellow + '] '+ cyan

pwd=os.getcwd()

logo="""\033[0;92m

██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.00500)
def sprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.0050)
        
def ige():
    os.system("clear")
    input(yellow+"\n  "+white+" Open Facebook? ")
    print(yellow+"  "+white+" Report Bugs...")
    os.system("xdg-open  https://www.facebook.com/Wahid Islam Bishal")
    time.sleep(7)
    input("\n [BACK]")
    main()           
        
#def about():
    
def mover(out_file):
    move= input(yellow+" "+white+" DO U WANT TO MOVE file ?(y/n) > "+green)
    if move=="y":
        mpath=input(yellow+" "+white+" Enter the path"+white+"(Exp: "+cyan+"/sdcard"+white+") > "+ green)
        if os.path.exists(mpath):
            os.system("mv -f '"+out_file+"' '"+mpath+"'")
            sprint(success+out_file+" moved to "+mpath+"\n")
            exit()
        else:
            sprint(error+"Path do not exist!\n")
            exit()
    else:
        print("\n")
        exit()
    exit()    
def obfuscate(VARIABLE_NAME, file_content):
    b64_content = base64.b64encode(file_content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("ELAHID_BISHAL/HACKER/ELAHID_BISHAL/HACKER")).decode("ELAHID_BISHAL/HACKER/ELAHID_BISHAL/HACKER"))'
    return code


def chunk_string(in_s, n):
    """Chunk string to max length of n"""
    return "\n".join(
        "{}\\".format(in_s[i : i + n]) for i in range(0, len(in_s), n)
    ).rstrip("\\")


def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in in_s),
                MAX_STR_LEN,
            ),
        )
    )


def encryptsh():
    in_file = input(yellow+"\n "+white+")⁠—Input file Name > "+cyan)
    if not os.path.exists(in_file):
        sprint(error+'file Not Found')
        os.system("sleep 50")
        encryptsh()
    os.system("bash-obfuscate " + in_file + " -o .temp")
    if not os.path.exists(".temp"):
        try:
            sprint(info+"Installing Bash-Obfuscate....\n")
            os.system("apt install nodejs -y && npm install -g bash-obfuscate")
            os.system("bash-obfuscate " + in_file + " -o .temp")
        except:
            sprint(error+" Bash-Obfuscate not installed! Install it by:\n"+green+"[+] \"apt install nodejs -y && npm install -g bash-obfuscate\"")
            exit(1)
    out_file= input(yellow+" "+white+"Output file " + green)   
    with open(".temp",'r') as temp_f, open(out_file,'w') as out_f:
        filedata = temp_f.read()
        out_f.write("# Encrypted by: ELAHID BISHAL\n# Whatsapp: +8801613312325\n# Github: https://github.com/X10-BISHAL\n\n"+filedata)
    os.remove(".temp")
    sprint(success + Out_file + " Saved in "+pwd)
    mover(out_file)
    

def encryptsh():
    in_file = input(yellow+"\n)⁠—"+white+" Input file Name > "+cyan)
    if not os.path.exists(in_file):
        sprint(error+'File not found')
        os.system("sleep 50")
        encryptsh()
    os.system("bash-obfuscate " + in_file + " -o .temp")
    if not os.path.exists(".temp"):
        try:
            sprint(info+"Installing Bash-Obfuscate....\n")
            os.system("apt install nodejs -y && npm install -g bash-obfuscate")
            os.system("bash-obfuscate " + in_file + " -o .temp")
        except:
            sprint(error+" Bash-Obfuscate not installed! Install it by:\n"+green+"[+] \"apt install nodejs -y && npm install -g bash-obfuscate\"")
            exit(1)
    out_file= input(yellow+")⁠—"+white+" Input New File Name > " + green)   
    with open(".temp",'r') as temp_f, open(out_file,'w') as out_f:
        filedata = temp_f.read()
        out_f.write("# Encrypted by : Tutul King\nBUT DECRYPTED AND FUCKED BY @bishal079 \n# Whatsapp OF FUCKER : +88016**********\n# CHANNEL : https://t.me/tools_free_termux/\n\n"+filedata)
    os.remove(".temp")
    sprint(success + out_file + " saved in "+pwd)
    mover(out_file)
    
def decryptsh():
    in_file = input(yellow+"\n)⁠—"+white+" Input File Name > "+cyan)
    if not os.path.exists(in_file):
        print(error+' File not found')
        os.system("sleep 50")
        decryptsh()
    with open(in_file,'r') as in_f, open(".temp1",'w') as temp_f:
        filedata = in_f.read()
        if not (filedata.find("eval") != -1):
            sprint(error+" Cannot be decrypted!")
            exit()
        newdata = filedata.replace("eval","echo")
        temp_f.write(newdata)
    out_file = input(yellow+")⁠— "+white+"Input New File Name > " +green)
    os.system("bash .temp1 > .temp2")
    os.remove(".temp1")
    with open(".temp2",'r') as temp_f2, open(out_file,'w') as out_f:
        filedata = temp_f2.read()
        out_f.write("# Encrypted by Abbakareo \n# Whatsapp +2349138749261\n# Github- https://github.com/Abbakarhacker\n\n"+filedata)
    os.remove(".temp2")
    sprint(success + out_file + " Saved in "+pwd)
    mover(out_file)
 
       
def encryptvar():
    var= 'Tutul/:P/:)/;*/;*'
    if (var==""):
        sprint(error + " No variable")
        os.system("sleep 3")
        encryptvar()
    if (var.find(" ")!= -1):
        sprint(error+" Only one word!")
        os.system("sleep 3")
        encryptvar()
    VARIABLE_NAME = var * 100
    in_file = input(yellow+")⁠—"+white+" Input File Name > "+cyan)
    if not os.path.isfile(in_file):
        print(error+' File not found')
        os.system("sleep 50")
        encryptvar()
    out_file = input(yellow+")⁠—"+white+" Input New File Name > " + green)
    with open(in_file, 'r', encoding='utf-8', errors='ignore') as in_f,open(out_file, 'w') as out_f:
       file_content = in_f.read()
       obfuscated_content = obfuscate(VARIABLE_NAME, file_content)
       out_f.write("# Encrypted by: Tutul King \n# Whatsapp: +8801608843956\n# Github: https://github.com/Tutul-King\n\n"+obfuscated_content)
    sprint(success + out_file + " saved in "+pwd)
    mover(out_file)
 
def encryptem():
    in_file= input(yellow+"\n)⁠—"+white+" Input File Name > "+cyan )
    if not os.path.isfile(in_file):
            print(error+' File not found')
            os.system("sleep 50")
            encryptem()
    out_file= input(yellow+")⁠— "+white+"Input New File Name > " + green)
    with open(in_file) as in_f, open(out_file, "w") as out_f:
        out_f.write("# Encrypted by: Tutul King \n# Whatsapp: +8801608843956\n# Github: https://github.com/Tutul-King\n\n")
        out_f.write(encode_string(in_f.read(), alphabet))
        sprint(success+out_file+" Saved in "+pwd)
        mover(out_file)
 
def main():
    os.system("clear")
    slowprint(logo)
    print(yellow+'╔═════════════['+white+' MAIN  MENU '+yellow+' ]═════ ')
    print(yellow+'║')
    print(yellow+'║'+green+' ['+white+'1'+green+']'+yellow+' Encrypt'+cyan+' Bash/Shell')
    print(yellow+'║'+green+' ['+white+'2'+green+']'+yellow+' Decrypt'+cyan+' Not Working')
    print(yellow+'║'+green+' ['+white+'3'+green+']'+yellow+' Encrypt'+cyan+' Not Working')
    print(yellow+'║'+green+' ['+white+'4'+green+']'+yellow+' Encrypt'+cyan+' Python Emoji \033[0;97m[\033[0;92mBest\033[0;97m]')
    print(yellow+'║'+green+' ['+white+'5'+green+']'+yellow+' More Tools')
    print(yellow+'║'+green+' ['+white+'6'+green+']'+yellow+' Contact Author')
   # print(yellow+'║'+green+' ['+white+'7'+green+']'+yellow+' About')
    print(yellow+'║'+green+' ['+white+'0'+green+']'+yellow+' Exit')
    print(yellow+'║')
    print(yellow+'║')
    choose = input(yellow+'╚════'+red+'▶ '+ cyan)
    os.system("xdg-open  https://www.facebook.com/Mr.Tutul.ok.Bro")
    while True:
        if choose == "1" or choose=="01":
            encryptsh()
        elif choose == "2" or choose=="02":
            decryptsh()
        elif choose == "3" or choose=="03":
            encryptvar()
        elif choose == "4" or choose=="04":
            encryptem()
        elif choose == "5" or choose=="05":
            if os.path.exists("/data/data/com.termux/files/home"):
                os.system('xdg-open --view  https://www.facebook.com/Mr.Tutul.ok.Bro')
                ret=input(white+"\nENTER TO BACK > "+green)
            main()    
   #         else:
    #   os.system('xdg-open  https://www.facebook.com/Mr.Tutul.ok.Bro')
          #     ret=input(" pilih  > "+green)
     #          time.sleep(5)
      #      main()
        elif choose == "6" or choose=="06":
            ige()
  #      elif choose == "7" or choose=="07": 
            about()   
        elif choose == "0":
            exit()
        else:
            sprint(error+'Wrong input!')
            os.system("sleep 50")
            main()
try:            
    main()
except KeyboardInterrupt:
    sprint(info+"BYE-BYE LOVE YOU")
    exit()
except Exception as e:
    sprint(error+str(e))
