
matches = {
'measure': 'mea', 
'note': 'n', 
'pitch':'p', 
'step':'s', 
'alter':'a', 
'octave':'o', 
'duration':'d', 
'voice':'v',
'stem': 'w',
'beam':'b',
'tie':'t',
'notations': 'u',
'tied':'x',
'accidental':'y',
'articulations': 'z',
'time-modification':'mod',
'actual-notes':'an',
'normal-notes':'nn',
'normal-type':'nt',
'staccato': 'q',
'metronome':'mt',
'direction-type': 'dt',
'attributes':'att',
'direction' :'dir',
'divisions': 'dis',
'dynamics':'dyn',
'top-syw-distance':'tsd'
}

def removeShit(s):
	start = s.find('"')
	end = s.find('"', start + 1)
	#print(s, start, end)
	#print(s[start:end + 1])
	s = s.replace(s[start - 1:end + 1], '')
	return s


with open('../input-raw.txt', 'r') as finn:
	with open('../input.txt', 'w') as fout:

		line = finn.readline()

		while line != "":

			for key, value in matches.items():

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
			
			fout.write(line)

			line = finn.readline()


