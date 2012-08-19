# python3 is required!

def put_anki():

	file = input('PATH TO FILE: ')
	tag = input('TAG: ')
	
	f = open(file, 'a')		
	try:
		while True:
			front = input('FRONT: ')
			if not front: break
			back = input('BACK: ')
			f.write(front + ', ' + back + ', ' + tag + '\n')
			print('ok')
	finally:
		f.close() 

if __name__ == '__main__':
	put_anki()