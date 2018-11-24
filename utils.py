import os
# from Crypto.Cipher import AES

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

counter = os.urandom(16)
key = os.urandom(32)

# retorna os dados de um arquivo
def file_data(file):
    path = ROOT_DIR + '/upload_files/{}'.format(file)
    if os.path.isfile(path):
        data = open(path, 'r')
        data = data.read()
        return data     

# verifica se um arquivo existe
def file_exists(file):
    path = ROOT_DIR + '/upload_files/{}'.format(file)
    if os.path.isfile(path):
        return True
    return False

# cria um novo arquivo com os dados baixados
def write_file(name, data):
    path = os.path.join(ROOT_DIR, 'download_files')
    if not os.path.exists(path):
        os.makedirs(path)
    file = open(path+'/'+name, 'a+')
    file.write(data)
    file.close()

# # criptografa
# def do_encrypt(message):
#     enc = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
#     encrypted = enc.encrypt(message)
#     return encrypted

# # descriptografa
# def do_decrypt(ciphertext):
#     dec = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
#     decrypted = dec.decrypt(ciphertext)
#     return decrypted
