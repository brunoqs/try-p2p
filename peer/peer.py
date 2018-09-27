from socket import *
import pickle

class Peer:
    # socket server peer
    def __init__(self, c_ip = None, c_port = None):
        self.c_port = c_port
        self.c_ip = c_ip

        if self.c_port != None and self.c_ip != None:
            self.sock = socket()
            self.sock.bind((self.c_ip, self.c_port))
            self.sock.listen(2)

        # dados servidor de controle
        self.s_ip = '127.0.0.1'
        self.s_port = 12000

    # conecta no servidor de controle para registrar seu ip e dado
    def register_peer(self):
        sock = socket()
        sock.connect((self.s_ip, self.s_port))
        data = input("Digite o arquivo que deseja registrar\n")
        sock.send(pickle.dumps(("REGISTER", data)))
        resp = pickle.loads(sock.recv(1024))

        if resp == "True":
            print("Arquivo registrado com sucesso")

        sock.close()

    # procura no servidor de controle se algum peer ja registrou o dado 
    def search_data(self):
        sock = socket()
        sock.connect((self.s_ip, self.s_port))
        data = input("Digite o arquivo que deseja procurar\n")
        sock.send(pickle.dumps(("SEARCH", data)))
        resp = pickle.loads(sock.recv(1024))

        if resp != None:
            sock.close()
            return True

        sock.close()
        return False

    # deixa o socket server peer lendo para outros peers buscar dados
    def listen(self):
        while True:
            conn, addr = self.sock.accept()
            data = pickle.loads(conn.recv(1024))
