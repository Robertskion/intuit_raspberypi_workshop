import io
import socket
import struct
import sys
import os
import errno
from PIL import Image

PATH = "/home/priyaman/face_rec/face_recognition/images"
PREFIX_NAME = 'USR006'
def rec_n_store():
	# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
	# all interfaces)
	server_socket = socket.socket()
	server_socket.bind(('0.0.0.0', 8000))
	server_socket.listen(0)

	# Accept a single connection and make a file-like object out of it
	connection = server_socket.accept()[0].makefile('rb')
	ctr = 0
	try:
	    while True:
		# Read the length of the image as a 32-bit unsigned int. If the
		# length is zero, quit the loop
		image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
		if not image_len:
		    break
		# Construct a stream to hold the image data and read the image
		# data from the connection
		image_stream = io.BytesIO()
		image_stream.write(connection.read(image_len))
		# Rewind the stream, open it as an image with PIL and do some
		# processing on it
		image_stream.seek(0)
		image = Image.open(image_stream)
		print('Image is %dx%d' % image.size)
		image.verify()
		print('Image is verified')

		image_stream.seek(0)
		image = Image.open(image_stream)
		image.save(PATH + '/' + PREFIX_NAME + '/' + PREFIX_NAME + '_' + str(ctr) + '.jpg')
		ctr += 1

	finally:
	    connection.close()
	    server_socket.close()

if __name__ == '__main__':
	print 'Storing Images for Label' + str(sys.argv[1])
	PREFIX_NAME = sys.argv[1]
	try:
		os.makedirs(PATH + '/' + PREFIX_NAME)	
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	rec_n_store()
