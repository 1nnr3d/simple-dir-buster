import requests
import urllib
from time import sleep
from threading import Thread
from colorama import Fore

def startDir():
    print(Fore.BLUE + """
    MMMMMMMMMMMMWNK0kxdoolllccclllodxk0KNWMMMMMMMMMMMM
    MMMMMMMMMWX0xdllccclccccclllcccccllldx0XWMMMMMMMMM
    MMMMMMWN0xollccccclllcccclllcccccccclclox0NWMMMMMM
    MMMMMN0dlccccccccccccccccccccccccclcclcccld0NWMMMM
    MMMWKxlcccccclodxkOOOOkxoollclccccccccccccclxKWMMM
    MMNOoccccccldOXNNXKKKXXNXXKkolcccccccccclcccloONMM
    MNklcccccld0NNK0KK0kxxxk0KXNXkolcccccccccccccclkNM
    NklcccccldKWX0KXK0OxxxxxxxxONNOoccccccccccccccclkN
    0oclcccco0WKOKXOxxxxxxxxxxxxONNklccccccccccccccco0
    xlccccccdXN0kOOxxxxxxxxxxxxxkKW0occccccccccccccclx
    occcccccdXW0xxxxxxxxxxxxxxxxkKW0occcccccccccccccco
    llccccclo0WXkxxxxxxxxxxxxxxx0NNxlccccccccccccccccl
    lcclccccld0NXOxxxxxxxxxxxxk0NNOlcccccccccccccccccl
    llcclcccclokXNX0OkxxxkkOKXNWMNOdlcclllccccccccccll
    occcccccclclok0XNXXXXXNXKK00XNXKdccclllcccccccccco
    klccccccccclcclodxkkkxxdlllldOkl,.';cccclccccccclk
    Xdlcccccccccccccccccccccllccllc'....';cccccccccldX
    WKdlllccccccccccccccccccccclcccc;'....';cclcclldKW
    MWKdlcccccccccccccccccccclccclcccc;'....,clccldKWM
    MMWXklcccccclcccccccccccccccccccclcc;'';cccclkXWMM
    MMMMN0dlcccccclccccccccccccccccccllcccccccld0NMMMM
    MMMMMWN0xlclcccccccccccccccccccccclccclclx0NWMMMMM
    MMMMMMMWNKkdllcccccccccccccccccccccllldkKNMMMMMMMM
    MMMMMMMMMMWNKOkdollcccclcccccccllodkOKNWMMMMMMMMMM
    MMMMMMMMMMMMMMWNKOxdolllcccllodxOKNWMMMMMMMMMMMMMM
    \t\t\t\t\t github/1nnr3d
    """)
    urL = input("URL: ")
    if "http://" in urL:
        pass
    elif "https://" in urL:
        pass
    elif len(urL) < 1:
        raise Exception("Link Wrong or Missing!")
    else:
        urL = "http://" + urL

    filePath = input("File Path: ")
    if len(filePath) < 1:
        raise Exception("File Path Wrong or Missing!")
    print("-"*50)

    Thread(target=fileRead, args=(urL,filePath)).start()

def fileRead(url,fp):
    with open(fp, "r") as f:
        words = f.readlines()
    Thread(target=dir, args=(url,words)).start()
def dir(url,wrds):
    if url[-1] != "/":
        for w in wrds:
            w = str(w).replace('\n','')
            u = f"{url}/{w}"
            r = requests.get(u, proxies=urllib.request.getproxies())
            r = str(r).replace('<', '').replace('>', '').replace('Response ', '')
            if "200" in r:
                print(f"{u} : {r} + FOUND!")
            else:
                print(f"{u} : {r} ? ")
    else:
        for w in wrds:
            w = str(w).replace('\n', '')
            u = url + w
            r = requests.get(u, proxies=urllib.request.getproxies())
            r = str(r).replace('<','').replace('>','').replace('Response ', '')
            if "200" in r:
                print(f"{u} : {r} + FOUND!")
            else:
                print(f"{u} : {r} ? ")
    sleep(2)
startDir()
