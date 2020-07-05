def do_stuff(num):
	try:
		if num:
			return int(num) + 5
		elif num == 0:
			return int(num) + 5
		else:
			return "Please inset a number"
	except ValueError as err:
		return err
