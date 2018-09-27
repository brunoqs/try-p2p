from server.server import *
from peer.peer import *

choice = input("1- Server / 2- Peer\n")
if choice == "1":
    s = Server('127.0.0.1', 12000) # ip e porta padrao servidor de controle
    s.run() 
else:
    choice2 = input("1-Download / 2-Upload\n")
    if choice2 == "1":
        p = Peer('127.0.0.1', 8000) # ip e porta padrao server peer
        found = p.search_data()
        if found:
            print("Arquivo encontrado")
        else:
            print("Arquivo nao encontrado")

    else:
        p = Peer() # ip e porta padrao server peer
        p.register_peer()

