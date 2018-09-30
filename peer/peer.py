from socket import *
import pickle
from utils import *

class Peer:
    # socket server peer
    def __init__(self, c_ip = None):
        self.c_ip = c_ip

        if self.c_ip != None:
            self.sock = socket()
            self.sock.bind((self.c_ip, 0)) # porta random
            self.sock.listen(2)
            self.c_port = self.sock.getsockname()[1]

        # dados servidor de controle
        self.s_ip = '127.0.0.1'
        self.s_port = 12000

    # conecta no servidor de controle para registrar o ip e arquivo e porta do peer
    def register_peer(self):
        file = input("Digite o arquivo que deseja registrar\n")
        if(not file_exists(file)):
            print("Arquivo nao existe, tente de novo.")
            return False

        sock = socket()
        sock.connect((self.s_ip, self.s_port))
        sock.send(pickle.dumps(("REGISTER", file, self.c_port))) # informa a porta do peer server
        resp = pickle.loads(sock.recv(1024))

        if resp == "True":
            print("Arquivo registrado com sucesso")

        sock.close()
        return True

    # procura no servidor de controle se algum peer ja registrou o dado 
    def search_file(self):
        file = input("Digite o arquivo que deseja procurar\n")
        sock = socket()
        sock.connect((self.s_ip, self.s_port))
        sock.send(pickle.dumps(("SEARCH", file)))
        resp = pickle.loads(sock.recv(1024))

        if resp != None:
            sock.close()
            return resp

        sock.close()
        return False

    # baixa o arquivo do peer encontrado pelo search_file 
    def download_file(self, file, addr, port):
        sock = socket()
        try:
            sock.connect((addr, port))
        except ConnectionRefusedError:
            print("Peer desligado!")
        sock.send(pickle.dumps(file))
        resp = pickle.loads(sock.recv(1024))
        sock.close()
        print("Download: " + resp)


    # deixa o socket server peer lendo para outros peers buscar dados
    def listen(self):
        while True:
            conn, addr = self.sock.accept()
            file = pickle.loads(conn.recv(1024))
            data = file_data(file)
            conn.send(pickle.dumps(data))
        conn.close()
