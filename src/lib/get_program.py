def get_program():
	a=""
	while True:
		try:
			a += raw_input() + " \n "
		except:
			break
	return a
