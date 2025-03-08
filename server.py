import socket
import hashlib
import threading


serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)   #initi en IPv4 en datagramme avec le protocole 0 l'objet socket
serv_socket.bind("127.0.0.1",12345)     #associe l'ip localhost A CHANGER EN REEL et le port 12345 à la socket



class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connexion de %s %s" % (self.ip, self.port, ))

        r = self.clientsocket.recv(2048)
        print("Ouverture du fichier: ", r, "...")
        fp = open(r, 'rb')
        self.clientsocket.send(fp.read())

        print("Client déconnecté...")


def ServStart():
    serv_socket.listen()    #accepte les connexions pour la socket













def calculer_hash_fichier(path, algo="sha256", buffer_size=65536):  #path + algo en sha256 et un buffer pour eviter la congestion de gros fichier
        
    try:
        hash_func = hashlib.new(algo) #init de la fonction de hashage
                
        with open(path,"rb") as f: #ouverture du fichier à partir du path en rb read only binary 
            for chunk in iter(lambda: f.read(buffer_size), b""):
                hash_func.update(chunk)

                return hash_func.hexdigest()
    
    except FileNotFoundError:
        return f"Erreur : fichier '{path}' introuvable."
    except Exception as e:
        return f"Erreur : {e}"


if __name__ == "__main__":
    servStart()
    
