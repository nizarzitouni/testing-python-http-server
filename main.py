import socket
SERVER_HOST= "0.0.0.0"
SERVER_PORT= 8080
# initing the socket
server_socket= socket.socket(
	family=socket.AF_INET, # IPV4
	type=socket.SOOK_DGRAM, # SOOK_STREAM: TCP Socket or you can use UDP socket with :
)

server_socket.setsockopt(
	socket.SOL_SOCKET,
	socket.SO_REUSEADDR, # the feauture we want to enable, allow this enpoint to be reused immediately after the socket closes
	1 # On=1, Off=0
)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print(f"Listening on port {SERVER_PORT} ...")

while True: # so that we continuously keep listening to new client connections
    
    # try:
    print('ran') # <----- add print statement to explain the blocking
    client_socket, client_address = server_socket.accept()
    print('ran2')  # <----- add print statement to explain the blocking
    # except BlockingIOError:
    #     time.sleep(1)
    #     continue
    
    request = client_socket.recv(1500).decode()
    print(request)

    headers = request.split('\n')
    first_header_components = headers[0].split()

    http_method = first_header_components[0]
    path = first_header_components[1]

    if http_method == 'GET':
        if path == '/':
            fin = open('index.html')
        elif path == '/book':
            fin = open('book.json')
        else:
            # handle the edge case
            pass
        
        content = fin.read()
        fin.close()
        response = 'HTTP/1.1 200 OK\n\n' + content
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET'

