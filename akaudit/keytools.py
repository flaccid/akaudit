def remove_public_key(ak=None, key=None, dry=False):
	f = open(ak, 'r')
	lines = f.readlines()
	f.close()
	if not dry:
		f = open(ak, 'w')
		for line in lines:
			if key not in line:
				f.write(line)
		f.close()
