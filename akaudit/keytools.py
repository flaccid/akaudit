def remove_public_key(ak=None, key=None, dry=True):
	print(ak, key)
	f = open(ak, 'r')
	lines = f.readlines()
	f.close()
	f = open(ak, 'w')
	for line in lines:
		if key not in line:
			f.write(line)
	f.close()
