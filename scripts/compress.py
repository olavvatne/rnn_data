from scripts.vocabular import matches

def removeShit(s):
	start = s.find('"')
	end = s.find('"', start + 1)
	#print(s, start, end)
	#print(s[start:end + 1])
	s = s.replace(s[start - 1:end + 1], '')
	return s


with open('../input-test', 'r') as finn:
	with open('../output-test.txt', 'w') as fout:

		line = finn.readline()

		while line != "":
			print(matches.items())
			dont_write = False
			for key, value in matches.items():

				if "print" in line:
					line = ""
					dont_write = True
				if "measure" in line:
					if "number" in line:
						line = removeShit(line)
						line = line.replace("number ", '')
					if "width" in line:
						line = removeShit(line)
						line = line.replace(" width", '')

				if "beam" in line:
					if "number" in line:
						line = removeShit(line)
						line = line.replace(" number", '')

				line = line.replace(key, value).strip() + "\n"

				# Remove default stuff
				if "default-x" in line:
					line = removeShit(line)
					line = line.replace(" default-x", '')
				if "default-y" in line:
					line = removeShit(line)
					line = line.replace(" default-y", '')

			if len(line)>2 and line[-2] == ">":
				line = line[0:-2] + "\n"
			if len(line)>2  and line[-2] == "/":
				line = line[0:-1]  + "\n"
			if not dont_write:
				fout.write(line)

			line = finn.readline()


