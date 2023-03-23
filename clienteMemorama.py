import socket
#192.168.1.168

# Crea un socket para el cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se conecta al servidor
adress = input("introdusca el ip en forma de cadena \t")
cliente.connect((adress, 5000))

# Recibe el tablero del servidor y lo imprime
difficulty = input("ingresa la dificultad 0 o 1: 1) Difícil 0) fácil ")
cliente.sendall(difficulty.encode())#aqui lo quite

#mensajito = cliente.recv(1024).decode('utf-8')
#print(f"nos llego {mensajito} como mensajito despues de enviar {difficulty}")

tablero = eval(cliente.recv(1024).decode()) #decode decodifica bites en una cadena y es lo que se pone con el recv
for fila in tablero:
    print(fila)

# Juega el juego
while True:
    # Pide al usuario que seleccione una carta para voltear
    carta = input('Seleccione una carta (fila,columna): ')
    
    # Envía la carta al servidor
    cliente.sendall(carta.encode())
    
    # Recibe el valor de la carta del servidor y lo imprime
    valor = str(cliente.recv(2048).decode())
    
    if valor == 'fin':
        print('Encontraste todos los matches')
        break
    print(f'La carta es {valor}')
    
# Cierra la conexión
cliente.close()
