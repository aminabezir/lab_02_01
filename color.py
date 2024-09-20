def coefficient_by_colour(number):
	k = 0
	if (number == 1 or number == 2 or number == 4):
		k = 1
	elif (number == 3):
		k = 1.1
	elif (number == 5):
		k = 1.2
	elif (number == 6):
		k = 1.3
	return k