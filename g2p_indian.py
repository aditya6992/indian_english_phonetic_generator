def loadDefault():
	default = open('default.txt')
	ret = {}
	for line in default:
		words = line.strip('\n').split(' ')
		ret[words[0]] = ' '.join(words[1:len(words)])
	return ret

def letter2sound(word):
	n = len(word)
	i = 0
	default = loadDefault()
	vowels = ['a', 'e', 'i', 'o', 'u']
	# transcription = ''
	transcription = []
	while i < n:
		initial = True if i == 0 else False
		previous = word[i - 1] if not initial else None
		try:
			next = word[i + 1]
		except IndexError:
			next = None
		try:
			preprevious = word[i - 2]
		except IndexError:
			preprevious = None
		try:
			nextnext = word[i + 2]
		except IndexError:
			nextnext = None
		try:
			prepreprevious = word[i - 3]
		except IndexError:
			prepreprevious = None

		if word[i] == 'a':
			if next == 'a':
				transcription.append('AA')
				i = i + 1
			elif next == 'e':
				transcription.append('EY')
				i = i + 1
			else:
				transcription.append(default['a'])
		elif word[i] == 'x':
			if initial:
				transcription.append('Z')
			else:
				transcription.append(default['x'])

		elif word[i] == 's':
			if next == 'h':
				transcription.append('SH')
				i = i + 1
			elif initial:
				transcription.append('S')
			else:
				if previous in vowels:
					transcription.append('Z')
				else:
					transcription.append(default['s'])

		elif word[i] == 'c':
			if next == 'c':
				transcription.append('K') 
				transcription.append('S')
				i += 1
			elif next == 'h':
				transcription.append('C') 
				transcription.append('H')
				i += 1
			elif next == 'a' or next == 'o' or next == 'u':
				transcription.append('K')
			elif next == 'e' or next == 'i':
				transcription.append('S')
			else:
				transcription.append(default['c'])

		elif word[i] == 'g':
			if next == 'a' or next == 'o' or next == 'u':
				transcription.append('G')
			elif next == 'e' or next == 'y':
				transcription.append('J')
			else:
				transcription.append(default['g'])

		elif word[i] == 'y':
			#y rules are a bit elaborate
			if i == 0:
				transcription.append('Y')
			else:
				if previous in vowels and next in vowels:
					transcription.append('Y')
				elif next in vowels and nextnext in vowels:
					transcription.append('Y')
				elif preprevious not in vowels and previous not in vowels:
					transcription.append('AY')
				elif previous not in vowels and previous != 'f' and previous != 'l' and previous != 'b' and previous != 'y':
					transcription.append('IY')
				elif previous == 'f':
					if preprevious not in vowels and preprevious != 's' and preprevious != 'y':
						transcription.append('IY')
					elif preprevious not in vowels and (preprevious == 's' or preprevious == 'y'):
						transcription.append('AY')
					elif preprevious in vowels and prepreprevious in vowels:
						if preprevious == 'i' or preprevious == 'e':
							transcription.append('AY')
						elif prepreprevious == 'u':
							transcription.append('AY')
						else:
							transcription.append('IY')
				elif previous == 'l':
					if preprevious == 'f':
						transcription.append('AY')
					elif preprevious == 'p':
						transcription.append('AY')
					else:
						transcription.append('IY')
				elif previous == 'b':
					transcription.append('AY')
				else:
					transcription.append('IY')

		elif word[i] == 'e':
			if i == n - 1 and word[i - 1] not in vowels:
				if word[i - 2] == 'a':
					transcription[-2] = 'EY'
				elif word[i - 2] == 'i':
					transcription[-2] = 'AY'
				elif word[i - 2] == 'o':
					transcription[-2] = 'OW'
				elif word[i-2] == 'u':
					transcription[-2] = 'UW'
				i = i + 1
			else:
				transcription.append(default['e'])
		else:
			transcription.append(default[word[i]])
		i = i + 1
	return transcription


def phonological(transcription):
	#rules that are to be applied once the phonetic sequence is established
	n = len(transcription)
	if n >= 3:
		if transcription[-1] == 'D' and transcription[-2] == 'EH':
			if transcription[-3] == 'T' or transcription[-3] == 'D':
				pass
			elif transcription[-3] == 'K' or transcription[-3] == 'S' or transcription[-3] == 'S' or transcription[-3] == 'SH':
				transcription[-1] = 'T'
				transcription.pop(-2)
			else:
				transcription.pop(-2)

		if transcription[-1] == 'S' or transcription[-1] == 'Z' and transcription[-2] == 'EH':
			if transcription[-3] == 'S' or transcription[-3] == 'Z' or transcription[-3] == 'CH' or transcription[-3] == 'JH':
				transcription[-1] = 'Z'
			elif transcription[-3] == 'K' or transcription[-3] == 'P' or transcription[-3] == 'T' or transcription[-3] == 'L':
				transcription[-1] = 'S'
				transcription.pop(-2)
			else:
				transcription[-1] = 'Z'

	return transcription


def main():
	print 'Interactive mode'
	while True:
		word = raw_input().strip()
		print ' '.join(phonological(letter2sound(word.lower())))

if __name__ == '__main__':
    main()




