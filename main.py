
from colorama import Fore, init, Style
from throwbin import ThrowBin
from navmenu import Menu
import pyPrivnote as pn
import re, requests,os, time
tb = ThrowBin()
os.system("title Note multitool - wow so epic - wow so seggsy - omg so amazing!")
init(convert = True)

def readpastebin():
    os.system("title Ready to read pastebin contents!")
    print(Fore.CYAN)
    input()
    pastebintoread = input("[!] Pastebin Link to read?\n[>] ")
    if 'pastebin' in pastebintoread:
        code = re.search("pastebin.com/(.*)", pastebintoread).group(1)
        pastebinresp = requests.get(f'https://pastebin.com/raw/{code}').text
        print(f"{Fore.GREEN}\n\n[+] Results from {pastebintoread}: \n\n{pastebinresp}\n\n")
    else:
        print(f"{Fore.RED}[!] Please input a valid link.")
        readpastebin()
    input(f"{Fore.CYAN}[!] Press Enter To Quit.\n[!] ")





def readprivnote():
    os.system("title Ready to read privnote contents!")
    print(Fore.CYAN)
    input()
    privnotetoread = input("[!] Privnote Link to read?\n[>] ")
    if 'privnote' in privnotetoread.lower():
        privnoteresp = pn.read_note(privnotetoread)
        print(f"{Fore.GREEN}\n\n[+] Results from {privnotetoread}: \n\n{privnoteresp}\n\n")
    else:
        print(f"{Fore.RED}[!] Please input a valid link.")
        readpastebin()
    input(f"{Fore.CYAN}[!] Press Enter To Quit.\n[!] ")





def makeprivnote():
    os.system("title Ready to create a privnote!")
    print(Fore.CYAN)
    input()
    textforprivnote = input("[!] Privnote message to write?\n[>] ")
    note_link = pn.create_note(textforprivnote)
    print(f"{Fore.GREEN}[+] Privnote Made!\n[+] Link:\n[+] {note_link}\n")
    input(f"{Fore.CYAN}[!] Press Enter To Quit.\n[!] ")


def readthrowbin():
    os.system("title Contact me if you can help with this :)")
    input()
    time.sleep(1)
    input(f"{Fore.RED}[!] Had trouble coding this.Press enter to quit.\n[>] ")

def makethrowbin():
    os.system("title Ready to create a throwbin!")
    input()
    print(Fore.CYAN)
    throwbintitle = input("[!] Throwbin Title?\n[>] ")
    throwbintext = input("[!] Throwbin Text?\n[>] ")
    binthrow = tb.post(
        title=throwbintitle,
        text=throwbintext,
        syntax="text"
    )
    print(f"{Fore.GREEN}[+] Throwbin Made!\n[+] Link:\n[+] {binthrow.link}\n")
    input(f"{Fore.CYAN}[!] Press Enter To Quit.\n[>] ")



def readnotepad():
    os.system("title Ready to read a text file!")
    input()
    print(Fore.CYAN)
    filelocation = input("[!] Please specify the filepath - if it's"+' in the same folder as this, just type "name.txt"\n[!] Else, copy the file location\n[>] ')#mixed ' and " hence the + in the middle of the sentence
    reading = open(filelocation, "r")
    print(f"{Fore.GREEN}\n\nResults from {filelocation}.\n\n{reading.read()}\n")
    input(f"{Fore.CYAN}[!] Press Enter To Quit.\n[>] ")




def notepadtime():
    os.system("title Ready to create some text files!")
    input()
    print(Fore.CYAN)
    answer = input("[1] = Make and write to a text file - while in this program.\n[2] = Open Notepad.\n[>] = ")
    if answer == "1":
        os.system("title Ready to write to a text file!")
        filename = input("[!] What should I name the textfile?\n[+] ")
        if filename[-4:] == ".txt":
            pass
        else:
            filename = filename +".txt"
        os.system(f"title Ready to write to a text file called {filename}!")
        text = input(f"[!] Text to write to {filename}?\n[+] ")
        f = open(filename, "w")
        f.write(text)
        f.close()
        os.system(f"title Wrote to a text file called {filename}!")
        print(f'{Fore.GREEN}\n\nSuccessfully wrote\n\n"{text}"\n\nTo:\n\n"{filename}"')
        os.system(filename)
        time.sleep(1)
    elif answer == "2":
        os.system("title Opened Notepad!!")
        os.system("notepad.exe")
        print(f"{Fore.GREEN}[+] Notepad Opened [+]")
        time.sleep(1)
    else:
        print(f"{Fore.RED}[!] Please answer '1' OR '2' - Press enter to continue.")
        notepadtime()

    

prefix = """
    Welcome to the note multitool
    I've wanted to make something like this for a while,
    When zoony1337 bought out their menu gui - navmenu - I thought I'd have an attempt
    https://github.com/zoony1337/NavMenu - Use it here - very interesting to play with!
"""

suffix = """
     Select an option!
"""


Menu.display(prefix=prefix, indent=5, color='blue', suffix=suffix, options={
    'Read pastebin': readpastebin,
    'Read Privnote': readprivnote,
    'Make Privnote': makeprivnote,
    'Read Throwbin': readthrowbin,
    'Make Throwbin': makethrowbin,
    'Read A Text File': readnotepad,
    'Make A Text File': notepadtime
})
