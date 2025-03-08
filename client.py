import hashlib
import socket


serv_ip = "0.0.0.0"
serv_port = "8000"

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.bind("127.0.0.1",12345)



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
    path_fichier = "journeymap.server.solara_dimension~solarademension.config"
    print(calculer_hash_fichier(path_fichier))

