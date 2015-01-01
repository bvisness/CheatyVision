import struct

def float_to_bytes(float):
	return struct.pack("f",float)

def bytes_to_float(bytes):
	return struct.unpack("f",bytes)

def float_to_bitstr(float):
	bytes = struct.pack("f",float)
	bits = ['{0:08b}'.format(ord(byte)) for byte in bytes]
	return ''.join(bits)
	
def bitstr_to_float(bitstr):
	bytes = ''.join([chr(int(bitstr[i:i+8],2)) for i in range(0,len(bitstr),8)])
	bytes = '\0' * (4 - len(bytes)) + bytes
	return struct.unpack("f",bytes)[0]
	
def float_to_str(float):
	return struct.pack("f",float)
	
def boolarr_to_bitstr(booleans):
	bits = ['1' if boolean else '0' for boolean in booleans]
	return ''.join(bits)
	
def floatarr_to_bitstr(floats):
	bits = [float_to_bitstr(float) for float in floats]
	return ''.join(bits)
	
def bitstr_to_str(bitstr):
	return ''.join([chr(int(bitstr[i:i+6],2)+59) for i in range(0,len(bitstr),6)])

def str_to_bitstr(str):
	return ''.join(['{0:06b}'.format(ord(char)-59) for char in str])

def bitstr_to_boolarr(bitstr):
	return [bit=="1" for bit in bitstr]
	
def bitstr_to_floatarr(bitstr):
	return [bitstr_to_float(bitstr[i:i+4*8]) for i in range(0,len(bitstr),4*8)]
		
def encode(buttons, axes):
	return bitstr_to_str(boolarr_to_bitstr(buttons))+"#"+bitstr_to_str(floatarr_to_bitstr(axes))
	
def decode(str):
	[boolstr,floatstr]=str.split('#')
	return [bitstr_to_boolarr(str_to_bitstr(boolstr)),bitstr_to_floatarr(str_to_bitstr(floatstr))]