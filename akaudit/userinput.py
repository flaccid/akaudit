from six.moves import input

def yesno(prompt='? '):
	# raw_input returns the empty string for "enter"
	yes = set(['yes','y', 'ye', ''])
	no = set(['no','n'])

	choice = input(prompt).lower()
	if choice in yes:
		return True
	elif choice in no:
		return False
	else:
		sys.stdout.write("Please respond with 'yes' or 'no'")
