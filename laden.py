klein = []
gross = []
alphabetGross = []
alphabetKlein = []
for i in range(26):
	alphabetGross.append(chr(65+i))
	alphabetKlein.append(chr(97+i))

for i in range(26):
	klein.append([])
	gross.append([])
file0 = open('wordlisteDeutschGross.txt','r')
wortlisteGross = file0.read()
file0.close()
file1 = open('wordlisteDeutschKlein.txt','r')
wortlisteKlein = file1.read()
file1.close()

zeilenGross = wortlisteGross.split('\n')
counter = 0
for zeile in zeilenGross:
	if zeile[0] == alphabetGross[counter]:
		gross[counter].append(zeile)
	else:
		if counter < len(zeilenGross):
			gross[counter+1].append(zeile)
			counter += 1
		else:
			pass
	


zeilenKlein = wortlisteKlein.split('\n')
counter = 0
for zeile in zeilenKlein:
	if zeile[0] == alphabetKlein[counter]:
		klein[counter].append(zeile)
	else:
		if counter < len(zeilenKlein):
			klein[counter+1].append(zeile)
			counter += 1
		else:
			pass


def search(character):
	if ord(character) in range(65,92):
		return gross[ord(character)-65]
	elif ord(character) in range(97,123):
		return klein[ord(character)-97]

def averageLength(character):
	liste = search(character)
	summe = 0
	for element in liste:
		summe += len(element)
	result = int(summe/len(liste))
	return result

def length(character):
	return len(search(character))

def nGramm(wort,n):
		
	
