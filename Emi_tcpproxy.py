import sys
import  socket
import  threading

def server_loop(local_host,local_port,remote_host,remote_port,receive_first):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.bind((local_host,local_port))
    except:
        print "[!!]Failed to listen on %s:%d" %(local_host,local_port)
        print "[!!]Check for other listening sockets or correct permission."
        sys.exit(0)

    print "[*]listening on %s%d" % (local_host,local_port)

    server.listen(5)

    while True:
        client_sockrt,addr = server.accept()

        print "[==>] Received incoming connection from %s%d" % (addr[0],addr[1])
        proxy_thread = threading.Thread(target=proxy_handler,args=(client_sockrt,remote_host,remote_port,receive_first))
        proxy_thread.start()
