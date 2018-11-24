from server.server import *
from peer.peer import *
from threading import Thread

choice = input("1- Server / 2- Peer\n")
if choice == "1":
    s = Server('127.0.0.1', 12000) # ip e porta padrao servidor de controle
    s.run()
else:
    choice2 = ""
    p = Peer('127.0.0.1')
    t = Thread(target=p.listen, args=[])
    t.start()
    while True:
        choice2 = input("1-Download / 2-Upload / 3-Fechar \n")
        if choice2 == "3":
            break
        elif choice2 == "1":
            peer = p.search_file()
            if peer:
                print(peer)
                p.download_file(peer[0][3], peer[0][0], int(peer[0][4]))
            else:
                print("Arquivo nao encontrado")
        else:
            p.register_peer()

