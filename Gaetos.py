while True:

	print("Options: [1]User Path [2]Main Path: ")
	chc = int(input("Your Choice: "))
	
	if chc == 1:
		import User
		break

	elif chc ==2:
		import main
		break

	else:
		print("Invalid input")