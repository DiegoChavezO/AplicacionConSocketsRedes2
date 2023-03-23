#programa para crear un memorama para saber como le voy a hacer para hacerlo con sockets
import socket
import random 
cartas = []
j=0
nombresCartas1 = ["GustavoCerati","CharlyGarcia","FitoPaez","AndresCalamaro","LuisSpinetta","vicentico","cachoTirado","Almendra",
                  "GustavoCerati","CharlyGarcia","FitoPaez","AndresCalamaro","LuisSpinetta","vicentico","cachoTirado","Almendra"] #matriz 3 x 4
nombresCartas2 = ["Bravo","Sonoyta","colorado","lerma","Tonala","Balsas","Nazas","papagayo","antigua",
                  "canchos","candelaria","Quetzala","Verde","Tuxpan","santiago","grijalva","Usumancita","panuco"
                  "Bravo","Sonoyta","colorado","lerma","Tonala","Balsas","Nazas","papagayo","antigua",
                  "canchos","candelaria","Quetzala","Verde","Tuxpan","santiago","grijalva","Usumancita","panuco"]

# Crea el tablero del memorama

random.shuffle(nombresCartas1)
tablero = [nombresCartas1[:4], nombresCartas1[4:8], nombresCartas1[8:12], nombresCartas1[12:]]
tablero1 = [["*","*","*","*",],["*","*","*","*",],["*","*","*","*",],["*","*","*","*",],]

random.shuffle(nombresCartas2)
tablero2 = [nombresCartas2[:6],
            nombresCartas2[6:12],
            nombresCartas2[12:18], 
            nombresCartas2[18:24],
            nombresCartas2[24:30],
            nombresCartas2[30:]]
tablero3 = [["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
            ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
            ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
            ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
            ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
            ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"], ]

# Crea un diccionario para realizar un seguimiento de las cartas volteadas
cartas_volteadas = {}

# Crea un socket para el servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configura el servidor para escuchar conexiones entrantes
adress = input("introdusca el ip en forma de cadena\t")
servidor.bind((adress, 5000)) #recibe adress y puerto servidor.bind(('localhost', 5000))
servidor.listen(1) 
print('Esperando conexiones...')

# Espera a que un cliente se conecte y acepta la conexión
cliente, direccion = servidor.accept()
print(f'Conexión establecida desde {direccion}') 




#parte del codigo para elegir la dificultad
dific = cliente.recv(1024).decode('utf-8')
print("El dato recibido del cliente es:", dific)
if dific=='1':
    cliente.sendall(str(tablero3).encode())
    tablero_seleccionado = tablero2
    #print(tablero_seleccionado)
    
else:
    cliente.sendall(str(tablero1).encode())
    tablero_seleccionado = tablero
    


# Envía el tablero al cliente


#cliente.sendall(str(tablero).encode())

#cliente.sendall(str(tablero1).encode())
# Juega el juego
while True:
    # Recibe la carta que el cliente ha volteado
    carta = cliente.recv(1024).decode()
    fila, columna = carta.split(',')
    fila, columna = int(fila), int(columna)
    

    # Voltea la carta
    
    cartas_volteadas[carta] = tablero_seleccionado[fila][columna] #aqui está el pex antes era tablero
    cliente.sendall(str(tablero_seleccionado[fila][columna]).encode())
    
    # Verifica si se han encontrado todas las parejas
    if len(cartas_volteadas) == len(nombresCartas1)-1:
        cliente.sendall(b'fin')
        break

# Cierra la conexión
cliente.close()
servidor.close()
