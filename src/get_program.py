def get_program():
	a=""
	while True:
		try:
			a += raw_input() + " "
		except:
			break
	return a
