#!/usr/bin/env python3

def put_anki(file, tag):
	"""
	if the file does not exit, it will be created
	inputed values will be saved in the file in the form: front; back; tag
	"""
	
	f = open(file, 'a')		
	try:
		while True:
			front = input('FRONT: ')
			if not front: break
			back = input('BACK: ')
			f.write(front + '; ' + back + '; ' + tag + '\n')
			print('ok')
	finally:
		f.close() 

if __name__ == '__main__':
	print('DO NOT USE \';\'!')
	
	file = input('PATH TO FILE: ')
	tag = input('TAG: ')
	
	put_anki(file, tag)
	

