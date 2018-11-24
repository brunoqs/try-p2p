from socket import *
from threading import Thread
# from utils import do_decrypt, do_encrypt
import pickle

class Server:
    def __init__(self, s_ip, s_port):
        self.s_port = s_port
        self.s_ip = s_ip
        self.sock = socket()
        self.sock.bind((self.s_ip, self.s_port))
        self.sock.listen(5)
        self.peer_lists = []

    def search_data(self, data):
        for peer in self.peer_lists:
            if data in peer[2]:
                return peer
        return None
    
    def register_data(self, addr, data):
        addr += (data, )
        self.peer_lists.append(addr)
        print(self.peer_lists)

    def conn_handler(self, conn, addr):
        data = pickle.loads(conn.recv(1024))
        if data[0] == "REGISTER":
            self.register_data(addr, data)
            resp = "True"
            conn.send(pickle.dumps(resp))
        elif data[0] == "SEARCH":
            peer = self.search_data(data[1])
            conn.send(pickle.dumps(peer))
        conn.close()

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            t = Thread(target=self.conn_handler, args=[conn, addr])
            t.start()