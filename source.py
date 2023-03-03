from subprocess import check_output
from shacrypt   import encrypt
from requests   import get
from time       import sleep
from os         import system

def auth(code: str, contact: str):
    paste = get(f"https://pastebin.com/raw/{code}")
    hwid  = encrypt(str(str(check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip()))
    
    if hwid in paste.text:
        print("")
    else:
        print(f"\n send this to {contact}: " + hwid)
        sleep(6)
        exit()
