import sys

from gevent.server import StreamServer

from SQueue import Queue
queue = Queue()

""" Example based on https://github.com/SiteSupport/gevent/blob/master/examples/echoserver.py code """
def handle(socket, address):
	print ('New connection from %s:%s' % address)
	socket.sendall('Welcome to the echo server! Type quit to exit.\r\n')
	fileobj = socket.makefile()
	while True:
		line = fileobj.readline()
		if not line:
			print ("client disconnected")
			break
		if line.strip().lower() == 'quit':
			print ("client quit")
			break
		if line.startswith("ENQUEUE"):
			data = line.split("ENQUEUE:")[1]   
			queue.enqueue(data)
			fileobj.write("OK \n")
		elif line.startswith("DEQUEUE"):
			data = line.split("DEQUEUE")[1]   
			el = queue.dequeue()
			fileobj.write(el)    	
		fileobj.flush()

if __name__ == "__main__":
	host, port = sys.argv[1].split(":")
	server = StreamServer((host, int(port)) , handle)
	server.serve_forever()